FROM oneoffcoder/r-jupyter:latest
LABEL One-Off Coder "info@oneoffcoder.com"

# setup ubuntu
RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get install libcurl4-openssl-dev libssl-dev -y \
    && apt-get clean

# install R packages
RUN Rscript \
    -e "a <- c('ggplot2', 'viridis', 'corrplot', 'ggbiplot', 'progress', 'devtools')" \
    -e "b <- c('RMySQL', 'ggExtra', 'threejs', 'leaflet', 'plotly')" \
    -e "c <- c('rgl', 'rgdal', 'plyr', 'lsa', 'rilba', 'caret', 'twitteR')" \
    -e "d <- c('quanteda', 'sentimentr', 'randomForest', 'ggrepel', 'rmarkdown')" \
    -e "e <- c('R6', 'jsonlite', 'lubridate', 'microbenchmark', 'shiny', 'shinythemes')" \
    -e "f <- c('ggthemr', 'tidyverse', 'readr')" \
    -e "libs <- c(a, b, c, d, e, f)" \
    -e "install.packages(libs, repos='https://mirrors.nics.utk.edu/cran/')" \
    -e "library(devtools)" \
    -e "install_github('vqv/ggbiplot')"