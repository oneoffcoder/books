FROM oneoffcoder/r-jupyter:latest
LABEL One-Off Coder "info@oneoffcoder.com"

# setup ubuntu
RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get install libcurl4-openssl-dev libssl-dev -y \
    && apt-get clean

# install R packages
RUN Rscript \
    -e "libs <- c('ggplot2', 'viridis', 'corrplot', 'ggbiplot', 'progress', 'devtools')" \
    -e "install.packages(libs, repos='https://mirrors.nics.utk.edu/cran/')" \
    -e "library(devtools)" \
    -e "install_github('vqv/ggbiplot')"