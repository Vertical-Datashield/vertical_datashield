#! /usr/bin/env python

#Olly Butters
#12/4/14


#Main controller for the whole thing.
#A=biobank A
#B=biobank B
#C=client
#M=general matrix
#T=transpose


#A good way to see what is going on is to run
#watch -d ls -ltr temp/A
#etc on each VM, then you see the files being made and passed around.

import os
import shutil
import subprocess
import time

import ds_config

#Define the dataset names
data_A='height_2.csv'
data_B='weight_2.csv'


print "\n###############################"
print "Starting vertical datashield(!)\n"

#Get rid of the temp dirs if they exist on each VM
subprocess.call(ds_config.source_dir+'common/tidy_paths.py')
cmd = 'ssh '+ds_config.remote_settings['A','username']+'@'+ds_config.remote_settings['A','ip_address']+' '+ds_config.source_dir+'common/tidy_paths.py'
os.system(cmd)
cmd = 'ssh '+ds_config.remote_settings['B','username']+'@'+ds_config.remote_settings['B','ip_address']+' '+ds_config.source_dir+'common/tidy_paths.py'
os.system(cmd)

#have a little nap to let the watch catch up
time.sleep(4)

#Top level root directory
print ds_config.root_dir
print ds_config.source_dir
print ds_config.data_dir
print ds_config.temp_dir
print '\n'

#############################################################
#Generate masking vector (v_A). This will copy to A. Do the same for v_B too.
#fn(masking_vector_name, where to store locally, where to copy to remotely)
subprocess.call([ds_config.source_dir+'client/generate_masking_vectors.py','A','v_A',ds_config.temp_dir+'client',ds_config.temp_dir+'A'])
subprocess.call([ds_config.source_dir+'client/generate_masking_vectors.py','B','v_B',ds_config.temp_dir+'client',ds_config.temp_dir+'B'])


#############################################################
#Start with A.B M_A.TA

#On A multiply the masking vector by the data to get (AT.v_A)
#fn(biobank name, masking vector name, data set name, where to store locally, where to copy to remotely) 
#subprocess.call([ds_config.source_dir+"A/mask_MT.py",'A','v_A',data_A,'A','B'])

remote_cmd = ds_config.source_dir+"A/mask_MT.py A v_A "+data_A+" A B"
cmd = 'ssh '+ds_config.remote_settings['A','username']+'@'+ds_config.remote_settings['A','ip_address']+' '+remote_cmd
print cmd
os.system(cmd)



#On B multiply the masked vector by B.v_B, => AT.v_A.B.v_B
#fn(biobank name, masking vector name, data from A, this data set name, where to store locally, where to copy to remotely)
#subprocess.call([ds_config.source_dir+'B/masked_M1_times_M2.py','B', 'v_B',data_A+'.v_A',data_B,ds_config.temp_dir+'B',ds_config.temp_dir+'client'])

remote_cmd = ds_config.source_dir+'B/masked_M1_times_M2.py B v_B '+data_A+'.v_A '+data_B+' B client'
cmd = 'ssh '+ds_config.remote_settings['B','username']+'@'+ds_config.remote_settings['B','ip_address']+' '+remote_cmd
print cmd
os.system(cmd)

#############################################################


#############################################################
#Do B.A now
#############################################################
#On B multiply the masking vector by the data to get (BT.M_B)
#fn(biobank name, masking vector name, data set name, where to store locally, where to copy to remotely) 
#subprocess.call([ds_config.source_dir+'B/mask_MT.py','B','v_B',data_B,ds_config.temp_dir+'B',ds_config.temp_dir+'A'])


remote_cmd = ds_config.source_dir+"B/mask_MT.py B v_B "+data_B+" B A"
cmd = 'ssh '+ds_config.remote_settings['B','username']+'@'+ds_config.remote_settings['B','ip_address']+' '+remote_cmd
print cmd
os.system(cmd)


#On A multiply the masked vector by A.M_A, => AT.M_A.B.M_B
#fn(biobank name, masking vector name, data from A, this data set name, where to store locally, where to copy to remotely)
#subprocess.call([ds_config.source_dir+'A/masked_M1_times_M2.py','A', 'v_A',data_B+'.v_B',data_A,ds_config.temp_dir+'A',ds_config.temp_dir+'client'])


