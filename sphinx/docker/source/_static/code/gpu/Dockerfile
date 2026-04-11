FROM nvidia/cuda:13.1.1-cudnn-devel-ubuntu24.04

ENV DEBIAN_FRONTEND=noninteractive
ENV JUPYTER_TYPE=lab

RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install --no-install-recommends python3 python3-pip python3-venv supervisor -y && \
    rm -rf /var/lib/apt/lists/*

COPY jupyter.conf /etc/supervisor/conf.d/

RUN python3 -m pip install --no-cache-dir --break-system-packages \
    jupyterlab \
    torch \
    torchvision \
    torchaudio

VOLUME ["/ipynb"]

EXPOSE 8888

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf", "-n"]
