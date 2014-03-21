#! /usr/bin/env python

#Take the masking vector and multiply the data by it.

import os
import sys
import shutil

import ds_config


#Get the params
biobank_name = sys.argv[1]
masking_vector_name = sys.argv[2]
masked_data_set_name = sys.argv[3]
unmasked_file_name = sys.argv[4]
unmasked_location_local = sys.argv[5]

print "UNmasking "+masked_data_set_name+" with "+masking_vector_name

#Build file paths
unmasked_data_path_local  = unmasked_location_local+ '/'+unmasked_file_name
print "Saving to: "+unmasked_data_path_local

#Run the R script to mask M
#fn(masking vector path, data set path, output path)
cmd = 'Rscript '+ds_config.source_dir+biobank_name+'/unmask_M.R '
cmd += ds_config.temp_dir+biobank_name+'/'+masking_vector_name+' '
cmd += ds_config.temp_dir+biobank_name+'/'+masked_data_set_name+' '
cmd += unmasked_data_path_local
os.system(cmd)

print "Finished UNmasking "+masked_data_set_name+"\n"
