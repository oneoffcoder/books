![One-Off Coder Logo](../logo.png "One-Off Coder")

# Purpose

This docker container is meant to be used for learning purpose for programming PySpark. It has the following components.

* Hadoop v3.2.1
* Spark v2.4.4
* Conda 3 with Python v3.7

After running the container, you may visit the following pages.

* [HDFS](http://localhost:9870)
* [YARN](http://localhost:8088)
* [Spark](http://localhost:8080)
* [Spark History](http://localhost:18080)
* [Jupyter Lab](http://localhost:8888)

As can be seen, Jupyter Lab is running on `localhost:8888`.

# Docker

To run the container.

```bash
docker run -it \
    -p 9870:9870 \
    -p 8088:8088 \
    -p 8080:8080 \
    -p 18080:18080 \
    -p 9000:9000 \
    -p 8888:8888 \
    -p 9864:9864 \
    -p 300:300 \
    -p 301:301 \
    -v $HOME/git/books/sphinx/spark-intro/source:/root/ipynb \
    -e PYSPARK_MASTER=spark://localhost:7077 \
    book-spark-intro:local
```

# Docker Hub

[Image](https://hub.docker.com/r/oneoffcoder/book-spark-intro)