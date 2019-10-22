FROM oneoffcoder:book-base
LABEL One-Off Coder "info@oneoffcoder.com"

# setup ubuntu
RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get clean

# setup conda
RUN $CONDA_HOME/bin/conda install -c anaconda scikit-learn -y