remote_cmd = ds_config.source_dir+'A/masked_M1_times_M2.py A v_A '+data_B+'.v_B '+data_A+' A client'
cmd = 'ssh '+ds_config.remote_settings['A','username']+'@'+ds_config.remote_settings['A','ip_address']+' '+remote_cmd
print cmd
os.system(cmd)




#############################################################
#Get ATA masked.
#############################################################
#fn(biobank name, masking vector name, data set name, where to store locally, where to copy to remotely)
#subprocess.call([ds_config.source_dir+'A/MTM.py','A','v_A',data_A,'A','client'])

remote_cmd = ds_config.source_dir+'A/MTM.py A v_A '+data_A+' A client'
cmd = 'ssh '+ds_config.remote_settings['A','username']+'@'+ds_config.remote_settings['A','ip_address']+' '+remote_cmd
print cmd
os.system(cmd)

#############################################################
#Get BTB masked.
#############################################################
#subprocess.call([ds_config.source_dir+'B/MTM.py','B','v_B',data_B,ds_config.temp_dir+'B',ds_config.temp_dir+'client'])

remote_cmd = ds_config.source_dir+'B/MTM.py B v_B '+data_B+' A client'
cmd = 'ssh '+ds_config.remote_settings['B','username']+'@'+ds_config.remote_settings['B','ip_address']+' '+remote_cmd
print cmd
os.system(cmd)



#############################################################
#Get the sum of each column
#############################################################
#subprocess.call([ds_config.source_dir+'A/sum_M.py','A',data_A,ds_config.temp_dir+'A',ds_config.temp_dir+'client'])
#subprocess.call([ds_config.source_dir+'B/sum_M.py','B',data_B,ds_config.temp_dir+'B',ds_config.temp_dir+'client'])


remote_cmd = ds_config.source_dir+'A/sum_M.py A '+data_A+' A client'
cmd = 'ssh '+ds_config.remote_settings['A','username']+'@'+ds_config.remote_settings['A','ip_address']+' '+remote_cmd
print cmd
os.system(cmd)

remote_cmd = ds_config.source_dir+'B/sum_M.py B '+data_B+' B client'
cmd = 'ssh '+ds_config.remote_settings['B','username']+'@'+ds_config.remote_settings['B','ip_address']+' '+remote_cmd
print cmd
os.system(cmd)

#Get the number of rows in each
remote_cmd = ds_config.source_dir+'common/numrows.py A '+data_A+' A client'
cmd = 'ssh '+ds_config.remote_settings['A','username']+'@'+ds_config.remote_settings['A','ip_address']+' '+remote_cmd
print cmd
os.system(cmd)

remote_cmd = ds_config.source_dir+'common/numrows.py B '+data_B+' B client'
cmd = 'ssh '+ds_config.remote_settings['B','username']+'@'+ds_config.remote_settings['B','ip_address']+' '+remote_cmd
print cmd
os.system(cmd)


#############################################################
#Unmask everything on the client
#############################################################
#height-weight first
subprocess.call([ds_config.source_dir+'client/unmask_M.py','client','v_B','v_B.'+data_A+'.v_A.'+data_B,'half_unmasked.csv',ds_config.temp_dir+'client'])
subprocess.call([ds_config.source_dir+'client/unmask_M.py','client','v_A','half_unmasked.csv','A.B.unmasked.csv',ds_config.temp_dir+'client'])

#weight-height now
subprocess.call([ds_config.source_dir+'client/unmask_M.py','client','v_A','v_A.'+data_B+'.v_B.'+data_A,'half_unmasked.csv',ds_config.temp_dir+'client'])
subprocess.call([ds_config.source_dir+'client/unmask_M.py','client','v_B','half_unmasked.csv','B.A.unmasked.csv',ds_config.temp_dir+'client'])

#height-height
subprocess.call([ds_config.source_dir+'client/unmask_M.py','client','v_A','v_A.'+data_A+'.'+data_A,'A.A.unmasked.csv',ds_config.temp_dir+'client'])

#weight-weight
subprocess.call([ds_config.source_dir+'client/unmask_M.py','client','v_B','v_B.'+data_B+'.'+data_B,'B.B.unmasked.csv',ds_config.temp_dir+'client'])


#Bind all the stuff together
os.system('Rscript client/build_covariance.R')





