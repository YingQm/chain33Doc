## 平行链超级节点创建和超级账户管理介绍
[TOC]

>平行链只有创建了超级账户组才能完成跨链资产的转移，包括从主链往平行链转移和从平行链向主链转移资产

### 1 搭建超级节点过程介绍
[搭建超级节点过程介绍](https://chain.33.cn/document/134#%EF%BC%91%EF%BC%8E%E6%90%AD%E5%BB%BA%E8%B6%85%E7%BA%A7%E8%8A%82%E7%82%B9%E8%BF%87%E7%A8%8B%E4%BB%8B%E7%BB%8D)

### 2 超级节点账户组创建交易结构详细介绍

> 超级节点账户组用于平行链超级节点共识的确认管理，只有在账户组内部的账户可以参与共识和得到挖矿奖励

**账户组创建提供了如下操作**
  - 申请创建超级节点账户组
  - 超级账户批准账户组的申请
  - 取消正在申请的超级节点账户组
  - 修改超级账户组参数

**说明**
  - 账户组的申请者需要预先在paracross合约存一定量的币，申请后即冻结
  - 超级账户批准所带的冻结币数量为准入币数量，申请者的冻结币不得少于审批者的币数量，否则申请者需取消申请，重新提交申请
  - 在账户组的申请未批准之前，申请者可以取消申请，冻结币释放
  - 超级账户组批准后也允许修改参数，比如冻结币数量，也需要超级管理员审批


#### 2.1 生成 申请创建账户组 的交易（未签名）
**调用接口**
```
rpc CreateTransaction(CreateTxIn) returns (UnsignTx) {}
```
**参数：**
```
message CreateTxIn {
    bytes  execer     = 1;
    string actionName = 2;
    bytes  payload    = 3;
}
message ParaNodeGroupConfig {
    string title       = 1;
    uint32 op          = 2;
    string id          = 3;
    string addrs       = 4;
    int64  coinsFrozen = 5;
    string blsPubKeys  = 6;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|execer|bytes|执行器名称, 必须是平行链的执行器, 这里固定为 user.p.para.paracross|
|actionName|string|操作名称, 这里固定为 NodeGroupConfig|
|payload|bytes|types.Encode(&ParaNodeGroupConfig)|
|title|string|平行链title名字|
|op|string|配置类型：1:申请, 2:审批, 3:取消申请, 4:修改|
|addrs|string|申请账户，可以有多个|
|coinsFrozen|string|冻结币数量| 

#### 2.2 审批 申请的创建账户组 的交易（未签名)
**调用接口**
```
rpc CreateTransaction(CreateTxIn) returns (UnsignTx) {}
```
**参数：**
```
message CreateTxIn {
    bytes  execer     = 1;
    string actionName = 2;
    bytes  payload    = 3;
}
message ParaNodeGroupConfig {
    string title       = 1;
    uint32 op          = 2;
    string id          = 3;
    string addrs       = 4;
    int64  coinsFrozen = 5;
    string blsPubKeys  = 6;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|execer|bytes|执行器名称, 必须是平行链的执行器, 这里固定为 user.p.para.paracross|
|actionName|string|操作名称, 这里固定为 NodeGroupConfig|
|payload|bytes|types.Encode(&ParaNodeGroupConfig)|
|op|string|配置类型：1:申请, 2:审批, 3:取消申请, 4:修改|
|id|string|须与申请创建的id一致,或者就是申请的交易hash|
|coinsFrozen|string|审批要求的币数量|

#### 2.3 取消 申请的创建账户组 的交易（未签名）
**调用接口**
```
rpc CreateTransaction(CreateTxIn) returns (UnsignTx) {}
```
**参数：**
```
message CreateTxIn {
    bytes  execer     = 1;
    string actionName = 2;
    bytes  payload    = 3;
}
message ParaNodeGroupConfig {
    string title       = 1;
    uint32 op          = 2;
    string id          = 3;
    string addrs       = 4;
    int64  coinsFrozen = 5;
    string blsPubKeys  = 6;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|execer|bytes|执行器名称, 必须是平行链的执行器, 这里固定为 user.p.para.paracross|
|actionName|string|操作名称, 这里固定为 NodeGroupConfig|
|payload|bytes|types.Encode(&ParaNodeGroupConfig)|
|op|string|配置类型：1：申请，2：审批通过,3:取消申请,4：修改|
|id|string|须与申请创建的账户完全一致|

#### 2.4 修改 创建账户组参数 的交易（未签名）
**调用接口**
```
rpc CreateTransaction(CreateTxIn) returns (UnsignTx) {}
```
**参数：**
```
message CreateTxIn {
    bytes  execer     = 1;
    string actionName = 2;
    bytes  payload    = 3;
}
message ParaNodeGroupConfig {
    string title       = 1;
    uint32 op          = 2;
    string id          = 3;
    string addrs       = 4;
    int64  coinsFrozen = 5;
    string blsPubKeys  = 6;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|execer|bytes|执行器名称, 必须是平行链的执行器, 这里固定为 user.p.para.paracross|
|actionName|string|操作名称, 这里固定为 NodeGroupConfig|
|payload|bytes|types.Encode(&ParaNodeGroupConfig)|
|op|string|配置类型：1：申请，2：审批,3:取消申请，4：修改|
|coinFrozen|int64|修改的冻结币的数量|

#### 2.5 查询 账户组的账户信息
**调用接口**
```
rpc QueryChain(ChainExecutor) returns (Reply) {}
```
**参数：**
```
message ChainExecutor {
    string driver    = 1;
    string funcName  = 2;
    bytes  stateHash = 3;
    bytes  param     = 4;
    //扩展字段，用于额外的用途
    bytes extra = 5;
}
message ReqParacrossNodeInfo {
    string title  = 1;
    string id     = 2;
    string addr   = 3;
    int32  status = 4;
    string blsPubKey  = 5;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|driver|bytes|执行器名称, 这里固定为 paracross|
|funcName|string|操作名称, 这里固定为 GetNodeGroupAddrs|
|stateHash|bytes|所有交易在对应的执行器执行后写入KVDB中重新计算得到的新state的哈希值|
|param|bytes|types.Encode(&ReqParacrossNodeInfo)|
|extra|bytes|扩展字段，用于额外的用途|
|title|string|平行链的title名字|

**返回数据：**
```
message ReplyConfig {
    string key   = 1;
    string value = 2;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|key|string|"mavl-paracross-nodes-title-user.p.para."|
|value|string|"[1KSBd17H7ZK8iT37aJztFB22XGwsPTdwE4 1JRNjdEqp4LJ5fqycUBm9ayCKSeeskgMKR 1NLHPEcbTWWxxU3dGUZBhayjrCHD3psX7k 1MCftFynyvG2F4ED5mdHYgziDxx6vDrScs]"|

#### 2.6 查询 账户组的当前状态
**调用接口**
```
rpc QueryChain(ChainExecutor) returns (Reply) {}
```
**参数：**
```
message ChainExecutor {
    string driver    = 1;
    string funcName  = 2;
    bytes  stateHash = 3;
    bytes  param     = 4;
    //扩展字段，用于额外的用途
    bytes extra = 5;
}
message ReqParacrossNodeInfo {
    string title  = 1;
    string id     = 2;
    string addr   = 3;
    int32  status = 4;
    string blsPubKey  = 5;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|driver|bytes|执行器名称, 这里固定为 paracross|
|funcName|string|操作名称, 这里固定为 GetNodeGroupStatus|
|stateHash|bytes|所有交易在对应的执行器执行后写入KVDB中重新计算得到的新state的哈希值|
|param|bytes|types.Encode(&ReqParacrossNodeInfo)|
|extra|bytes|扩展字段，用于额外的用途|
|title|string|平行链的title名字|

**返回数据：**
```
message ParaNodeGroupStatus {
    string id          = 1;
    int32  status      = 2;
    string title       = 3;
    string targetAddrs = 4;
    int64  coinsFrozen = 5;
    string fromAddr    = 6;
    int64  height      = 7;
    string blsPubKeys  = 8;
}
```

#### 2.7 查询 按状态查询账户组的申请信息
**调用接口**
```
rpc QueryChain(ChainExecutor) returns (Reply) {}
```
**参数：**
```
message ChainExecutor {
    string driver    = 1;
    string funcName  = 2;
    bytes  stateHash = 3;
    bytes  param     = 4;
    //扩展字段，用于额外的用途
    bytes extra = 5;
}
message ReqParacrossNodeInfo {
    string title  = 1;
    string id     = 2;
    string addr   = 3;
    int32  status = 4;
    string blsPubKey  = 5;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|driver|bytes|执行器名称, 这里固定为 paracross|
|funcName|string|操作名称, 这里固定为 ListNodeGroupStatus|
|stateHash|bytes|所有交易在对应的执行器执行后写入KVDB中重新计算得到的新state的哈希值|
|param|bytes|types.Encode(&ReqParacrossNodeInfo)|
|extra|bytes|扩展字段，用于额外的用途|
|status|int|0: 全部，1：申请，2：批准，3：退出，4：修改|

**返回数据：**
```
message RespParacrossNodeGroups {
    repeated ParaNodeGroupStatus ids = 1;
}

message ParaNodeGroupStatus {
    string id          = 1;
    int32  status      = 2;
    string title       = 3;
    string targetAddrs = 4;
    int64  coinsFrozen = 5;
    string fromAddr    = 6;
    int64  height      = 7;
    string blsPubKeys  = 8;
}
```

### 3 超级节点账户组管理

**账户组管理提供了如下操作**
  - 申请加入超级节点账户组
  - 对申请的账户投票，当前账户组超过2/3账户投票通过或否决
  - 申请退出超级节点账户组
  - 申请在未投票通过前撤销

**说明**
  - 加入账户组的申请者需要预先在paracross合约存一定量的币，币数量不少于账户组申请冻结币数量，申请后即冻结
  - 当前超级账户组成员投票同意或否决新节点的加入
  - 当前超级账户组成员申请退出账户组
  - 申请加入和退出都是针对某个账户提的提案，可以对此提案投票或撤销

#### 3.1 生成 申请加入账户组 的交易（未签名）

**调用接口**
```
rpc CreateTransaction(CreateTxIn) returns (UnsignTx) {}
```
**参数：**
```
message CreateTxIn {
    bytes  execer     = 1;
    string actionName = 2;
    bytes  payload    = 3;
}
message ParaNodeAddrConfig {
    string title       = 1;
    uint32 op          = 2;
    string id          = 3;
    string addr        = 4;
    uint32 value       = 5;
    int64  coinsFrozen = 6;
    string blsPubKey   = 7; //本地址私钥对应的bls聚合签名的公钥
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|execer|bytes|执行器名称, 必须是平行链的执行器, 这里固定为 user.p.para.paracross|
|actionName|string|操作名称, 这里固定为 NodeConfig|
|payload|bytes|types.Encode(&ParaNodeAddrConfig)|
|op|string|配置类型：1：申请加入，2：投票，3：申请退出，4：撤销|
|addrs|string|申请账户，只允许一个|
|coinsFrozen|string|冻结币数量| 

#### 3.2 生成 对申请加入账户组的账户投票 的交易（未签名）

**调用接口**
```
rpc CreateTransaction(CreateTxIn) returns (UnsignTx) {}
```
**参数：**
```
message CreateTxIn {
    bytes  execer     = 1;
    string actionName = 2;
    bytes  payload    = 3;
}
message ParaNodeAddrConfig {
    string title       = 1;
    uint32 op          = 2;
    string id          = 3;
    string addr        = 4;
    uint32 value       = 5;
    int64  coinsFrozen = 6;
    string blsPubKey   = 7; //本地址私钥对应的bls聚合签名的公钥
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|execer|bytes|执行器名称, 必须是平行链的执行器, 这里固定为 user.p.para.paracross|
|actionName|string|操作名称, 这里固定为 |
|payload|bytes|types.Encode(&ParaNodeAddrConfig)|
|op|uint32|配置类型：2：投票|
|id|string|申请的账户的申请id|
|value|uint32|1：yes,2:no| 

#### 3.3 生成 退出账户组 的交易（未签名）

**调用接口**
```
rpc CreateTransaction(CreateTxIn) returns (UnsignTx) {}
```
**参数：**
```
message CreateTxIn {
    bytes  execer     = 1;
    string actionName = 2;
    bytes  payload    = 3;
}
message ParaNodeAddrConfig {
    string title       = 1;
    uint32 op          = 2;
    string id          = 3;
    string addr        = 4;
    uint32 value       = 5;
    int64  coinsFrozen = 6;
    string blsPubKey   = 7; //本地址私钥对应的bls聚合签名的公钥
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|execer|bytes|执行器名称, 必须是平行链的执行器, 这里固定为 user.p.para.paracross|
|actionName|string|操作名称, 这里固定为 |
|payload|bytes|types.Encode(&ParaNodeAddrConfig)|
|op|uint32|配置类型：3：退出账户组|
|addrs|string|申请退出的账户，只允许一个|

#### 3.4 查询 按状态查询账户的申请信息

**调用接口**
```
rpc QueryChain(ChainExecutor) returns (Reply) {}
```
**参数：**
```
message ChainExecutor {
    string driver    = 1;
    string funcName  = 2;
    bytes  stateHash = 3;
    bytes  param     = 4;
    //扩展字段，用于额外的用途
    bytes extra = 5;
}
message ReqParacrossNodeInfo {
    string title  = 1;
    string id     = 2;
    string addr   = 3;
    int32  status = 4;
    string blsPubKey  = 5;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|driver|bytes|执行器名称, 这里固定为 paracross|
|funcName|string|操作名称, 这里固定为 ListNodeStatus|
|stateHash|bytes|所有交易在对应的执行器执行后写入KVDB中重新计算得到的新state的哈希值|
|param|bytes|types.Encode(&ReqParacrossNodeInfo)|
|extra|bytes|扩展字段，用于额外的用途|
|title|string|平行链的title名字| 
|status|int|0：全部，1：申请加入，2：申请退出，3：申请关闭，4：申请撤销|

**返回数据：**
```
message RespParacrossNodeAddrs {
    repeated ParaNodeIdStatus ids = 1;
}

message ParaNodeIdStatus {
    string             id          = 1;
    int32              status      = 2;
    string             title       = 3;
    string             targetAddr  = 4;
    int64              coinsFrozen = 5;
    ParaNodeVoteDetail votes       = 6;
    string             fromAddr    = 7;
    int64              height      = 8;
    string             blsPubKey   = 9;
}
```

#### 3.5 查询 按账户查询账户的申请信息
**调用接口**
```
rpc QueryChain(ChainExecutor) returns (Reply) {}
```
**参数：**
```
message ChainExecutor {
    string driver    = 1;
    string funcName  = 2;
    bytes  stateHash = 3;
    bytes  param     = 4;
    //扩展字段，用于额外的用途
    bytes extra = 5;
}
message ReqParacrossNodeInfo {
    string title  = 1;
    string id     = 2;
    string addr   = 3;
    int32  status = 4;
    string blsPubKey  = 5;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|driver|bytes|执行器名称, 这里固定为 paracross|
|funcName|string|操作名称, 这里固定为 GetNodeAddrInfo|
|stateHash|bytes|所有交易在对应的执行器执行后写入KVDB中重新计算得到的新state的哈希值|
|param|bytes|types.Encode(&ReqParacrossNodeInfo)|
|extra|bytes|扩展字段，用于额外的用途|
|title|string|平行链的title名字| 
|addr|string|申请的账户信息|

**返回数据：**
```
message ParaNodeAddrIdStatus {
    string addr       = 1;
    string proposalId = 2;
    string quitId     = 3;
    int32  status     = 4;
    string title      = 5;
    string blsPubKey  = 6;
}
```
|参数|类型|说明|
|----|----|----|
|status|int32|10：joined， 11： quited|

### 4 共识问题的排查
#### 4.1 是否共识账户组已经配好
```
平行链上查询共识账户组账户，如果返回错误说明没配置好，查询之前的para nodegroup apply和 approve 步骤的交易是否执行成功

./chain33-cli  --rpc_laddr http://ip:8901  --paraName user.p.game.  para nodegroup addrs
{
    "key": "mavl-paracross-nodes-title-user.p.game.",
    "value": "[1JRNjdEqp4LJ5fqycUBm9ayCKSeeskgMKR 1NLHPEcbTWWxxU3dGUZBhayjrCHD3psX7k 1MCftFynyvG2F4ED5mdHYgziDxx6vDrScs 1KSBd17H7ZK8iT37aJztFB22XGwsPTdwE4]"
}
```

#### 4.2 是否平行链钱包解锁状态
```
./bityuan-cli --rpc_laddr http://ip:8901 wallet status
{
    "isWalletLock": false,  ----- 需要是false
    "isAutoMining": true,
    "isHasSeed": true,
    "isTicketLock": true
}

```

#### 4.3 是否当前节点共识账户配置在配置文件
```
[consensus.sub.para]
authAccount="1KSBd17H7ZK8iT37aJztFB22XGwsPTdwE4"  ---不可为空

```


#### 4.4 当前共识高度的查看
**调用接口**
```
rpc QueryChain(ChainExecutor) returns (Reply) {}
```
**参数：**
```
message ChainExecutor {
    string driver    = 1;
    string funcName  = 2;
    bytes  stateHash = 3;
    bytes  param     = 4;
    //扩展字段，用于额外的用途
    bytes extra = 5;
}
message ReqString {
    string data = 1;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|driver|bytes|执行器名称, 这里固定为 paracross|
|funcName|string|操作名称, 这里固定为 GetHeight|
|stateHash|bytes|所有交易在对应的执行器执行后写入KVDB中重新计算得到的新state的哈希值|
|param|bytes|types.Encode(&ReqString)|
|extra|bytes|扩展字段，用于额外的用途|
|data|string|"{user.p.para}."|

**返回数据：**
```
message ParacrossConsensusStatus {
    string title            = 1;
    int64  chainHeight      = 2;
    int64  consensHeight    = 3;
    string consensBlockHash = 4;
}
```

**说明:**
>如果是在主链查询，chainHeight 和consensHeight 都是平行链共识到的高度，如果是在平行链查询，如下说明：

* chainHeight: 当前链的高度
* consensHeight: 当前链共识到的高度

#### 4.5 查看某个高度共识发送情况
>如果共识到某个高度不再增长，可以查看下一个高度超级账户发送共识细节

**调用接口**
```
rpc QueryChain(ChainExecutor) returns (Reply) {}
```
**参数：**
```
message ChainExecutor {
    string driver    = 1;
    string funcName  = 2;
    bytes  stateHash = 3;
    bytes  param     = 4;
    //扩展字段，用于额外的用途
    bytes extra = 5;
}
message ReqParacrossTitleHeight {
    string title  = 1;
    int64  height = 2;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|driver|bytes|执行器名称, 这里固定为 paracross|
|funcName|string|操作名称, 这里固定为 GetTitleHeight|
|stateHash|bytes|所有交易在对应的执行器执行后写入KVDB中重新计算得到的新state的哈希值|
|param|bytes|types.Encode(&ReqParacrossTitleHeight)|
|extra|bytes|扩展字段，用于额外的用途|

**返回数据：**
```
message ParacrossHeightStatusRsp {
    int32    status                            = 1;
    string   title                             = 2;
    int64    height                            = 3;
    int64    mainHeight                        = 4;
    string   mainHash                          = 5;
    repeated string commitAddrs                = 6;
    repeated string commitBlockHash            = 7;
    repeated string commitSupervisionAddrs     = 8;
    repeated string commitSupervisionBlockHash = 9;
}
```

**说明:**
* height: 平行链高度
* mainHeight: 平行链高度对应主链高度
* commitAddrs: 在此高度有哪些超级账户发送了共识
* commitBlockHash: 对应超级账户发送的共识块hash
* 可以看到“1NLHPEcbTWWxxU3dGUZBhayjrCHD3psX7k”　发送的共识hash是“0x77c5b9b657a3438634a91f1a56f7f18f71c3918e52dbfc22477580df25260fb2”　和其他账户发送不同，是导致共识不过的原因

#### 4.6 如果主链是联盟链且Title=local场景
>由于主链是联盟链，所有fork都跟BTY不一致，平行链两个配置项需要相应修改

```
[consensus.sub.para]
mainForkParacrossCommitTx=10
mainLoopCheckCommitTxDoneForkHeight=60
这两个高度和local的主链场景下的fork高度保持一致，如果联盟链Title不是local, 可以 mainForkParacrossCommitTx=1，mainLoopCheckCommitTxDoneForkHeight=1（不能为0，否则代码会解析为最大高度），同时配置文件的startHeight需要大于1. 

```
