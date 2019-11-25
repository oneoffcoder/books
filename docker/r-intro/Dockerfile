FROM oneoffcoder/r-jupyter:latest
LABEL One-Off Coder "info@oneoffcoder.com"

# setup ubuntu
RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get install libcurl4-openssl-dev libssl-dev -y \
    && apt-get clean

# install R packages
RUN Rscript \
    -e "a <- c('ggplot2', 'viridis', 'corrplot', 'progress', 'devtools')" \
    -e "b <- c('ggExtra', 'leaflet', 'plotly')" \
    -e "c <- c('plyr', 'lsa', 'caret', 'twitteR', 'e1071', 'fastAdaboost')" \
    -e "d <- c('quanteda', 'sentimentr', 'randomForest', 'ggrepel', 'rmarkdown')" \
    -e "e <- c('R6', 'jsonlite', 'lubridate', 'microbenchmark', 'shiny', 'shinythemes')" \
    -e "f <- c('tidyverse', 'readr', 'comprehenr', 'maps', 'mapproj', 'ggthemes')" \
    -e "libs <- c(a, b, c, d, e, f)" \
    -e "install.packages(libs, repos='https://mirrors.nics.utk.edu/cran/', Ncpus=10)" \
    -e "library(devtools)" \
    -e "install_github('vqv/ggbiplot')" \
    -e "install_version('caret', version='6.0-84')"
