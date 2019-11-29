FROM nvidia/cuda:10.0-cudnn7-devel

ENV DEBIAN_FRONTEND=noninteractive
ENV CONDA_HOME="/opt/anaconda"
ENV PATH="${CONDA_HOME}/bin:${PATH}"
ENV JUPYTER_TYPE=lab

# update OS
RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install wget supervisor -y

# setup supervisor
COPY jupyter.conf /etc/supervisor/conf.d/

# install conda
RUN wget -q https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh -O /tmp/anaconda.sh && \
    /bin/bash /tmp/anaconda.sh -b -p $CONDA_HOME

# install python packages
RUN conda install pytorch torchvision cudatoolkit=10.0 -y -c pytorch

# setup mount point
VOLUME ["/ipynb"]

# setup ports
EXPOSE 8888

# clean up
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf", "-n"]