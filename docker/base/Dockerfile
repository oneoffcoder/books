FROM ubuntu:disco
LABEL One-Off Coder "info@oneoffcoder.com"

ENV CONDA_HOME=/usr/local/conda
ENV PATH=${CONDA_HOME}/bin:${PATH}
ENV NOTEBOOK_PASSWORD=""

# setup ubuntu
RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get -y install wget supervisor \
    && apt-get clean

# setup conda
RUN wget -q https://repo.anaconda.com/archive/Anaconda3-2019.07-Linux-x86_64.sh -O /tmp/Anaconda3-2019.07-Linux-x86_64.sh \
    && /bin/bash /tmp/Anaconda3-2019.07-Linux-x86_64.sh -b -p $CONDA_HOME \
    && $CONDA_HOME/bin/conda update -n root conda -y
COPY ubuntu/root/.jupyter /root/.jupyter/

# setup volumes
RUN mkdir /root/ipynb
VOLUME [ "/root/ipynb" ]

# setup supervisor
COPY ubuntu/etc/supervisor/supervisor.conf /etc/supervisor/supervisor.conf
COPY ubuntu/etc/supervisor/conf.d/all.conf /etc/supervisor/conf.d/all.conf

# clean up
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf", "-n"]