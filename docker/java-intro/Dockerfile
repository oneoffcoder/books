FROM oneoffcoder:book-base
LABEL One-Off Coder "info@oneoffcoder.com"

# setup ubuntu
RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get -y install openjdk-12-jdk unzip \
    && apt-get clean

# setup conda
RUN wget -q https://github.com/SpencerPark/IJava/releases/download/v1.3.0/ijava-1.3.0.zip -O /tmp/ijava-1.3.0.zip \
    && unzip /tmp/ijava-1.3.0.zip -d /tmp/ijava \
    && python /tmp/ijava/install.py --sys-prefix

# clean up
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
