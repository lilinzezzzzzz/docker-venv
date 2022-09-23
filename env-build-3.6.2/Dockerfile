FROM python:3.6.2
LABEL maintainer="lilinze@yimian.com.cn"

WORKDIR /root
RUN mkdir .pip
COPY ./pip.conf /root/.pip

RUN cd /etc/apt && mv ./sources.list ./sources.list.back
COPY ./sources.list /etc/apt

RUN apt-get update &&  \
    apt-get -y upgrade && \
    apt-get install -y sudo && \
    apt-get install -y openssl &&  \
    apt-get install -y openssh-server &&  \
    apt-get install -y vim &&  \
    apt-get install -y net-tools && \
    apt-get install -y libssl-dev && \
    apt-get install -y libevent-dev && \
    apt-get install -y python3-dev && \
    apt-get install -y libffi-dev && \
    apt-get install -y libxslt-dev && \
    apt-get install -y libsasl2-dev && \
    apt-get install -y rsync