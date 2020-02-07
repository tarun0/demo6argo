#!/usr/bin/env python
# coding: utf-8

# In[3]:


from fastai.vision import *

path = Path('/tmp/data/bears')
print(path.ls())

defaults.device = torch.device('cpu')

img = open_image('testimage.jpg')

learn = load_learner(path)

pred_class,pred_idx,outputs = learn.predict(img)
print("Predicted class: ", pred_class)


# In[ ]:




