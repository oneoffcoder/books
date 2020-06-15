FROM ubuntu:eoan
LABEL org="One-Off Coder"
LABEL author="Jee Vang, Ph.D."
LABEL email="info@oneoffcoder.com"
LABEL website="https://www.oneoffcoder.com"
LABEL facebook="https://www.facebook.com/oneoffcoder"
LABEL twitter="https://twitter.com/oneoffcoder"
LABEL instagram="https://www.instagram.com/oneoffcoder/"
LABEL youtube="https://www.youtube.com/channel/UCCCv8Glpb2dq2mhUj5mcHCQ"
LABEL linkedin="https://www.linkedin.com/company/one-off-coder"

ENV NODE_HOME=/usr/local/node-v14.4.0-linux-x64
ENV CONDA_HOME=/usr/local/conda
ENV PATH=${NODE_HOME}/bin:${CONDA_HOME}/bin:${PATH}
ENV NOTEBOOK_PASSWORD=""

# setup ubuntu
RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get -y install wget supervisor \
    && apt-get clean

# setup nodejs
RUN wget -q https://nodejs.org/dist/v14.4.0/node-v14.4.0-linux-x64.tar.xz -O /tmp/node-v14.4.0-linux-x64.tar.xz \
    && tar xf /tmp/node-v14.4.0-linux-x64.tar.xz -C /usr/local \
    && node --version \
    && npm --version

# setup conda
RUN wget -q https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /tmp/anaconda.sh \
    && /bin/bash /tmp/anaconda.sh -b -p $CONDA_HOME \
    && conda update --all \
    && conda install -c conda-forge nodejs \
    && conda install xeus-cling -c conda-forge -y \
    && conda install -c conda-forge jupyterlab -y \
    && conda update -c conda-forge jupyterlab \
    && pip install jupyterlab-commenting-service \
    && jupyter labextension install @jupyterlab/commenting-extension @jupyterlab/toc @krassowski/jupyterlab-lsp \
    && conda install -c conda-forge python-language-server r-languageserver
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