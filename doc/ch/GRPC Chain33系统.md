## Chain33系统接口
[TOC]

### 1 获取远程节点列表 GetPeerInfo
**调用接口**
```
rpc GetPeerInfo(P2PGetPeerReq) returns (PeerList) {}
```
**参数：**
```
message P2PGetPeerReq {
    string p2pType = 1;
}
```

**参数说明：**

|参数|类型|是否必填|说明|
|----|----|----|----|

**返回数据：**
```
message PeerList {
    repeated Peer peers = 1;
}

message Peer {
    string addr        = 1;
    int32  port        = 2;
    string name        = 3;
    bool   self        = 4;
    int32  mempoolSize = 5;
    Header header      = 6;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|peers|array|当前节点连接的所有节点信息|
|addr|string|节点外网IP|
|port|int32|节点P2P端口，有可能经过端口映射|
|name|string|节点名称|
|mempoolSize|int32|节点中内存池缓存的交易条数|
|self|bool|是否为当前节点（执行查询命令的节点）|
|header|-|节点最新区块头信息|

### 2 查询节点状态 GetNetInfo
**调用接口**
```
rpc NetInfo(P2PGetNetInfoReq) returns (NodeNetInfo) {}
```
**参数：**
```
message P2PGetNetInfoReq {
    string p2pType = 1;
}
```

**参数说明：**

|参数|类型|是否必填|说明|
|----|----|----|----|

**返回数据：**
```
message NodeNetInfo {
    string externaladdr = 1;
    string localaddr    = 2;
    bool   service      = 3;
    int32  outbounds    = 4;
    int32  inbounds     = 5;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|externaladdr|string|表示自身的外网地址信息|
|localaddr|string|表示节点监听的本地地址信息，例如：192.168.1.108:13802|
|service|bool|为true 时，表示别的节点可以连接到自己,false 表示自身节点对其它节点不可见，别的节点无法连接到自己|
|outbounds|int32|扇出数，表示对外连接的节点个数|
|inbounds|int32|扇入数，表示有多少外部节点连接本节点|

### 3 查询时间状态 GetTimeStatus
程序员小哥哥正在努力研发中...
<div style='display: none'>

**调用接口**
```

```
**参数：**
```

```
```json
{
    "jsonrpc":"2.0",
    "id":int32,
    "method":"Chain33.GetTimeStatus",
    "params":[]
}
```
**参数说明：**

|参数|类型|是否必填|说明|
|----|----|----|----|

**返回数据：**
```

```
```json
{
    "ntpTime":"string",
    "localTime":"string",
    "diff":int64
}
```
**参数说明：**

|参数|类型|说明|
|----|----|----|
|ntpTime|string|网络标准时间|
|localTime|string|节点本地时间|
|diff|int64|本地事件和标准时间差，单位：秒，如本地时间较快则为整数，否则为负数|
</div>

### 4 查询同步状态 IsSync
**调用接口**
```
rpc IsSync(ReqNil) returns (Reply) {}
```
**参数：**
nil

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
|isOk|bool|为true时表示同步成功|

### 5 获取主代币信息 GetCoinSymbol
程序员小哥哥正在努力研发中...
<div style='display: none'>

**调用接口**
```

```
**参数：**
```

```
```json
{
    "jsonrpc":"2.0",
    "id":int32,
    "method":"Chain33.GetCoinSymbol",
    "params":[]
}
```
**参数说明：**

|参数|类型|是否必填|说明|
|----|----|----|----|

**返回数据：**
```

```
```json
{
   "id" : int32,
   "error" : string,
   "result" : {
      "data" : string
   }
}
```
**参数说明：**

|参数|类型|说明|
|----|----|----|
|data|string|当前节点的主代币信息, 如 bty|
</div>

### 6 获取系统支持签名类型 GetCryptoList
程序员小哥哥正在努力研发中...
<div style='display: none'>

**调用接口**
```

```
**参数：**
```

```
```json
{
    "jsonrpc":"2.0",
    "id":int32,
    "method":"Chain33.GetCryptoList",
    "params":[]
}
```
**参数说明：**

|参数|类型|是否必填|说明|
|----|----|----|----|

**返回数据：**
```

```
```json
{
   "id" : int32,
   "error" : string,
   "result" : {
      "cryptos" : [{"name":"secp256k1", "typeID":1}]
   }
}
```
**参数说明：**

|参数|类型|说明|
|----|----|----|
|cryptos|数组|签名类型数组|
|name|string|签名类型名称|
|typeID|int32|签名类型ID|
</div>
