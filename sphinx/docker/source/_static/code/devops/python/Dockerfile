
FROM continuumio/anaconda3

ARG ARG_VERSION
ARG ARG_REPO

ENV API_VERSION=$ARG_VERSION
ENV API_REPO=$ARG_REPO
ENV PATH /opt/conda/bin:$PATH

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install build-essential -y
    
WORKDIR /pydemo

COPY . .

RUN conda install --file requirements.txt -y

RUN /pydemo/publish.sh