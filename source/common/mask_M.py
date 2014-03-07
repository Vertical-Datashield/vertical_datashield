#! /usr/bin/env python

#Take the masking vector and multiply the data by it.

import os
import sys
import shutil

import ds_config


#Get the params
biobank_name = sys.argv[1]
masking_vector_name = sys.argv[2]
data_set_name = sys.argv[3]
masked_location_local = sys.argv[4]
masked_location_remote = sys.argv[5]

print "Masking "+data_set_name+" with "+masking_vector_name

#Build file paths
masked_data_path_local  = masked_location_local+ '/'+data_set_name+'.'+masking_vector_name
masked_data_path_remote = masked_location_remote+'/'+data_set_name+'.'+masking_vector_name
print "Saving to: "+masked_data_path_local

#Run the R script to mask M
#fn(masking vector path, data set path, output path)
cmd = 'Rscript '+ds_config.source_dir+biobank_name+'/mask_M.R '+ds_config.temp_dir+'/'+biobank_name+'/'+masking_vector_name+' '+ds_config.data_dir+'/'+biobank_name+'/'+data_set_name+' '+masked_data_path_local
os.system(cmd)


#Copy files to data dirs
print "Copying to: "+masked_data_path_remote
shutil.copyfile(masked_data_path_local,masked_data_path_remote)

print "Finished masking "+data_set_name+"\n"
