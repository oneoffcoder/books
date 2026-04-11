FROM eclipse-temurin:25-jdk
LABEL maintainer="One-Off Coder <info@oneoffcoder.com>"
COPY . /code
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends maven \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /code
RUN mvn test
