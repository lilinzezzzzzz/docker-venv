# 使用官方的 python 3.12.9 镜像作为基础镜像
FROM python:3.12.9

# 设置时区和环境变量
ENV TZ=UTC
ENV LANG=C.UTF-8
RUN ln -sf /usr/share/zoneinfo/UTC /etc/localtime && \
    echo "UTC" > /etc/timezone
# 安装常用工具：vim, curl, git, iproute2, net-tools, openssh-server
RUN apt-get update && \
    apt-get install -y \
    vim \
    curl \
    git \
    build-essential \
    iproute2 \
    net-tools \
    openssh-server \
    iputils-ping \
    && rm -rf /var/lib/apt/lists/*

# 配置 SSH 服务
RUN mkdir /var/run/sshd

# 设置 root 密码，确保可以通过 SSH 登录，还需要修改/etc/ssh/sshd_config 文件，将 PermitRootLogin 设置为 yes
RUN echo 'root:123456' | chpasswd

# 安装 Python 开发环境所需工具，例如 pip 和一些常用的 Python 库
RUN pip install --upgrade pip && \
    pip install --no-cache-dir \
    setuptools \
    wheel \
    flake8 \
    black \
    autopep8

# 暴露 SSH 端口
EXPOSE 22

# 设置工作目录
WORKDIR /app
