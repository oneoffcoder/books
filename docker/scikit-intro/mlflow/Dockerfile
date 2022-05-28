FROM continuumio/miniconda3:4.11.0

WORKDIR /mlflow/

RUN mkdir -p /mlflow/ \
    && pip install  \
        mlflow==1.26.1 

EXPOSE 5000
CMD mlflow server \
    --backend-store-uri sqlite:///mlflow.db \
    --default-artifact-root /tmp/mlflow \
    --host 0.0.0.0