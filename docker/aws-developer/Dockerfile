FROM oneoffcoder/book-base:latest
LABEL org="One-Off Coder"
LABEL author="Jee Vang, Ph.D."
LABEL email="info@oneoffcoder.com"
LABEL website="https://www.oneoffcoder.com"
LABEL facebook="https://www.facebook.com/oneoffcoder"
LABEL twitter="https://twitter.com/oneoffcoder"
LABEL instagram="https://www.instagram.com/oneoffcoder/"
LABEL youtube="https://www.youtube.com/channel/UCCCv8Glpb2dq2mhUj5mcHCQ"
LABEL linkedin="https://www.linkedin.com/company/one-off-coder"

ENV AWS_REGION="us-east-1"
ENV AWS_ACCESS_KEY="NEED_TO_SET_KEY"
ENV AWS_SECRET_KEY="NEED_TO_SET_SECRET"

# setup ubuntu
RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get clean

# setup conda
RUN pip install awscli boto3 nodejs

# setup jupyter
RUN jupyter labextension install @ijmbarr/jupyterlab_spellchecker

# setup aws cli
COPY ubuntu/root/.aws /root/.aws
ADD ubuntu/usr/local/sbin /usr/local/sbin/
ADD ubuntu/etc/supervisor/conf.d /etc/supervisor/conf.d/