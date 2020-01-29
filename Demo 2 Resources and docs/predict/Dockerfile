FROM tensorflow/tensorflow:latest
RUN apt-get -y update
RUN pip install -q pyyaml h5py
RUN apt-get install -y git

ADD predict.py /t/predict.py
ADD pull.py /t/pull.py

WORKDIR /t
