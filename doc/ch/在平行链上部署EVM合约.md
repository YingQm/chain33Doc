## 在平行链上部署 EVM 合约
[TOC]

### 1 部署合约
#### 1.1 创建合约交易(未签名) 
**请求报文<!--[dapp/evm/types/EvmContractCreateReq]-->：**
```json
{
    "jsonrpc":"2.0",
    "id": int32,
    "method":"evm.CreateDeployTx",
    "params":[
		{
			"code":"string",
			"abi":"string",
			"fee":100000000,
			"note": "string",
			"alias": "string",
			"parameter": "string",
			"expire":"string",
			"paraName":"string",
			"amount":0
		}
	]
}
```

**参数说明：**

|参数|类型|是否必填|说明|
|----|----|----|----|
|code|string|是|需要部署合约的 bin 内容|
|abi|string|是|部署合约的 abi 内容|
|fee|int64|是|精确的手续费可以通过EstimateGas这个jrpc接口进行估算, 同时该交易费需要满足根据部署交易体积大小计算出来的交易费要求|
|note|string|否|备注|
|alias|string|是|合约别名|
|parameter|string|是|部署合约的参数, 例如 "constructor(zbc, zbc, 3300, '${evm_creatorAddr}')" 原型为 constructor (string memory name_, string memory symbol_,uint256 supply, address owner),这里表示部署一个名称和symbol都为 zbc, 总金额3300*le8, 拥有者为 evm_creatorAddr 的ERC20合约|
|expire|string|是|过期时间可输入如”300s”, ”-1.5h”或者”2h45m”的字符串, 有效时间单位为”ns”, “us” (or “µs”), “ms”, “s”, “m”, “h”|
|paraName|string|是|如果是平行链参数 paraName 的值为 user.p.para. 如果是主链则为空|
|amount|int64|否|-|

