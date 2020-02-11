#!/usr/bin/env python
# coding: utf-8

# In[3]:


#!/usr/bin/env python
# coding: utf-8

# In[2]:


from fastai.vision import *

base_path = 'data'
path = Path(base_path+ '/items')
print(path.ls())


classes = ['guns','teddys']

np.random.seed(42)
data = ImageDataBunch.from_folder(path, train=".", valid_pct=0.2,
        ds_tfms=get_transforms(), size=95, num_workers=1).normalize(imagenet_stats)


# In[8]:


learn = cnn_learner(data, models.resnet34, metrics=error_rate)
learn.fit_one_cycle(3)


# In[9]:


learn.save('mymodel')


# In[13]:


learn.export('final model.pkl')

print("Model exported after training")


# In[ ]:




