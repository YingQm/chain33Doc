## 事件接口
[TOC]
### 1 生成发布事件的交易（未签名） CreateTransaction
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

message EventPublish {
    string type         = 2; //游戏类别
    string subType      = 3; //游戏子类别
    int64  time         = 4; //结果公布参考时间
    string content      = 5; //事件内容
    string introduction = 6; //事件描述
}
```

**参数说明：**

Chain33.CreateTransaction结构按通用要求填写：
execer,执行器名称，这里固定为oralce
actionName,操作名称，这里固定为EventPublish
payload携带的内容格式如下：

|参数|类型|说明|
|----|----|----|
|type|string|事件类型|
|subType|string|事件子类型|
|time|int64|事件结果预计公布时间，UTC时间|
|content|string|事件内容，例如可以用json格式表示|
|introduction|string|事件介绍|

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

### 2 生成取消发布事件的交易（未签名） EventAbort
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

message EventAbort {
    string eventID = 2; //发布事件的ID
}

```

**参数说明**

Chain33.CreateTransaction结构按通用要求填写：
execer,执行器名称，这里固定为oralce
actionName,操作名称，这里固定为EventAbort
payload携带的内容格式如下：

|参数|类型|说明|
|----|----|----|
|eventID|string|发布事件的事件ID|

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

### 3 生成预发布事件结果交易（未签名） ResultPrePublish

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

message ResultPrePublish {
    string eventID = 2; //发布事件的ID
    string source  = 3; //数据来源
    string result  = 4; //发布数据
}
```

**参数说明**

Chain33.CreateTransaction结构按通用要求填写：
execer,执行器名称，这里固定为oralce
actionName,操作名称，这里固定为ResultPrePublish
payload携带的内容格式如下：

|参数|类型|说明|
|----|----|----|
|eventID|string|发布事件的事件ID|
|source|string|发布结果的源，比如XX体育|
|result|string|发布的事件结果，比如比赛比分|

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


**参数说明**

|参数|类型|说明|
|----|----|----|
|result|string|交易十六进制编码后的字符串|

### 4 生成取消预发布结果的交易（未签名） ResultAbort

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

message ResultAbort {
    string eventID = 2; //发布事件的ID
}
```

**参数说明**

Chain33.CreateTransaction结构按通用要求填写：
execer,执行器名称，这里固定为oralce
actionName,操作名称，这里固定为ResultAbort
payload携带的内容格式如下：

|参数|类型|说明|
|----|----|----|
|eventID|string|发布事件的事件ID|

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

### 5 生成正式发布事件结果交易（未签名） ResultPublish

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

message ResultPublish {
    string eventID = 2; //发布事件的ID
    string source  = 3; //数据来源
    string result  = 4; //发布数据
}
```

**参数说明**

Chain33.CreateTransaction结构按通用要求填写：
execer,执行器名称，这里固定为oralce
actionName,操作名称，这里固定为ResultPublish
payload携带的内容格式如下：

|参数|类型|说明|
|----|----|----|
|eventID|string|发布事件的事件ID|
|source|string|发布结果的源，比如XX体育|
|result|string|发布的事件结果，比如比赛比分|

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
