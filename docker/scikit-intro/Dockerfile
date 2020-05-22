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
# https://stackoverflow.com/questions/53800051/repository-does-not-have-a-release-file-error
RUN sed -i -e 's|disco|eoan|g' /etc/apt/sources.list \
    && apt-get update -y \
    && apt-get upgrade -y \
    && apt-get install libgraphviz-dev ffmpeg -y \
    && apt-get clean

# setup conda
RUN conda update -n base -c defaults conda \
    && conda install scikit-learn missingno pygraphviz yellowbrick squarify \
        -c anaconda \
        -c conda-forge \
        -c districtdatalabs \
        -y
