## 钱包找回合约
[TOC]

### 1 生成交易(未签名) 备份主地址 Backup
**调用接口**
```
rpc Backup(BackupRetrieve) returns (UnsignTx) {}
```
**参数：**
```
message BackupRetrieve {
    string backupAddress  = 1;
    string defaultAddress = 2;
    int64  delayPeriod    = 3;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|backupAddress|string|备份地址|
|defaultAddress|string|主账户地址|
|delayPeriod|int64|生效延时时间|

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

### 2 备份地址准备 Prepare
**调用接口**
```
rpc Prepare(PrepareRetrieve) returns (UnsignTx) {}
```
**参数：**
```
message PrepareRetrieve {
    string backupAddress  = 1;
    string defaultAddress = 2;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|backupAddress|string|备份地址|
|defaultAddress|string|主账户地址|

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

### 3 备份地址生效 CreateRawRetrievePerformTx
**调用接口**
```
rpc Perform(PerformRetrieve) returns (UnsignTx) {}
```
**参数：**
```
message PerformRetrieve {
    string   backupAddress      = 1;
    string   defaultAddress     = 2;
    repeated AssetSymbol assets = 3;
}

message AssetSymbol {
    string exec   = 1;
    string symbol = 2;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|backupAddress|string|备份地址|
|defaultAddress|string|主账户地址|
|assets|[]AssetSymbol|资产名称列表|

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

### 4 取消备份(已准备还未生效) CreateRawRetrieveCancelTx
**调用接口**
```
rpc Cancel(CancelRetrieve) returns (UnsignTx) {}
```
**参数：**
```
message CancelRetrieve {
    string backupAddress  = 1;
    string defaultAddress = 2;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|backupAddress|string|备份地址|
|defaultAddress|string|主账户地址|

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
