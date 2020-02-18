from fastai.vision import *

import sys
import pathlib

folder1 = 'guns'
file1 = 'guns.csv'

folder2 = 'teddys'
file2 = 'teddys.csv'

f=open("flow.txt", "w")
f.write('==============Loading started=============\n')

path = pathlib.Path('data')
print(sys.argv[-1])

if not sys.argv[-1].endswith('json') and not sys.argv[-1].endswith('py') :
    path = pathlib.Path(sys.argv[-1])
    f.write('Path provided in arguments. Set to: ' + str(path)+ '\n')
    print('setting to' , path)
else:
    print('Path not provided as argument. Defaulting to: ', path)
    f.write('Path not provided as argument. Defaulting to: ' + str(path) + '\n')

dest1 = path/folder1
dest1.mkdir(parents=True, exist_ok=True)

dest2 = path/folder2
dest2.mkdir(parents=True, exist_ok=True)

classes = ['guns','teddys']
download_images(file1, dest1, max_pics=95)
download_images(file2, dest2, max_pics=95)


verify_images(path/classes[0], delete=True, max_size=95)

verify_images(path/classes[1], delete=True, max_size=95)
f.write('==============Loading ended=============\n')
