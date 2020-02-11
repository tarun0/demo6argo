#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os    
import shutil
import sys

testfile = (os.listdir(os.curdir+'/test'))[0]
sourcefilepath = os.path.join(os.path.abspath(os.curdir+'/test'),testfile)
if sys.argv[-1].endswith('jpg'):
    testfile = sys.argv[-1]
    sourcefilepath = os.path.join(os.path.abspath(os.curdir+'/test'),sys.argv[-1])
    print('testfile provided in arguments: ', sourcefilepath)
else:
    print('no file provided. trying with default...', os.path.join(os.path.abspath(os.curdir+'/test'),testfile))

sourcePathTeddy = os.path.join(os.path.abspath(os.curdir+'/data/items/teddys'),testfile)
sourcePathGuns = os.path.join(os.path.abspath(os.curdir+'/data/items/guns'),testfile)

if testfile.startswith('newt') and testfile.endswith('jpg'):
        #print('new image file: ' + f)
    print( 'Copied to teddy: ', shutil.copyfile(sourcefilepath, sourcePathTeddy))
elif testfile.startswith('newg') and testfile.endswith('jpg'):
    print('Copied to Guns', shutil.copyfile(sourcefilepath, sourcePathGuns))
