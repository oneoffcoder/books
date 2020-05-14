FROM oneoffcoder/book-base:latest
LABEL One-Off Coder "info@oneoffcoder.com"

# setup ubuntu
# https://stackoverflow.com/questions/53800051/repository-does-not-have-a-release-file-error
RUN sed -i -e 's|disco|eoan|g' /etc/apt/sources.list \
    && apt-get update -y \
    && apt-get upgrade -y \
    && apt-get clean

# setup conda
RUN conda update -n base -c defaults conda \
    && conda install scikit-learn missingno pygraphviz yellowbrick \
        -c anaconda \
        -c conda-forge \
        -c districtdatalabs \
        -y
