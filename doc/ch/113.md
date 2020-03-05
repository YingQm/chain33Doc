# 联盟链部署及发行Token

[TOC]

本文主要介绍如何基于chain33搭建一条联盟链，并在链上实现数据存证，token发行，转账等能力。
以下的操作命令都是在Linux系统上执行，使用git bash命令行工具，Windows上的命令与之相似，区别只在于chain33主程序和命令行工具的名称。

## 1 部署chain33联盟链
同pbft一样，tendermint的节点数也是要满足N>3f，所以至少3f+1个节点
### 1.1 部署4节点的联盟链集群

```shell
# 创建四个节点
# 节点可通过本地VMware Workstation设置多个Ubuntu虚拟机来创建
# Ubuntu镜像地址推荐：http://mirrors.aliyun.com/ubuntu-releases/18.04/ubuntu-18.04.3-live-server-amd64.iso

# 下载编译好的文件（在每个节点上下载并解压）
$ wget https://bty33.oss-cn-shanghai.aliyuncs.com/chain33_tendermint_v6.3.0.tar.gz

# 解压
$ tar -zxvf chain33_tendermint_v6.3.0.tar.gz

# 为目录赋予权限：
$ chmod 775 chain33_tendermint_v6.3.0

# 进入chain33_tendermint_v6.3.0目录：
$ cd chain33_tendermint_v6.3.0

# 为可执行文件赋予权限：
$ chmod 775 chain33 chain33-cli
```

> 文件介绍：
- chain33: chain33区块链的主程序文件
- chain33-cli: 命令行工具（可以用它来实现对区块链的操作，包括创建账户，转账，发送交易，查询等一系列功能）
- chain33.toml: 主程序对应的配置文件
- genesis.json，priv_validator_1.json， priv_validator_2.json，priv_validator_3.json， priv_validator_4.json： 4个节点需要的公私钥文件

> 备注：
- priv_validator_x.json中是各个节点私钥信息，具有隐私性，不应该公开。 此处只为简化搭建流程。
- 正式环境部署时，参考 https://chain.33.cn/document/129 中的流程。

> 环境启动前准备工作：
- 修改样例中的配置文件 chain33.toml，将两处的 IP 地址替换为所部署节点的 IP

```shell
......
[p2p]
seeds=["10.0.0.1:13802","10.0.0.2:13802","10.0.0.3:13802","10.0.0.4:13802"]
......
[consensus.sub.tendermint]
validatorNodes=["10.0.0.1:46656","10.0.0.2:46656","10.0.0.3:46656","10.0.0.4:46656"]
......
```

- 第一个节点保留priv_validator_1.json 并将其重命名为 priv_validator.json。 同时可以删除priv_validator_2.json，priv_validator_3.json，priv_validator_4.json
- 第二个节点保留priv_validator_2.json 并将其重命名为 priv_validator.json。 同时可以删除priv_validator_1.json，priv_validator_3.json，priv_validator_4.json
- 第三个节点保留priv_validator_3.json 并将其重命名为 priv_validator.json。 同时可以删除priv_validator_1.json，priv_validator_2.json，priv_validator_4.json
- 第四个节点保留priv_validator_4.json 并将其重命名为 priv_validator.json。 同时可以删除priv_validator_1.json，priv_validator_2.json，priv_validator_3.json

> 启动环境：
- 在4个节点上启动 chain33，顺序不分前后，建议在一分钟内全都启动

```shell
# 启动
$ nohup ./chain33 -f chain33.toml >> log.out 2>&1 &
```

> 节点状态检查
- 查询节点是否已经和其它节点同步(5分钟左右)

```shell
$ ./chain33-cli net is_sync
true
```

> 节点信息查询
- 查看各个节点的信息

