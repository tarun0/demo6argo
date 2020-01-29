import os
import subprocess
import time

from subprocess import Popen, PIPE, STDOUT


def upload_model():
	print('Uploading model by running git commands...')
	p1 = Popen('git add my_model.h5', universal_newlines=True, shell=True, stdout=PIPE, stdin=PIPE, stderr=STDOUT)
	time.sleep(2)
	
	p2= Popen('git commit -m "commit message"',universal_newlines=True, shell=True, stdout=PIPE, stdin=PIPE, stderr=STDOUT)
	time.sleep(2)

	p3 = Popen('git push origin master', universal_newlines=True, shell=True, stdout=PIPE, stdin=PIPE, stderr=STDOUT)
	time.sleep(20)
	print('Model Uploaded!')
