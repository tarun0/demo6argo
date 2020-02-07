FROM ubuntu:18.04

USER root
RUN apt-get -y update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN pip3 install http://download.pytorch.org/whl/cpu/torch-1.0.0-cp36-cp36m-linux_x86_64.whl

RUN pip3 install --user fastai
