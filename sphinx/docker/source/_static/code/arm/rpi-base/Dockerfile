FROM arm32v7/ubuntu

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y && \
    apt-get upgrade -y

RUN apt-get install -y \
    wget \
    build-essential \
    tk-dev \
    libncurses5-dev \
    libncursesw5-dev \
    libreadline6-dev \
    libdb5.3-dev \
    libgdbm-dev \
    libsqlite3-dev \
    libssl-dev \
    libbz2-dev \
    libexpat1-dev \
    liblzma-dev \
    zlib1g-dev \
    libffi-dev \
    gfortran \
    libopenblas-dev \
    liblapack-dev \
    python-dev \
    default-libmysqlclient-dev \
    libfreetype6-dev \
    libxml2-dev \
    libxslt1-dev

RUN apt-get clean