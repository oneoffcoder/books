FROM oneoffcoder/conda-deeplearning:latest
LABEL author="One-Off Coder"
LABEL email="info@oneoffcoder.com"

# setup ubuntu
RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get install libgraphviz-dev ffmpeg -y \
    && apt-get clean

# setup libraries
RUN conda install autograd gensim nltk pyldavis nodejs pygraphviz tqdm missingno wordcloud shap -c conda-forge -y \
    && conda install -c anaconda pygraphviz -y \
    && pip install yellowbrick librosa textblob fancyimpute \
    && pip install pybbn \
    && python -m nltk.downloader all