### docker-env
#### 注意事项
- 此项目基于docker,docker-compose。用于快速构建Python开发环境以及一些可能需要的中间件。
- 使用`容器网络模式`，所以中间件和Python容器一个网络。映射出一些常用的端口，所以服务之间可以使用`127.0.0.1`访问。
- 如果需要构建其他的Python环境,可以使用指定容器模式链接到`docker-rnv_default`网络。
- 构建的Python环境需要用ssh或者sftp远程链接使用，默认映射端口`10029:22`， 可以按需在docker-compose修改。
- ./command.py 常用的docker命令
- ./info.txt 中间件的一些命令
- 中间件版本按需指定，ES分词器需要自己匹配
- ./test 用于构建单个Python解释器
#### 使用
- 使用docker-compose构建之前，先确定你要使用的Python容器是基于什么Linux版本，不同的版本需要不同的source.list（`tail /etc/os-release 查看操作系统` ）。
- 确定好操作系统，更换Dockerfile构建文件夹得source.list
- docker-compose up -d
- 各个中间件远程访问都已经配置完成
- 启动服务之后，需要进去py-env容器，配置SSH远程访问，并且重启SSH