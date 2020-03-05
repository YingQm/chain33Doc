## 1 EVM 接口
[TOC]

### 1.1 创建EVM合约交易 CreateTransaction CreateCall
> 这里创建的是原始交易，除此之外，还需要进行交易的签名以及发送操作，具体可以参考[这里](93)

**请求报文<!--[dapp/evm/types/CreateCallTx]-->：**
```json
{
    "jsonrpc":"2.0",
    "id":int32,
    "method":"Chain33.CreateTransaction",
    "params":[
        {
            "execer":"string",
            "actionName":"string",
            "payload":{
                "isCreate":bool,
                "name": "string",
                "code": "string",
                "abi": "string",
                "alias": "string",
                "note": "string",
                "amount": uint64,
                "fee": int64,
                "gasLimit": uint64,
                "gasPrice": uint32
            }
        ]
	}
}
```

**参数说明：**

Chain33.CreateTransaction结构按通用要求填写：
execer,执行器名称，这里固定为evm，如果是在平行链上则需要加上前缀，比如user.p.game.evm
actionName,操作名称，这里固定为CreateCall
payload携带的内容格式如下：

|参数|类型|是否必填|说明|
|----|----|----|----|----|
|isCreate|bool|是|是否为创建合约动作，创建合约为true，调用合约为false|
|name|string|否|调用的合约名称，当isCreate为false时有效且必填|
|code|string|否|需要部署或者调用合约合约代码|
|abi|string|否|需要部署或调用的合约ABI代码|
|alias|string|否|部署新合约时的合约别名，方便识别不同合约|
|note|string|否|本次交易的备注信息|
|amount|uint64|否|合约调用时，如果需要传递金额，通过这个参数|
|fee|int64|否|本次交易你的手续费，需要大约合约消耗的gas值*gasPrice|
|gasPrice|uint32|否|单位gas定价，默认为1|
|gasLimit|uint64|否|本次交易允许消耗的最大gas量，默认值和fee相等|

> 注意：在部署合约是，code必填，abi可选； 在调用合约时，code和abi两者选一；


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
|result|string|交易内容十六进制字符串|

**示例：**
Request1 部署合约交易:
```json
{
    "jsonrpc":"2.0",
    "id": 2,
    "method":"Chain33.CreateTransaction",
    "params":[
        {
            "execer":"evm",
            "actionName":"CreateCall",
            "payload":{
                "isCreate":true,
                "code": "608060405234801561001057600080fd5b506298967f60008190555060df806100296000396000f3006080604052600436106049576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff16806360fe47b114604e5780636d4ce63c146078575b600080fd5b348015605957600080fd5b5060766004803603810190808035906020019092919050505060a0565b005b348015608357600080fd5b50608a60aa565b6040518082815260200191505060405180910390f35b8060008190555050565b600080549050905600a165627a7a72305820bdc06397a67a222e127b061778ed83240dcf42ad5f554ea1c0ee97305dcf71f30029",
                "abi":"[{\"constant\":false,\"inputs\":[{\"name\":\"x\",\"type\":\"uint256\"}],\"name\":\"set\",\"outputs\":[],\"payable\":false,\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"constant\":true,\"inputs\":[],\"name\":\"get\",\"outputs\":[{\"name\":\"\",\"type\":\"uint256\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"payable\":false,\"stateMutability\":\"nonpayable\",\"type\":\"constructor\"}]"
            }
        }
    ]
}
```

Request2 调用合约交易(abi):
```json
{
    "jsonrpc":"2.0",
    "id": 2,
    "method":"Chain33.CreateTransaction",
    "params":[
        {
            "execer":"evm",
            "actionName":"CreateCall",
            "payload":{
                "isCreate":false,
                "name": "user.evm.0x49e5da1fe3952c638b02c5a3093a445192d2074dc78ad31834410c0770e9599d"
                "abi": "get()"
            }
        }
    ]
}
```

### 1.2 估算合约调用Gas消耗 EstimateGas
> 本操作仅模拟执行，估算大致需要消耗的gas，并不会真正执行代码；

