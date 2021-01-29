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

# setup ubuntu
RUN apt-get update -y \
    && apt-get upgrade -y \
    && DEBIAN_FRONTEND=noninteractive apt-get install graphviz libgraphviz-dev pkg-config ffmpeg -y \
    && apt-get clean

# setup conda
RUN conda install -c conda-forge pygraphviz missingno squarify shap xgboost lightgbm catboost plotly eli5 sklearn-contrib-lightning boruta_py stumpy tsfresh imbalanced-learn -y \
    && conda install -c districtdatalabs yellowbrick -y \
    && pip install lime \
    && conda install -y -c conda-forge python-blosc cytoolz dask dask-ml lz4 dask-labextension \
    && jupyter labextension install dask-labextension
