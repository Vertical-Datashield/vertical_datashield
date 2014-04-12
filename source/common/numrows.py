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
sum_M_location_local = sys.argv[3]
sum_M_location_remote = sys.argv[4]

print "Numrows "+data_set_name

#Build file paths
sum_M_data_path_local  = sum_M_location_local+ '/numrows.'+data_set_name
sum_M_data_path_remote = sum_M_location_remote+'/numrows.'+data_set_name
print "Saving to: "+sum_M_data_path_local

#Run the R script to mask A
cmd = 'Rscript '+ds_config.source_dir+'common/numrows.R '
cmd += ds_config.data_dir+biobank_name+'/'+data_set_name+' '
cmd += sum_M_data_path_local
os.system(cmd)


#Copy files to data dirs
#print "Copying to: "+sum_M_data_path_remote
#shutil.copyfile(sum_M_data_path_local,sum_M_data_path_remote)

if ds_config.local_only == True:
    #Copy file to data dir
    print "Copying to: "+sum_M_data_path_remote
    shutil.copyfile(sum_M_data_path_local,sum_M_data_path_remote)
else:
    #Copy the data to the remote client
    cmd = 'scp '+sum_M_data_path_local+' '+ds_config.remote_settings['client','username']+'@'+ds_config.remote_settings['client','ip_address']+':'+sum_M_data_path_remote
    print cmd

print "Finished numrows "+data_set_name+"\n"
