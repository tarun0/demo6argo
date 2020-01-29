FROM tensorflow/tensorflow:latest
RUN apt-get -y update
RUN pip install -q pyyaml h5py
RUN apt-get install -y git

ADD train.py /t/train.py
ADD pull.py /t/pull.py
ADD push.py /t/push.py

WORKDIR /t
