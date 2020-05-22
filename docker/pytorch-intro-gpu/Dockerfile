FROM oneoffcoder/conda-deeplearning:latest
LABEL author="One-Off Coder"
LABEL email="info@oneoffcoder.com"

# setup ubuntu
RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get install git -y \
    && apt-get clean

RUN pip install pycocotools
