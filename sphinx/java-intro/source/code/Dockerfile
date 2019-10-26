FROM openjdk:13.0.1-buster
LABEL One-Off Coder "info@oneoffcoder.com"
ENV PATH /maven/bin:$PATH
ENV MAVEN_URL http://apache.mirrors.ionfish.org/maven/maven-3/3.6.1/binaries/apache-maven-3.6.1-bin.tar.gz
COPY . /code
RUN wget -q ${MAVEN_URL} -O /tmp/maven.tar.gz \
    && tar xzvf /tmp/maven.tar.gz -C / \
    && ln -s /apache-maven-3.6.1 /maven
WORKDIR /code
RUN mvn test