FROM oneoffcoder/spark-jupyter:latest
LABEL org="One-Off Coder"
LABEL author="Jee Vang, Ph.D."
LABEL email="info@oneoffcoder.com"
LABEL website="https://www.oneoffcoder.com"
LABEL facebook="https://www.facebook.com/oneoffcoder"
LABEL twitter="https://twitter.com/oneoffcoder"
LABEL instagram="https://www.instagram.com/oneoffcoder/"
LABEL youtube="https://www.youtube.com/channel/UCCCv8Glpb2dq2mhUj5mcHCQ"
LABEL linkedin="https://www.linkedin.com/company/one-off-coder"

# setup ubuntu
RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get clean

COPY ubuntu/etc/supervisor/conf.d/*.conf /etc/supervisor/conf.d/
COPY ubuntu/usr/local/bin/*.py /usr/local/bin/

RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*