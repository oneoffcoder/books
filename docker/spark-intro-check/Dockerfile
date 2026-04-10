FROM python:3.11-slim-bookworm

ENV DEBIAN_FRONTEND=noninteractive \
    JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64 \
    PATH=/opt/venv/bin:$PATH \
    PYSPARK_PYTHON=/opt/venv/bin/python \
    PYSPARK_DRIVER_PYTHON=/opt/venv/bin/python \
    PYARROW_IGNORE_TIMEZONE=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    SPARK_LOCAL_IP=127.0.0.1 \
    SPARK_LOCAL_HOSTNAME=localhost \
    OPENBLAS_NUM_THREADS=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        bash \
        ca-certificates \
        curl \
        openjdk-17-jre-headless \
        procps \
    && python -m venv /opt/venv \
    && rm -rf /var/lib/apt/lists/*

RUN /opt/venv/bin/pip install --no-cache-dir --upgrade pip setuptools wheel \
    && /opt/venv/bin/pip install --no-cache-dir \
        graphframes==0.6 \
        ipykernel \
        jupyterlab==4.5.6 \
        nbclient \
        nbconvert \
        numpy==1.26.4 \
        pandas==2.2.3 \
        pyarrow==15.0.2 \
        pyspark==3.5.8 \
        scikit-learn==1.5.2

RUN mkdir -p /opt/spark/jars \
    && curl -fsSL \
        https://repos.spark-packages.org/graphframes/graphframes/0.8.3-spark3.5-s_2.12/graphframes-0.8.3-spark3.5-s_2.12.jar \
        -o /opt/spark/jars/graphframes-0.8.3-spark3.5-s_2.12.jar

ENV SPARK_GRAPHFRAMES_JAR=/opt/spark/jars/graphframes-0.8.3-spark3.5-s_2.12.jar

RUN python -m ipykernel install --sys-prefix --name python3 --display-name "Python 3"

RUN mkdir -p /workspace && chmod 0777 /workspace

WORKDIR /workspace
