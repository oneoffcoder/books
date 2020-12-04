FROM oneoffcoder/r-jupyter:latest
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
    && DEBIAN_FRONTEND=noninteractive apt-get install libcurl4-openssl-dev libssl-dev -y \
    && apt-get clean

# install R packages
RUN Rscript \
    -e "repos <- 'https://cloud.r-project.org/'" \
    -e "dependencies <- c('Depends', 'Imports', 'LinkingTo', 'Suggests', 'Enhances')" \
    -e "a <- c('ggplot2', 'viridis', 'corrplot', 'progress', 'devtools')" \
    -e "b <- c('ggExtra', 'leaflet', 'plotly', 'pROC', 'PRROC', 'sets', 'mclust', 'fpc')" \
    -e "c <- c('plyr', 'lsa', 'caret', 'twitteR', 'e1071', 'fastAdaboost')" \
    -e "d <- c('quanteda', 'sentimentr', 'randomForest', 'ggrepel', 'rmarkdown')" \
    -e "e <- c('R6', 'jsonlite', 'lubridate', 'microbenchmark', 'shiny', 'shinythemes')" \
    -e "f <- c('tidyverse', 'readr', 'comprehenr', 'maps', 'mapproj', 'ggthemes')" \
    -e "g <- c('mice', 'VIM', 'Amelia', 'missForest', 'mi')" \
    -e "h <- c('skimr', 'RANN', 'gbm', 'xgboost', 'caretEnsemble', 'C50', 'earth')" \
    -e "i <- c('Hmisc', 'mlr3', 'survival', 'survey', 'nlme', 'multcomp', 'vcd')" \
    -e "j <- c('BayesNetBP', 'bnlearn', 'bnpa', 'BNSL', 'bnstruct', 'bnviewer', 'catnet', 'dbnlearn', 'dbnR', 'deal')" \
    -e "k <- c('sem', 'lavaan', 'lava', 'tidySEM', 'blavaan', 'bsem', 'gSEM', 'netSEM', 'psychonetrics', 'regsem', 'rsem', 'SELF')" \
    -e "l <- c('survivalmodels', 'survivalMPL', 'survivalsvm', 'CausalMBSTS', 'causalweight')" \
    -e "libs <- c(a, b, c, d, e, f)" \
    -e "install.packages(libs, repos=repos, Ncpus=10, dependencies=dependencies)" \
    -e "install.packages(g, repos=repos, Ncpus=10, dependencies=dependencies)" \
    -e "install.packages(h, repos=repos, Ncpus=10, dependencies=dependencies)" \
    -e "install.packages(i, repos=repos, Ncpus=10, dependencies=dependencies)" \
    -e "install.packages(j, repos=repos, Ncpus=10, dependencies=dependencies)" \
    -e "install.packages(k, repos=repos, Ncpus=10, dependencies=dependencies)" \
    -e "install.packages(l, repos=repos, Ncpus=10, dependencies=dependencies)" \
    -e "library(devtools)" \
    -e "install_github('vqv/ggbiplot')" \
    -e "install_version('caret', version='6.0-84')"
