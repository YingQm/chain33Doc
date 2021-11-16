## 平行链共识节点挖矿奖励规则
[TOC]
>平行链共识节点是参与平行链共识安全的节点，发送共识交易，同时享受平行链挖矿奖励

### 1 平行链共识节点挖矿奖励规则
[平行链共识节点挖矿奖励规则](https://chain.33.cn/document/291#1%20%E5%85%B1%E8%AF%86%E8%8A%82%E7%82%B9%E8%B5%84%E6%A0%BC)

### 2 绑定挖矿命令
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

message ParaBindMinerCmd{
    int32  bindAction   = 1;  // 1: bind, 2:unbind
    int64  bindCoins    = 2;  // bind coins count
    string targetNode   = 3;  // super node addr
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|method|string|Chain33.CreateTransaction|
|execer|string|必须是平行链的执行器user.p.para.paracross,title:user.p.para.按需调整|
|actionName|string|ParaBindMiner|
|bindAction|string|绑定:1，解绑定:2|
|bindCoins|int|绑定挖矿冻结币的份额，需冻结平行链原生代币，解绑定不需要此配置|
|targetNode|string|绑定目标共识节点，需要是共识账户组的成员|

**返回数据：**
```
message UnsignTx {
    bytes data = 1;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|data|bytes|交易十六进制编码后的数据|

### 3 挖矿奖励的转出
[挖矿奖励的转出](https://chain.33.cn/document/291#6%20%E6%8C%96%E7%9F%BF%E5%A5%96%E5%8A%B1%E7%9A%84%E8%BD%AC%E5%87%BA)
