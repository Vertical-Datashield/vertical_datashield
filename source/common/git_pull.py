#! /usr/bin/env python

#Do a git pull on all VMs - including this one.

import os

import ds_config


cmd = 'ssh '+ds_config.remote_settings['A','username']+'@'+ds_config.remote_settings['A','ip_address']+' \'cd vertical_datashield; git pull\''
print cmd
os.system(cmd)

cmd = 'ssh '+ds_config.remote_settings['B','username']+'@'+ds_config.remote_settings['B','ip_address']+' \'cd vertical_datashield; git pull\''
print cmd
os.system(cmd)


cmd = 'ssh '+ds_config.remote_settings['client','username']+'@'+ds_config.remote_settings['client','ip_address']+' \'cd vertical_datashield; git pull\''
print cmd
os.system(cmd)
