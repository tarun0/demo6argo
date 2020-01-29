import kfp
from kfp import dsl

#Container one to download docker image, train the model and push it to Github
def trainscript():
    return dsl.ContainerOp(
        name='Train Model',
        image='docker.io/tarun0/demo2train:v6',
        command=['sh', '-c'],
	arguments=['python $0','train.py'],
    )
    
#Container two to download docker image, download the model and then predict
def predictscript():
   return dsl.ContainerOp(
        name='Predict Output',
        image='docker.io/tarun0/demo2predict:v6',
        command=['sh', '-c'],
	arguments=['python $0','predict.py']
    )

@dsl.pipeline(
    name='Demo2',
    description='A simple MNIST pipeline'
)

# Pipeline method. .after(comp) assures that the component will run when comp has finished
def demo2pipeline():
    training = trainscript()
    predict = predictscript().after(training)

if __name__ == '__main__':
    kfp.compiler.Compiler().compile(demo2pipeline, __file__ + '.tar.gz')
