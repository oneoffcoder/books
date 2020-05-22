FROM oneoffcoder/spark-jupyter:latest
LABEL author="One-Off Coder"
LABEL email="info@oneoffcoder.com"

# setup ubuntu
RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get clean

COPY ubuntu/etc/supervisor/conf.d/*.conf /etc/supervisor/conf.d/
COPY ubuntu/usr/local/bin/*.py /usr/local/bin/

RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*