```shell
$ ./chain33-cli net peer_info
{
    "peers": [
        {
            "addr": "172.18.0.2",
            "port": 13802,
            "name": "0210c1c09b0d61e41d819e28dcbf1148ebae5fb12a8066a9064e7e1c2346432c91",
            "mempoolSize": 100,
            "self": false,
            "header": {
                "version": 0,
                "parentHash": "0x38e72824d7eb1e147ec5b45f281746f934d152d3f1c04d165b9aa326d7cf407d",
                "txHash": "0xfc26ee8f9aab9362e3f6b6289dad94111eedf9278972a61fcfa5a0aae471d3bf",
                "stateHash": "0x88f0b06df8cd2cd6da81e1580e6f179128e42aa8c66e2dba9c38af3e18f9fa44",
                "height": 52510,
                "blockTime": 1545876177,
                "txCount": 101,
                "hash": "0x808a985f4fa63922c96fb68d896a840a637bbf94655c2eccacb876f5a07849af",
                "difficulty": 0
            }
        },
        {
            "addr": "172.18.0.3",
            "port": 13802,
            "name": "03e8c670f6641e2cc73d149610fd81ffb94c20b83e9428bd61f834adcbf33b3927",
            "mempoolSize": 100,
            "self": false,
            "header": {
                "version": 0,
                "parentHash": "0x38e72824d7eb1e147ec5b45f281746f934d152d3f1c04d165b9aa326d7cf407d",
                "txHash": "0xfc26ee8f9aab9362e3f6b6289dad94111eedf9278972a61fcfa5a0aae471d3bf",
                "stateHash": "0x88f0b06df8cd2cd6da81e1580e6f179128e42aa8c66e2dba9c38af3e18f9fa44",
                "height": 52510,
                "blockTime": 1545876177,
                "txCount": 101,
                "hash": "0x808a985f4fa63922c96fb68d896a840a637bbf94655c2eccacb876f5a07849af",
                "difficulty": 0
            }
        },
        {
            "addr": "172.18.0.4",
            "port": 13802,
            "name": "03a4f80a2d73f999b44e3b1137676e00e5eb1357ce22e9a296b5032cf1d128e0dc",
            "mempoolSize": 100,
            "self": false,
            "header": {
                "version": 0,
                "parentHash": "0x38e72824d7eb1e147ec5b45f281746f934d152d3f1c04d165b9aa326d7cf407d",
                "txHash": "0xfc26ee8f9aab9362e3f6b6289dad94111eedf9278972a61fcfa5a0aae471d3bf",
                "stateHash": "0x88f0b06df8cd2cd6da81e1580e6f179128e42aa8c66e2dba9c38af3e18f9fa44",
                "height": 52510,
                "blockTime": 1545876177,
                "txCount": 101,
                "hash": "0x808a985f4fa63922c96fb68d896a840a637bbf94655c2eccacb876f5a07849af",
                "difficulty": 0
            }
        },
        {
            "addr": "172.18.0.5",
            "port": 13802,
            "name": "0382362b8b1d374646f728ae4e93e103f237747ef59a7518117f4c3483cb05a17b",
            "mempoolSize": 100,
            "self": true,
            "header": {
                "version": 0,
                "parentHash": "0x38e72824d7eb1e147ec5b45f281746f934d152d3f1c04d165b9aa326d7cf407d",
                "txHash": "0xfc26ee8f9aab9362e3f6b6289dad94111eedf9278972a61fcfa5a0aae471d3bf",
                "stateHash": "0x88f0b06df8cd2cd6da81e1580e6f179128e42aa8c66e2dba9c38af3e18f9fa44",
                "height": 52510,
                "blockTime": 1545876177,
                "txCount": 101,
                "hash": "0x808a985f4fa63922c96fb68d896a840a637bbf94655c2eccacb876f5a07849af",
                "difficulty": 0
            }
        }
    ]
}
```

## 2 token的系统配置
在完成上一步操作后，登录到任意一个区块链节点上，使用chain33-cli命令行工具操作。由于以下这些操作对于一条区块链来说，只需要在链部署好后执行一次就可以，所以这边直接使用命令行来演示。

发行token之前需要有以下两步准备工作：
### 2.1 配置本条链的超级管理员
超级管理员的作用是增加系统配置，比如下面的token-blacklist, token-finisher的配置。 
在chain33.toml中修改添加以下两项配置，把这两个地址改成自己想设置的地址 
（最好改一下，自己创建的地址私钥自己保管好；不愿意改的，这边也提供下面地址对应的私钥：3990969DF92A5914F7B71EEB9A4E58D6E255F32BF042FEA5318FC8B3D50EE6E8 ）。
```shell
[exec.sub.manage]
superManager=[
    "1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs",
]

[exec.sub.token]
saveTokenTxList=true
tokenApprs = [
        "1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs",
]
```
修改配置文件完毕后，重启该节点并读取新修改的配置文件：
```shell
$ pkill chain33
$ nohup ./chain33 -f chain33.toml >> log.out 2>&1 &
```

### 2.2 配置token-finisher和token-blacklist
token-finisher: token审核人的地址， 用来在token预创建之后，对token的信息（名称，额度）进行审核。
token-blacklist：token黑名单，指示哪些名称不可以在链上创建，比如BTC,ETH等等。

