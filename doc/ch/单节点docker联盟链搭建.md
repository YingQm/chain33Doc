# 搭建单节点docker联盟链
QBFT联盟链共识机制，是复杂美自研的一种共识算法，意为快速的拜占庭容错算法。在正式的开发环境中QBFT联盟链共识机制要求节点数满足N>3f，至少需要3f+1个节点（也就是最少需要4台服务器），但在前期调研测试场景下也能实现以1台服务器搭建单节点联盟链。

## 应用场景
本文介绍在Linux操作系统上以QBFT联盟链共识机制搭建单节点测试联盟链。
在测试联盟链中无需真实的4个联盟共识节点，而是虚拟出4个docker容器作为共识节点，由于是在1台服务器上部署的联盟链，所以无法避免单点故障，所以仅能在测试场景下使用，不可在生产环境中使用。


## 准备环境

**- 安装前检查**
确保curl和wget命令可用，如果不可用，通过以下方式安装。如果提示`Failed connect to...`，可能是因为服务器无法访问镜像，请绑定公网后重试。
```bash
#ubuntu系统
sudo apt-get install wget
sudo apt-get install curl

#centos系统
sudo yum install wget
sudo yum install curl
```

**- 下载软件包**

下载单节点docker联盟链软件包: [资源下载](https://chain.33.cn/resource)

解压软件包到服务器任意目录，软件包中包含以下文件：
```text
chain33            -- chain33节点程序
chain33-cli        -- chain33节点命令行工具
chain33.toml       -- chain33主链配置文件
docker-build.sh    -- docker镜像生成脚本
env.sh             -- docker和docker-compser安装脚本
```

## 安装启动

### 安装docker(支持ubunt和centos)
如果服务器上没有安装docker命令，可使用`env.sh`安装，如果已经安装则跳过此步骤。
```bash
# 在软件包解压缩目录下，执行以下命令，安装docker。
sudo bash env.sh

# 当出现以下提示，表示docker和docker-compose安装成功
Checking env..... SUCCESS
```
**注意：**如果用户是centos操作系统，在安装docker过程中可能会出现`no docker-compose in (/sbin:/bin:/usr/sbin:/usr/bin)`问题，导致docker-compose组件安装失败。此时，需要用户在上述指定目录下自行下载安装docker-compose组件，安装成功后再重新执行docker安装命令。
![docker-compose安装失败](https://public.zhaobi.tech/web/storage/upload/20211103/0eb21f3d5ff091f4319e13b729421645.png "docker-compose安装失败")

### 生成配置文件
`docker-build.sh`脚本用于生成chain33镜像和对应的配置文件。
```bash
# 执行以下命令，生成chain33镜像和对应的配置文件。
sudo bash docker-build.sh

# 当出现以下提示，表示环境编译成功
docker build chain33 image sucess!
```
【说明】默认使用4个节点和172.50.0.0网段，用户也可以自己配置。
```bash
#用法
./docker-build.sh <num> <network>
    num --- 节点数量，默认是4个节点。
    network -- 节点网络，默认是172.50.0.0。

#例子
./docker-build.sh 4 172.50.0.0
```
执行成功后会生成`docker-compose.yaml`和`Dockerfile`文件，以及对应节点的挂载目录。

### 启动docker
```bash
sudo docker-compose -f docker-compose.yaml up --build -d

# 当出现以下提示，表示docker联盟链环境启动成功。
Creating network "chain33_qbft_docker_app_net" with driver "bridge"
Creating chain33-172.50.0.3 ... done
Creating chain33-172.50.0.2 ... done
Creating chain33-172.50.0.5 ... done
Creating chain33-172.50.0.4 ... done
```

### 检查启动情况
```bash
sudo docker-compose ps

       Name                     Command               State                          Ports                       
-----------------------------------------------------------------------------------------------------------------
chain33-172.50.0.2   /app/chain33 -f /app/chain ...   Up      33001/tcp, 0.0.0.0:8801->8801/tcp,:::8801->8801/tcp
chain33-172.50.0.3   /app/chain33 -f /app/chain ...   Up      33001/tcp, 0.0.0.0:8802->8801/tcp,:::8802->8801/tcp
chain33-172.50.0.4   /app/chain33 -f /app/chain ...   Up      33001/tcp, 0.0.0.0:8803->8801/tcp,:::8803->8801/tcp
chain33-172.50.0.5   /app/chain33 -f /app/chain ...   Up      33001/tcp, 0.0.0.0:8804->8801/tcp,:::8804->8801/tcp
```

### 检查同步状态

```bash
sudo docker exec chain33-172.50.0.2 /app/chain33-cli net is_sync

true
```
### 检查节点连接
```bash
sudo docker exec chain33-172.50.0.2 /app/chain33-cli net peer

"peers": [
        {
            "addr": "172.50.0.3",
            "port": 13802,
            "name": "033aab14ba5baa4870e2b46bede8e7e1533a90d9cd0140f3db1beaa00322f6df2e",
            "mempoolSize": 0,
            "self": false,
            "header": {
                "version": 0,
                "parentHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "txHash": "0x22db70a26130f2fe4758fd65bf016949c1c46f5642b4a556f8a0ff7a41350898",
                "stateHash": "0xc34a7713273f1ac2256355c754b6c8ed9b9c726b84d16866ccaa4b7df29d7cc8",
                "height": 0,
                "blockTime": 1514533394,
                "txCount": 1,
                "hash": "0xc8799befacd9709a5f4dfa68d6fd53a37ccce83352997a132adfed7f46747757",
                "difficulty": 0
            }
        },
        {
            "addr": "172.50.0.4",
            "port": 13802,
            "name": "02b541a2ca571732da6d10267ad7d6b61f3f01381a31d217ea1112d04a2758ae13",
            "mempoolSize": 0,
            "self": false,
            "header": {
                "version": 0,
                "parentHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "txHash": "0x22db70a26130f2fe4758fd65bf016949c1c46f5642b4a556f8a0ff7a41350898",
                "stateHash": "0xc34a7713273f1ac2256355c754b6c8ed9b9c726b84d16866ccaa4b7df29d7cc8",
                "height": 0,
                "blockTime": 1514533394,
                "txCount": 1,
                "hash": "0xc8799befacd9709a5f4dfa68d6fd53a37ccce83352997a132adfed7f46747757",
                "difficulty": 0
            }
        },
        {
            "addr": "172.50.0.5",
            "port": 13802,
            "name": "03616eea07ff17147a1475fe938ae2638c77421f01c48e1c003e3ff37959585a7a",
            "mempoolSize": 0,
            "self": false,
            "header": {
                "version": 0,
                "parentHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "txHash": "0x22db70a26130f2fe4758fd65bf016949c1c46f5642b4a556f8a0ff7a41350898",
                "stateHash": "0xc34a7713273f1ac2256355c754b6c8ed9b9c726b84d16866ccaa4b7df29d7cc8",
                "height": 0,
                "blockTime": 1514533394,
                "txCount": 1,
                "hash": "0xc8799befacd9709a5f4dfa68d6fd53a37ccce83352997a132adfed7f46747757",
                "difficulty": 0
            }
        },
        {
            "addr": "172.50.0.2",
            "port": 13802,
            "name": "033bc186f046b3098facc0f6954f23d8e65ca9ddcbe2f789a834c526dbc5e3446d",
            "mempoolSize": 0,
            "self": true,
            "header": {
                "version": 0,
                "parentHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "txHash": "0x22db70a26130f2fe4758fd65bf016949c1c46f5642b4a556f8a0ff7a41350898",
                "stateHash": "0xc34a7713273f1ac2256355c754b6c8ed9b9c726b84d16866ccaa4b7df29d7cc8",
                "height": 0,
                "blockTime": 1514533394,
                "txCount": 1,
                "hash": "0xc8799befacd9709a5f4dfa68d6fd53a37ccce83352997a132adfed7f46747757",
                "difficulty": 0
            }
        }
    ]

```