#! /usr/bin/env python

#Generate the masking vectors on the client then 
#send them to A/B


#import os
import shutil
import subprocess
import os
import sys

import ds_config

#Get the params
masking_vector_name = sys.argv[1]
masking_vector_location_client = sys.argv[2]
masking_vector_location_remote = sys.argv[3]

print "Generating masking vector "+masking_vector_name

#Build location where this will get saved
masking_vector_path_client = masking_vector_location_client + '/' + masking_vector_name
print "Saving to: " + masking_vector_path_client


#Run the R script to make the masking vectors
cmd = 'Rscript '+ds_config.source_dir+'client/generate_masking_vector.R '+masking_vector_path_client+' 2'
os.system(cmd)

#Build location where this will get saved remotely
masking_vector_path_remote = masking_vector_location_remote + '/' + masking_vector_name
print "Copying to: " + masking_vector_path_remote

#Copy file to data dir
shutil.copyfile(masking_vector_path_client,masking_vector_path_remote)

print "Finished generating masking vector\n"
