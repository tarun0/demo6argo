#!/usr/bin/env python
# coding: utf-8

# In[40]:


from fastai.vision import *
import os

testfile = (os.listdir(os.curdir+'/test'))[0]
testfilepath = os.path.join(os.path.abspath(os.curdir+'/test'),testfile)
if sys.argv[-1].endswith('jpg'):
    testfile = sys.argv[-1]
    testfilepath = os.path.join(os.path.abspath(os.curdir+'/test'),sys.argv[-1])
    print('testfile provided: ', testfilepath)
else:
    print('no file provided. trying with default...', os.path.join(os.path.abspath(os.curdir+'/test'),testfile))


# In[35]:


def start_prediction():
    base_path = 'data'
    path = Path(base_path+ '/items')
    print('Content of dir where model will be searched: ', path.ls())

    defaults.device = torch.device('cpu')

    img = open_image(testfilepath)

    learn = load_learner(path, 'final model.pkl')

    pred_class,pred_idx,outputs = learn.predict(img)
    print("Predicted class: ", pred_class)


# In[36]:


#path = Path('/tmp/data/bears')
#print(path.ls())
print(testfile)
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
    start_prediction()
else:
    result = ('some file')
    print(result)


# In[ ]:




