## 1 EVM Interface
[TOC]

### 1.1 Create EVM Contract Transaction CreateTransaction
> The original transaction is created here, and in addition to that, you need to sign the transaction and send it. For details you can refer to [HERE](93)

**Request message**
```json
{
    "jsonrpc":"2.0", 
    "id": 2, 
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
```

**Parameter description：**

|Parameter|Type|If Necessary|Description|
|----|----|----|----|
|execer|string|Yes|actuator name，fixed here as evm|
|actionName|string|Yes|function name, fixed here as CreateCall|
|isCreate|bool|Yes|Whether it is a create contract action, create the contract as true, call the contract as false.|
|name|string|No|invoked contract name, valid and necessary when isCreate is false|
|code|string|No|contract code that needs to be deployed or invoked|
|abi|string|No|contract ABI code that needs to be deployed or invoked|
|alias|string|No|Contract alias when deploying a new contract to facilitate identification of different contracts.|
|note|string|No|notes for this transaction|
|amount|uint64|No|When the contract is invoked, if the amount needs to be passed, pass this parameter.|
|fee|int64|No|Your handling fee for this transaction, needs to be about the gas value *gasPrice of contract consumption|
|gasPrice|uint32|No|unit gas pricing, default is 1|
|gasLimit|uint64|No|The maximum amount of gas allowed to be consumed in this transaction, default value equal to fee.|

> Note: in the deployment contract, code is required and abi is optional; when calling the contract, choose one between code and abi.


**Response message:**
```json
{
    "id":int32,
    "result":"string",
    "error":null
}
```

**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|result|string|hexadecimal string of transaction contents|

**Example：**
Request1 Deploy contract transaction:
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

Request2 Invoke contract transaction(abi):
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

### 1.2 Estimate Consumption of Contract Call Gas 
> This operation only simulates the execution, estimates the gas consumption roughly, and does not actually execute the code;

**Request message：**
```json
{
    "jsonrpc":"2.0", 
    "id": int32, 
    "method":"Chain33.Query",
    "params":[{
        "execer":"string", 
        "funcName":"string", 
        "payload":{
            "to": "string",
            "code": "string",
            "abi": "string",
            "caller": "string",
            "amount": "string"
        }
    }] 
}
```

**Parameter description：**

|Parameter|Type|If Necessary|Description|
|----|----|----|----|
|execer|string|Yes|actuator name，fixed here as evm|
|funcName|string|Yes|function name, fixed here as EstimateGas|
|to|string|No|The target address, if pupose is to create the contract, leave it blank here, otherwise fill in the contract address here.|
|code|string|No|Contract code that needs to be deployed or invoked. If it is a deployment contract, this field is required|
|abi|string|No|contract ABI code that needs to be deployed or invoked|
|caller|string|No|The initiator of this call, if not filled in, the EVM contract itself is considered to initiate the call.|
|amount|uint64|No|When the contract is invoked, if the amount needs to be passed, pass this parameter|


**Response message:**
```json
{
    "id":int32,
    "result":{
        "gas":uint64
    },
    "error":null
}
```

**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|gas|uint64|the gas value to be consumed in this transaction|

### 1.3 Query EVM Contract Address
> The EVM contract has two identifiers, one is contract address, the other is contract name, and they are the unique one-to-one correspondence. Due to the system design, the contract name must be used to operate the transfer operation, so this interface provides the mutual checking ability of the two.

**Request message：**
```json
{
    "jsonrpc":"2.0", 
    "id": int32, 
    "method":"Chain33.Query",
    "params":[{
        "execer":"string", 
        "funcName":"string", 
        "payload":{
            "addr": "string"
        }
    }] 
}
```

**Parameter description：**

|Parameter|Type|If Necessary|Description|
|----|----|----|----|
|execer|string|Yes|actuator name，fixed here as evm|
|funcName|string|Yes|function name, fixed here as CheckAddrExists|
|addr|string|Yes|contract address or contract name, fill in any one and return the other|

**Response message:**
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

