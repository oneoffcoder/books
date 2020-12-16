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
    && DEBIAN_FRONTEND=noninteractive apt-get install libcurl4-openssl-dev libssl-dev libv8-dev -y \
    && apt-get clean \
    && ln -s /bin/tar /bin/gtar

# install R packages
RUN Rscript \
    -e "repos <- 'https://cloud.r-project.org/'" \
    -e "dependencies <- c('Depends', 'Imports', 'LinkingTo', 'Suggests', 'Enhances')" \
    -e "libs <- c('ggplot2', 'viridis', 'corrplot', 'progress', 'devtools')" \
    -e "install.packages(libs, repos=repos, Ncpus=10, dependencies=dependencies)"
RUN Rscript \
    -e "repos <- 'https://cloud.r-project.org/'" \
    -e "dependencies <- c('Depends', 'Imports', 'LinkingTo', 'Suggests', 'Enhances')" \
    -e "libs <- c('ggExtra', 'leaflet', 'plotly', 'pROC', 'PRROC', 'sets', 'mclust', 'fpc')" \
    -e "install.packages(libs, repos=repos, Ncpus=10, dependencies=dependencies)"
RUN Rscript \
    -e "repos <- 'https://cloud.r-project.org/'" \
    -e "dependencies <- c('Depends', 'Imports', 'LinkingTo', 'Suggests', 'Enhances')" \
    -e "libs <- c('plyr', 'lsa', 'caret', 'twitteR', 'e1071', 'fastAdaboost')" \
    -e "install.packages(libs, repos=repos, Ncpus=10, dependencies=dependencies)"
RUN Rscript \
    -e "repos <- 'https://cloud.r-project.org/'" \
    -e "dependencies <- c('Depends', 'Imports', 'LinkingTo', 'Suggests', 'Enhances')" \
    -e "libs <- c('quanteda', 'sentimentr', 'randomForest', 'ggrepel', 'rmarkdown')" \
    -e "install.packages(libs, repos=repos, Ncpus=10, dependencies=dependencies)"
RUN Rscript \
    -e "repos <- 'https://cloud.r-project.org/'" \
    -e "dependencies <- c('Depends', 'Imports', 'LinkingTo', 'Suggests', 'Enhances')" \
    -e "libs <- c('R6', 'jsonlite', 'lubridate', 'microbenchmark', 'shiny', 'shinythemes')" \
    -e "install.packages(libs, repos=repos, Ncpus=10, dependencies=dependencies)"
RUN Rscript \
    -e "repos <- 'https://cloud.r-project.org/'" \
    -e "dependencies <- c('Depends', 'Imports', 'LinkingTo', 'Suggests', 'Enhances')" \
    -e "libs <- c('tidyverse', 'readr', 'comprehenr', 'maps', 'mapproj', 'ggthemes')" \
    -e "install.packages(libs, repos=repos, Ncpus=10, dependencies=dependencies)"
RUN Rscript \
    -e "repos <- 'https://cloud.r-project.org/'" \
    -e "dependencies <- c('Depends', 'Imports', 'LinkingTo', 'Suggests', 'Enhances')" \
    -e "libs <- c('mice', 'VIM', 'Amelia', 'missForest', 'mi')" \
    -e "install.packages(libs, repos=repos, Ncpus=10, dependencies=dependencies)"
RUN Rscript \
    -e "repos <- 'https://cloud.r-project.org/'" \
    -e "dependencies <- c('Depends', 'Imports', 'LinkingTo', 'Suggests', 'Enhances')" \
    -e "libs <- c('skimr', 'RANN', 'gbm', 'xgboost', 'caret', 'caretEnsemble', 'C50', 'earth')" \
    -e "install.packages(libs, repos=repos, Ncpus=10, dependencies=dependencies)"
RUN Rscript \
    -e "repos <- 'https://cloud.r-project.org/'" \
    -e "dependencies <- c('Depends', 'Imports', 'LinkingTo', 'Suggests', 'Enhances')" \
    -e "libs <- c('Hmisc', 'mlr3', 'survival', 'survey', 'nlme', 'multcomp', 'vcd')" \
    -e "install.packages(libs, repos=repos, Ncpus=10, dependencies=dependencies)"
RUN Rscript \
    -e "repos <- 'https://cloud.r-project.org/'" \
    -e "dependencies <- c('Depends', 'Imports', 'LinkingTo', 'Suggests', 'Enhances')" \
    -e "libs <- c('BayesNetBP', 'bnlearn', 'bnpa', 'BNSL', 'bnstruct', 'bnviewer', 'catnet', 'dbnlearn', 'dbnR', 'deal')" \
    -e "install.packages(libs, repos=repos, Ncpus=10, dependencies=dependencies)"
RUN Rscript \
    -e "repos <- 'https://cloud.r-project.org/'" \
    -e "dependencies <- c('Depends', 'Imports', 'LinkingTo', 'Suggests', 'Enhances')" \
    -e "libs <- c('sem', 'lavaan', 'lava', 'tidySEM', 'blavaan', 'bsem', 'gSEM', 'netSEM', 'psychonetrics', 'regsem', 'rsem', 'SELF')" \
    -e "install.packages(libs, repos=repos, Ncpus=10, dependencies=dependencies)"
RUN Rscript \
    -e "repos <- 'https://cloud.r-project.org/'" \
    -e "dependencies <- c('Depends', 'Imports', 'LinkingTo', 'Suggests', 'Enhances')" \
    -e "libs <- c('survivalmodels', 'survivalMPL', 'survivalsvm', 'CausalMBSTS', 'causalweight')" \
    -e "install.packages(libs, repos=repos, Ncpus=10, dependencies=dependencies)"
RUN Rscript \
    -e "library(devtools)" \
    -e "install_github('vqv/ggbiplot')"
