## EVM 接口
EVM的接口主要是用来完成创建交易（包括部署合约交易和调用合约交易），估算调用交易需要支付的gas（gas会在执行时，通过支付交易费1:1进行兑换；以及相关查询。

[TOC]

### 1 估算部署交易或者调用交易需要的gas
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
    bytes  extra     = 5;
}

message EstimateEVMGasReq {
    string tx     = 1;
    string from   = 2;
}
```

**参数说明：**

|参数|类型|是否必填|说明|
|----|----|----|----|
|driver|bytes|是|执行器名称, 这里固定为 evm，如果是在平行链上则需要加上前缀，比如user.p.game.evm|
|funcName|string|是|操作名称, 这里固定为 EstimateGas|
|stateHash|bytes|否|所有交易在对应的执行器执行后写入KVDB中重新计算得到的新state的哈希值|
|param|bytes|是|types.Encode(&EstimateEVMGasReq)|
|extra|bytes|否|扩展字段，用于额外的用途|
|tx|string|是|部署合约交易或者调用合约交易的序列化后的字符串|
|from|string|是|合约交易调用者地址|

**返回数据：**
```
message EstimateEVMGasResp {
    uint64 gas = 1;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|gas|uint64|估算需要的gas数值|

### 2 创建部署合约交易 CreateDeployTx
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
    "id": int32,
    "method":"evm.CreateDeployTx",
    "params":[
		{
			"code":"string",
			"abi":"string",
			"fee":int64,
			"note": "string",
			"alias": "string",
			"parameter": "string",
			"expire":"string",
			"paraName":"string",
			"amount":int64
		}
	]
}
```

**参数说明：**

|参数|类型|是否必填|说明|
|----|----|----|----|
|parameter|string|是|部署合约的参数 "constructor(zbc, zbc, 3300, '${evm_creatorAddr}')" 原型为 constructor (string memory name_, string memory symbol_,uint256 supply, address owner),这里表示部署一个名称和symbol都为 zbc，总金额3300*le8，拥有者为 evm_creatorAddr 的ERC20合约|
|abi|string|是|部署合约的 abi 内容|
|code|string|是|需要部署合约的 bin 内容|
|fee|int64|是|精确的手续费可以通过EstimateGas这个jrpc接口进行估算，同时该交易费需要满足根据部署交易体积大小计算出来的交易费要求
|paraName|string|是|如果是平行链参数 paraName 的值为 user.p.para. 如果是主链则为空|
|alias|string|是|合约别名|

**返回数据：**
```

```
```json
{
    "id":int32,
    "result":{
        "data":"string",
    },
    "error":null
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|data|string|创建的交易数据|
</div>

### 3 创建调用合约交易 CreateCallTx
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
    "id": int32,
    "method":"evm.CreateCallTx",
    "params":[
		{
			"abi":"string",
			"fee":int64,
			"note": "string",
			"parameter": "string",
			"expire":"string",
			"paraName":"string",
			"contractAddr":"string",
			"amount":int64
		}
	]
}
```

**参数说明：**

|参数|类型|是否必填|说明|
|----|----|----|----|
|parameter|string|是|操作合约的参数，例如转账交易 "transfer('${evm_transferAddr}', 20)"|
|abi|string|是|部署合约的 abi 内容|
|contractAddr|string|是|合约地址|
|fee|int64|是|精确的手续费可以通过EstimateGas这个jrpc接口进行估算，同时该交易费需要满足根据部署交易体积大小计算出来的交易费要求，一般调用交易的交易费直接设置为通过交易体积大小计算出来的交易费即可|
|paraName|string|是|如果是平行链参数 paraName 的值为 user.p.para. 如果是主链则为空|

**返回数据：**
```

```
```json
{
    "id":int32,
    "result":{
        "data":"string",
    },
    "error":null
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|data|string|创建的交易数据|
</div>

### 4 获取合约地址 CalcNewContractAddr
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
    "id": int32,
    "method":"evm.CalcNewContractAddr",
    "params":[
		{
			"caller":"string",
			"txhash":"string"
		}
	]
}
```

**参数说明：**

|参数|类型|是否必填|说明|
|----|----|----|----|
|caller|string|是|部署合约的地址|
|txhash|string|是|创建合约的交易哈希，去掉前面的 0x|

**返回数据：**
```

```
```json
{
    "id":int32,
    "result":"string",
    "error":null
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|result|string|合约地址|
</div>

### 5 查询合约地址是否存在 CheckAddrExists
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
    bytes  extra     = 5;
}

