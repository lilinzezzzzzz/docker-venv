FROM ubuntu:22.04
LABEL maintainer="lilinze@yimian.com.cn"

WORKDIR /root
RUN mkdir .pip
COPY ./pip.conf /root/.pip

RUN apt-get update && \
    apt-get install build-essential && \
    apt-get install libreadline-dev  && \
    apt-get libncursesw5-dev  && \
    apt-get libssl-dev && \
    apt-get libsqlite3-dev  && \
    apt-get tk-dev  && \
    apt-get libgdbm-dev  && \
    apt-get libc6-dev  && \
    apt-get libbz2-dev  && \
    apt-get libffi-dev  && \
    apt-get zlib1g-dev  && \
    cd /opt && \
    wget https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tgz && \
    tar xzf Python-3.6.2.tgz && \
    cd Python-3.6.2 && \
    ./configure --enable-optimizations && \
    make altinstall && \
    update-alternatives --install /usr/bin/python3 python3 /usr/local/bin/python3.6 1 && \
    update-alternatives --config python3