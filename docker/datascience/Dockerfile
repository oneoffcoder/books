FROM oneoffcoder/conda-deeplearning:latest
LABEL One-Off Coder "info@oneoffcoder.com"

# setup ubuntu
RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get install libgraphviz-dev ffmpeg -y \
    && apt-get clean

# setup libraries
RUN conda install autograd gensim nltk pyldavis nodejs pygraphviz tqdm missingno wordcloud shap -c conda-forge -y \
    && pip install yellowbrick librosa textblob \
    && python -m nltk.downloader all