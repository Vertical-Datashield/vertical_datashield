#! /usr/bin/env python

import os
import ds_config

def run_remote_cmd(location, remote_cmd):
    cmd = 'ssh '+ds_config.remote_settings[location,'username']+'@'+ds_config.remote_settings[location,'ip_address']+' '+remote_cmd
    print cmd
    os.system(cmd)
