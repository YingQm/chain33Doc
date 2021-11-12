# 平行链部署及发行Token

[TOC]

本节整体介绍一下如何快速搭建一条平行链，并通过java-sdk实现token的发行和转账的能力。
以下的操作命令都是在Linux系统上执行，使用git bash命令行工具，Windows上的命令与之相似，区别只在于chain33主程序和命令行工具的名称。

## 1 部署chain33平行链
### 1.1 Linux环境上部署chain33平行链
具体部署过程参见 [平行链环境搭建](https://chain.33.cn/document/130)

> 文件介绍：
- chain33: chain33区块链的主程序文件
- chain33-cli: 命令行工具（可以用它来实现对区块链的操作，包括创建账户，转账，发送交易，查询等一系列功能）
- chain33.para.toml: 主程序对应的配置文件

> 环境启动前准备工作：
- 通常情况下需要修改chain33.para.toml文件中的ParaRemoteGrpcClient和genesis这两个配置项，指向自己部署的Chain33主链（BTY主网）地址与创世地址。这边提供了公开的主网节点，需要在配置文件中找到对应字段并修改。

具体修改参见 [平行链配置文件修改](https://chain.33.cn/document/130#1.3%20%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6%E4%BF%AE%E6%94%B9)

> 启动环境：
- 启动 chain33

```shell
$ nohup ./chain33 -f chain33.para.toml >> log.out 2>&1 &
```

> 节点状态检查
- 查询节点是否已经和主链同步 (平行链需要从主链上拉取区块，所以同步需要花一些时间)

```shell
$ ./chain33-cli --rpc_laddr="http://localhost:8901" --paraName="user.p.devtest." para is_sync
true
```

> 节点区块检查
- 查看区块同步的状态

```shell
$ ./chain33-cli --rpc_laddr="http://localhost:8901" --paraName="user.p.devtest." block last_header
{
    "version": 0,
    "parentHash": "0x905d3c3ab62718381436720382e436a52976b6798896c77c97cb4e751e3a67c9",
    "txHash": "0x765a8babc9b63f7a5c608afb0943001741f3591f676026cd67dd99f6b3ad5122",
    "stateHash": "0xeb240fe1248028e9c7271ae2838ea3970bb880031764c8154c8bce2d16262cb7",
    "height": 57,
    "blockTime": 1546501778,
    "txCount": 1,
    "hash": "0xac2be112305b231b9851a34f6db7bde1745a2b7c9c3a684c736dc59baf3e6e51",
    "difficulty": 0
}
```

>注意：平行链节点执行指令时，需要添加`--rpc_laddr`以及`--paraName`后缀，rpc_laddr表示平行链节点启动的IP和监听端口，**paraName表示平行链的名称（请根据平行链配置文件中的Title项进行设置，示例为"user.p.devtest."）**

### 1.2 Windows环境上部署chain33平行链
具体部署过程参见 [平行链环境搭建](https://chain.33.cn/document/130)

> 文件介绍：
- chain33.exe: chain33区块链的主程序文件
- chain33-cli.exe: 命令行工具（可以用它来实现对区块链的操作，包括创建账户，转账，发送交易，查询等一系列功能）
- chain33.para.toml: 主程序对应的配置文件

> 环境启动前准备工作：
- 通常情况下需要修改chain33.para.toml文件中的ParaRemoteGrpcClient和genesis这两个配置项，指向自己部署的Chain33主链（BTY主网）地址与创世地址。这边提供了公开的主网节点，需要在配置文件中找到对应字段并修改。

具体修改参见 [平行链配置文件修改](https://chain.33.cn/document/130#1.3%20%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6%E4%BF%AE%E6%94%B9)

> 启动环境：
- 启动 chain33.exe

```shell
$ ./chain33.exe -f chain33.para.toml
```

> 备注：
其余操作和上面Linux环境上的类似，注意主程序文件和命令行工具和Linux上名字的区别

>注意：平行链节点执行指令时，需要添加`--rpc_laddr`以及`--paraName`后缀，rpc_laddr表示平行链节点启动的IP和监听端口，**paraName表示平行链的名称（请根据平行链配置文件中的Title项进行设置，示例为"user.p.devtest."）**

## 2 token的系统配置
在完成上一步操作后，在平行链上使用chain33-cli命令行工具操作。由于以下这些操作对于一条区块链来说，只需要在链部署好后执行一次就可以，所以这边直接使用命令行来演示。

发行token之前需要有以下两步准备工作：
### 2.1 配置本条链的超级管理员，
超级管理员的作用是增加系统配置，比如下面的token-blacklist，token-finisher的配置。 
在chain33.toml中修改以下两项配置，把这两个地址改成自己想设置的地址 
（可以不用修改，直接使用官方提供的私钥，里面有少量比特元可以用于缴纳手续费：3990969DF92A5914F7B71EEB9A4E58D6E255F32BF042FEA5318FC8B3D50EE6E8 ）。
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
# Liunx
$ pkill chain33
$ nohup ./chain33 -f chain33.para.toml >> log.out 2>&1 &

# Windows
CTRL + C
$ ./chain33.exe -f chain33.para.toml
```

### 2.2 命令行配置token-finisher、token-blacklist，发行token
token-finisher: token审核人的地址， 用来在token预创建之后，对token的信息（名称，额度）进行审核。
token-blacklist：token黑名单，指示哪些名称不可以在链上创建，比如BTC,ETH等等。

```shell
# 配置token-finisher，-c：固定填"token-finisher"，-o：add(表示添加)，-v：token-finisher的地址，--rpc_laddr：平行链节点监听地址，--paraName：对应平行链的名称
$ ./chain33-cli --rpc_laddr="http://localhost:8901" --paraName="user.p.devtest." config config_tx -c token-finisher -o add -v 1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs
# 签名交易，-k：区块链的超级管理员的私钥匙
$ ./chain33-cli --rpc_laddr="http://localhost:8901" --paraName="user.p.devtest." wallet sign -k 3990969DF92A5914F7B71EEB9A4E58D6E255F32BF042FEA5318FC8B3D50EE6E8 -d "上一步生成的数据"
# 发送交易
$ ./chain33-cli --rpc_laddr="http://localhost:8901" --paraName="user.p.devtest." wallet send -d "上一步生成的签名后的数据"

# 查询结果
$ ./chain33-cli --rpc_laddr="http://localhost:8901" --paraName="user.p.devtest." config query -k token-finisher
# 输出样例
{
    "key": "token-finisher",
    "value": "[1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs]"
}

# 配置token-blacklist，-c: 固定填"token-blacklist"，-o：add(表示添加)，-v：黑名单名称，比如这边的BTY，--rpc_laddr：平行链节点监听地址，--paraName：对应平行链的名称
$ ./chain33-cli --rpc_laddr="http://localhost:8901" --paraName="user.p.devtest." config config_tx -c token-blacklist -o add -v BTY
$ ./chain33-cli --rpc_laddr="http://localhost:8901" --paraName="user.p.devtest." wallet sign -k 3990969DF92A5914F7B71EEB9A4E58D6E255F32BF042FEA5318FC8B3D50EE6E8 -d "上一步生成的数据"
$ ./chain33-cli --rpc_laddr="http://localhost:8901" --paraName="user.p.devtest." wallet send -d "上一步生成的签名后的数据"

# 查询结果
$ ./chain33-cli --rpc_laddr="http://localhost:8901" --paraName="user.p.devtest." config query -k token-blacklist
# 输出样例
{
    "key": "token-blacklist",
    "value": "[BTY]"
}

# token预创建
$ ./chain33-cli --rpc_laddr="http://localhost:8901" --paraName="user.p.devtest." token precreate -f 0.001 -i 开发者币 -n "DEVELOP COINS" -a "token接收者的地址，可以是自己，也可以指定别人" -p 0 -s "COINSDEVX" -t 19900000000
$ ./chain33-cli --rpc_laddr="http://localhost:8901" --paraName="user.p.devtest." wallet sign -k 3990969DF92A5914F7B71EEB9A4E58D6E255F32BF042FEA5318FC8B3D50EE6E8 -d "上一步生成的签名后的数据"
$ ./chain33-cli --rpc_laddr="http://localhost:8901" --paraName="user.p.devtest." wallet send -d "上一步生成的签名后的数据"

# 查询，这一步完成，才可以进入到下面的流程
$ ./chain33-cli --rpc_laddr="http://localhost:8901" --paraName="user.p.devtest." token get_precreated
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
$ ./chain33-cli --rpc_laddr="http://localhost:8901" --paraName="user.p.devtest." token finish -s COINSDEVX -f 0.001 -a "token接收者的地址"
$ ./chain33-cli --rpc_laddr="http://localhost:8901" --paraName="user.p.devtest." wallet sign -k 3990969DF92A5914F7B71EEB9A4E58D6E255F32BF042FEA5318FC8B3D50EE6E8 -d "上一步生成的签名后的数据"
$ ./chain33-cli --rpc_laddr="http://localhost:8901" --paraName="user.p.devtest." wallet send -d "上一步生成的签名后的数据"

# 查询
$ ./chain33-cli --rpc_laddr="http://localhost:8901" --paraName="user.p.devtest." token get_finish_created
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
$ ./chain33-cli --rpc_laddr="http://localhost:8901" --paraName="user.p.devtest." token token_balance -a "token接收者的地址"  -s COINSDEVX -e token
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
使用JAVA-SDK实现实现数据上链，token的发行功能。私链/联盟链和公链/平行链的用法有所区别，此处只介绍公链/平行链用法。

### 3.1 token预创建
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

再调用RpcClient.createNoBalanceTx()

**参数说明：**

|参数|类型|说明|
|----|----|----|
|txHex|string|上一步生成的交易txhex|
|payAddr|string|代扣手续费对应的地址|

### 3.2 token完成
调用RpcClient.createRawTokenFinishTx()

**参数说明：**

|参数|类型|说明|
|----|----|----|
|fee|long|手续费，私链/联盟链填0|
|symbol|string|token的名称，只支持大写字母，同一条链不允许相同symbol存在|
|ownerAddr|string|token的拥有者，token生成后存的地址|

再调用RpcClient.createNoBalanceTx()

**参数说明：**

|参数|类型|说明|
|----|----|----|
|txHex|string|上一步生成的交易txhex|
|payAddr|string|代扣手续费对应的地址|

### 3.3 token转账
调用RpcClient.createRawTransaction()

**参数说明：**

|参数|类型|说明|
|----|----|----|
|to|long|手续费，私链/联盟链填0|
|amount|long|发送金额|
|fee|long|手续费|
|note|string|备注|
|isToken|boolean|是否是token类型的转账|
|isWithdraw|boolean|是否为取款交易|
|tokenSymbol|string|token 的 symbol|

再调用RpcClient.createNoBalanceTx()

**参数说明：**

|参数|类型|说明|
|----|----|----|
|txHex|string|上一步生成的交易txhex|
|payAddr|string|代扣手续费对应的地址|

详细的实现可以参考以下链接：
调用例子: <a href="https://github.com/andyYuanFZM/chain33-sdk-java/blob/sdk_test/src/test/java/cn/chain33/javasdk/client/TokenParaTest.java" target="_blank">JAVA-SDK的调用例子</a>
