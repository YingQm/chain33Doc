## 多重签名
[TOC]
### 1 多重签名合约功能：
#### 1.1 多重签名账户的创建
   。需要设置默认的owner以及权重，指定资产的每日限额，请求权重的值
#### 1.2 多重签名账户属性的修改
   。owner的add/del/modify/replace
   。资产每日限额的修改
   。请求权重的修改
#### 1.3 多重签名账户的转账
   。转入时，to地址必须是多重签名地址，from地址必须是非多重签名地址；
   。转出时，from地址必须是多重签名地址，to地址必须是非多重签名地址； 传出交易需要校验权重

### 2 多重签名合约命令行
[多重签名合约命令行](https://chain.33.cn/document/115#2%20%E5%A4%9A%E9%87%8D%E7%AD%BE%E5%90%8D%E5%90%88%E7%BA%A6%E5%91%BD%E4%BB%A4%E8%A1%8C)

### 3 多重签名合约 GRPC 接口说明

#### 3.1 account

##### 3.1.1 创建多重签名账户（未签名） MultiSigAccCreateTx
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
    "id":int32,
    "method":"multisig.MultiSigAccCreateTx",
    "params":[
		{
			"owners":[{"ownerAddr":"string","weight":uint64}],
			"RequiredWeight":uint64,
			"dailyLimit":{"symbol":"string","execer":"string","dailyLimit":uint64}
		}
	]
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|owners|[]*Owner|owner数组(ownerAddr:string,weight:uint64),最少2个owner|
|requiredWeight|uint64|交易被执行的请求权重值，此值不能大于所有owner权重的总和|
|dailyLimit|*SymbolDailyLimit|资产的每日限额值(execer:string,symbol:string,dailyLimit:uint64)|

**返回数据：**
```

```

```json
{
    "id":int32,
    "error":null,
    "result":"string"
}
```
**参数说明：**

|参数|类型|说明|
|----|----|----|
|result|string|返回交易十六进制编码后的字符串|
</div>

##### 3.1.2 多重签名账户修改RequiredWeight值（未签名） MultiSigAccOperateTx

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
    "id":int32,
    "method":"multisig.MultiSigAccOperateTx",
    "params":[
		{
			"multiSigAccAddr":string,
			"newRequiredWeight":uint64,
			"operateFlag":bool
		}
	]
}
```
**参数说明：**

|参数|类型|说明|
|----|----|----|
|multiSigAccAddr|string|多重签名账户地址|
|newRequiredWeight|uint64|新的请求权重值|
|operateFlag|bool|account账户操作类型：true 修改RequiredWeight值|
|dailyLimit|*SymbolDailyLimit|资产的每日限额值(execer:string,symbol:string,dailyLimit:uint64)|

**返回数据：**
```

```

```json
{
    "id":int32,
    "error":null,
    "result":"string"
}
```
**参数说明：**

参数|类型|说明
|----|----|----|
|result|string|返回交易十六进制编码后的字符串|
</div>

##### 3.1.3 多重签名账户修改DailyLimit每日限额(未签名) MultiSigAccOperateTx

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
    "id":int32,
    "method":"multisig.MultiSigAccOperateTx",
    "params":[
		{
			"multiSigAccAddr":"string",
			"dailyLimit":{"symbol":"string","execer":"string","dailyLimit":uint64},
			"operateFlag":bool
		}
	]
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|multiSigAccAddr|string|多重签名账户地址|
|dailyLimit|*SymbolDailyLimit|资产的每日限额值(execer:string,symbol:string,dailyLimit:uint64)|
|operateFlag|bool|account账户操作类型：false 修改DailyLimit值|
|newRequiredWeight|uint64|新的请求权重值|


**返回数据：**
```

```

```json
{
    "id":int32,
    "error":null,
    "result":"string"
}
```
**参数说明：**

|参数|类型|说明|
|----|----|----|
|result|string|返回交易十六进制编码后的字符串|
</div>


##### 3.1.4 获取已经创建的多重签名账户个数 MultiSigAccCount

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
```

