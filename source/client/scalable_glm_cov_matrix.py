#! /usr/bin/env python

#Build the covariance matrix from all the bits

import os
import sys
import shutil

import ds_config

#sum_M1_file_name = sys.argv[1]
#sum_M2_file_name = sys.argv[2]
#numrows_file_name = sys.argv[3]

cov_matrix_file_name='covariance_matrix.csv'
x_var_list_file_name='explanatory_vars.csv'
y_var_list_file_name='outcome.csv'

print "Solving the GLM!\n\n"

#Build file paths
cov_matrix_path = ds_config.temp_dir+'client/'+cov_matrix_file_name
x_var_list_path = ds_config.temp_dir+'client/'+x_var_list_file_name
y_var_list_path = ds_config.temp_dir+'client/'+y_var_list_file_name

#Run the R script to mask M
#fn(masking vector path, data set path, output path)
cmd = 'Rscript '+ds_config.source_dir+'client/scalable_glm_cov_matrix.R '
cmd += cov_matrix_path+' '
cmd += x_var_list_path+' '
cmd += y_var_list_path
os.system(cmd)

print "\n\nFinished everything!\n"
