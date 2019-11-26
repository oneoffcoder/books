FROM oneoffcoder/r-jupyter:latest
LABEL One-Off Coder "info@oneoffcoder.com"

# setup ubuntu
RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get install libcurl4-openssl-dev libssl-dev -y \
    && apt-get clean

# install R packages
RUN Rscript \
    -e "repos <- 'https://cloud.r-project.org/'" \
    -e "dependencies <- c('Depends', 'Imports', 'LinkingTo', 'Suggests', 'Enhances')" \
    -e "a <- c('ggplot2', 'viridis', 'corrplot', 'progress', 'devtools')" \
    -e "b <- c('ggExtra', 'leaflet', 'plotly', 'pROC', 'sets', 'mclust', 'fpc')" \
    -e "c <- c('plyr', 'lsa', 'caret', 'twitteR', 'e1071', 'fastAdaboost')" \
    -e "d <- c('quanteda', 'sentimentr', 'randomForest', 'ggrepel', 'rmarkdown')" \
    -e "e <- c('R6', 'jsonlite', 'lubridate', 'microbenchmark', 'shiny', 'shinythemes')" \
    -e "f <- c('tidyverse', 'readr', 'comprehenr', 'maps', 'mapproj', 'ggthemes')" \
    -e "g <- c('mice', 'VIM', 'Amelia', 'missForest', 'mi')" \
    -e "h <- c('skimr', 'RANN', 'gbm', 'xgboost', 'caretEnsemble', 'C50', 'earth')" \
    -e "i <- c('Hmisc')" \
    -e "libs <- c(a, b, c, d, e, f)" \
    -e "install.packages(libs, repos=repos, Ncpus=10, dependencies=dependencies)" \
    -e "install.packages(g, repos=repos, Ncpus=10, dependencies=dependencies)" \
    -e "install.packages(h, repos=repos, Ncpus=10, dependencies=dependencies)" \
    -e "install.packages(i, repos=repos, Ncpus=10, dependencies=dependencies)" \
    -e "library(devtools)" \
    -e "install_github('vqv/ggbiplot')" \
    -e "install_version('caret', version='6.0-84')"
