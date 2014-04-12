#! /usr/bin/env python

#get rid of any old temp data sitting around

import os
import shutil

import ds_config


#Get rid of the temp dir if it exists                                                                                                                                                               
if (os.path.exists(ds_config.root_dir+'/temp') == True):
    shutil.rmtree(ds_config.root_dir+'/temp')

#Make the temp dir and its sub dirs.                                                                                                                                                                
os.mkdir(ds_config.root_dir+'/temp')
os.mkdir(ds_config.root_dir+'/temp/A')
os.mkdir(ds_config.root_dir+'/temp/B')
os.mkdir(ds_config.root_dir+'/temp/client')
