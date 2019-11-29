
FROM continuumio/anaconda3

ARG ARG_VERSION
ARG ARG_REPO

ENV API_VERSION=$ARG_VERSION
ENV API_REPO=$ARG_REPO
ENV PATH /opt/conda/bin:$PATH

RUN apt-get update \
    && apt-get upgrade

WORKDIR /pydemo

COPY ./pydemo .

RUN conda install --file requirements.txt -y

RUN /py-bbn/publish.sh