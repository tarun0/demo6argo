#!/usr/bin/env python
# coding: utf-8

# In[2]:


from fastai.vision import *

folder1 = 'black'
file1 = 'urls_black.csv'

folder2 = 'teddys'
file2 = 'urls_teddys.csv'

folder3 = 'grizzly'
file3 = 'urls_grizzly.csv'

path = Path('/tmp/data/bears')
print(path.ls())

dest1 = path/folder1
dest1.mkdir(parents=True, exist_ok=True)

dest2 = path/folder2
dest2.mkdir(parents=True, exist_ok=True)

dest3 = path/folder3
dest3.mkdir(parents=True, exist_ok=True)

classes = ['teddys','grizzly','black']
download_images(path/file1, dest1, max_pics=95)
download_images(path/file2, dest2, max_pics=95)
download_images(path/file3, dest3, max_pics=95)


verify_images(path/classes[0], delete=True, max_size=95)

verify_images(path/classes[1], delete=True, max_size=95)

verify_images(path/classes[2], delete=True, max_size=95)

np.random.seed(42)
data = ImageDataBunch.from_folder(path, train=".", valid_pct=0.2,
        ds_tfms=get_transforms(), size=224, num_workers=4).normalize(imagenet_stats)

print(data.classes)


# In[ ]:




