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
masked_data_path_local  = ds_config.temp_dir+masked_location_local+'/'+masking_vector_name+'.'+data_from_M1+'.'+data_set_name
masked_data_path_remote  = ds_config.temp_dir+masked_location_remote+'/'+masking_vector_name+'.'+data_from_M1+'.'+data_set_name
print "Saving to: "+masked_data_path_local

#Run R script
cmd = 'Rscript '+ds_config.source_dir+'B/masked_M1_times_M2.R '
cmd += ds_config.temp_dir+biobank_name+'/'+masking_vector_name+' '
cmd += ds_config.temp_dir+biobank_name+'/'+data_from_M1+' '
cmd += ds_config.data_dir+biobank_name+'/'+data_set_name+' '
cmd += masked_data_path_local
os.system(cmd)

#Copy files to data dirs
print "Copying to: "+masked_data_path_remote
#shutil.copyfile(masked_data_path_local,masked_data_path_remote)

if ds_config.local_only == True:
    #Copy file to data dir
    print "Copying to: "+masked_data_path_remote
    shutil.copyfile(masked_data_path_local,masked_data_path_remote)
else:
    #Do something                                                                                                                                                   
    print "else"
    cmd = 'scp '+masked_data_path_local+' '+ds_config.remote_settings['client','username']+'@'+ds_config.remote_settings['client','ip_address']+':'+masked_data_path_remote
    print cmd



print 'Finished masking '+masking_vector_name+'.'+data_from_M1+'.'+data_set_name+'\n'