**参数说明：**

|参数|类型|是否必须|说明|
|----|----|----|----|
|driver|bytes|是|执行器名称, 这里固定为 multisig|
|funcName|string|是|操作名称, 这里固定为 MultiSigAccCount|
|stateHash|bytes|否|所有交易在对应的执行器执行后写入KVDB中重新计算得到的新state的哈希值|
|param|bytes|是|nil|
|extra|bytes|否|扩展字段，用于额外的用途|

**返回数据：**
```
message Int64 {
    int64 data = 1;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|data|int64|多重签名账户个数|


##### 3.1.5 获取多重签名地址 MultiSigAccounts

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

message ReqMultiSigAccs {
    int64 start = 1;
    int64 end   = 2;
}
```

**参数说明：**

|参数|类型|是否必须|说明|
|----|----|----|----|
|driver|bytes|是|执行器名称, 这里固定为 multisig|
|funcName|string|是|操作名称, 这里固定为 MultiSigAccounts|
|stateHash|bytes|否|所有交易在对应的执行器执行后写入KVDB中重新计算得到的新state的哈希值|
|param|bytes|是|types.Encode(&ReqMultiSigAccs)|
|extra|bytes|否|扩展字段，用于额外的用途|
|start|int64|是|多重签名账户index索引，从0开始|
|end|int64|是|多重签名账户index索引，end>=start && end< MultiSigAccCount获取的值|

**返回数据：**
```
message ReplyMultiSigAccs {
    repeated string address = 1;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|address|[]string|多重签名账户地址列表|

##### 3.1.6 获取多重签名账户信息 MultiSigAccountInfo

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

message ReqMultiSigAccInfo {
    string multiSigAccAddr = 1;
}
```

**参数说明：**

|参数|类型|是否必须|说明|
|----|----|----|----|
|driver|bytes|是|执行器名称, 这里固定为 multisig|
|funcName|string|是|操作名称, 这里固定为 MultiSigAccountInfo|
|stateHash|bytes|否|所有交易在对应的执行器执行后写入KVDB中重新计算得到的新state的哈希值|
|param|bytes|是|types.Encode(&ReqMultiSigAccInfo)|
|extra|bytes|否|扩展字段，用于额外的用途|
|multiSigAccAddr|string|是|多重签名账户地址|


**返回数据：**
```
message MultiSig {
    string   createAddr                = 1;
    string   multiSigAddr              = 2;
    repeated Owner owners              = 3;
    repeated DailyLimit dailyLimits    = 4;
    uint64              txCount        = 5;
    uint64              requiredWeight = 6;
}

// owner 结构体：owner账户地址，以及权重
message Owner {
    string ownerAddr = 1;
    uint64 weight    = 2;
}

//每日资产限额，不同的资产价格不一致，需要设置各自的每日限额。没有设置或者限额是0时，表示不能取币
// spentToday今天已经花费的额度。用于和dailyLimit做对比，超过每日限额时需要多重签名
// lastDay记录当天开始的时间戳，新的一天需要重置spentToday为初始值0，并修改lastDay的时间戳
message DailyLimit {
    string symbol     = 1;
    string execer     = 2;
    uint64 dailyLimit = 3;
    uint64 spentToday = 4;
    int64  lastDay    = 5;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|createAddr|string|创建本多重签名账户的创建者地址|
|multiSigAddr|string|本多重签名账户地址|
|ownerAddr|string|owner地址|
|weight|uint64|owner权重|
|execer|string|资产执行器名|
|symbol|string|资产标识|
|dailyLimit|uint64|本资产的每日限额值|
|spentToday|uint64|当天已经花费的资产值|
|lastDay|int64|当天开始时间|
|txCount|uint64|本多重签名账户上的交易数量|
|requiredWeight|uint64|本多重签名账户执行交易需要的权重|

##### 3.1.7 查询多重签名账户指定资产当日免密余额 MultiSigAccUnSpentToday

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

message ReqAccAssets {
    string multiSigAddr = 1;
    Assets assets       = 2;
    bool   isAll        = 3;
}

message Assets {
    string execer = 1;
    string symbol = 2;
}

```

