from fastai.vision import *

import os
import sys
import pathlib

flow=open("/tmp/flow.txt", "a")
flow.write('\n==============Training started=============\n')

path = pathlib.Path(os.getcwd())
print(sys.argv[-1])
os.chdir('/tmp')
if not sys.argv[-1].endswith('json') and not sys.argv[-1].endswith('py') :
    path = pathlib.Path(sys.argv[-1])
    flow.write('Path provided in arguments. Set to: ' + str(path)+ '\n')
    print('setting to' , path)
else:
    path = pathlib.Path('/tmp')
    print('Path not provided as argument. Defaulting to /tmp :', path)
    flow.write('Path not provided as argument. Defaulting to /tmp :  ' + str(path) + '\n')

print(os.listdir(path))
classes = ['guns','teddys']

np.random.seed(42)
data = ImageDataBunch.from_folder(path, train=".", valid_pct=0.2,
        ds_tfms=get_transforms(), size=95, num_workers=1).normalize(imagenet_stats)


learn = cnn_learner(data, models.resnet34, metrics=error_rate)
learn.fit_one_cycle(3)

flow.write('\nModel trained. Saving...\n')

learn.save('mymodel')

flow.write('\nModel Saved!\n')
name = 'final model.pkl'
learn.export(path/name)

flow.write('\nModel Exported!\n')

print("Model exported after training")

flow.write('\n==============Training ended=============\n')
flow.close()