```shell
# 配置token-finisher，-c：固定填"token-finisher"，-o：add(表示添加)，-v：token-finisher的地址
$ ./chain33-cli config config_tx -c token-finisher -o add -v 1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs
# 签名交易，-k：区块链的超级管理员的私钥匙
$ ./chain33-cli wallet sign -k 3990969DF92A5914F7B71EEB9A4E58D6E255F32BF042FEA5318FC8B3D50EE6E8 -d "上一步生成的数据"
# 发送交易
$ ./chain33-cli wallet send -d "上一步生成的签名后的数据"

# 查询结果
$ ./chain33-cli config query_config -k token-finisher
# 输出样例
{
    "key": "token-finisher",
    "value": "[1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs]"
}

# 配置token-blacklist，-c: 固定填"token-blacklist"，-o：add(表示添加)，-v：黑名单名称，比如这边的BTY
$ ./chain33-cli  config config_tx -c token-blacklist -o add -v BTY
$ ./chain33-cli  wallet sign -k 3990969DF92A5914F7B71EEB9A4E58D6E255F32BF042FEA5318FC8B3D50EE6E8 -d "上一步生成的数据"
$ ./chain33-cli  wallet send -d "上一步生成的签名后的数据"

# 查询结果
$ ./chain33-cli config query_config -k token-blacklist
# 输出样例
{
    "key": "token-blacklist",
    "value": "[BTY]"
}

# token预创建 
$ ./chain33-cli token precreate -f 0.001 -i 开发者币 -n "DEVELOP COINS" -a "token接收者的地址，可以是自己，也可以指定别人" -p 0 -s "COINSDEVX" -t 19900000000
$ ./chain33-cli wallet sign -k 3990969DF92A5914F7B71EEB9A4E58D6E255F32BF042FEA5318FC8B3D50EE6E8 -d "上一步生成的签名后的数据"
$ ./chain33-cli wallet send -d "上一步生成的签名后的数据"

# 查询，这一步完成，才可以进入到下面的流程
$ ./chain33-cli token get_precreated
# 输出样例
{
    "name": "DEVELOP COINS",
    "symbol": "COINSDEVX",
    "introduction": "开发者币",
    "total": 19900000000,
    "owner": "1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs",
    "creator": "1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs",
    "prepareCreateHeight": 14,
    "prepareCreateTime": 1577432549,
    "precision": 8
}

# token finish 
$ ./chain33-cli token finish -s COINSDEVX -f 0.001 -a "token接收者的地址"
$ ./chain33-cli wallet sign -k 3990969DF92A5914F7B71EEB9A4E58D6E255F32BF042FEA5318FC8B3D50EE6E8 -d "上一步生成的签名后的数据"
$ ./chain33-cli wallet send -d "上一步生成的签名后的数据"

# 查询
$ ./chain33-cli token get_finish_created
# 输出样例
{
    "name": "DEVELOP COINS",
    "symbol": "COINSDEVX",
    "introduction": "开发者币",
    "total": 19900000000,
    "owner": "1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs",
    "creator": "1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs",
    "status": 1,
    "createdHeight": 15,
    "createdTime": 1577432745,
    "prepareCreateHeight": 14,
    "prepareCreateTime": 1577432549,
    "precision": 8
}

# 根据地址查询
$ ./chain33-cli token token_balance -a "token接收者的地址"  -s COINSDEVX -e token
# 输出样例
[
    {
        "Token": "COINSDEVX",
        "balance": "19900000000.0000",
        "frozen": "0.0000",
        "addr": "1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs"
    }
]
```
注意，只有在token-finisher和token-blacklist配置成功后，才可以进入下一步发行token的流程。

## 3 JAVA-SDK的使用
使用JAVA-SDK实现实现数据上链，token的发行功能。私链/联盟链和公链/平行链的用法有所区别，此处只介绍私链/联盟链的用法，公链/平行链在其它章节中介绍

### 3.1 数据上链
调用TransactionUtil.createTx()

**参数说明：**

|参数|类型|说明|
|----|----|----|
|privateKey|string|签名者的私钥|
|execer|string|调用的合约名称：user.write|
|payLoad|string|上链内容，json格式|
|fee|long|手续费，私链/联盟链填0|

### 3.2 token预创建
调用RpcClient.createRawTokenPreCreateTx()

**参数说明：**

|参数|类型|说明|
|----|----|----|
|name|string|token的注释名称|
|symbol|string|token的名称，只支持大写字母，同一条链不允许相同symbol存在|
|introduction|string|token介绍|
|ownerAddr|string|token的拥有者，token生成后存的地址|
|total|long|token总额，比如500个，系统最大支持900亿|
|price|long|发行token愿意承担的费用，填0就行|
|fee|long|手续费，私链/联盟链填0|

### 3.3 token完成
调用RpcClient.createRawTokenFinishTx()

**参数说明：**

|参数|类型|说明|
|----|----|----|
|fee|long|手续费，私链/联盟链填0|
|symbol|string|token的名称，只支持大写字母，同一条链不允许相同symbol存在|
|ownerAddr|string|token的拥有者，token生成后存的地址|

详细的实现可以参考以下链接：
调用例子: <a href="https://github.com/andyYuanFZM/chain33-sdk-java/blob/sdk_test/src/test/java/cn/chain33/javasdk/client/TokenTest.java" target="_blank">JAVA-SDK的调用例子</a>
