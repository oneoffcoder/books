FROM oneoffcoder/book-base:latest
LABEL One-Off Coder "info@oneoffcoder.com"

# setup ubuntu
RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get clean

# setup conda
RUN $CONDA_HOME/bin/conda install scikit-learn missingno -c anaconda -c conda-forge -y
