# spark-intro-check

This image exists to execute the `sphinx/spark-intro` notebooks end-to-end with a local Spark runtime.

It is intentionally separate from the legacy `docker/spark-intro` Jupyter image:

- no Hadoop or HDFS services
- no standalone Spark master or worker daemons
- notebook execution uses `local[*]`
- GraphFrames is available through a bundled Spark 3.5 jar

Current pinned runtime:

- `Python 3.11`
- `OpenJDK 17`
- `PySpark 3.5.8`
- `GraphFrames 0.8.3` Spark package with the `graphframes 0.6` Python wrapper
- `JupyterLab 4.5.6`

Build the image:

```bash
docker build -t book-spark-intro-check:local docker/spark-intro-check
```

Execute all notebooks:

```bash
docker/spark-intro-check/execute-notebooks.sh
```

Execute selected notebooks:

```bash
docker/spark-intro-check/execute-notebooks.sh rdd.ipynb dataframes.ipynb
```

Executed notebooks are written to `sphinx/spark-intro/build/executed-notebooks`.