**参数说明：**

|参数|类型|是否必须|说明|
|----|----|----|----|
|driver|bytes|是|执行器名称, 这里固定为 multisig|
|funcName|string|是|操作名称, 这里固定为 MultiSigAccUnSpentToday|
|stateHash|bytes|否|所有交易在对应的执行器执行后写入KVDB中重新计算得到的新state的哈希值|
|param|bytes|是|types.Encode(&ReqAccAssets)|
|extra|bytes|否|扩展字段，用于额外的用途|
|multiSigAddr|string|是|多重签名账户地址|
|assets|*Assets|是|资产信息("execer":string,"symbol":string)|
|isAll|bool|是|是否所有资产，true：所有资产，false：只查询指定资产的|

**返回数据：**
```
message ReplyUnSpentAssets {
    repeated UnSpentAssets unSpentAssets = 3;
}

message UnSpentAssets {
    Assets assets = 1;
    uint64 amount = 2;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|execer|string|本多重签名账户资产执行器名|
|symbol|string|本多重签名账户资产标识|
|amount|uint64|本多重签名账户指定资产当日免密余额|

##### 3.1.8 查询多重签名账户指定资产信息 MultiSigAccAssets

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

message ReqAccAssets {
    string multiSigAddr = 1;
    Assets assets       = 2;
    bool   isAll        = 3;
}
```

**参数说明：**

|参数|类型|是否必须|说明|
|----|----|----|----|
|driver|bytes|是|执行器名称, 这里固定为 multisig|
|funcName|string|是|操作名称, 这里固定为 MultiSigAccAssets|
|stateHash|bytes|否|所有交易在对应的执行器执行后写入KVDB中重新计算得到的新state的哈希值|
|param|bytes|是|types.Encode(&ReqAccAssets)|
|extra|bytes|否|扩展字段，用于额外的用途|
|multiSigAddr|string|是|多重签名账户地址|
|assets|*Assets|是|资产信息("execer":string,"symbol":string)|
|isAll|bool|是|是否所有资产，true：所有资产时不需要填写具体的assets信息，false：只查询指定资产的信息|

**返回数据：**
```
message ReplyAccAssets {
    repeated AccAssets accAssets = 1;
}

message AccAssets {
    Assets  assets     = 1;
    int64   recvAmount = 2;
    Account account    = 3;
}

message Assets {
    string execer = 1;
    string symbol = 2;
}

message Account {
    string addr    = 1;
    string frozen  = 2;
    string balance = 3;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|execer|string|资产执行器名|
|symbol|string|资产标识|
|frozen|int64|冻结的资产|
|currency|int32|coins标识，目前没有使用|
|balance|int64|余额|
|addr|string|查询的账户地址|
|recvAmount|uint64|查询账户收到此资产的所有值|


##### 3.1.9 查询指定地址创建的多重签名账户列表 MultiSigAccAllAddress

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
message ReqMultiSigAccInfo {
    string multiSigAccAddr = 1;
}
```

**参数说明：**

|参数|类型|是否必须|说明|
|----|----|----|----|
|driver|bytes|是|执行器名称, 这里固定为 multisig|
|funcName|string|是|操作名称, 这里固定为 MultiSigAccAllAddress|
|stateHash|bytes|否|所有交易在对应的执行器执行后写入KVDB中重新计算得到的新state的哈希值|
|param|bytes|是|types.Encode(&ReqMultiSigAccInfo)|
|extra|bytes|否|扩展字段，用于额外的用途|
|multiSigAccAddr|是|string|创建者地址|

