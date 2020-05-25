FROM oneoffcoder/book-base:latest
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
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get clean

# && apt-get -y install build-essential \
#         cmake \
#         libboost-all-dev \
#         gcc \
#         clang \
#         gdb \
#         libblkid-dev \
#         e2fslibs-dev \
#         libaudit-dev \
#         valgrind \
#         ninja-build \
#         doxygen \
#         graphviz \
#         mscgen \
#         dia \
#         lcov \

# setup conda
RUN conda install xeus-cling -c conda-forge -y

# clean up
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
