# 搭建Solo单节点主链
Solo单节点共识机制，是一个简单易部署的但只能用于非生产环境的共识机制，通常被区块链初始者用于搭建单节点测试链。

## 应用场景
用户在做区块链调研的开发测试中，可以采用Solo单节点共识机制快速部署测试链，完成数据上链的验证。
本文分别介绍Window和Linux两种操作系统上搭建单节点Chain33主链，请根据实际情况查阅对应文档。

## 下载软件包
下载主链软件包: [资源下载](https://chain.33.cn/resource)

根据操作系统，下载对应版本的软件包，再解压到任意指定目录。软件包包含以下文件：
```text
# window版本下包含：
chain33.exe       -- chain33节点程序
chain33-cli.exe   -- chain33节点命令行工具
chain33.solo.toml -- chain33主链配置文件

# linux版本下包含：
chain33           -- chain33节点程序
chain33-cli       -- chain33节点命令行工具
chain33.solo.toml -- chain33主链配置文件
```

## 修改配置文件

根据实际情况修改配置文件中以下参数：
```text
[rpc]
# 链的jsonrpc和grpc地址，可以自定义，也可直接使用默认端口。
jrpcBindAddr=":8801"
grpcBindAddr=":8802"

[consensus.sub.solo]
# 创世积分所在的地址，可以修改成自己的地址。
  · 命令行地址生成方式：https://chain.33.cn/document/126 【创建一个账户地址和私钥】
  · JAVA-SDK地址生成方式：https://baas.33.cn/doc/detail/69 【创建区块链公私钥和地址】
genesis="14KEKbYtKKQm4wMthSK9J4La4nAiidGozt"

[exec.sub.manage]
# 链管理合约的super manager地址，用于设置一些合约权限相关的配置，地址生成方式参考上述genesis地址。
superManager=["14KEKbYtKKQm4wMthSK9J4La4nAiidGozt"]
```

## 搭建单节点主链
- windows
1.在软件包解压目录打开windows终端，执行启动命令。
```bash
chain33.exe -f chain33.solo.toml
```
2.执行以下命令查询主链网络信息，判断单节点主链是否创建成功。
```bash
chain33-cli.exe net peer
```
创建成功后，将输出如下类似的节点信息：
``` text
{
    "peers": [
        {
            "addr": "192.168.0.157",
            "port": 13802,
            "name": "03a2314f11d5f78b93f13aba18618d61a652720003d8941415c6e8008761d58452",
            "mempoolSize": 0,
            "self": true,
            "header": {
                "version": 0,
                "parentHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "txHash": "0xe34a933c5abf350db4db5122abbf43f6a54da2dbd67d214f67362c36bd70d23e",
                "stateHash": "0x88f0b06df8cd2cd6da81e1580e6f179128e42aa8c66e2dba9c38af3e18f9fa44",
                "height": 0,
                "blockTime": 1514533394,
                "txCount": 1,
                "hash": "0xfd39dbdbd2cdeb9f34bcec3612735671b35e2e2dbf9a4e6e3ed0c34804a757bb",
                "difficulty": 0
            }
        }
    ]
}
```
如果执行出错，请检查`logs/chain33.log`文件中的错误信息。


- linux
1.打开终端，进入到软件包解压目录，执行启动命令。
```bash
nohup ./chain33 -f chain33.solo.toml >/dev/null 2>&1 &
```
2.执行命令，查看进程。
```bash
ps -ef | grep -v grep | grep chain33
```
3.如果进程已经启动，执行命令查询主链网络信息。
```bash
./chain33-cli net peer
```
创建成功后，将输出如下类似的节点信息：
``` text
{
    "peers": [
        {
            "addr": "192.168.0.157",
            "port": 13802,
            "name": "03a2314f11d5f78b93f13aba18618d61a652720003d8941415c6e8008761d58452",
            "mempoolSize": 0,
            "self": true,
            "header": {
                "version": 0,
                "parentHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "txHash": "0xe34a933c5abf350db4db5122abbf43f6a54da2dbd67d214f67362c36bd70d23e",
                "stateHash": "0x88f0b06df8cd2cd6da81e1580e6f179128e42aa8c66e2dba9c38af3e18f9fa44",
                "height": 0,
                "blockTime": 1514533394,
                "txCount": 1,
                "hash": "0xfd39dbdbd2cdeb9f34bcec3612735671b35e2e2dbf9a4e6e3ed0c34804a757bb",
                "difficulty": 0
            }
        }
    ]
}
```
如果执行出错，请检查`logs/chain33.log`文件中的错误信息。