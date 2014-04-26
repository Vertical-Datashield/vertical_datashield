#! /usr/bin/env python

#Figure out the sum of each column
#Not masked.

import os
import sys
import shutil

import ds_config

#Get the params
biobank_name = sys.argv[1]
data_set_name = sys.argv[2]
summary_M_location_local = sys.argv[3]
summary_M_location_remote = sys.argv[4]

print "Getting summary data for "+data_set_name

#Build file paths
summary_M_data_path_local  = ds_config.temp_dir+summary_M_location_local+ '/summary.'+data_set_name
summary_M_data_path_remote = ds_config.temp_dir+summary_M_location_remote+'/summary.'+data_set_name
print "Saving to: "+summary_M_data_path_local

#Run the R script to mask A
cmd = 'Rscript '+ds_config.source_dir+'common/summary_M.R '
cmd += ds_config.data_dir+biobank_name+'/'+data_set_name+' '
cmd += summary_M_data_path_local
os.system(cmd)


#Copy files to data dirs

if ds_config.local_only == True:
    #Copy file to data dir
    print "Copying to: "+summary_M_data_path_remote
    shutil.copyfile(summary_M_data_path_local,summary_M_data_path_remote)
else:
    #Copy the data to the remote client
    cmd = 'scp '+summary_M_data_path_local+' '+ds_config.remote_settings['client','username']+'@'+ds_config.remote_settings['client','ip_address']+':'+summary_M_data_path_remote
    print cmd
    os.system(cmd)

print "Finished generating summary data for "+data_set_name+"\n"
