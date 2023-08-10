FROM ubuntu:18.04
LABEL maintainer="lilinze@yimian.com.cn"

WORKDIR /root
RUN mkdir .pip
COPY ./pip.conf /root/.pip
COPY /Users/linzeli/.ssh /root/.ssh

RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get -y install sudo && \
    apt-get -y install build-essential && \
    apt-get -y install libreadline-dev  && \
    apt-get -y install libssl-dev && \
    apt-get -y install libsqlite3-dev  && \
    apt-get -y install tk-dev  && \
    apt-get -y install libgdbm-dev  && \
    apt-get -y install libc6-dev  && \
    apt-get -y install libbz2-dev  && \
    apt-get -y install libffi-dev  && \
    apt-get -y install zlib1g-dev  && \
    apt-get -y install openssl && \
    apt-get -y install openssh-server &&  \
    apt-get -y install vim && \
    apt-get -y install net-tools && \
    apt-get -y install rsync && \
    apt-get -y install libsasl2-dev && \
    apt-get -y install libxslt-dev && \
    apt-get -y install libssl-dev && \
    apt-get -y install libevent-dev && \
    apt-get -y install python3-dev && \
    apt-get -y install libffi-dev && \
    cd /opt && \
    wget https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tgz && \
    tar xzf Python-3.6.2.tgz && \
    cd Python-3.6.2 && \
    ./configure --enable-optimizations && \
    make altinstall && \
    update-alternatives --install /usr/bin/python3 python3 /usr/local/bin/python3.6 1 && \
    update-alternatives --config python3