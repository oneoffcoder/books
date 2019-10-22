#!/bin/bash

service ssh start
echo "started ssh"

$HADOOP_HOME/sbin/start-all.sh
echo "started hadoop"

$SPARK_HOME/sbin/start-all.sh
echo "started spark"

$SPARK_HOME/sbin/start-history-server.sh
echo "started spark history"

# pyspark --master spark://localhost:7077 > /tmp/jupyter.log 2>&1 &
$SPARK_HOME/bin/pyspark \
    --packages graphframes:graphframes:0.7.0-spark2.4-s_2.11 \
    --master $PYSPARK_MASTER > /tmp/jupyter.log 2>&1 &
echo "started pyspark"

if [ -d "/root/ipynb" ] && [ -f "/root/ipynb/data.csv" ]; then
    hdfs dfs -copyFromLocal /root/ipynb/data.csv /data.csv
    echo "copied data.csv to hdfs"
else
    echo "/root/ipynb/data.csv does not exists"
fi

echo "done!"

exit 0