**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|contract|bool|is there any EVM contract under this address|
|contractAddr|string|this contract address|
|contractName|string|contract name|
|aliasName|string|contract alias|

**Example：**
Request:
```json
{
    "jsonrpc":"2.0", 
    "id": 2, 
    "method":"Chain33.Query",
    "params":[{
        "execer":"evm", 
        "funcName":"CheckAddrExists", 
        "payload":{
            "addr": "1LuigHsSy55KEsZgBMJtYfo3wrhz7YbbDD"
        }
    }] 
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

### 1.4 Query Contract ABI
> If the EVM contract is bound to an ABI at deployment, ABI information bindings can be obtained through this interface.

**Request message：**
```json
{
    "jsonrpc":"2.0", 
    "id": int32, 
    "method":"Chain33.Query",
    "params":[{
        "execer":"string", 
        "funcName":"string", 
        "payload":{
            "address": "string"
        }
    }] 
}
```

**Parameter description：**

|Parameter|Type|If Necessary|Description|
|----|----|----|----|
|execer|string|Yes|actuator name，fixed here as evm|
|funcName|string|Yes|function name, fixed here as CheckAddrExists|
|address|string|Yes|EVM contract address|

**Response message:**
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

**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|address|string|this contract address|
|abi|string|The ABI to which this contract is bound|

### 1.5 Contract Read-Only Call (through ABI)
> In EVM contract deployment, if ABI information is bound, the method called determines whether it is a read-only call or not. This call can be directly returned by querying the database, not in transaction, no fee;
**Request message：**
```json
{
    "jsonrpc":"2.0", 
    "id": int32, 
    "method":"Chain33.Query",
    "params":[{
        "execer":"string", 
        "funcName":"string", 
        "payload":{
            "address": "string",
            "input": "string",
            "caller": "string"
        }
    }] 
}
```

**Parameter description：**

|Parameter|Type|If Necessary|Description|
|----|----|----|----|
|execer|string|Yes|actuator name，fixed here as evm|
|funcName|string|Yes|function name, fixed here as Query|
|address|string|Yes|contract address|
|input|string|Yes|ABI methods and parameters|
|caller|string|No|The initiator of this call, if not filled in, the EVM contract itself is considered to initiate the call.|

**Response message:**
```json
{
    "id":int32,
    "result":{
        "address": "string",
        "input": "string",
        "caller": "string",
        "rawData":"string",
        "jsonData":"string"
    },
    "error":null
}
```

**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|address|string|contract address|
|input|string|call input|
|caller|string|caller|
|rawData|string|call returned raw data|
|jsonData|string|Call return data in json format|

**Example：**
Request:
```json
{
    "jsonrpc":"2.0", 
    "id": 2, 
    "method":"Chain33.Query",
    "params":[{
        "execer":"evm", 
        "funcName":"Query", 
        "payload":{
            "address": "1LuigHsSy55KEsZgBMJtYfo3wrhz7YbbDD",
            "input": "get()",
            "caller": "1Kkq2neiAWSGkk3djkJ9SPoG2tdGzfwDpa"
        }
    }] 
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


### 1.6 EVM Debugging Settings
> EVM internal bytecode interpreter debugging switch, open the switch can see the detailed information of each EVM instruction execution in the log;

**Request message：**
```json
{
    "jsonrpc":"2.0", 
    "id": int32, 
    "method":"Chain33.Query",
    "params":[{
        "execer":"string", 
        "funcName":"string", 
        "payload":{
            "optype": int32
        }
    }] 
}
```

**Parameter description：**

|Parameter|Type|If Necessary|Description|
|----|----|----|----|
|execer|string|Yes|actuator name, fixed here as evm|
|funcName|string|Yes|function name, fixed here as EvmDebug|
|optype|int32|Yes|operation type, 0: query debugging status, 1: on, -1: off|

**Response message:**
```json
{
    "id":int32,
    "result":{
        "debugStatus":"string",
    },
    "error":null
}
```

**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|debugStatus|bool|current debug switch status|

