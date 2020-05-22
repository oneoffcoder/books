FROM oneoffcoder/conda-deeplearning:latest
LABEL org="One-Off Coder"
LABEL author="Jee Vang, Ph.D."
LABEL website="https://www.oneoffcoder.com"
LABEL email="info@oneoffcoder.com"
LABEL facebook="https://www.facebook.com/oneoffcoder"
LABEL twitter="https://twitter.com/oneoffcoder"
LABEL instagram="https://www.instagram.com/oneoffcoder/"
LABEL youtube="https://www.youtube.com/channel/UCCCv8Glpb2dq2mhUj5mcHCQ"
LABEL linkedin="https://www.linkedin.com/company/one-off-code"

# setup ubuntu
RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get install git -y \
    && apt-get clean

RUN pip install pycocotools
