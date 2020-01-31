# Draft 1

# Installation Docs https://www.kubeflow.org/docs/fairing/install-fairing/#set-up-kubeflow-fairing-in-a-hosted-jupyter-notebook

#refer https://www.docker.com/blog/docker-can-now-run-within-docker/

FROM gcr.io/kubeflow-images-public/tensorflow-2.0.0a0-notebook-cpu:v0.7.0

# To install software/dependencies
USER root

# Fairing use docker to pakckage code. Install Docker
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common \
    lxc \
    iptables
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
RUN add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

RUN apt-get update
RUN apt-get install -y docker-ce docker-ce-cli containerd.io

RUN apt-get install --reinstall -y systemd
RUN exec bash && systemctl start docker
#RUN systemctl start docker
# Add docker to sudo group
#RUN usermod -aG docker $(whoami)

ENV SHELL /bin/bash
RUN exec bash
# Verify Docker installation
#RUN ls -l /var/run/docker.sock
RUN whoami 
#RUN docker ps

# default notebook doesn't have virtualenv
RUN pip3 install virtualenv

# Make virtual environment and activate it 
RUN virtualenv venv --python=python3
RUN source venv/bin/activate

# Install Kubeflow Fairing 
RUN pip3 install kubeflow-fairing

# Verify installation
RUN pip3 show kubeflow-fairing

# RUN Jupyter lab
CMD ["sh", "-c", "jupyter lab --notebook-dir=/home/jovyan --ip=0.0.0.0 --no-browser --allow-root --port=8888 --LabApp.token='' --LabApp.password='' --LabApp.allow_origin='*' --LabApp.base_url=${NB_PREFIX}"]
