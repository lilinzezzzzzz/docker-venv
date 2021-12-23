"""
python 容器
    阿里云源:https://ygz2147j.mirror.aliyuncs.com

    离线下载所有包，依赖
    pip download -d path flask
    pip download -d flasgger

docker run -itd --name env-3.6.1 -p 10022:22 --privileged=true python:3.6.1 /bin/bash

docker run -itd --name env-3.10.0 -p 10023:22 --privileged=true python:3.10.0 /bin/bash

docker run -itd --name env-3.9.2 --network onewiki -p 10029:22 -p 3306:3306 -p 6379:6379 -p 27017:27017 -p 9200:9200 -p 9300:9300 -p 8000:8000 py-3.9.2:v1 /bin/bash

使用container网络构建环境：
    1.先docker run 一个Python环境的容器(py-env),需要映射出docker-compose所有服务需要的端口
    2.docker-compose network_mode:"py-env"

    Python环境容器和docker-compose各服务容器共享一个网络栈，可以使用127.0.0.1互相访x问
    宿主机也可以通过127.0.0.1:端口访问docker-compose服务

查看操作系统
    tail /etc/os-release 
查看端口进程
    lsof -i tcp:port

拷贝文件
    docker cp [宿主机路径] [容器:容器路径]
    docker cp [容器:容器路径] [宿主机路径] 

容器commit生成镜像
    docker commit -a "作者" -m "提交信息" [container name/id]  镜像名:标签(tag)


构建镜像Dockerfile
    当前路径
    docker build -t py-env3.8.7 .
    指定路径
    docker build -f /path/to/a/Dockerfile .

保存容器
docker save 保存的是镜像（image），docker export 保存的是容器(container)
docker load 用来载入镜像包，docker import 用来载入容器包，但两者都会恢复为镜像
docker load 不能对载入的镜像重命名，而 docker import 可以为镜像指定新名称。

保存镜像
docker export
docker import

容器网络:
    查看所有网络
        docker network ls
    创建网络
        docker network create [network name] -d [network_mode bridge/host/none]
        例：docker network create network_name -d bridge
    查看网络下的容器
        docker network inspect [container name/id]
        例：docker network inspect xxs
    容器链接(断开)新网络
        docker network(disconnect) connect [network name/id] [container name/id]
        例：docker network connect(connect) network_name xxs
        通过docker inspect xxs 查看xxs容器的网络信息，增加(减少)了network_name网络
        
    bridge: 同一个bridge网络的容器可以互相通信，各个容器IP不同，可能会有变动
    container: 同一个container网络下的容易共享网络，一个IP，容器之间可以使用 localhost 高效快速通信。
        docker run -itd --name xxs --network container:[container name/id] kky:v1 /bin/bash
    host: 共享宿主机网络
    
    network_mode: "bridge"
    network_mode: "host"
    network_mode: "none"
    network_mode: "service:[service name]"
    network_mode: "container:[container name/id]"

docker daemon配置
{
  "registry-mirrors": [
    "https://ygz2147j.mirror.aliyuncs.com"
  ],
  "features": {
    "buildkit": true
  },
  "experimental": false,
  "builder": {
    "gc": {
      "enabled": true,
      "defaultKeepStorage": "20GB"
    }
  },
  "log-driver":"json-file",
  "log-opts":{ "max-size" :"100m","max-file":"3"}
}
"""
