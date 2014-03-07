#! /usr/bin/env python

#Take a matrix (M) and multiply it by its transpose.
#Not masked.

import os
import sys
import shutil

import ds_config

#Get the params
biobank_name = sys.argv[1]
#masking_vector_name = sys.argv[2]
data_set_name = sys.argv[2]
MTM_location_local = sys.argv[3]
MTM_location_remote = sys.argv[4]

print "Multiplying "+data_set_name+" by itself"

#Build file paths
MTM_data_path_local  = MTM_location_local+ '/'+data_set_name+'.'+data_set_name
MTM_data_path_remote = MTM_location_remote+'/'+data_set_name+'.'+data_set_name
print "Saving to: "+MTM_data_path_local

#Run the R script to mask A
cmd = 'Rscript '+biobank_name+'/MTM.R '+ds_config.data_dir+biobank_name+'/'+data_set_name+' '+MTM_data_path_local
os.system(cmd)


#Copy files to data dirs
print "Copying to: "+MTM_data_path_remote
shutil.copyfile(MTM_data_path_local,MTM_data_path_remote)

print "Finished self multiplying "+data_set_name+"\n"
