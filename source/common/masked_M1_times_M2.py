#! /usr/bin/env python
#This runs on M2
#Take the masked value of M1 and multiply by M2

import os
import sys
import shutil

import ds_config

#Get the params
biobank_name = sys.argv[1]
masking_vector_name = sys.argv[2]
data_from_M1 = sys.argv[3]
data_set_name = sys.argv[4]
masked_location_local = sys.argv[5]
masked_location_remote = sys.argv[6]

print 'Calculating '+masking_vector_name+'.'+data_from_M1+'.'+data_set_name
#masked_data_path_local  = masked_location_local+ '/A.M_A.B.M_B'
masked_data_path_local  = masked_location_local+'/'+masking_vector_name+'.'+data_from_M1+'.'+data_set_name
#masked_data_path_remote = masked_location_remote+'/A.M_A.B.M_B'
masked_data_path_remote  = masked_location_remote+'/'+masking_vector_name+'.'+data_from_M1+'.'+data_set_name
print "Saving to: "+masked_data_path_local

#Run R script
cmd = 'Rscript '+ds_config.source_dir+'B/masked_M1_times_M2.R '+ds_config.temp_dir+'/'+biobank_name+'/'+masking_vector_name+' '+ds_config.temp_dir+'/'+biobank_name+'/'+data_from_M1+' '+ds_config.data_dir+'/'+biobank_name+'/'+data_set_name+' '+masked_data_path_local
os.system(cmd)

#Copy files to data dirs
print "Copying to: "+masked_data_path_remote
shutil.copyfile(masked_data_path_local,masked_data_path_remote)

print 'Finished masking '+masking_vector_name+'.'+data_from_M1+'.'+data_set_name+'\n'
