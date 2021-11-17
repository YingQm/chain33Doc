##  区块链接口
[TOC]
### 1 获取版本 Version

**调用接口**
```
rpc Version(ReqNil) returns (VersionInfo) {}
```
**参数：**
nil

**返回数据：**
```
message VersionInfo {
    string title   = 1;
    string app     = 2;
    string chain33 = 3;
    string localDb = 4;
    int32  chainID = 5;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|title|string|区块链名，该节点chain33.toml中配置的title值|
|app|string|应用app的版本|
|chain33|string|版本信息，版本号-GitCommit(前八个字符)|
|localDb|string|localdb版本号|
|chainID|string|chain ID|

### 2 获取区间区块 GetBlocks

**调用接口**
```
rpc GetBlocks(ReqBlocks) returns (Reply) {}
```
**参数：**
```
 {
    int64    start      = 1;
    int64    end        = 2;
    bool     isDetail   = 3;
    repeated string pid = 4;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|start|int64|开始区块高度|
|end|int64|结束区块高度|
|isDetail|bool|是否打印区块详细信息|
|pid|[]string|peer列表|

**返回数据：**
```
message Reply {
    bool  isOk = 1;
    bytes msg  = 2;
}

Decode msg 得到 BlockDetails

message BlockDetails {
    repeated BlockDetail items = 1;
}

message BlockDetail {
    Block    block                   = 1;
    repeated ReceiptData receipts    = 2;
    repeated KeyValue KV             = 3;
    bytes             prevStatusHash = 4;
}

message Block {
    int64     version        = 1;
    bytes     parentHash     = 2;
    bytes     txHash         = 3;
    bytes     stateHash      = 4;
    int64     height         = 5;
    int64     blockTime      = 6;
    uint32    difficulty     = 11;
    bytes     mainHash       = 12;
    int64     mainHeight     = 13;
    Signature signature      = 8;
    repeated Transaction txs = 7;
}

message ReceiptData {
    int32    ty              = 1;
    repeated ReceiptLog logs = 3;
}

message ReceiptLog {
    int32 ty  = 1;
    bytes log = 2;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|items|BlockDetail|区块数组；包含区块信息；|
|items.block|Block|区块的信息|
|items.block.version|int64|区块版本|
|items.block.parentHash|bytes|上一区块的部分header信息序列化后的哈希值|
|items.block.txHash|bytes|所有交易序列化后的哈希值|
|items.block.stateHash|bytes|所有交易在对应的执行器执行后写入KVDB中重新计算得到的新state的哈希值|
|items.block.txs|Transaction|交易信息|
|items.recipts|ReceiptData|交易执行结果信息|

### 3 获取最新的区块头 GetLastHeader

**调用接口**
```
rpc GetLastHeader(ReqNil) returns (Header) {}
```
**参数：**
nil

**返回数据：**
```
message Header {
    int64     version    = 1;
    bytes     parentHash = 2;
    bytes     txHash     = 3;
    bytes     stateHash  = 4;
    int64     height     = 5;
    int64     blockTime  = 6;
    int64     txCount    = 9;
    bytes     hash       = 10;
    uint32    difficulty = 11;
    Signature signature  = 8;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|version|int64|区块版本|
|parentHash|bytes|上一区块的部分header信息序列化后的哈希值|
|txHash|bytes|所有交易序列化后的哈希值|
|stateHash|bytes|所有交易在对应的执行器执行后写入KVDB中重新计算得到的新state的哈希值|
|difficulty|uint32|困难值|

### 4 获取区间区块头 GetHeaders

**调用接口**
```
rpc GetHeaders(ReqBlocks) returns (Headers) {}
```
**参数：**
```
message ReqBlocks {
    int64    start      = 1;
    int64    end        = 2;
    bool     isDetail   = 3;
    repeated string pid = 4;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|start|int64|开始区块高度|
|end|int64|结束区块高度|
|isDetail|bool|是否打印区块详细信息|
|pid|[]string|peer列表|

**返回数据：**
```
message Headers {
    repeated Header items = 1;
}

message Header {
    int64     version    = 1;
    bytes     parentHash = 2;
    bytes     txHash     = 3;
    bytes     stateHash  = 4;
    int64     height     = 5;
    int64     blockTime  = 6;
    int64     txCount    = 9;
    bytes     hash       = 10;
    uint32    difficulty = 11;
    Signature signature  = 8;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|items|[]Header|区块头信息数组|

### 5 获取区块哈希值 GetBlockHash
**调用接口**
```
rpc GetBlockHash(ReqInt) returns (ReplyHash) {}
```
**参数：**
```
message ReqInt {
    int64 height = 1;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|height|int64|需要获取哈希的区块的高度|

**返回数据：**
```
message ReplyHash {
    bytes hash = 1;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|hash|bytes|区块哈希值|

### 6 获取区块的详细信息 GetBlockOverview
**调用接口**
```
rpc GetBlockOverview(ReqHash) returns (BlockOverview) {}
```
**参数：**
```
message ReqHash {
    bytes hash    = 1;
    bool  upgrade = 2;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|hash|string|区块哈希值|

**返回数据：**
```
message BlockOverview {
    Header   head           = 1;
    int64    txCount        = 2;
    repeated bytes txHashes = 3;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|head|Header|区块头信息|
|txHashes|[]bytes|交易哈希数组，包含每个交易的哈希值|

### 7 通过区块哈希获取区块信息 GetBlockByHashes
**调用接口**
```
rpc GetBlockByHashes(ReqHashes) returns (BlockDetails) {}
```
**参数：**
```
message ReqHashes {
    repeated bytes hashes = 1;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|hashes|[]string|区块哈希列表|

**返回数据：**
```
message BlockDetails {
    repeated BlockDetail items = 1;
}

message BlockDetail {
    Block    block                   = 1;
    repeated ReceiptData receipts    = 2;
    repeated KeyValue KV             = 3;
    bytes             prevStatusHash = 4;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|items|[]BlockDetail|区块数组；包含区块信息|
|items.block|Block|区块的信息|
|items.recipts|[]ReceiptData|交易执行结果信息|

### 8 获取区块的序列信息 GetBlockSequences

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
	"method": "Chain33.GetBlockSequences",
	"params": [
		{
			"start": int64,
			"end": int64,
			"isDetail": bool
		}
	]
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|start|int64|开始区块高度|
|end|int64|结束区块高度|
|isDetail|bool|是否打印区块详细信息|

**返回数据：**
```

```

```json
{
	"id": 0,
	"result": {
		"blkseqInfos": [
			{
				"hash": "string",
				"type": int64
			}
		]
	},
	"error": null
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|hash|string|区块哈希值|
|type|int64|区块类型，1：增加区块，2：删除区块|

**示例：**

Request:
```json
{
	"method": "Chain33.GetBlockSequences",
	"params": [
		{
			"start": 0,
			"end": 0,
			"isDetail": false
		}
	],
	"id": 0
}
```
Response:
```json
{
	"id": 0,
	"result": {
		"blkseqInfos": [
			{
				"hash": "0xfd39dbdbd2cdeb9f34bcec3612735671b35e2e2dbf9a4e6e3ed0c34804a757bb",
				"type": 1
			}
		]
	},
	"error": null
}
```
</div>

### 9 获取最新区块的序列号 GetLastBlockSequence
**调用接口**
```
rpc GetLastBlockSequence(ReqNil) returns (Int64) {}
```
**参数：**
nil

**返回数据：**
```
Int64
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|result|int64|区块序列号|


### 10 注册区块（区块头）推送服务或者合约回执推送服务 AddPushSubscribe

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
	"method": "Chain33.AddPushSubscribe",
	"params": [
		{
			"name": "string",
			"URL": "string",
			"encode": "string",
			"lastSequence": int64,
			"lastHeight": int64,
			"lastBlockHash": "string",
			"type": int32,
			"contract": map[string]bool
		}
	]
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|name|string|注册名称，长度不能超过 128；一旦通过 name 完成注册，其他订阅用户就不能使用相同的名字进行注册。|
|URL|string|接受推送的 URL，长度不能超过 1024；<br>当 name 相同，URL 不同，提示该 name 已经被注册，注册失败；<br>当 name 相同，URL 相同 如果推送已经停止，则重新开始推送，如果推送正常，则继续推送。|
|encode|string|数据编码方式；json 或者 proto|
|lastSequence|int64|推送开始序列号|
|lastHeight|int64|推送开始高度|
|lastBlockHash|string|推送开始块哈希|
|last三个参数||必须保持一致，不然会出错；<br>都不填，或者 lastSequence=0，lastHeight=0，lastBlockHash=“”，从零开始推送。|
|type|int32|推送的数据类型；0:代表区块；1:代表区块头信息；2：代表交易回执|
|contract|map[string]bool|订阅的合约名称，当type=2的时候起效，比如“coins=true”|

<!--
|lastSequence|int64|推送不是从零开始|
|lastHeight|int64|推送不是从零开始r|
|lastBlockHash|string|推送不是从零开始|

last三个参数有三种组合可以使用
 1. lastSequence = lastHeight = 0, lastBlockHash = “”， 从零开始推送
 1. lastSequence = -1,  lastHeight， lastBlockHash 指定特定的值，从 lastHeader， lastBlockHash 指定的值开始推送。 有些业务可能是从某高度开始推送的， 不知道 对应的sequence
 1. lastSequence lastHeight lastBlockHash 指定特定的值， 从指定的值开始推送
-->


**返回数据：**
```

```

```json
{
	"id":int32,
	"result": {
		"isOK": bool,
		"msg": "string"
	},
	"error": null
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|isOK|bool|是否设置成功|
|msg|string|错误信息|

**示例：**

Request:
```json
{
	"method": "Chain33.AddPushSubscribe",
	"params": [
		{
			"name": "test",
			"URL": "http://127.0.0.1:9999/",
			"encode": "json",
			"type": 0
		}
	],
	"id": 0
}
```
Response:
```json
{
	"id": 0,
	"result": {
		"isOK": true,
		"msg": ""
	},
	"error": null
}
```
</div>

### 11 列举推送服务 ListPushes

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
	"method":"Chain33.ListPushes",
	"params":[]
}
```
**参数说明：**

|参数|类型|是否必填|说明|
|----|----|----|----|

**返回数据：**
```

```

```json
{
	"id":int32,
	"result": {
		"items": [
			{
				"name":"string",
				"URL":"string",
				"encode":"string"
				"lastSequence": int64,
				"lastHeight": int64,
				"lastBlockHash": "string",
				"type": int32,
				"contract": map[string]bool
			}
		]
	},
	"error": null
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|items|json|推送服务列表|

**示例：**

Request:
```json
{
	"method": "Chain33.ListPushes",
	"params": [],
	"id": 0
}
```
Response:
```json
{
	"id": 0,
	"result": {
		"items": [
			{
				"name": "test",
				"URL": "http://127.0.0.1:9999/",
				"encode": "json",
				"lastSequence": 100,
				"lastHeight": 100,
				"lastBlockHash": "0xe15fb9d8ee52be4654d7250266cdf8c86e84f6d0518ad81699b3d81e71fc3828",
				"type": 1,
				"contract": {}
			}
		]
	},
	"error": null
}
```
</div>

### 12 获取某推送服务最新序列号的值 GetPushSeqLastNum

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
	"method":"Chain33.GetPushSeqLastNum",
	"params": [
		{
			"data":"string"
		}
	]
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|data|string|推送服务名|

**返回数据：**
```

```

```json
{
	"id":int32,
	"result": {
		"data": int64
	},
	"error": null
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|data|string|序列号|

**示例：**

Request:
```json
{
	"method": "Chain33.GetPushSeqLastNum",
	"params": [
		{
			"data": "test"
		}
	],
	"id": 0
}
```
Response:
```json
{
	"id": 0,
	"result": {
		"data": -1
	},
	"error": null
}
```
</div>