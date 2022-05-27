FROM continuumio/miniconda3:4.11.0

RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get install awscli build-essential -y \
    && conda update -n base -c defaults conda -y \
    && conda install -y -c anaconda -c conda-forge \
        seaborn \
        scikit-learn \
        numpy \
        pip \
    && pip install mlflow==1.26.0 boto3 s3fs fsspec \
    && pip install sagemaker-training \
    && pip install lifelines scikit-survival sagemaker-training imbalanced-learn \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*