message CheckEVMAddrReq {
    string addr = 1;
}
```

**参数说明：**

|参数|类型|是否必填|说明|
|----|----|----|----|
|driver|bytes|是|执行器名称, 这里固定为 evm，如果是在平行链上则需要加上前缀，比如user.p.game.evm|
|funcName|string|是|操作名称, 这里固定为 CheckAddrExists|
|stateHash|bytes|否|所有交易在对应的执行器执行后写入KVDB中重新计算得到的新state的哈希值|
|param|bytes|是|types.Encode(&CheckEVMAddrReq)|
|extra|bytes|否|扩展字段，用于额外的用途|
|addr|string|是|被查询的合约地址|

**返回数据：**
```
message CheckEVMAddrResp {
    bool   contract     = 1;
    string contractAddr = 2;
    string contractName = 3;
    string aliasName    = 4;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|contract|bool|合约地址是否存在, 1 为存在, 0 为不存在|
|contractAddr|string|合约地址|
|contractName|string|合约名称|
|aliasName|string|合约别名|

### 6 查询合约信息 GetPackData Query GetUnpackData
#### 6.1 GetPackData
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
    bytes  extra     = 5;
}

message EvmGetPackDataReq {
    string abi          = 1;
    string parameter    = 2;
}
```

**参数说明：**

|参数|类型|是否必填|说明|
|----|----|----|----|
|driver|bytes|是|执行器名称, 这里固定为 evm，如果是在平行链上则需要加上前缀，比如user.p.game.evm|
|funcName|string|是|操作名称, 这里固定为 GetPackData|
|stateHash|bytes|否|所有交易在对应的执行器执行后写入KVDB中重新计算得到的新state的哈希值|
|param|bytes|是|types.Encode(&EvmGetPackDataReq)|
|extra|bytes|否|扩展字段，用于额外的用途|
|abi|string|是|合约abi|
|parameter|string|是|查询的参数信息|

**返回数据：**
```
message EvmGetPackDataRespose {
    string packData     = 1;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|packData|string|需要查询的信息 pack 后的数据|

#### 6.2 Query
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
    bytes  extra     = 5;
}

message EvmQueryReq {
    string address = 1;
    string input   = 2;
    string caller  = 3;
}
```

**参数说明：**

|参数|类型|是否必填|说明|
|----|----|----|----|
|driver|bytes|是|执行器名称, 这里固定为 evm，如果是在平行链上则需要加上前缀，比如user.p.game.evm|
|funcName|string|是|操作名称, 这里固定为 Query|
|stateHash|bytes|否|所有交易在对应的执行器执行后写入KVDB中重新计算得到的新state的哈希值|
|param|bytes|是|types.Encode(&EvmQueryReq)|
|extra|bytes|否|扩展字段，用于额外的用途|
|address|string|是|合约地址|
|input|string|是|需要查询的信息 pack 后的数据|
|caller|string|是|合约部署者地址|

**返回数据：**
```
message EvmQueryResp {
    string address  = 1;
    string input    = 2;
    string caller   = 3;
    string rawData  = 4;
    string jsonData = 5;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|address|string|合约地址|
|input|string|需要查询的信息 pack 后的数据|
|caller|string|合约部署者地址|
|rawData|string|查询到的结果|
|jsonData|string|json数据|

#### 6.3 GetUnpackData
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
    bytes  extra     = 5;
}

message EvmGetUnpackDataReq {
    string abi          = 1;
    string parameter    = 2;
    string data         = 3;
}
```

**参数说明：**

|参数|类型|是否必填|说明|
|----|----|----|----|
|driver|bytes|是|执行器名称, 这里固定为 evm，如果是在平行链上则需要加上前缀，比如user.p.game.evm|
|funcName|string|是|操作名称, 这里固定为 GetUnpackData|
|stateHash|bytes|否|所有交易在对应的执行器执行后写入KVDB中重新计算得到的新state的哈希值|
|param|bytes|是|types.Encode(&EvmGetUnpackDataReq)|
|extra|bytes|否|扩展字段，用于额外的用途|
|abi|string|是|合约abi|
|methodName|string|是|方法名称|
|data|string|是|需要 Unpack 的数据|

**返回数据：**
```
message EvmGetUnpackDataRespose {
    repeated string unpackData     = 1;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|unpackData|[]string|Unpack 的数据|