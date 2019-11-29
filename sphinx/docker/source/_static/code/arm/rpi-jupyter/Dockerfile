FROM rpi-base:local

ENV CONDA_HOME=/root/miniconda
ENV PATH=${CONDA_HOME}/bin:${PATH}
ENV JUPYTER_TYPE=lab

# setup OS
RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install supervisor -y

# setup supervisor
COPY jupyter.conf /etc/supervisor/conf.d/

# setup miniconda: scikit-learn numpy scipy matplotlib
RUN wget -q http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-armv7l.sh -O /tmp/miniconda.sh && \
    /bin/bash /tmp/miniconda.sh -b -p /root/miniconda && \
    conda update -n root conda -y && \
    conda update --all -y && \
    pip install --upgrade pip && \
    conda config --add channels rpi && \
    conda install python=3.6 -y && \
    conda install jupyter jupyterlab -y -c anaconda -c conda-forge

# setup mount point
RUN mkdir /ipynb
VOLUME ["/ipynb"]

# setup ports
EXPOSE 8888

# clean up
RUN apt-get clean

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf", "-n"]