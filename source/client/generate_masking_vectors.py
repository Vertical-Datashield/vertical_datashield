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
biobank_name = sys.argv[1]
masking_vector_name = sys.argv[2]
masking_vector_location_client = sys.argv[3]
masking_vector_location_remote = sys.argv[4]

print "Generating masking vector "+masking_vector_name

#Build location where this will get saved
masking_vector_path_client = masking_vector_location_client + '/' + masking_vector_name
print "Saving to: " + masking_vector_path_client


#Run the R script to make the masking vectors
cmd = 'Rscript '+ds_config.source_dir+'client/generate_masking_vector.R '
cmd += masking_vector_path_client+' '
cmd += '2'
os.system(cmd)

#Build location where this will get saved remotely
masking_vector_path_remote = masking_vector_location_remote + '/' + masking_vector_name
print "Copying to: " + masking_vector_path_remote

if ds_config.local_only == True:
    #Copy file to data dir
    shutil.copyfile(masking_vector_path_client,masking_vector_path_remote)
else:
    #Do something
    print "else"
    cmd = 'scp '+masking_vector_path_client+' '+ds_config.remote_settings[biobank_name,'username']+'@'+ds_config.remote_settings[biobank_name,'ip_address']+':'+masking_vector_path_remote
    print cmd
    os.system(cmd)


print "Finished generating masking vector\n"
