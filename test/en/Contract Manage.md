## 1 Manage
[TOC]

manage actuator, the main function is to dynamically configure and adjust the value of parameters for other actuators. For example, adding blacklist to token executor, setting maximum gambling capital to game executor and so on.
All changes are made through the specified manager account address, sending the transaction to modify parameter value.This prevents the system from hard branching by modifying the parameter values.

### 1.1 Add a Token-Finisher
```json
{
    "jsonrpc":"2.0",
    "id":int32,
    "method":"Chain33.CreateTransaction",
    "params":[{"execer" : "manage",
               "actionName" : "Modify",
               "payload" : {
			   		"key": "token-finisher",
					"value": "1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs",
					"op":"add"
			   }
    }]
}
```

### 1.2 Delete a Token-Finisher
```json
{
    "jsonrpc":"2.0",
    "id":int32,
    "method":"Chain33.CreateTransaction",
    "params":[{"execer" : "manage",
               "actionName" : "Modify",
               "payload" : {
			   		"key": "token-finisher",
					"value": "1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs",
					"op":"delete"
			   }
    }]
}
```

### 1.3 View Finish Apprv List
```json
{
    "jsonrpc":"2.0",
    "id":int32,
    "method":"Chain33.Query",
    "params":[{"execer" : "manage",
               "funcName" : "GetConfigItem",
               "payload" : {
			   		"data": "token-finisher"
			   }
    }]
}
```

**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|method|string|Chain33.Query|
|execer|string|name of the actuator, here is manage|
|FuncName|string|query method，here corresponds to GetConfigItem under manage|
|payload|object||
|payload.data|string|Specific data, here is token-finisher. Specify queried is the finish apprv list.|

Response data:

```json
{
  "id":int32,
  "error":null,
  "result":[
    {
    "key": "token-finisher",
    "value": ["1Q8hGLfoGe63efeWa8fJ4Pnukhkngt6poK"]
    }
   ]
}
```

**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|key|string|identifier of the configuration item|
|value|string|value of the configuration item, here is the corresponding address list|
### 1.4 Other Configurations
Referring to the above operation, while the value of key is different.
Existing supported configuration items.

token-finisher
token-blacklist