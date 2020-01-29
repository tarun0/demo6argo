import os
import subprocess
import time

from subprocess import Popen, PIPE, STDOUT

# Method to run git commands to fetch the model from Github
def download_model():
	print('Pulling model from git by running git commands...')
	p0 = Popen('git init', universal_newlines=True, shell=True,  stdin=PIPE, stderr=STDOUT)
	print('initializing...')
	time.sleep(2)
	p1= Popen('git remote add origin https://tarun0:workstation21@github.com/tarun0/aidevops.git',universal_newlines=True, shell=True,  stdin=PIPE, stderr=STDOUT)
	time.sleep(2)
        print('1 added remote')
	p2 = Popen('git config --global user.email "tarun.mudgal@aricent.com"', universal_newlines=True, shell=True,  stdin=PIPE, stderr=STDOUT)
	time.sleep(2)
	print('2 user mail')	
	p3 = Popen('git config --global user.name "Tarun"', universal_newlines=True, shell=True,  stdin=PIPE, stderr=STDOUT)
	time.sleep(2)
	print('3 name set')	
	p4 = Popen('git pull origin master', universal_newlines=True, shell=True, stdin=PIPE, stderr=STDOUT)
	print('4 Fetching model from Github')
	time.sleep(12)
	print('4 Model Fetched')
