## 挖矿接口
代码位置: `github.com/33cn/plugin/plugin/dapp/ticket/proto`

[TOC]
### 1 绑定挖矿地址 CreateBindMiner
**调用接口**
```
rpc CreateBindMiner(ReqBindMiner) returns (ReplyBindMiner) {}
```
**参数：**
```
message ReqBindMiner {
    string bindAddr     = 1;
    string originAddr   = 2;
    int64  amount       = 3;
    bool   checkBalance = 4;
}
```

**参数说明：**

|参数|类型|是否必填|说明|
|----|----|----|----|
|bindAddr|string|是|挖矿绑定地址|
|originAddr|string|是|原始地址|
|amount|int64|是|用于购买ticket的bty数量|
|checkBalance|bool|是|是否进行额度检查|

**返回数据：**
```
message ReplyBindMiner {
    string txHex = 1;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|txhex|string|交易十六进制字符串|

### 2 设置自动挖矿 SetAutoMining
**调用接口**
```
rpc SetAutoMining(MinerFlag) returns (Reply) {}
```
**参数：**
```
message MinerFlag {
    int32 flag    = 1;
    int64 reserve = 2;
}
```

**参数说明：**

|参数|类型|是否必填|说明|
|----|----|----|----|
|flag|int32|是|标识符，1 为开启自动挖矿，0 为关闭自动挖矿。|
|reserve|int64|否|保留字段|

**返回数据：**
```
message Reply {
    bool  isOk = 1;
    bytes msg  = 2;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|isok|bool|在成功时，返回 true；失败时，返回 false。|
|msg|bytes|在成功时，为空；失败时，返回错误信息。|

### 3 获取Ticket的数量 GetTicketCount
**调用接口**
```
rpc GetTicketCount(types.ReqNil) returns (Int64) {}
```
**参数：**
nil

**返回数据：**
```
Int64
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|result|int64|返回ticket的数量|

### 4 构造买票交易 ticket open
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

message TicketOpen {
    string minerAddress      = 1;
    int32 count              = 2;
    string returnAddress     = 3;
    int64 randSeed           = 4;
    repeated bytes pubHashes = 5;
}
```

**参数说明：**

|参数|类型|是否必填|说明|
|----|----|----|----|
|execer|bytes|是|ticket|
|actionName|string|是|Topen|
|payload|bytes|是|TicketOpen结构, Topen需要的参数|
|payload.minerAddress|string|是|用户挖矿的ticket 地址|
|payload.returnAddress|string|是| 收益地址/币实际存储的地址，(非委托挖矿时，和挖矿地址一致) |
|payload.count|int32|是|购买ticket的数目|
|payload.randSeed|int64|否|随机数种子|
|payload.pubHashes|[]bytes|是| 数组长度为count, 每个pubHash 用随机的源字符串通过SHA256算法生成。 挖矿时需要公布生成pubHash的源字符串，源字符串用于生成链上随机数 |

> 注意： 实现需要保留生成的pubHash的源字符串， 一般将这个功能集成到钱包， 由钱包来管理的随机字符串

**返回数据：**
```
message UnsignTx {
    bytes data = 1;
}
```
**参数说明：**

|参数|类型|说明|
|----|----|----|
|data|bytes|待签名数据|