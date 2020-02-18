import os    
import shutil
import sys

flow=open("/tmp/flow.txt", "a")
flow.write('\n==============Copy started=============\n')
os.chdir('/tmp')

testfile = (os.listdir(os.getcwd()+'/test'))[0]
sourcefilepath = os.path.join(os.path.abspath(os.getcwd()+'/test'),testfile)
if sys.argv[-1].endswith('jpg'):
    testfile = sys.argv[-1]
    sourcefilepath = os.path.join(os.path.abspath(os.getcwd()+'/test'),sys.argv[-1])
    print('testfile provided in arguments: ', sourcefilepath)
    flow.write(' Testfile found in arg ' + str(sourcefilepath))
else:
    print('Copy: Trying with default...', os.path.join(os.path.abspath(os.getcwd()+'/test'),testfile))
    flow.write(' Default file ' + str(os.path.join(os.path.abspath(os.getcwd()+'/test'),testfile)))

sourcePathTeddy = os.path.join(os.path.abspath(os.getcwd()+'/data/teddys'),testfile)
sourcePathGuns = os.path.join(os.path.abspath(os.getcwd()+'/data/guns'),testfile)

if testfile.startswith('newt') and testfile.endswith('jpg'):
        #print('new image file: ' + f)
    print( 'Copied to teddy: ', shutil.copyfile(sourcefilepath, sourcePathTeddy))
elif testfile.startswith('newg') and testfile.endswith('jpg'):
    print('Copied to Guns', shutil.copyfile(sourcefilepath, sourcePathGuns))

flow.write('\n==============Copy ended=============\n')
