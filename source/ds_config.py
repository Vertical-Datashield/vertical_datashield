#! /usr/bin/env python

import os

#Set up the directory paths
#root_dir=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
#root_dir="/home/ob13747/vertical_datashield/vertical_datashield/trunk"
root_dir="/home/vds/vertical_datashield"
source_dir=root_dir+"/source/"
data_dir=root_dir+"/data/"
temp_dir=root_dir+"/temp/"

#Flag to decide if copy things locally or remotely. True/False
local_only=False

#Some settings of remote hosts. Only used if local_only=False
remote_settings = {}
remote_settings['A','username']='vds'
remote_settings['A','ip_address']='192.168.56.100'

remote_settings['B','username']='vds'
remote_settings['B','ip_address']='192.168.56.101'

remote_settings['client','username']='vds'
remote_settings['client','ip_address']='192.168.56.102'

#username='vds'
#client_ip='192.168.56.100'
#host_A_ip='192.168.56.101'
#host_B_ip='192.168.56.102'
