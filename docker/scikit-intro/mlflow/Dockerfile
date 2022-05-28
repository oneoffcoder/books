FROM continuumio/miniconda3:4.11.0

ENV BACKEND_URI sqlite:///mlflow.db
ENV ARTIFACT_ROOT /mlflow/mlflow-artifacts

WORKDIR /mlflow/

RUN mkdir -p /mlflow/ \
  && apt-get update \
  && apt-get -y install --no-install-recommends default-libmysqlclient-dev libpq-dev build-essential \
  && pip install \
    mlflow==1.26.1 \
    sqlalchemy \
    boto3 \
    google-cloud-storage \
    psycopg2 \
    mysql

EXPOSE 5000
CMD mlflow server \
    --backend-store-uri ${BACKEND_URI} \
    --default-artifact-root ${ARTIFACT_ROOT} \
    --host 0.0.0.0