FROM continuumio/miniconda3:4.9.2

RUN conda update -n base -c defaults conda -y \
    && conda install -y -c anaconda \
        seaborn \
        scikit-learn \
        numpy \
        pip \
    && conda install -y -c conda-forge \
        mlflow \
        lifelines \
        boto3 \
        awscli \
        ipykernel \
        imbalanced-learn \
    && conda install -y -c sebp scikit-survival \
    && pip install s3fs fsspec