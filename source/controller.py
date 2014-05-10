#! /usr/bin/env python

###########################################################################
#Olly Butters
#10/5/14


#Main controller for the whole thing.
#A=biobank A
#B=biobank B
#C=client
#M=general matrix
#T=transpose

#A good way to see what is going on is to run
#watch -d ls -ltr temp/A
#etc on each VM, then you see the files being made and passed around.
###########################################################################

#Import the system libs
import os
import shutil
import subprocess
import time
import sys

#Import local stuff
import ds_config

sys.path.append('common')
from run_remote_cmd import run_remote_cmd

###########################################################################
#User vars. These would probably come from the clients R script.
#Define the dataset names
#data_A='height.csv'
#data_B='weight.csv'


data_A='height_2.csv'
data_B='weight_2.csv'
outcome_var='weight_2'
explanatory_vars=['height','weight_1']


#data_A='a.csv'
#data_B='b.csv'
#outcome_var='selfharm'
#explanatory_vars=['smoke','random1']


###########################################################################



print "\n###############################"
print "Starting vertical datashield(!)\n"

#############################################################
#Get rid of the temp dirs if they exist on each VM
#############################################################
subprocess.call(ds_config.source_dir+'common/tidy_paths.py')
cmd = 'ssh '+ds_config.remote_settings['A','username']+'@'+ds_config.remote_settings['A','ip_address']+' '+ds_config.source_dir+'common/tidy_paths.py'
os.system(cmd)
cmd = 'ssh '+ds_config.remote_settings['B','username']+'@'+ds_config.remote_settings['B','ip_address']+' '+ds_config.source_dir+'common/tidy_paths.py'
os.system(cmd)

#have a little nap to let the watch command catch up and show directories are empty
time.sleep(4)

#Top level root directory
print ds_config.root_dir
print ds_config.source_dir
print ds_config.data_dir
print ds_config.temp_dir
print '\n'


#############################################################
#Get the summaries of each data set. This would be a good
#point to check if things are ok, e.g. same number of rows etc
#############################################################
remote_cmd = ds_config.source_dir+'common/summary_M.py A '+data_A+' A client'
cmd = 'ssh '+ds_config.remote_settings['A','username']+'@'+ds_config.remote_settings['A','ip_address']+' '+remote_cmd
print cmd
os.system(cmd)

remote_cmd = ds_config.source_dir+'common/summary_M.py B '+data_B+' B client'
cmd = 'ssh '+ds_config.remote_settings['B','username']+'@'+ds_config.remote_settings['B','ip_address']+' '+remote_cmd
print cmd
os.system(cmd)

#Grab the summary data from the files and store it locally
summary = {}
file_path=ds_config.temp_dir+'client/summary.'+data_A
with open(file_path) as myfile:
    for line in myfile:
        name, var = line.partition(",")[::2]
        summary['A',name.strip("\"")] = var.strip()

file_path=ds_config.temp_dir+'client/summary.'+data_B
with open(file_path) as myfile:
    for line in myfile:
        name, var = line.partition(",")[::2]
        summary['B',name.strip("\"")] = var.strip()


print summary


#Output the outcome and explanatory vars into a file
f = open(ds_config.temp_dir+'client/outcome.csv', 'w')
f.write('\"'+outcome_var+'\"\n')
f.close

temp=",".join("\""+this_var+"\"" for this_var in explanatory_vars)
temp+='\n'
f = open(ds_config.temp_dir+'client/explanatory_vars.csv', 'w')
f.write(temp)
f.close



#############################################################
#Generate masking vector (v_A). This will copy to A. Do the same for v_B too.
#############################################################
#fn(masking_vector_name, where to store locally, where to copy to remotely)
subprocess.call([ds_config.source_dir+'client/generate_masking_vectors.py','A','v_A',summary['A','num_cols'],ds_config.temp_dir+'client',ds_config.temp_dir+'A'])
subprocess.call([ds_config.source_dir+'client/generate_masking_vectors.py','B','v_B',summary['B','num_cols'],ds_config.temp_dir+'client',ds_config.temp_dir+'B'])


#############################################################
#Calculate A.B
#############################################################
#On A multiply the masking vector by the data to get (AT.v_A)
#fn(biobank name, masking vector name, data set name, where to store locally, where to copy to remotely) 
#subprocess.call([ds_config.source_dir+"A/mask_MT.py",'A','v_A',data_A,'A','B'])
remote_cmd = ds_config.source_dir+"common/mask_MT.py A v_A "+data_A+" A B"
run_remote_cmd("A", remote_cmd)

#On B multiply the masked vector by B.v_B, => AT.v_A.B.v_B
#fn(biobank name, masking vector name, data from A, this data set name, where to store locally, where to copy to remotely)
#subprocess.call([ds_config.source_dir+'B/masked_M1_times_M2.py','B', 'v_B',data_A+'.v_A',data_B,ds_config.temp_dir+'B',ds_config.temp_dir+'client'])
remote_cmd = ds_config.source_dir+'common/masked_M1_times_M2.py B v_B '+data_A+'.v_A '+data_B+' B client'
run_remote_cmd("B", remote_cmd)

