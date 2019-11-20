FROM oneoffcoder/book-base:latest
LABEL One-Off Coder "info@oneoffcoder.com"

# setup ubuntu
RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get install build-essential git -y \
    && apt-get clean

# setup conda
RUN $CONDA_HOME/bin/conda install pytorch torchvision cpuonly -c pytorch -y
RUN $CONDA_HOME/bin/pip install pycocotools
