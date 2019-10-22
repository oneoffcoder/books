FROM ubuntu:disco
LABEL One-Off Coder "info@oneoffcoder.com"

ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
ENV HDFS_NAMENODE_USER=root
ENV HDFS_DATANODE_USER=root
ENV HDFS_SECONDARYNAMENODE_USER=root
ENV YARN_RESOURCEMANAGER_USER=root
ENV YARN_NODEMANAGER_USER=root
ENV YARN_PROXYSERVER_USER=root
ENV HADOOP_HOME=/usr/local/hadoop
ENV HADOOP_YARN_HOME=${HADOOP_HOME}
ENV HADOOP_CONF_DIR=${HADOOP_HOME}/etc/hadoop
ENV HADOOP_LOG_DIR=${HADOOP_YARN_HOME}/logs
ENV HADOOP_IDENT_STRING=root
ENV HADOOP_MAPRED_IDENT_STRING=root
ENV HADOOP_MAPRED_HOME=${HADOOP_HOME}
ENV SPARK_HOME=/usr/local/spark
ENV CONDA_HOME=/usr/local/conda
ENV PYSPARK_MASTER=yarn
ENV PATH=${CONDA_HOME}/bin:${SPARK_HOME}/bin:${HADOOP_HOME}/bin:${PATH}

# setup ubuntu
RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get -y install openjdk-8-jdk wget openssh-server sshpass supervisor \
    && apt-get -y install nano net-tools lynx \
    && apt-get clean

# setup ssh
RUN ssh-keygen -t rsa -P "" -f /root/.ssh/id_rsa \
    && cat /root/.ssh/id_rsa.pub >> /root/.ssh/authorized_keys \
    && chmod 0600 /root/.ssh/authorized_keys
COPY ubuntu/root/.ssh/config /root/.ssh/config

# setup hadoop
RUN wget -q http://apache.mirrors.tds.net/hadoop/common/hadoop-3.2.1/hadoop-3.2.1.tar.gz -O /tmp/hadoop-3.2.1.tar.gz \
    && tar -xzf /tmp/hadoop-3.2.1.tar.gz -C /usr/local/ \
    && ln -s /usr/local/hadoop-3.2.1 /usr/local/hadoop \
    && rm -fr /usr/local/hadoop/etc/hadoop/* \
    && mkdir /usr/local/hadoop/extras \
    && mkdir /var/hadoop \
	&& mkdir /var/hadoop/hadoop-datanode \
	&& mkdir /var/hadoop/hadoop-namenode \
	&& mkdir /var/hadoop/mr-history \
	&& mkdir /var/hadoop/mr-history/done \
	&& mkdir /var/hadoop/mr-history/tmp
COPY ubuntu/usr/local/hadoop/etc/hadoop/* /usr/local/hadoop/etc/hadoop/
COPY ubuntu/usr/local/hadoop/extras/* /usr/local/hadoop/extras/
RUN $HADOOP_HOME/bin/hdfs namenode -format oneoffcoder

# setup spark
RUN wget -q http://mirrors.advancedhosters.com/apache/spark/spark-2.4.4/spark-2.4.4-bin-hadoop2.7.tgz -O /tmp/spark-2.4.4-bin-hadoop2.7.tgz \
    && tar -xzf /tmp/spark-2.4.4-bin-hadoop2.7.tgz -C /usr/local/ \
    && ln -s /usr/local/spark-2.4.4-bin-hadoop2.7 /usr/local/spark \
    && rm /usr/local/spark/conf/*.template
COPY ubuntu/usr/local/spark/conf/* /usr/local/spark/conf/

# setup conda
COPY ubuntu/root/ipynb/environment.yml /tmp/environment.yml
RUN wget -q https://repo.anaconda.com/archive/Anaconda3-2019.07-Linux-x86_64.sh -O /tmp/Anaconda3-2019.07-Linux-x86_64.sh \
    && /bin/bash /tmp/Anaconda3-2019.07-Linux-x86_64.sh -b -p $CONDA_HOME \
    && $CONDA_HOME/bin/conda env update -n base --file /tmp/environment.yml \
    && $CONDA_HOME/bin/conda update -n root conda -y \
    && $CONDA_HOME/bin/conda update --all -y \
    && $CONDA_HOME/bin/pip install --upgrade pip

# setup volumes
RUN mkdir /root/ipynb
VOLUME [ "/root/ipynb" ]

# setup supervisor
COPY ubuntu/etc/supervisor/supervisor.conf /etc/supervisor/supervisor.conf
COPY ubuntu/etc/supervisor/conf.d/all.conf /etc/supervisor/conf.d/all.conf
COPY ubuntu/usr/local/bin/start-all.sh /usr/local/bin/start-all.sh

# clean up
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && mkdir /tmp/spark-events

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf", "-n"]