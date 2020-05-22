FROM oneoffcoder/book-base:latest
LABEL author="One-Off Coder"
LABEL email="info@oneoffcoder.com"

ENV AWS_REGION="us-east-1"
ENV AWS_ACCESS_KEY="NEED_TO_SET_KEY"
ENV AWS_SECRET_KEY="NEED_TO_SET_SECRET"

# setup ubuntu
RUN apt-get update -y \
    && apt-get upgrade -y

# setup conda
RUN conda install awscli boto3 nodejs -c conda-forge -y

# setup jupyter
RUN jupyter labextension install @ijmbarr/jupyterlab_spellchecker
COPY ubuntu/root/.jupyter /root/.jupyter

# setup aws cli
COPY ubuntu/root/.aws /root/.aws
ADD ubuntu/usr/local/sbin /usr/local/sbin/
ADD ubuntu/etc/supervisor/conf.d /etc/supervisor/conf.d/

RUN apt-get clean