**响应报文：**
```json
{
    "id":int32,
    "result":{
        "data":"string"
    },
    "error":null
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|data|string|创建的交易数据|

#### 1.2 签名交易
> 调用 jrpc `Chain33.SignRawTx` 接口签名交易
* 参考 [签名交易接口](https://chain.33.cn/document/93#1.2%20%E4%BA%A4%E6%98%93%E7%AD%BE%E5%90%8D%20SignRawTx) 使用

#### 1.3 发送交易
> 调用 jrpc `Chain33.SendTransaction` 接口发送交易
* 参考 [发送交易接口](https://chain.33.cn/document/93#1.3%20%E5%8F%91%E9%80%81%E4%BA%A4%E6%98%93%20SendTransaction) 使用
* 交易发送后, 生成的交易哈希

#### 1.4 获取合约地址
**请求报文<!--[dapp/evm/types/EvmContractCreateReq]-->：**
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
|txhash|string|是|创建合约的交易哈希, 去掉前面的 0x, `txhash=${txHash:2}`|

**响应报文：**
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

#### 1.5 检查合约地址是否正确
**请求报文<!--[dapp/evm/types/CheckEVMAddrReq]-->：**
```json
{
    "jsonrpc":"2.0",
    "id": int32,
    "method":"Chain33.Query",
    "params":[
		{
			"execer":"evm",
			"funcName":"CheckAddrExists",
			"payload":{
				"addr": "string"
			}
		}
	]
}
```

**参数说明：**

|参数|类型|是否必填|说明|
|----|----|----|----|
|method|string|是|这里固定为 Chain33.Query|
|execer|执行器名称|是|这里固定为evm, 如果是在平行链上则需要加上前缀, 比如 user.p.game.evm|
|funcName|string|是|操作名称, 这里固定为 CheckAddrExists|
|addr|string|是|被查询的合约地址|

**响应报文<!--[dapp/evm/types/CheckEVMAddrResp]-->：**
```json
{
    "id":int32,
    "result": {
		"contract":bool,
		"contractAddr":"string",
		"contractName":"string",
		"aliasName":"string"
	},
    "error":null
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|contract|bool|合约地址是否存在, true 为存在, false 为不存在|
|contractAddr|string|合约地址|
|contractName|string|合约名称|
|aliasName|string|合约别名|


### 2 合约使用
#### 创建调用合约交易 CreateCallTx
**请求报文<!--[dapp/evm/types/EvmContractCallReq]-->：**
```json
{
    "jsonrpc":"2.0",
    "id": int32,
    "method":"evm.CreateCallTx",
    "params":[
		{
			"abi": "string",
			"fee": int64,
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
|parameter|string|是|操作合约的参数, 例如转账交易 "transfer('${evm_transferAddr}', 20)"|
|abi|string|是|部署合约的 abi 内容|
|contractAddr|string|是|合约地址|
|fee|int64|是|精确的手续费可以通过EstimateGas这个jrpc接口进行估算, 同时该交易费需要满足根据部署交易体积大小计算出来的交易费要求, 一般调用交易的交易费直接设置为通过交易体积大小计算出来的交易费即可|
|paraName|string|是|如果是平行链参数 paraName 的值为 user.p.para. 如果是主链则为空|

**响应报文：**
```json
{
    "id":int32,
    "result":{
        "data":"string"
    },
    "error":null
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|data|string|创建的交易数据|

### 3 查询合约信息 GetPackData Query GetUnpackData
#### 3.1 把要查询的信息 pack 一下
**请求报文<!--[dapp/evm/types/EvmGetPackDataReq]-->：**
```json
{
    "jsonrpc":"2.0",
    "id": int32,
    "method":"Chain33.Query",
    "params":[
		{
			"execer":"evm",
			"funcName":"GetPackData",
			"payload":{
				"abi":"string",
				"parameter":"string"
			}
		}
	]
}
```

**参数说明：**

|参数|类型|是否必填|说明|
|----|----|----|----|
|method|string|是|这里固定为 Chain33.Query|
|execer|执行器名称|是|这里固定为evm, 如果是在平行链上则需要加上前缀, 比如 user.p.game.evm|
|funcName|string|是|操作名称, 这里固定为 GetPackData|
|abi|string|是|合约abi|
|parameter|string|是|查询的参数信息|

**响应报文<!--[dapp/evm/types/EvmGetPackDataRespose]-->：**
```json
{
    "id":int32,
    "result": {
		"packData":"string"
	},
    "error":null
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|packData|string|需要查询的信息 pack 后的数据|

#### 3.2 查询 pack 后的数据
**请求报文<!--[dapp/evm/types/EvmQueryReq]-->：**
```json
{
    "jsonrpc":"2.0",
    "id": int32,
    "method":"Chain33.Query",
    "params":[
		{
			"execer":"evm",
			"funcName":"Query",
			"payload":{
				"address":"string",
				"input":"string",
				"caller":"string"
			}
		}
	]
}
```

**参数说明：**

|参数|类型|是否必填|说明|
|----|----|----|----|
|method|string|是|这里固定为 Chain33.Query|
|execer|执行器名称|是|这里固定为evm, 如果是在平行链上则需要加上前缀, 比如 user.p.game.evm|
|funcName|string|是|操作名称, 这里固定为 Query|
|address|string|是|合约地址|
|input|string|是|需要查询的信息 pack 后的数据|
|caller|string|是|合约部署者地址|

**响应报文<!--[dapp/evm/types/EvmQueryResp]-->：**
```json
{
    "id":int32,
    "result": {
		"address":"string",
		"input":"string",
		"caller":"string",
		"rawData":"string",
		"jsonData":"string",
	},
    "error":null
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

#### 3.3 把查询到的结果 unpack
**请求报文<!--[dapp/evm/types/EvmGetUnpackDataReq]-->：**
```json
{
    "jsonrpc":"2.0",
    "id": int32,
    "method":"Chain33.Query",
    "params":[
		{
			"execer":"evm",
			"funcName":"GetUnpackData",
			"payload":{
				"abi":"string",
				"parameter":"string",
				"data":"string"
			}
		}
	]
}
```

**参数说明：**

|参数|类型|是否必填|说明|
|----|----|----|----|
|method|string|是|这里固定为 Chain33.Query|
|execer|执行器名称|是|这里固定为evm, 如果是在平行链上则需要加上前缀, 比如 user.p.game.evm|
|funcName|string|是|操作名称, 这里固定为 GetUnpackData|
|abi|string|是|合约abi|
|methodName|string|是|方法名称|
|data|string|是|需要 Unpack 的数据|

**响应报文<!--[dapp/evm/types/EvmGetUnpackDataRespose]-->：**
```json
{
    "id":int32,
    "result": {
		"unpackData":"[]string"
	},
    "error":null
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|unpackData|[]string|Unpack 的数据|
