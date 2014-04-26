#! /usr/bin/env python

#Build the covariance matrix from all the bits

import os
import sys
import shutil

import ds_config

sum_M1_file_name = sys.argv[1]
sum_M2_file_name = sys.argv[2]
numrows_file_name = sys.argv[3]

#sum_M1_file_name='sum.height_2.csv'
#sum_M2_file_name='sum.weight_2.csv'
#numrows_file_name='numrows.weight_2.csv'

M1M1_file_name='A.A.unmasked.csv'
M1M2_file_name='A.B.unmasked.csv'
M2M1_file_name='B.A.unmasked.csv'
M2M2_file_name='B.B.unmasked.csv'

covariance_out_file_name='covariance_matrix.csv'

print "Building the covariance matrix"

#Build file paths
M1M1_path = ds_config.temp_dir+'client/'+M1M1_file_name
M1M2_path = ds_config.temp_dir+'client/'+M1M2_file_name
M2M1_path = ds_config.temp_dir+'client/'+M2M1_file_name
M2M2_path = ds_config.temp_dir+'client/'+M2M2_file_name

sum_M1_path = ds_config.temp_dir+'client/'+sum_M1_file_name
sum_M2_path = ds_config.temp_dir+'client/'+sum_M2_file_name

numrows_path = ds_config.temp_dir+'client/'+numrows_file_name

covariance_out_path = ds_config.temp_dir+'client/'+covariance_out_file_name

#Run the R script to mask M
#fn(masking vector path, data set path, output path)
cmd = 'Rscript '+ds_config.source_dir+'client/build_covariance.R '
cmd += M1M1_path+' '
cmd += M1M2_path+' '
cmd += M2M1_path+' '
cmd += M2M2_path+' '
cmd += sum_M1_path+' '
cmd += sum_M2_path+' '
cmd += numrows_path+' '
cmd += covariance_out_path
os.system(cmd)

print "Finished building covariance matrix\n"
