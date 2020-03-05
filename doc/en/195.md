## 1 Mining Setting
[TOC]
### 1.1 Get Actuator Address
```json
Request message:
{
	"method":"Chain33.ConvertExectoAddr",
    "params":[
		{
			"execname":"string"
		}
	]
}
```
**Parameter description：**

|Parameter|Type|If Necessary|Description|
|----|----|----|----|
|execer|string|yes|actuator name|

```json
Response message:
{
    "result":"string"
}
```
**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|result|string|actuator address|


### 1.2 Bind Mining Address
```json
Request message:
{
	"method":"Chain33.CreateBindMiner",
    "params":{
		"bindAddr":"string", 
		"originAddr":"string",
		"amount":int64,
		"checkBalance":bool
	}
}
```
**Parameter description：**

|Parameter|Type|If Necessary|Description|
|----|----|----|----|
|bindAddr|string|yes|mining binding address|
|originAddr|string|yes|original address|
|amount|int64|yes|BTY quantity to buy ticket|
|checkBalance|bool|yes|whether to conduct quota check|

```json
Response message:
{
    "result":[
		{
			"txhex":"string"
		}
	]
}
```
**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|txhex|string|hexadecimal transaction strings|
### 1.3 Set up Automatic Mining
```json
Request message:
{
    "id":int32,
    "method":"ticket.SetAutoMining",
    "params":[
	    {
		    "flag":int32
		}
	]
}
```
**Parameter description：**

|Parameter|Type|If Necessary|Description|
|----|----|----|----|
|flag|int32|yes|Identifier, 1 means start auto mining, 0 means close auto mining.|

```json
Response message:
{
    "id":int32,
    "result":[
	     {
		     "isOK":true,
			 "msg":""
	     }
	],
    "error":null
}
```
**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|isok|bool|When successful, return true; on failure, return false.|
|msg|string|When successful, is empty; On failure, return error message.|