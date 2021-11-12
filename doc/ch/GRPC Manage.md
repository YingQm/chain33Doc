## Manage
[TOC]

manage 管理执行器，主要功能是动态地给其他执行器配置和调整参数值。如给token执行器增加黑名单，给game执行器设置最大的赌资等等。
所有修改都是通过指定的manager账户地址，发送交易去修改参数值。这样做可以避免系统因为修改参数值而导致硬分叉。

### 添加/删除一个token-finisher CreateTransaction
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

message ModifyConfig {
    string key   = 1;
    string value = 2;
    string op    = 3;
    string addr  = 4;
}
```

**参数说明：**

Chain33.CreateTransaction结构按通用要求填写：
execer,执行器名称，这里固定为manage
actionName,操作名称，这里固定为Modify
payload携带的内容格式如下：

|参数|类型|说明|
|----|----|----|
|key|string|目前支持token-finisher，token-blacklist|
|value|string|对应地址，如: 1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs|
|op|string|操作方法，add 添加，delete 删除|
|addr|string|可为空|

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
