#! /usr/bin/env python

#Olly Butters
#28/2/14


#Main controller for the whole thing.
#A=biobank A
#B=biobank B
#C=client
#M=general matrix
#T=transpose


import os
import subprocess
#import numpy

import ds_config

print "\n###############################"
print "Starting vertical datashield(!)\n"

#Top level root directory
print ds_config.root_dir
print ds_config.source_dir
print ds_config.data_dir
print ds_config.temp_dir
print '\n'

#Generate masking vector (M_A). This will copy to A. Do the same for M_B too.
#fn(masking_vector_name, where to store locally, where to copy to remotely)
subprocess.call([ds_config.source_dir+'client/generate_masking_vectors.py','M_A',ds_config.temp_dir+'client',ds_config.temp_dir+'A'])
subprocess.call([ds_config.source_dir+'client/generate_masking_vectors.py','M_B',ds_config.temp_dir+'client',ds_config.temp_dir+'B'])

#############################################################
#Start with A.B M_A.TA

#On A multiply the masking vector by the data to get (AT.M_A)
#fn(biobank name, masking vector name, data set name, where to store locally, where to copy to remotely) 
subprocess.call([ds_config.source_dir+"A/mask_M.py",'A','M_A','height.csv',ds_config.temp_dir+'A',ds_config.temp_dir+'B'])

#On B multiply the masked vector by B.M_B, => AT.M_A.B.M_B
#fn(biobank name, masking vector name, data from A, this data set name, where to store locally, where to copy to remotely)
subprocess.call([ds_config.source_dir+'B/masked_M1_times_M2.py','B', 'M_B','height.csv.M_A','weight.csv',ds_config.temp_dir+'B',ds_config.temp_dir+'client'])
#execfile("b/masked_a_times_b.py")
#############################################################

#############################################################
#Do B.A now
#############################################################
#On B multiply the masking vector by the data to get (BT.M_B)
#fn(biobank name, masking vector name, data set name, where to store locally, where to copy to remotely) 
subprocess.call([ds_config.source_dir+'B/mask_M.py','B','M_B','weight.csv',ds_config.temp_dir+'B',ds_config.temp_dir+'A'])

#On A multiply the masked vector by A.M_A, => AT.M_A.B.M_B
#fn(biobank name, masking vector name, data from A, this data set name, where to store locally, where to copy to remotely)
subprocess.call([ds_config.source_dir+'A/masked_M1_times_M2.py','A', 'M_A','weight.csv.M_B','height.csv',ds_config.temp_dir+'A',ds_config.temp_dir+'client'])


#############################################################
#Get ATA. This is unmasked.
#############################################################
#fn(biobank name, data set name, where to store locally, where to copy to remotely)
subprocess.call([ds_config.source_dir+'A/MTM.py','A','height.csv',ds_config.temp_dir+'A',ds_config.temp_dir+'client'])

#############################################################
#Get BTB. This is unmasked.
#############################################################
subprocess.call([ds_config.source_dir+'B/MTM.py','B','weight.csv',ds_config.temp_dir+'B',ds_config.temp_dir+'client'])



#############################################################
#Put it all together
#Really should get R scripts to output JSON
#############################################################
#AA
aa_file=open("../temp/client/height.csv.height.csv")
aa_value=aa_file.read()
aa_value=aa_value.rstrip()
aa_file.close

#AB
ab_file=open("../temp/client/M_A.weight.csv.M_B.height.csv")
ab_value=ab_file.read()
ab_value=ab_value.rstrip()
ab_file.close


#BB
bb_file=open("../temp/client/weight.csv.weight.csv")
bb_value=bb_file.read()
bb_value=bb_value.rstrip()
bb_file.close

#BA
ba_file=open("../temp/client/M_B.height.csv.M_A.weight.csv")
ba_value=ab_file.read()
ba_value=ab_value.rstrip()
ba_file.close

print "| "+aa_value+" | "+ab_value+" |"
print "| "+ba_value+" | "+bb_value+" |"







