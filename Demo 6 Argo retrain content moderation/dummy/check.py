import random

f=open("/tmp/check-output.txt", "w")
coin = random.randint(1, 2)

if (coin==1):
    print('predict')
    f.write('predict')
else:
    print('retrain')
    f.write('retrain')

f.close()
