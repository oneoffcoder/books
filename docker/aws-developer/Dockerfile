FROM oneoffcoder/book-base:latest
LABEL One-Off Coder "info@oneoffcoder.com"

ENV AWS_REGION="us-east-1"
ENV AWS_ACCESS_KEY="NEED_TO_SET_KEY"
ENV AWS_SECRET_KEY="NEED_TO_SET_SECRET"

# setup ubuntu
RUN apt-get update -y \
    && apt-get upgrade -y

# setup conda
RUN $CONDA_HOME/bin/conda install awscli boto3 -c conda-forge -y

# setup aws cli
RUN mkdir /root/.aws
COPY /ubuntu/root/.aws/config /root/.aws/config
COPY /ubuntu/root/.aws/credentials /root/.aws/credentials
COPY /ubuntu/usr/local/bin/setup-awscli.sh /usr/local/sbin/setup-awscli.sh
COPY /ubuntu/etc/supervisor/conf.d/aws-cli.conf /etc/supervisor/conf.d/aws-cli.conf

RUN apt-get clean