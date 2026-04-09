FROM python:3.13-slim

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        ca-certificates \
        git \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir \
        ipykernel \
        jupyterlab \
        nbclient \
        nbconvert \
    && pip install --no-cache-dir \
        --index-url https://download.pytorch.org/whl/cu128 \
        torch \
        torchvision \
    && pip install --no-cache-dir \
        ipywidgets \
        matplotlib \
        numpy \
        pandas \
        pillow \
        pycocotools \
        scikit-learn \
          scipy \
          tensorboard

RUN pip install --no-cache-dir \
          onnx \
          onnxscript

WORKDIR /workspace
