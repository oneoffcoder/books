FROM oneoffcoder/conda-deeplearning:latest
LABEL org="One-Off Coder"
LABEL author="Jee Vang, Ph.D."
LABEL website="https://www.oneoffcoder.com"
LABEL email="info@oneoffcoder.com"
LABEL facebook="https://www.facebook.com/oneoffcoder"
LABEL twitter="https://twitter.com/oneoffcoder"
LABEL instagram="https://www.instagram.com/oneoffcoder/"
LABEL youtube="https://www.youtube.com/channel/UCCCv8Glpb2dq2mhUj5mcHCQ"
LABEL linkedin="https://www.linkedin.com/company/one-off-coder"

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