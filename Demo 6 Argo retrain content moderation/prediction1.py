from fastai.vision import *
import os

flow=open("/tmp/flow.txt", "a")
flow.write('\n==============Prediction started=============\n')

os.chdir('/tmp')
testfile = (os.listdir(os.getcwd()+'/test'))[0]
testfilepath = os.path.join(os.path.abspath(os.getcwd()+'/test'),testfile)
if sys.argv[-1].endswith('jpg'):
    testfile = sys.argv[-1]
    testfilepath = os.path.join(os.path.abspath(os.getcwd()+'/test'),sys.argv[-1])
    print('testfile provided: ', testfilepath)
    flow.write('Provided file: ' + str(testfilepath) + '\n')
else:
    print('no file provided. trying with default...', os.path.join(os.path.abspath(os.getcwd()+'/test'),testfile))
    flow.write('Using default file: ' + str(os.path.join(os.path.abspath(os.getcwd()+'/test')),testfile) + '\n')


def start_prediction():
    base_path = os.getcwd()
    path = Path(base_path)
    print('Content of dir where model will be searched: ', path.ls())
    flow.write('Content of dir where model will be searched ' + str(path) + '\n')

    defaults.device = torch.device('cpu')

    img = open_image(testfilepath)

    learn = load_learner(path, 'final model.pkl')

    pred_class,pred_idx,outputs = learn.predict(img)
    print("Predicted class: ", pred_class)
    print("Predicted output: ", str(outputs))
    flow.write('Predictions:\n ' + str(pred_class) + '\n Outputs:---\n' + str(outputs) + '\n')
    

start_prediction()

flow.write('\n==============Prediction ended=============\n')
