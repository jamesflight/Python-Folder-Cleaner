#! /usr/local/bin/python3

import time
import os
import yaml
import shutil

directory = os.path.dirname(os.path.realpath(__file__))
configFile = open(directory + '/config.yaml', 'r').read()

config = yaml.load(configFile)

seconds = 86400 * config['days_to_keep_files']

time_ago = time.time() - seconds

def process_folder(folder):
	os.chdir(folder)
	for somefile in os.listdir(folder):
	    st=os.stat(somefile)
	    mtime=st.st_mtime
	    if mtime < time_ago:
	    	if os.path.isfile(somefile):
	    		os.unlink(somefile)
	    	else:
	        	shutil.rmtree(somefile)

for i, folder in enumerate(config['folders']):
	process_folder(folder)

