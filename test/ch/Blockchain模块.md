# Blockchain 模块

[TOC]

## 1 模块介绍

Blockchain 模块是处理 block 的组件，包括存储 block 信息，将 block 加入主链或者侧链，同步 block。同时对外提供查询 block 以及区块链状态信息的接口。

## 2 逻辑架构及上下文

### 2.1 Blockchain 上下文

![Blockchain上下文](https://public.33.cn/web/storage/upload/20190717/0d0f0c3e5588512428222175a8f8b085.jpg)

- 与 Consensus 模块的交互：处理 Consensus 模块打包的区块，处理 Consensus 模块查询 block 信息的请求

- 与 P2P 模块的交互：处理 P2P 模块接收的广播区块，向 P2P 模块发送区块进行广播，处理 P2P 模块查询 block 信息的请求

- 与 Mempool，Executor 模块的交互：处理这两个模块查询区块链状态的请求

### 2.2 Blockchain 逻辑结构

Blockchain 模块主要由三个子模块组成：消息接收模块，区块同步模块和区块存储模块

> 消息接收模块

接受其他模块的有关 block 以及区块链状态的信息查询的消息

> 区块同步模块

在节点起动之后，比较网络中 peer 最新高度和自己的高度，如果自己的高度比 peer 的最新高度低就主动发起 block 的同步请求追赶主链

> 区块存储模块

将 block 信息按照不同类型存储到数据库

## 3 处理逻辑

> 下面介绍三个模块的处理逻辑

### 3.1 消息接收模块

包括如下消息：

#### block 相关信息

- EventGetBlocks： 获取 block 信息
- EventGetHeaders： 获取 block header信息
- EventAddBlock：添加从 peer 同步过来的 block
- EventAddBlockHeaders： 添加从 peer 同步过来的 block header
- EventAddBlockDetail：添加从共识模块过来的 block
- EventBroadcastAddBlock：添加从 peer 广播过来的 block
- EventGetBlockHeight：获取最新 block 高度
- EventGetLastHeader： 获取最新 block header 信息
- EventGetLastBlock：获取最新 block 信息

#### 区块链浏览器相关的消息

- EventGetTransactionByAddr：通过账户地址获取地址上所有交易的 hash 值
- EventGetTransactionByHash：通过交易的 hash 值获取对应的交易信息
- EventGetBlockOverview：通过 block hash 值获取此 block 的 header 信息以及交易 hash 列表
- EventGetAddrOverview：通过账户地址获取账户收到的币，账户当前余额以及参与的交易数量
- EventGetBlockHash：通过 block 高度获取 block hash
- EventQueryTx：通过交易 hash 获取具体的交易信息，包含 txproof 证明

#### 平行链相关消息

- EventGetLastBlockSequence：获取本节点最新区块对应的 sequence
- EventGetSeqByHash：获取区块哈希对应的 sequence
- EventAddParaChainBlockDetail：添加来自平行链共识的 block
- EventDelParaChainBlockDetail：删除来自平行链共识的 block
- EventLocalGet：查询存储的键值对

#### 其他消息

- EventIsSync：查询区块链的同步状态
- EventIsNtpClockSync：查询 ntp 网络时间同步状态
- EventLocalPrefixCount：查询指定前缀的 key 的数量

### 3.2 区块同步模块

包括定时处理逻辑和即时处理逻辑

#### 定时处理

1. FetchPeerList：定时从 p2p 模块获取网络中 peer 信息，并保存到本地 peerList
2. SynBlocksFromPeers：定时从 peerList 中请求指定的 blocks
3. CheckTipBlockHash：定时检测本节点最新高度 block hash 是否和 peerlist 中对应高度的 block hash 一致
4. CheckBestChain：定时检测并获取一个最优链列表，保证请求 block 的 peers 和本节点都在同一条链上
5. RecoveryFaultPeer：故障 peer 节点的定时检测恢复

#### 即时处理

收到三种来源的 block 并进行处理：共识模块打包的 block，广播 block，同步 block

处理入口函数 ProcessBlock()，过程如下：

- 判断 block 是否已经存在本节点的主/侧链上
- 判断 block 是否已经存在本节点的孤儿链上
- 判断 block 的父 block 是否已存在本节点的主/侧链上
- 尝试将 block 添加到主/侧链上
- 尝试处理孤儿链中以此 block 为父区块的孤儿 block

### 3.3 区块存储模块

#### 存储数据内容

存储格式均为 key-value 形式，包括如下数据内容：

> 区块相关

1. key("blockLastHeight")：存储最新区块高度
2. key("Hash:%v", blockhash)：存储区块高度
3. key("Body:%v", blockhash)：存储区块 body
4. key("Header:%v", blockhash)：存储区块 header
5. key("TD:%v", blockhash)：存储区块 body
6. key("Height:%v", height)：存储区块高度对应的区块 hash
7. key("HH:%v", height)：存储区块高度对应的区块 header
8. key("LastSequence")：存储最新 sequence
9. key("Seq:%v", sequence)：存储 sequence 对应的区块 hash
10. key("HashToSeq:%v", blockhash): 存储区块 hash 对应的 sequence

> 交易相关

1. key("TxAddrHash:%s:%s", addr, heightindex)：存储地址相关的交易 hash 列表
2. key("TxAddrDirHash:%s:%d:%s", addr, flag, heightindex)：存储地址相关的某个分类的的交易 hash 列表
3. key("AddrTxsCount:%s", addr)：存储地址参与的交易数量

#### 数据访问接口

> 获取和存储最新 block 信息

- UpdateHeight
- UpdateLastBlock
- LastHeader
- LastBlock

> 获取和存储 block 信息

- LoadBlockByHeight
- LoadBlockByHash
- GetHeightByBlockHash
- GetBlockHashByHeight
- GetBlockHeaderByHeight
- GetBlockHeaderByHash
- GetTdByBlockHash
- SaveTdByBlockHash

> 存储和删除区块和交易

- SaveBlock
- DelBlock
- GetTx
- AddTxs
- DelTxs