**请求报文<!--[dapp/evm/types/EstimateEVMGasReq]-->：**
```json
{
    "jsonrpc":"2.0",
    "id": int32,
    "method":"Chain33.Query",
    "params":[
		{
			"execer":"string",
			"funcName":"string",
			"payload":{
				"to": "string",
				"code": "string",
				"abi": "string",
				"caller": "string",
				"amount": "string"
			}
		}
	]
}
```

**参数说明：**

Chain33.Query结构按通用要求填写：
execer,执行器名称，这里固定为evm，如果是在平行链上则需要加上前缀，比如user.p.game.evm
funcName,操作名称，这里固定为EstimateGas
payload携带的内容格式如下：

|参数|类型|是否必填|说明|
|----|----|----|----|----|
|to|string|否|目标地址，如果为创建合约，这里留空，如果为调用合约这里填写合约地址|
|code|[]byte|否|需要部署或调用的合约代码，如果是部署合约，本字段必填|
|abi|string|否|需要部署或调用的合约ABI代码|
|caller|string|否|本次调用的发起者，如果不填写则认为EVM合约自身发起的调用|
|amount|uint64|否|合约调用时，如果需要传递金额，通过这个参数|


**响应报文：**
```json
{
    "id":int32,
    "result":{
        "gas":uint64
    },
    "error":null
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|gas|uint64|本次交易需要消耗的gas值|

### 1.3 查询EVM合约地址 CheckAddrExists
> EVM合约有两个标识，一个是合约地址，一个是合约名称，两者为一对一的唯一对应关系，因为系统设计原因，在设计到转账操作时必需使用合约名称进行操作，所以本接口提供了两者的互查能力；

**请求报文<!--[dapp/evm/types/CheckEVMAddrReq]-->：**
```json
{
    "jsonrpc":"2.0",
    "id": int32,
    "method":"Chain33.Query",
    "params":[
		{
			"execer":"string",
			"funcName":"string",
			"payload":{
				"addr": "string"
			}
		}
	]
}
```

**参数说明：**

Chain33.Query结构按通用要求填写：
execer,执行器名称，这里固定为evm，如果是在平行链上则需要加上前缀，比如user.p.game.evm
funcName,操作名称，这里固定为CheckAddrExists
payload携带的内容格式如下：

|参数|类型|是否必填|说明|
|----|----|----|----|----|
|addr|string|是|合约地址或合约名称，填写任何一个，则返回另外一个|

**响应报文：**
```json
{
    "id":int32,
    "result":{
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
|contract|bool|本地址下是否存在EVM合约|
|contractAddr|string|本合约地址|
|contractName|string|本合约名称|
|aliasName|string|本合约别名|

**示例：**
Request:
```json
{
    "jsonrpc":"2.0",
    "id": 2,
    "method":"Chain33.Query",
    "params":[
	{
			"execer":"evm",
			"funcName":"CheckAddrExists",
			"payload":{
				"addr": "1LuigHsSy55KEsZgBMJtYfo3wrhz7YbbDD"
			}
		}
	]
}
```

Response:
```json
{
    "id": 2,
    "result":{
        "contract": true,
        "contractAddr": "1LuigHsSy55KEsZgBMJtYfo3wrhz7YbbDD",
        "contractName": "user.evm.0x49e5da1fe3952c638b02c5a3093a445192d2074dc78ad31834410c0770e9599d",
        "aliasName": ""
    },
    "error": null
}
```

### 1.4 查询合约ABI QueryABI
> 如果EVM合约在部署的时候绑定了ABI，则可以通过本接口获取到绑定的ABI信息；

**请求报文<!--[dapp/evm/types/EvmQueryAbiReq]-->：**
```json
{
    "jsonrpc":"2.0",
    "id": int32,
    "method":"Chain33.Query",
    "params":[
		{
			"execer":"string",
			"funcName":"string",
			"payload":{
				"address": "string"
			}
		}
	]
}
```

**参数说明：**
Chain33.Query结构按通用要求填写：
execer,执行器名称，这里固定为evm，如果是在平行链上则需要加上前缀，比如user.p.game.evm
funcName,操作名称，这里固定为 QueryABI
payload携带的内容格式如下：

|参数|类型|是否必填|说明|
|----|----|----|----|----|
|address|string|是|EVM合约地址|

**响应报文：**
```json
{
    "id":int32,
    "result":{
        "address":"string",
        "abi":"string"
    },
    "error":null
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|address|string|本合约地址|
|abi|string|本合约绑定的ABI|

### 1.5 EVM合约只读调用（通过ABI） Query
> EVM合约在部署时，如果绑定了ABI信息，则通过调用的方法即可判断出是否为只读调用；这种调用可以直接通过查询数据库的方式返回，不需要通过交易的方式，不收取手续费；

**请求报文<!--[dapp/evm/types/EvmQueryReq]-->：**
```json
{
    "jsonrpc":"2.0",
    "id": int32,
    "method":"Chain33.Query",
    "params":[
		{
			"execer":"string",
			"funcName":"string",
			"payload":{
				"address": "string",
				"input": "string",
				"caller": "string"
			}
		}
	]
}
```

**参数说明：**
Chain33.Query结构按通用要求填写：
execer,执行器名称，这里固定为evm，如果是在平行链上则需要加上前缀，比如user.p.game.evm
funcName,操作名称，这里固定为 Query
payload携带的内容格式如下：

|参数|类型|是否必填|说明|
|----|----|----|----|----|
|address|string|是|合约地址|
|input|string|是|abi方法及参数|
|caller|string|否|本次调用的发起者，如果不填写则认为EVM合约自身发起的调用|

**响应报文：**
```json
{
    "id":int32,
    "result":{
        "address":"string",
        "input":"string",
        "caller":"string",
        "rawData":"string",
        "jsonData":"string"
    },
    "error":null
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|address|string|合约地址|
|input|string|调用输入|
|caller|string|调用方|
|rawData|string|调用返回的原始数据|
|jsonData|string|调用返回数据json格式化|

**示例：**
Request:
```json
{
    "jsonrpc":"2.0",
    "id": 2,
    "method":"Chain33.Query",
    "params":[
		{
			"execer":"evm",
			"funcName":"Query",
			"payload":{
				"address":"1LuigHsSy55KEsZgBMJtYfo3wrhz7YbbDD",
				"input":"get()",
				"caller":"1Kkq2neiAWSGkk3djkJ9SPoG2tdGzfwDpa"
			}
		}
	]
}
```

Response:
```json
{
    "id": 2,
    "result":{
        "address": "1LuigHsSy55KEsZgBMJtYfo3wrhz7YbbDD",
        "input": "get()",
        "caller": "1Kkq2neiAWSGkk3djkJ9SPoG2tdGzfwDpa",
        "rawData": "0x000000000000000000000000000000000000000000000000000000000098967f",
        "jsonData": "[{\"name\":\"\",\"type\":\"uint256\",\"value\":9999999}]"
    },
    "error": null
}
```


### 1.6 EVM调试设置 EvmDebug
> EVM内部字节码解释器调试开关，打开开关后可以在日志中看到每一条EVM指令执行的详细信息；

**请求报文<!--[dapp/evm/types/EvmDebugReq]-->：**
```json
{
    "jsonrpc":"2.0",
    "id": int32,
    "method":"Chain33.Query",
    "params":[
		{
			"execer":"string",
			"funcName":"string",
			"payload":{
				"optype": int32
			}
		}
	]
}
```

**参数说明：**

Chain33.Query结构按通用要求填写：
execer,执行器名称，这里固定为evm，如果是在平行链上则需要加上前缀，比如user.p.game.evm
funcName,操作名称，这里固定为 EvmDebug
payload携带的内容格式如下：

|参数|类型|是否必填|说明|
|----|----|----|----|----|
|optype|int32|是|操作类型，0：查询调试状态， 1：打开， -1：关闭|

**响应报文：**
```json
{
    "id":int32,
    "result":{
        "debugStatus":"string",
    },
    "error":null
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|debugStatus|bool|当前调试开关状态|

