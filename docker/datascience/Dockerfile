FROM oneoffcoder/conda-deeplearning:latest
LABEL One-Off Coder "info@oneoffcoder.com"

# setup ubuntu
RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get install libgraphviz-dev -y \
    && apt-get clean

# setup libraries
RUN conda install gensim nltk pyldavis nodejs pygraphviz -c conda-forge -y \
    && python -m nltk.downloader all