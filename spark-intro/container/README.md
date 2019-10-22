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

As can be seen, Jupyter Lab is running on port `8888`. An example notebook is mounted at `/root/ipynb`. To get the PySpark code to run, you will have to upload the `data.csv` file to HDFS first. [View the example notebook](https://nbviewer.jupyter.org/github/oneoffcoder/docker-containers/blob/master/spark-jupyter/ubuntu/root/ipynb/demo.ipynb?flush_cache=true).

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
    -v $HOME/git/docker-containers/spark-jupyter/ubuntu/root/ipynb:/root/ipynb \
    -e PYSPARK_MASTER=spark://localhost:7077 \
    spark-jupyter:local
```

Stuff to do after going into the container e.g. `docker exec -it <id> /bin/bash`

```bash
# test yarn
yarn jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.2.1.jar pi 1 50

# test spark against yarn
$SPARK_HOME/bin/spark-submit --class org.apache.spark.examples.SparkPi \
    --master yarn \
    $SPARK_HOME/examples/jars/spark-examples*.jar \
    100

# test spark standalone
$SPARK_HOME/bin/spark-submit --class org.apache.spark.examples.SparkPi \
    --master spark://localhost:7077 \
    $SPARK_HOME/examples/jars/spark-examples*.jar \
    100

# start a scala spark shell
$SPARK_HOME/bin/spark-shell --master spark://localhost:7077

# start a python spark shell
pyspark --master spark://localhost:7077 > /tmp/jupyter.log 2>&1 &

# start a python spark shell against yarn
pyspark \
    --driver-memory 2g \
    --executor-memory 2g \
    --num-executors 1 \
    --executor-cores 1 \
    --conf spark.driver.maxResultSize=8g \
    --conf spark.network.timeout=2000 \
    --queue default \
    --master yarn-client > /tmp/jupyter.log 2>&1 &
```

# Docker Hub

[Image](https://hub.docker.com/r/oneoffcoder/spark-jupyter)

# References

* [List of all ports](https://kontext.tech/docs/DataAndBusinessIntelligence/p/default-ports-used-by-hadoop-services-hdfs-mapreduce-yarn)
* [Enable CORS for WebHDFS](https://stackoverflow.com/questions/52768514/how-to-enable-cors-origin-allow-in-webhdfs-hdfs-hadoop-origin-http-local)
* [core-default.xml](https://hadoop.apache.org/docs/r3.2.1/hadoop-project-dist/hadoop-common/core-default.xml)
* [hdfs-default.xml](http://hadoop.apache.org/docs/r3.2.1/hadoop-project-dist/hadoop-hdfs/hdfs-default.xml)
* [yarn-default.xml](https://hadoop.apache.org/docs/r3.2.1/hadoop-yarn/hadoop-yarn-common/yarn-default.xml)
* [mapred-default.xml](https://hadoop.apache.org/docs/r3.2.1/hadoop-mapreduce-client/hadoop-mapreduce-client-core/mapred-default.xml)
* [Keep docker container running after services start](https://stackoverflow.com/questions/25775266/how-to-keep-docker-container-running-after-starting-services)