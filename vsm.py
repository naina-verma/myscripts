#!/usr/bin/python

import os
from avocado.utils import process


def vsm_plugin_install():
    ''' method installs the cdk vagrant plugins '''
    ''' returns the output of the vagrant plugin install cmd '''
    cmd = "vagrant plugin install ./vagrant-registration-*.gem ./vagrant-sshfs-*.gem ./vagrant-service-manager-*.gem"
    out = process.run(cmd, shell=True)
    return out


def vsm_env_info(vagrant_BOX_PATH, service):
    ''' method to get the env variable details for 
        services and returns the output of the cmd '''
    os.chdir(vagrant_BOX_PATH)
    cmd = "vagrant service-manager env %s" %(service)
    out = process.run(cmd, shell=True)
    return out


def vsm_box_info(vagrant_BOX_PATH, option, readable):
    ''' method to get the box version and ip details 
        and returns the output of the cmd '''
    try:
	os.chdir(vagrant_BOX_PATH)
	cmd = "vagrant service-manager box %s %s" %(option, readable)
    	out = process.run(cmd, shell=True)
    	return out
    except:
	print "Could NOT get the info of the Vagrant box. Maybe something went wrong..."

def vsm_service_handling(vagrant_BOX_PATH, operation, service):
    ''' method to start/stop/restart and get status of 
        services and returns the output of the cmd '''
    os.chdir(vagrant_BOX_PATH)
    cmd = "vagrant service-manager %s %s" %(operation, service)
    out = process.run(cmd, shell=True)
    return out

def vsm_is_service_running(vagrant_BOX_PATH, service):
    ''' checks status of service and returns True if running '''
    try:
        os.chdir(vagrant_BOX_PATH)
        cmd = "vagrant service-manager status %s" %(service)
        out = process.run(cmd, shell=True)
        if "%s - running\n" %(service) == out.stdout:
	    return True
        elif "%s - stopped\n" %(service) == out.stdout:
            return False
    except:
	print "Could NOT get the status of the service. Maybe something went wrong..."






