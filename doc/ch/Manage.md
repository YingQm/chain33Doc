## Manage
[TOC]

manage 管理执行器，主要功能是动态地给其他执行器配置和调整参数值。如给token执行器增加黑名单，给game执行器设置最大的赌资等等。
所有修改都是通过指定的manager账户地址，发送交易去修改参数值。这样做可以避免系统因为修改参数值而导致硬分叉。

### 1 添加/删除一个token-finisher CreateTransaction
**请求报文<!--[types/ModifyConfig]-->：**
```json
{
	"jsonrpc":"2.0",
    "id":int32,
    "method":"Chain33.CreateTransaction",
    "params":[
		{
			"execer" : "manage",
			"actionName" : "Modify",
			"payload" : {
				"key": "token-finisher",
				"value": "string",
				"op":"string",
				"addr":"string"
			}
		}
	]
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

**响应报文：**
```json
{
    "id":int32,
    "result":"string"
}
```
**参数说明：**

|参数|类型|说明|
|----|----|----|
|result|string|交易的hex字节码|

### 2 查看finish apprv列表apprv列表 GetConfigItem
**请求报文<!--[types/ReqString]-->：**
```json
{
    "jsonrpc":"2.0",
    "id":int32,
    "method":"Chain33.Query",
    "params":[
		{
			"execer" : "manage",
			"funcName" : "GetConfigItem",
			"payload" : {"data":"token-finisher"}
		}
	]
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|data|string|具体数据，这里是token-finisher. 指定查询的是 finish apprv列表|

**响应报文：**

```json
{
	"id":int32,
	"result":{
		"key": "token-finisher",
		"value": "string"
	},
	"error":null
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|key|string|配置项的标识符|
|value|string|配置项的值， 这里是对应地址列表|
