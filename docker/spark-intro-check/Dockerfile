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
        delta-spark==3.3.2 \
        graphframes==0.6 \
        ipykernel \
        jupyterlab==4.5.6 \
        nbclient \
        nbconvert \
        numpy==1.26.4 \
        pandas==2.2.3 \
        pyarrow==15.0.2 \
        "pyspark[connect]==3.5.8" \
        pytest==8.3.4 \
        scikit-learn==1.5.2

RUN mkdir -p /opt/spark/jars \
    && curl -fsSL \
        https://repos.spark-packages.org/graphframes/graphframes/0.8.3-spark3.5-s_2.12/graphframes-0.8.3-spark3.5-s_2.12.jar \
        -o /opt/spark/jars/graphframes-0.8.3-spark3.5-s_2.12.jar \
    && curl -fsSL \
        https://repo1.maven.org/maven2/io/delta/delta-spark_2.12/3.3.2/delta-spark_2.12-3.3.2.jar \
        -o /opt/spark/jars/delta-spark_2.12-3.3.2.jar \
    && curl -fsSL \
        https://repo1.maven.org/maven2/io/delta/delta-storage/3.3.2/delta-storage-3.3.2.jar \
        -o /opt/spark/jars/delta-storage-3.3.2.jar \
    && curl -fsSL \
        https://repo1.maven.org/maven2/org/antlr/antlr4-runtime/4.9.3/antlr4-runtime-4.9.3.jar \
        -o /opt/spark/jars/antlr4-runtime-4.9.3.jar \
    && curl -fsSL \
        https://repo1.maven.org/maven2/org/apache/iceberg/iceberg-spark-runtime-3.5_2.12/1.10.1/iceberg-spark-runtime-3.5_2.12-1.10.1.jar \
        -o /opt/spark/jars/iceberg-spark-runtime-3.5_2.12-1.10.1.jar

ENV SPARK_GRAPHFRAMES_JAR=/opt/spark/jars/graphframes-0.8.3-spark3.5-s_2.12.jar \
    SPARK_DELTA_JARS=/opt/spark/jars/delta-spark_2.12-3.3.2.jar,/opt/spark/jars/delta-storage-3.3.2.jar,/opt/spark/jars/antlr4-runtime-4.9.3.jar \
    SPARK_ICEBERG_JAR=/opt/spark/jars/iceberg-spark-runtime-3.5_2.12-1.10.1.jar

RUN python -m ipykernel install --sys-prefix --name python3 --display-name "Python 3"

RUN mkdir -p /workspace && chmod 0777 /workspace

WORKDIR /workspace
