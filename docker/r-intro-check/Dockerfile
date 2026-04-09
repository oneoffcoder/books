FROM rocker/r-ver:4.5.3

ENV DEBIAN_FRONTEND=noninteractive \
    PATH=/opt/venv/bin:$PATH \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        gfortran \
        git \
        curl \
        cmake \
        ca-certificates \
        python3 \
        python3-venv \
        python3-pip \
        libcurl4-openssl-dev \
        libssl-dev \
        libxml2-dev \
        libgit2-dev \
        libfontconfig1-dev \
        libfreetype6-dev \
        libfribidi-dev \
        libharfbuzz-dev \
        libjpeg-dev \
        libmbedtls-dev \
        libpng-dev \
        libtiff5-dev \
        libgsl-dev \
    && python3 -m venv /opt/venv \
    && rm -rf /var/lib/apt/lists/*

RUN /opt/venv/bin/pip install --no-cache-dir --upgrade pip \
    && /opt/venv/bin/pip install --no-cache-dir \
    jupyterlab==4.5.6 \
    nbconvert \
    nbclient

COPY install.R /tmp/install.R
RUN Rscript /tmp/install.R && rm /tmp/install.R

WORKDIR /workspace