**返回数据：**
```
message AccAddress {
    repeated string address = 1;
}
```

**参数说明：**

参数|类型|说明
|----|----|----|
|address|[]string|多重签名账户地址列表|

##### 3.1.10 查询owner地址拥有的多重签名账户列表 MultiSigAddresList

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
    "id":int32,
    "method":"multisig.MultiSigAddresList",
    "params":[{"data":"string"}]
}

```
**参数说明：**

|参数|类型|说明|
|----|----|----|
|data|string|owner地址,不指定地址时获取本钱包所有地址拥有的多重签名账户列表：|

**返回数据：**
```

```

```json
{
    "id":int32,
	"result" : {
		"items": [
			{
				"multiSigAddr": "3MrcA7jcWNdLYmrbuS5eEVoPbx8BWPGB5F",
				"ownerAddr": "1C5xK2ytuoFqxmVGMcyz9XFKFWcDA8T3rK",
				"weight": 20
			}
		]
	},
	"error" : null
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|multiSigAddr|string|多重签名地址|
|ownerAddr|string|owner地址地址, 或者空字符串""|
|weight|uint64|owner地址在此多重签名账户中的权重|
</div>


#### 3.2 owner

##### 3.2.1 多重签名账户增加owner（未签名） MultiSigOwnerOperateTx

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
    "id":int32,
    "method":"multisig.MultiSigOwnerOperateTx",
    "params":[
		{
			"multiSigAccAddr":"string",
			"newOwner":"string",
			"newWeight":uint64,
			"operateFlag":uint64
		}
	]
}
```

**参数说明：**

|参数|类型|是否必填|说明|
|----|----|----|----|
|multiSigAccAddr|string|是|多重签名账户地址|
|newOwner|string|是|需要添加的owner地址|
|newWeight|uint64|是|需要添加的owner拥有的权重|
|operateFlag|uint64|是|owner操作类型：1|
|oldOwner|string|否|需要删除的owner地址，在该场景中忽略不填|

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
|---|---|---|
|result|string|返回交易十六进制编码后的字符串|
</div>


##### 3.2.2 多重签名账户删除owner（未签名） MultiSigOwnerOperateTx

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
    "id":int32,
    "method":"multisig.MultiSigOwnerOperateTx",
    "params":[
		{
			"multiSigAccAddr":"string",
			"oldOwner":"string",
			"operateFlag":uint64
		}
	]
}
```

**参数说明：**

|参数|类型|是否必填|说明|
|----|----|----|----|
|multiSigAccAddr|string|是|多重签名账户地址|
|newOwner|string|否|需要添加的owner地址，在该场景中忽略不填|
|newWeight|uint64|否|需要添加的owner拥有的权重，在该场景中忽略不填|
|operateFlag|uint64|是|owner操作类型：1|
|oldOwner|string|是|需要删除的owner地址|

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

参数|类型|说明
|----|----|----|
|result|string|返回交易十六进制编码后的字符串|
</div>


##### 3.2.3 多重签名账户owner权重修改（未签名） MultiSigOwnerOperateTx

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
    "id":int32,
    "method":"multisig.MultiSigOwnerOperateTx",
    "params":[
		{
			"multiSigAccAddr":"string",
			"oldOwner":"string",
			"newWeight":uint64,
			"operateFlag":uint64
		}
	]
}
```

**参数说明：**

|参数|类型|是否必填|说明|
|----|----|----|----|
|multiSigAccAddr|string|是|多重签名账户地址|
|newOwner|string|否|需要添加的owner地址，在该场景中忽略不填|
|newWeight|uint64|否|需要添加的owner拥有的权重|
|operateFlag|uint64|是|owner操作类型：3|
|oldOwner|string|是|需要删除的owner地址|

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

参数|类型|说明
---|---|---
result|string|返回交易十六进制编码后的字符串
</div>

##### 3.2.4 多重签名账户owner替换（未签名） MultiSigOwnerOperateTx

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
    "id":int32,
    "method":"multisig.MultiSigOwnerOperateTx",
    "params":[
		{
			"multiSigAccAddr":"string",
			"oldOwner":"string",
			"newOwner":"string",
			"operateFlag":uint64
		}
	]
}
```