#############################################################


#############################################################
#Do B.A now
#############################################################
#On B multiply the masking vector by the data to get (BT.M_B)
#fn(biobank name, masking vector name, data set name, where to store locally, where to copy to remotely) 
#subprocess.call([ds_config.source_dir+'B/mask_MT.py','B','v_B',data_B,ds_config.temp_dir+'B',ds_config.temp_dir+'A'])

remote_cmd = ds_config.source_dir+"common/mask_MT.py B v_B "+data_B+" B A"
run_remote_cmd("B", remote_cmd)

#On A multiply the masked vector by A.M_A, => AT.M_A.B.M_B
#fn(biobank name, masking vector name, data from A, this data set name, where to store locally, where to copy to remotely)
#subprocess.call([ds_config.source_dir+'A/masked_M1_times_M2.py','A', 'v_A',data_B+'.v_B',data_A,ds_config.temp_dir+'A',ds_config.temp_dir+'client'])


remote_cmd = ds_config.source_dir+'common/masked_M1_times_M2.py A v_A '+data_B+'.v_B '+data_A+' A client'
run_remote_cmd("A", remote_cmd)

#############################################################
#Get ATA masked.
#############################################################
#fn(biobank name, masking vector name, data set name, where to store locally, where to copy to remotely)
#subprocess.call([ds_config.source_dir+'A/MTM.py','A','v_A',data_A,'A','client'])

remote_cmd = ds_config.source_dir+'common/MTM.py A v_A '+data_A+' A client'
run_remote_cmd("A", remote_cmd)

#############################################################
#Get BTB masked.
#############################################################
#subprocess.call([ds_config.source_dir+'B/MTM.py','B','v_B',data_B,ds_config.temp_dir+'B',ds_config.temp_dir+'client'])

remote_cmd = ds_config.source_dir+'common/MTM.py B v_B '+data_B+' A client'
run_remote_cmd("B", remote_cmd)


#############################################################
#Get the sum of each column
#############################################################
remote_cmd = ds_config.source_dir+'common/sum_M.py A '+data_A+' A client'
run_remote_cmd("A", remote_cmd)

remote_cmd = ds_config.source_dir+'common/sum_M.py B '+data_B+' B client'
run_remote_cmd("B", remote_cmd)

#############################################################
#Get the number of rows in each
#############################################################
remote_cmd = ds_config.source_dir+'common/numrows.py A '+data_A+' A client'
run_remote_cmd("A", remote_cmd)

remote_cmd = ds_config.source_dir+'common/numrows.py B '+data_B+' B client'
run_remote_cmd("B", remote_cmd)

#############################################################
#Unmask everything on the client
#############################################################
#height-weight first
#subprocess.call([ds_config.source_dir+'client/unmask_M.py','client','v_B','v_B.'+data_A+'.v_A.'+data_B,'half_unmasked.csv',ds_config.temp_dir+'client'])
#subprocess.call([ds_config.source_dir+'client/unmask_M.py','client','v_A','half_unmasked.csv','A.B.unmasked.csv',ds_config.temp_dir+'client'])
subprocess.call([ds_config.source_dir+'client/unmask_M.py','client','v_A','v_B.'+data_A+'.v_A.'+data_B,'A.B.unmasked.csv',ds_config.temp_dir+'client'])
#subprocess.call([ds_config.source_dir+'client/unmask_M.py','client','v_A','half_unmasked.csv','A.B.unmasked.csv',ds_config.temp_dir+'client'])


#weight-height now
#subprocess.call([ds_config.source_dir+'client/unmask_M.py','client','v_A','v_A.'+data_B+'.v_B.'+data_A,'half_unmasked.csv',ds_config.temp_dir+'client'])
#subprocess.call([ds_config.source_dir+'client/unmask_M.py','client','v_B','half_unmasked.csv','B.A.unmasked.csv',ds_config.temp_dir+'client'])
subprocess.call([ds_config.source_dir+'client/unmask_M.py','client','v_B','v_A.'+data_B+'.v_B.'+data_A,'B.A.unmasked.csv',ds_config.temp_dir+'client'])
#subprocess.call([ds_config.source_dir+'client/unmask_M.py','client','v_B','half_unmasked.csv','B.A.unmasked.csv',ds_config.temp_dir+'client'])


#height-height
subprocess.call([ds_config.source_dir+'client/unmask_M.py','client','v_A','v_A.'+data_A+'.'+data_A,'A.A.unmasked.csv',ds_config.temp_dir+'client'])

#weight-weight
subprocess.call([ds_config.source_dir+'client/unmask_M.py','client','v_B','v_B.'+data_B+'.'+data_B,'B.B.unmasked.csv',ds_config.temp_dir+'client'])


#Bind all the stuff together to make the covarianve matrix
subprocess.call([ds_config.source_dir+'client/build_covariance.py','sum.'+data_A,'sum.'+data_B,'numrows.'+data_A])


#Solve the GLM with the covariance matrix
subprocess.call([ds_config.source_dir+'client/scalable_glm_cov_matrix.py'])





