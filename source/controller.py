#! /usr/bin/env python

#Olly Butters
#21/3/14


#Main controller for the whole thing.
#A=biobank A
#B=biobank B
#C=client
#M=general matrix
#T=transpose


import os
import shutil
import subprocess

import ds_config

print "\n###############################"
print "Starting vertical datashield(!)\n"

#Get rid of the temp dir if it exists
if (os.path.exists('../temp') == True):
    shutil.rmtree('../temp')

#Make the temp dir and its sub dirs.
os.mkdir('../temp')
os.mkdir('../temp/A')
os.mkdir('../temp/B')
os.mkdir('../temp/client')



#Top level root directory
print ds_config.root_dir
print ds_config.source_dir
print ds_config.data_dir
print ds_config.temp_dir
print '\n'

#############################################################
#Generate masking vector (v_A). This will copy to A. Do the same for v_B too.
#fn(masking_vector_name, where to store locally, where to copy to remotely)
subprocess.call([ds_config.source_dir+'client/generate_masking_vectors.py','v_A',ds_config.temp_dir+'client',ds_config.temp_dir+'A'])
subprocess.call([ds_config.source_dir+'client/generate_masking_vectors.py','v_B',ds_config.temp_dir+'client',ds_config.temp_dir+'B'])


#############################################################
#Start with A.B M_A.TA

#On A multiply the masking vector by the data to get (AT.v_A)
#fn(biobank name, masking vector name, data set name, where to store locally, where to copy to remotely) 
subprocess.call([ds_config.source_dir+"A/mask_M.py",'A','v_A','height.csv',ds_config.temp_dir+'A',ds_config.temp_dir+'B'])

#On B multiply the masked vector by B.v_B, => AT.v_A.B.v_B
#fn(biobank name, masking vector name, data from A, this data set name, where to store locally, where to copy to remotely)
subprocess.call([ds_config.source_dir+'B/masked_M1_times_M2.py','B', 'v_B','height.csv.v_A','weight.csv',ds_config.temp_dir+'B',ds_config.temp_dir+'client'])
#execfile("b/masked_a_times_b.py")
#############################################################


#############################################################
#Do B.A now
#############################################################
#On B multiply the masking vector by the data to get (BT.M_B)
#fn(biobank name, masking vector name, data set name, where to store locally, where to copy to remotely) 
subprocess.call([ds_config.source_dir+'B/mask_M.py','B','v_B','weight.csv',ds_config.temp_dir+'B',ds_config.temp_dir+'A'])

#On A multiply the masked vector by A.M_A, => AT.M_A.B.M_B
#fn(biobank name, masking vector name, data from A, this data set name, where to store locally, where to copy to remotely)
subprocess.call([ds_config.source_dir+'A/masked_M1_times_M2.py','A', 'v_A','weight.csv.v_B','height.csv',ds_config.temp_dir+'A',ds_config.temp_dir+'client'])


#############################################################
#Get ATA masked.
#############################################################
#fn(biobank name, masking vector name, data set name, where to store locally, where to copy to remotely)
subprocess.call([ds_config.source_dir+'A/MTM.py','A','v_A','height.csv',ds_config.temp_dir+'A',ds_config.temp_dir+'client'])


#############################################################
#Get BTB masked.
#############################################################
subprocess.call([ds_config.source_dir+'B/MTM.py','B','v_B','weight.csv',ds_config.temp_dir+'B',ds_config.temp_dir+'client'])



#############################################################
#Unmask everything on the client
#############################################################
#height-weight first
subprocess.call([ds_config.source_dir+'client/unmask_M.py','client','v_B','v_B.height.csv.v_A.weight.csv','half_unmasked.csv',ds_config.temp_dir+'client'])
subprocess.call([ds_config.source_dir+'client/unmask_M.py','client','v_A','half_unmasked.csv','A.B.unmasked.csv',ds_config.temp_dir+'client'])

#weight-height now
subprocess.call([ds_config.source_dir+'client/unmask_M.py','client','v_A','v_A.weight.csv.v_B.height.csv','half_unmasked.csv',ds_config.temp_dir+'client'])
subprocess.call([ds_config.source_dir+'client/unmask_M.py','client','v_B','half_unmasked.csv','B.A.unmasked.csv',ds_config.temp_dir+'client'])

#height-height
subprocess.call([ds_config.source_dir+'client/unmask_M.py','client','v_A','v_A.height.csv.height.csv','height_height_unmasked.csv',ds_config.temp_dir+'client'])

#weight-weight
subprocess.call([ds_config.source_dir+'client/unmask_M.py','client','v_B','v_B.weight.csv.weight.csv','weight_weight_unmasked.csv',ds_config.temp_dir+'client'])



#############################################################
#Put it all together
#Really should get R scripts to output JSON
#############################################################
#AA
aa_file=open("../temp/client/height_height_unmasked.csv")
aa_value=aa_file.read()
aa_value=aa_value.rstrip()
aa_file.close

#AB
#ab_file=open("../temp/client/v_A.weight.csv.v_B.height.csv")
ab_file=open("../temp/client/A.B.unmasked.csv")
ab_value=ab_file.read()
ab_value=ab_value.rstrip()
ab_file.close

#BB
bb_file=open("../temp/client/weight_weight_unmasked.csv")
bb_value=bb_file.read()
bb_value=bb_value.rstrip()
bb_file.close

#BA
#ba_file=open("../temp/client/v_B.height.csv.v_A.weight.csv")
ba_file=open("../temp/client/B.A.unmasked.csv")
ba_value=ba_file.read()
ba_value=ba_value.rstrip()
ba_file.close

print "| "+aa_value+" | "+ab_value+" |"
print "| "+ba_value+" | "+bb_value+" |"