**参数说明：**

|参数|类型|是否必填|说明|
|----|----|----|----|
|multiSigAccAddr|string|是|多重签名账户地址|
|newOwner|string|是|新的owner地址|
|newWeight|uint64|否|需要添加的owner拥有的权重，在该场景中忽略不填|
|operateFlag|uint64|是|owner操作类型：4|
|oldOwner|string|是|需要删除的owner地址|

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
|result|string|返回交易十六进制编码后的字符串|
</div>

#### 3.3 tx

##### 3.3.1 多重签名账户资产转入（未签名） MultiSigAccTransferInTx

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
    "id":int32,
    "method":"multisig.MultiSigAccTransferInTx",
    "params":[
		{
			"symbol":"string",
			"execname":"string",
			"note":"string",
			"to":"string",
			"amount":int64
		}
	]
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|symbol|string|资产标识,例如：BTY|
|execname|string|资产执行器名，例如：coins|
|to|string|收账地址，必须是多重签名地址|
|note|string|转账说明|
|amount|int64|转入的资产额度|

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
|result|string|返回交易十六进制编码后的字符串|
</div>

##### 3.3.2 多重签名账户资产转出（未签名） MultiSigAccTransferOutTx

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
    "id":int32,
    "method":"multisig.MultiSigAccTransferOutTx",
    "params":[
		{
			"symbol":"string",
			"execname":"string",
			"note":"string",
			"to":"string",
			"from":"string",
			"amount":int64
		}
	]
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|symbol|string|资产标识,例如：BTY|
|execname|string|资产执行器名，例如：coins|
|from|string|出账地址，必须是多重签名地址|
|to|string|收账地址，必须是非多重签名地址|
|note|string|转账说明|
|amount|int64|转入的资产额度|

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
|result|string|返回交易十六进制编码后的字符串|
</div>

##### 3.3.3 多重签名账户交易确认（未签名） MultiSigConfirmTx

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
    "id":int32,
    "method":"multisig.MultiSigConfirmTx",
    "params":[
		{
			"multiSigAccAddr":"string",
			"txId":uint64,
			"confirmOrRevoke":bool
		}
	]
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|multiSigAccAddr|string|多重签名地址|
|txId|uint64|需要确认或者撤销的交易index，从0开始|
|confirmOrRevoke|bool|确认/撤销交易。true：确认交易|

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
|result|string|返回交易十六进制编码后的字符串|
</div>

