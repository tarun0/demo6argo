#!/usr/bin/env python
# coding: utf-8

# In[11]:


from fastai.vision import *
import os

testfile = (os.listdir(os.curdir+'/test'))[0]
if sys.argv[-1].endswith('jpg'):
    print('testfile provided: ', sys.argv[-1])
else:
    print('no file provided. trying with default...', os.path.join(os.path.abspath(os.curdir),testfile))


# In[13]:


#path = Path('/tmp/data/bears')
#print(path.ls())
result = ''
if testfile.startswith('new') and testfile.endswith('jpg'):
        #print('new image file: ' + f)
    result = 'retrain'
    print(result)
elif testfile.startswith('new') and not testfile.endswith('jpg'):
    result = 'new file: ' + f
    print(result)
elif testfile.endswith('jpg'):
    result = 'predict'
    print(result)
else:
    result = ('some file')
    print(result)


# In[ ]:




