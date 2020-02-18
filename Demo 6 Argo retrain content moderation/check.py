import os
import sys

flow=open("/tmp/flow.txt", "a")
flow.write('\n==============Checking started=============\n')
os.chdir('/tmp')

testfile = (os.listdir(os.getcwd()+'/test'))[0]
if sys.argv[-1].endswith('jpg'):
    print('testfile provided: ', sys.argv[-1])
    flow.write('\n Checking file (from argument): '+sys.argv[-1] + '\n')
else:
    print('Trying with default...', os.path.join(os.path.abspath(os.getcwd()),testfile))
    flow.write('\n Checking default file: '+ str(os.path.join(os.path.abspath(os.getcwd()),testfile)) + '\n')

f=open("check-output.txt", "w")

result = ''
if testfile.startswith('new') and testfile.endswith('jpg'):
        #print('new image file: ' + f)
    result = 'retrain'
    print(result)
    f.write(result)
    flow.write('Detected new image: Retrain\n')
elif testfile.startswith('new') and not testfile.endswith('jpg'):
    result = 'new file: ' + f
    print(result)
elif testfile.endswith('jpg'):
    result = 'predict'
    print(result)
    f.write(result)
    flow.write('Detected image: Predict\n')
else:
    result = ('some file')
    print(result)
flow.write('\n==============Checking ended=============\n')
