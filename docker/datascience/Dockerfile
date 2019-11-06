FROM oneoffcoder/conda-deeplearning:latest
LABEL One-Off Coder "info@oneoffcoder.com"

# setup ubuntu
RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get install libgraphviz-dev -y \
    && apt-get clean

# setup libraries
# && conda install yellowbrick -c districtdatalabs -y \
# && conda install fancyimpute -c gwerbin -y \
# librosa textblob
RUN conda install autograd gensim nltk pyldavis nodejs pygraphviz tqdm missingno wordcloud shap -c conda-forge -y \
    && python -m nltk.downloader all