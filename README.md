# docker-env  

## 注意事项

- 此项目基于docker,docker-compose。用于快速构建Python开发环境以及一些可能需要的中间件。
- 使用`容器网络模式`，所以中间件和Python容器一个网络。映射出一些常用的端口，所以服务之间可以使用`127.0.0.1`访问。
- 如果需要构建其他的Python环境,可以使用指定容器模式链接到`docker-rnv_default`网络。
- 构建的Python环境需要用ssh或者sftp远程链接使用，默认映射端口`10029:22`， 可以按需在docker-compose修改。
- ./command.py 常用的docker命令
- ./info.txt 中间件的一些命令
- 中间件版本按需指定，ES分词器需要自己匹配
- ./test 用于构建单个Python解释器

## 使用

- 使用docker-compose构建之前，先确定你要使用的Python容器是基于什么Linux版本，不同的版本需要不同的source.list（`tail /etc/os-release 查看操作系统` ）。
- 确定好操作系统，更换Dockerfile构建文件夹得source.list
- docker-compose up -d
- 各个中间件远程访问都已经配置完成
- 启动服务之后，需要进去py-env容器，配置SSH远程访问，并且重启SSH

## 远程登录

```sql
use mysql;
select host, user, authentication_string, plugin from user;
update user set host='%' where user='root';

ALTER USER 'root'@'%' IDENTIFIED BY 'password' PASSWORD EXPIRE NEVER;
ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY 'password';

ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY '123456!';
```

### Redis

```docker
info Server  # 查看redis信息
docker run -itd --name nosugar-redis -p 6379:6379 redis 
docker run -itd --name nosugar-redis -p 6379:6379 -v "d:\docker-volume\redis\redis.conf:/etc/redis/redis.conf" -v "d:\docker-volume\redis\logs\redis.log:/var/log/redis/redis.log" -v "d:\docker-volume\redis\data:/data" redis
```

### Elasticsearch

```docker
http.cors.enabled: true
http.cors.allow-origin: "*"

docker pull elasticsearch:6.5.4

docker run --name es-env -itd -e ES_JAVA_OPTS="-Xms256m -Xmx256m" -e "discovery.type=single-node" -p 9200:9200 -p 9300:9300 elasticsearch:6.5.4

docker run --name es-env -itd -e ES_JAVA_OPTS="-Xms256m -Xmx256m" --net host --restart=always -e "discovery.type=single-node" -p 9200:9200 -p 9300:9300 elasticsearch:6.5.4

elasticsearch-plugin install https://github.com/medcl/elasticsearch-analysis-ik/releases/download/v6.5.4/elasticsearch-analysis-ik-6.5.4.zip

curl -X GET 127.0.0.1:9200/_analyze?pretty -H 'content-Type:application/json' -d '{"analyzer": "ik_max_word", "text": "我是&中国人"}'
```

查看操作系统

``` shell
tail /etc/os-release 
```

查看端口进程

``` shell
lsof -i tcp:port
```

离线下载所有包，依赖

```python
pip download -d path flask
pip download -d flasgger
```

``` docker
docker run -itd --name env-3.6.1 -p 10022:22 --privileged=true python:3.6.1 /bin/bash

docker run -itd --name env-3.10.0 -p 10023:22 --privileged=true python:3.10.0 /bin/bash

docker run -itd --name env-3.9.2 --network onewiki -p 10029:22 -p 3306:3306 -p 6379:6379 -p 27017:27017 -p 9200:9200 -p 9300:9300 -p 8000:8000 py-3.9.2:v1 /bin/bash
```

使用container网络构建环境

```docker
1.先docker run 一个Python环境的容器(py-env),需要映射出docker-compose所有服务需要的端口
2.docker-compose network_mode:"py-env"

Python环境容器和docker-compose各服务容器共享一个网络栈，可以使用127.0.0.1互相访问宿主机也可以通过127.0.0.1:端口访问docker-compose服务
```

拷贝文件

```docker
docker cp [宿主机路径] [容器:容器路径]
docker cp [容器:容器路径] [宿主机路径] 
```

容器commit生成镜像

```docker
docker commit -a "作者" -m "提交信息" [container name/id]  镜像名:标签(tag)
```

构建镜像Dockerfile

```docker
当前路径
    docker build -t py-env3.8.7 .
指定路径
    docker build -f /path/to/a/Dockerfile .
```

保存容器

```docker
    docker save 保存的是镜像（image），docker export 保存的是容器(container)
    docker load 用来载入镜像包，docker import 用来载入容器包，但两者都会恢复为镜像
    docker load 不能对载入的镜像重命名，而 docker import 可以为镜像指定新名称。
```

保存镜像

```docker
    docker export
    docker import
```

查看所有网络

```docker
    docker network ls
```

创建网络

```docker
    docker network create [network name] -d [network_mode bridge/host/none]
    例：docker network create network_name -d bridge
```

查看网络下的容器

```docker
    docker network inspect [container name/id]
    例：docker network inspect xxs
```

容器链接(断开)新网络

```docker
    docker network(disconnect) connect [network name/id] [container name/id]
    例：docker network connect(connect) network_name xxs
    通过docker inspect xxs 查看xxs容器的网络信息，增加(减少)了network_name网络
```

网络类型

```docker
host: 共享宿主机网络
bridge: 同一个bridge网络的容器可以互相通信，各个容器IP不同，可能会有变动
container: 同一个container网络下的容易共享网络，一个IP，容器之间可以使用 localhost 高效快速通信。
    docker run -itd --name xxs --network container:[container name/id] kky:v1 /bin/bash

network_mode: "bridge"
network_mode: "host"
network_mode: "none"
network_mode: "service:[service name]"
network_mode: "container:[container name/id]"
```

docker daemon配置

```docker
阿里云源:https://ygz2147j.mirror.aliyuncs.com
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
```