##### 3.3.4 获取多重签名账户交易数 MultiSigAccTxCount

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
message ReqMultiSigAccInfo {
    string multiSigAccAddr = 1;
}
```

**参数说明：**

|参数|类型|是否必须|说明|
|----|----|----|----|
|driver|bytes|是|执行器名称, 这里固定为 multisig|
|funcName|string|是|操作名称, 这里固定为 MultiSigAccTxCount|
|stateHash|bytes|否|所有交易在对应的执行器执行后写入KVDB中重新计算得到的新state的哈希值|
|param|bytes|是|types.Encode(&ReqMultiSigAccInfo)|
|extra|bytes|否|扩展字段，用于额外的用途|
|multiSigAccAddr|string|是|多重签名账户地址|

**返回数据：**
```
message Uint64 {
    uint64 data = 1;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|data|int64|多重签名账户地址个数|


##### 3.3.5 获取指定区间的指定状态的多重签名交索引易 MultiSigTxids

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
message ReqMultiSigTxids {
    string multiSigAddr = 1;
    uint64 fromTxId     = 2;
    uint64 toTxId       = 3;
    bool   pending      = 4;
    bool   executed     = 5;
}
```

**参数说明：**

|参数|类型|是否必须|说明|
|----|----|----|----|
|driver|bytes|是|执行器名称, 这里固定为 multisig|
|funcName|string|是|操作名称, 这里固定为 MultiSigTxids|
|stateHash|bytes|否|所有交易在对应的执行器执行后写入KVDB中重新计算得到的新state的哈希值|
|param|bytes|是|types.Encode(&ReqMultiSigTxids)|
|extra|bytes|否|扩展字段，用于额外的用途|
|multiSigAddr|string|是|多重签名账户地址|
|fromTxId|uint64|是|多重签名账户交易索引值，fromTxId>=0|
|toTxId|uint64|是|多重签名账户交易索引,toTxId< MultiSigAccTxCount 获取的交易数|
|pending|bool|是|未执行的交易|
|executed|bool|是|已执行的交易|

**返回数据：**
```
message ReplyMultiSigTxids {
    string   multiSigAddr = 1;
    repeated uint64 txids = 2;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|multiSigAddr|string|多重签名账户地址|
|txids|[]uint64|多重签名账户交易索引|


##### 3.3.6 获取多重签名交信息 MultiSigTxInfo

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
message ReqMultiSigTxInfo {
    string multiSigAddr = 1;
    uint64 txId         = 2;
}
```

**参数说明：**

|参数|类型|是否必须|说明|
|----|----|----|----|
|driver|bytes|是|执行器名称, 这里固定为 multisig|
|funcName|string|是|操作名称, 这里固定为 MultiSigTxInfo|
|stateHash|bytes|否|所有交易在对应的执行器执行后写入KVDB中重新计算得到的新state的哈希值|
|param|bytes|是|types.Encode(&ReqMultiSigTxInfo)|
|extra|bytes|否|扩展字段，用于额外的用途|
|multiSigAddr|string|是|多重签名账户地址|
|txId|uint64|是|多重签名账户交易索引值，fromTxId>=0|

**返回数据：**
```
message MultiSigTx {
    uint64   txid                 = 1;
    string   txHash               = 2;
    bool     executed             = 3;
    uint64   txType               = 4;
    string   multiSigAddr         = 5;
    repeated Owner confirmedOwner = 6;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|txId|uint64|多重签名账户交易id值|
|txHash|string|多重签名账户交易hash值|
|executed|bool|多重签名账户交易执行状态，true：已执行，false：未执行|
|txType|uint64|多重签名账户交易类型。1：owner属性相关的交易 2:account属性相关的交易 3：转账相关的交易|
|multiSigAddr|string|多重签名账户地址|
|confirmedOwner|[]*Owner|确认此多重签名账户交易的owner列表|
|ownerAddr|string|多重签名账户owner地址|
|weight|uint64|多重签名账户owner权重|

##### 3.3.7 获取指定交易被确认的权重信息 MultiSigTxConfirmedWeight

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
message ReqMultiSigTxInfo {
    string multiSigAddr = 1;
    uint64 txId         = 2;
}
```

**参数说明：**

|参数|类型|是否必须|说明|
|----|----|----|----|
|driver|bytes|是|执行器名称, 这里固定为 multisig|
|funcName|string|是|操作名称, 这里固定为 MultiSigTxConfirmedWeight|
|stateHash|bytes|否|所有交易在对应的执行器执行后写入KVDB中重新计算得到的新state的哈希值|
|param|bytes|是|types.Encode(&ReqMultiSigTxInfo)|
|extra|bytes|否|扩展字段，用于额外的用途|
|multiSigAddr|string|是|多重签名账户地址|
|txId|uint64|是|多重签名账户交易索引值，0 <= fromTxId < MultiSigAccTxCount 获取的交易数|

**返回数据：**
```
message Uint64 {
    uint64 data = 1;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|data|uint64|多重签名账户交易被确认的权重|