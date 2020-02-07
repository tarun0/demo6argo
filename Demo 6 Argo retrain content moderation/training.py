#!/usr/bin/env python
# coding: utf-8

# In[2]:


from fastai.vision import *

path = Path('/tmp/data/bears')
print(path.ls())


classes = ['teddys','grizzly','black']

np.random.seed(42)
data = ImageDataBunch.from_folder(path, train=".", valid_pct=0.2,
        ds_tfms=get_transforms(), size=224, num_workers=0).normalize(imagenet_stats)


# In[3]:


learn = cnn_learner(data, models.resnet34, metrics=error_rate)
learn.fit_one_cycle(4)
learn.unfreeze()
learn.lr_find()
# If the plot is not showing try to give a start and end learning rate
# learn.lr_find(start_lr=1e-5, end_lr=1e-1)
learn.recorder.plot()
learn.fit_one_cycle(2, max_lr=slice(3e-5,3e-4))

learn.save('stage-2')

interp = ClassificationInterpretation.from_learner(learn)

interp.plot_confusion_matrix()

learn.export()

print("Model exported after training")

