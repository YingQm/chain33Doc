# 1 Blockchain Interface
[TOC]
## 1.1  Get Version

**Request message:**

```json
{
	"jsonrpc":"2.0",
	"method": "Chain33.Version",
	"params": [
		null
	],
	"id": int32
}
```

**Parameter description：**

No parameter.

**Response message:**

```json
{
    "id":int32,
    "result":{
        "title":"string",
        "app":"string",
        "chain33":"string",
        "localDb":"string"
        },
    "error":null
}
```

**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|result.title|string|blockchain name, the title value configured in the node chain33.toml|
|result.app|string|version of applying app|
|result.chain33|string|version information, version number -GitCommit(first eight characters)|
|result.localDb|string|localdb version number|

**Example:**

Request:
```json
{
	"method": "Chain33.Version",
	"params": [
		null
	],
	"id": 0,
}
```
Response:
```json
{
    "id":0,
    "result":{
        "title":"chain33",
        "app":"1.0.0",
        "chain33":"6.0.2-46bd6ab9",
        "localDb":"1.0.0"
        },
    "error":null
}
```

## 1.2 Get Interval Block

**Request message:**

```json
{
	"jsonrpc":"2.0",
	"method": "Chain33.GetBlocks",
	"params": [
		{
			"start": int32,
			"end": int32,
			"isDetail": bool
		}
	],
	"id": int32
}
```

**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|start|int32|starting block height|
|end|int32|ending block height|
|isDetail|bool|whether to print block details|

**Response message:**

```json
{
  "id": 0,
  "result": {
    "items": [
      {
        "block": {
          "version": int64,
          "parentHash": "string",
          "txHash": "string",
          "stateHash": "string",
          "height": int64,
          "blockTime": int64,
          "txs": [
            {
              "execer": "string",
              "payload": {
                "genesis": {
                  "amount": "string",
                  "returnAddress": "string"
                },
                "ty": int32
              },
              "rawPayload": "string",
              "signature": {
                "ty": int32,
                "pubkey": "string",
                "signature": "string"
              },
              "fee": int64,
              "feefmt": "string",
              "expire": int64,
              "nonce": int64,
              "from": "string",
              "to": "string"
            }
          ]
        },
        "recipts": {
            "ty":int32,
            "tyName":"string",
            "logs":{
                "ty":int32,
                "tyName":"string",
                "log":"string",
                "rawLog":"string"
            }
        }
      },
      {
        "block": {
          "version": int64,
          "parentHash": "string",
          "txHash": "string",
          "stateHash": "string",
          "height": int64,
          "blockTime": int64,
          "txs": [
            {
              "execer": "string",
              "payload": {
                "topic": "",
                "content": "string"
              },
              "rawPayload": "string",
              "signature": {
                "ty": int32,
                "pubkey": "string",
                "signature": "string"
              },
              "fee": int64,
              "feefmt": "string",
              "expire": int64,
              "nonce": int64,
              "from": "string",
              "to": "string"
            }
          ]
        },
        "recipts": null
      }
    ]
  },
  "error": null
}
```

**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|items|json|block array: contains block information;|
|items.block|json|block information|
|items.block.version|int64|block version|
|items.block.parentHash|string|the hash value of the serialized portion of header information in the previous block|
|items.block.txHash|string|hash value of all transactions serialized|
|items.block.stateHash|string|after the corresponding actuator executes write the hash value of the new state recalculated in KVDB into all transactions|
|items.block.txs|json|transaction information|
|items.recipts|json|交易 execution result information|

**Example:**

Request:
```json
{
	"method": "Chain33.GetBlocks",
	"params": [
		{
			"start": 0,
			"end": 10,
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
    "items": [
      {
        "block": {
          "version": 0,
          "parentHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "txHash": "0xe34a933c5abf350db4db5122abbf43f6a54da2dbd67d214f67362c36bd70d23e",
          "stateHash": "0x2863c8dbc7fe3146c8d4e7acf2b8bbe4666264d658356e299e240f462a382a51",
          "height": 0,
          "blockTime": 1514533394,
          "txs": [
            {
              "execer": "coins",
              "payload": {
                "genesis": {
                  "amount": "10000000000000000",
                  "returnAddress": ""
                },
                "ty": 2
              },
              "rawPayload": "0x1802120910808084fea6dee111",
              "signature": {
                "ty": 0,
                "pubkey": "",
                "signature": ""
              },
              "fee": 0,
              "feefmt": "0.0000",
              "expire": 0,
              "nonce": 0,
              "from": "1HT7xU2Ngenf7D4yocz2SAcnNLW7rK8d4E",
              "to": "14KEKbYtKKQm4wMthSK9J4La4nAiidGozt"
            }
          ]
        },
        "recipts": null
      },
      {
        "block": {
          "version": 0,
          "parentHash": "0xfd39dbdbd2cdeb9f34bcec3612735671b35e2e2dbf9a4e6e3ed0c34804a757bb",
          "txHash": "0x2af1d0131f37ded31eee9bd16630af761b7299ee53a16ebe8f15dfdf1b9d2b0f",
          "stateHash": "0x2863c8dbc7fe3146c8d4e7acf2b8bbe4666264d658356e299e240f462a382a51",
          "height": 1,
          "blockTime": 1543920166,
          "txs": [
            {
              "execer": "user.write",
              "payload": {
                "topic": "",
                "content": "NDtZZxe"
              },
              "rawPayload": "0x4e44745a5a7865",
              "signature": {
                "ty": 1,
                "pubkey": "0x030f9e532cd668a0b32dd96cac3325ed8eddc46901535c20fb2253acea34213eaf",
                "signature": "0x3045022100b8364f68d8bd35b66b3a346239ec7fddbec3b6c37aeee6694153d724f693e6bd02200e0c5c824c088bd24b180fc9da4f7c569929d20141e66fdab820f731f5db00d0"
              },
              "fee": 1000000,
              "feefmt": "0.0100",
              "expire": 4611686018427388000,
              "nonce": 0,
              "from": "1MoMByk8Jp9qB97VJQ1mjPk23EqheSpKgg",
              "to": "1DNaSDRG9RD19s59meAoeN4a2F6RH97fSo"
            }
          ]
        },
        "recipts": null
      }
    ]
  },
  "error": null
}
```

## 1.3 Get the Latest Block Header

**Request message:**

```json
{
	"jsonrpc":"2.0",
	"method": "Chain33.GetLastHeader",
	"params": [
		null
	],
	"id": int32
}
```

**Parameter description：**

No parameter.

**Response message:**

```json
{
  "id": int32,
  "result": {
    "version": int64,
    "parentHash": "string",
    "txHash": "string",
    "stateHash": "string",
    "height": int64,
    "blockTime": int64,
    "txCount": int64,
    "hash": "string",
    "difficulty": uint32
  },
  "error": null
}
```

**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|version|int64|block version|
|parentHash|string|hash value of the serialized portion of header information in the previous block|
|txHash|string|hash value of all transactions serialized|
|stateHash|string|after the corresponding actuator executes write the hash value of the new state recalculated in KVDB into all transactions|
|difficulty|uint32|difficulty value|

**Example:**

Request:
```json
{
	"method": "Chain33.GetLastHeader",
	"params": [
		null
	],
	"id": 0
}
```
Response:
```json
{
  "id": 0,
  "result": {
    "version": 0,
    "parentHash": "0xfd39dbdbd2cdeb9f34bcec3612735671b35e2e2dbf9a4e6e3ed0c34804a757bb",
    "txHash": "0x2af1d0131f37ded31eee9bd16630af761b7299ee53a16ebe8f15dfdf1b9d2b0f",
    "stateHash": "0x2863c8dbc7fe3146c8d4e7acf2b8bbe4666264d658356e299e240f462a382a51",
    "height": 1,
    "blockTime": 1543920166,
    "txCount": 1,
    "hash": "0x8a7cf829cd993a23933c8b6914e6d1e560c17c50ce224aa6639ecee950699dff",
    "difficulty": 523239423
  },
  "error": null
}
```

## 1.4 Get the Interval Block Header

**Request message:**

```json
{
	"jsonrpc":"2.0",
	"method": "Chain33.GetHeaders",
	"params": [
		{
			"start": int64,
			"end": int64,
			"isDetail": bool
		}
	],
	"id": int32
}
```

**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|start|int32|starting block height|
|end|int32|ending block height|
|isDetail|bool|whether to print block details|

**Response message:**
```json
{
  "id": 0,
  "result": {
    "items": [
      {
        "version": int64,
        "parentHash": "string",
        "txHash": "string",
        "stateHash": "string",
        "height": int64,
        "blockTime": int64,
        "txCount": int64,
        "hash": "string",
        "difficulty": uint32
      }
    ]
  },
  "error": null
}
```

**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|items|json|array of block header information|

## 1.5 Get Block Hash Value

**Request message:**

```json
{
	"jsonrpc":"2.0",
	"method": "Chain33.GetBlockHash",
	"params": [
		{
			"height": int64
		}
	],
	"id": int32
}
```

**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|height|int64|the height of the hash block need to get|

**Response message:**

```json
{
  "id": int32,
  "result": {
    "hash": "string"
  },
  "error": null
}
```

**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|hash|string|block hash value|

**Example:**

Request:
```json
{
	"method": "Chain33.GetBlockHash",
	"params": [
		{
			"height": 1
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
    "hash": "0x8a7cf829cd993a23933c8b6914e6d1e560c17c50ce224aa6639ecee950699dff"
  },
  "error": null
}
```

## 1.6 Get Block Details

**Request message:**

```json
{
	"jsonrpc":"2.0",
	"method": "Chain33.GetBlockOverview",
	"params": [
		{
			"hash": "string"
		}
	],
	"id": int32
}
```

**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|hash|string|block hash value|

**Response message:**

```json
{
  "id": 0,
  "result": {
    "head": {
      "version": int64,
      "parentHash": "string",
      "txHash": "string",
      "stateHash": "string",
      "height": int64,
      "blockTime": int64,
      "txCount": int64,
      "hash": "string",
      "difficulty": uint32
    },
    "txCount": int64,
    "txHashes": [
      "string"
    ]
  },
  "error": null
}
```

**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|head|json|block header information|
|txHashes|json|hash array, containing the hash value of each transaction|

## 1.7 Get Block Information By Block Hash

**Request message:**

```json
{
	"jsonrpc":"2.0",
	"method": "Chain33.GetBlockByHashes",
	"params": [
		{
			"hashes": [
				"string"
			],
			"disableDetail": bool
		}
	],
	"id": int32
}
```

**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|hashs|json|block hash list|
|disableDetail|bool|whether to print block details|

**Response message:**

```json
{
  "id": 0,
  "result": {
    "items": [
      {
        "block": {
          "version": 0,
          "parentHash": "string",
          "txHash": "string",
          "stateHash": "string",
          "height": int64,
          "blockTime": int64,
          "txs": [
            {
              "execer": "string",
              "payload": {
                "genesis": {
                  "amount": "string",
                  "returnAddress": "string"
                },
                "ty": int32
              },
              "rawPayload": "string",
              "signature": {
                "ty": int32,
                "pubkey": "string",
                "signature": "string"
              },
              "fee": int64,
              "feefmt": "string",
              "expire": int64,
              "nonce": int64,
              "from": "string",
              "to": "string",
              "hash": "string"
            }
          ]
        },
        "recipts": [
          {
            "ty": int32,
            "tyName": "string",
            "logs": [
              {
                "ty": int32,
                "tyName": "string",
                "log": {
                  "prev": {
                    "currency": int32,
                    "balance": "string",
                    "frozen": "string",
                    "addr": "string"
                  },
                  "current": {
                    "currency": int32,
                    "balance": "string",
                    "frozen": "string",
                    "addr": "string"
                  }
                },
                "rawLog": "string"
              }
            ]
          }
        ]
      }
    ]
  },
  "error": null
}
```

**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|items|json|hash array, containing the hash information|
|items.block|json|block information|
|items.recipts|json|transaction execution result information|

## 1.8 Get Sequence information of the block

**Request message:**

```json
{
	"jsonrpc":"2.0",
	"method": "Chain33.GetBlockSequences",
	"params": [
		{
			"start": int64,
			"end": int64,
			"isDetail": bool
		}
	],
	"id": int32
}
```

**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|start|int32|starting block height|
|end|int32|ending block height|
|isDetail|bool|whether to print block details|

**Response message:**

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

**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|hash|string|block hash value|
|type|int64|block type, 1: add block, 2: delete block|

**Example:**

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

## 1.9 Get the Serial Number of the Latest Block

**Request message:**

```json
{
	"jsonrpc":"2.0",
	"method": "Chain33.GetLastBlockSequence",
	"params": [
		null
	],
	"id": int32
}
```

**Parameter description：**

No parameter.

**Response message:**

```json
{
  "id": int32,
  "result": int64,
  "error": null
}
```

**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|result|int64|block serial number|

**Example:**

Request:
```json
{
	"method": "Chain33.GetLastBlockSequence",
	"params": [
		null
	],
	"id": 0
}
```
Response:
```json
{
  "id": 0,
  "result": 0,
  "error": null
}
```

## 1.10 Add Block Sequence Number Change Callback

**Request message:**

```json
{
	"jsonrpc":"2.0",
	"method": "Chain33.AddSeqCallBack",
	"params": [
		{
			"name": "string",
			"URL": "string",
			"encode": "string"
		}
	],
	"id": int32
}
```

**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|name|string|callback name, length cannot exceed 128|
|URL|string| notification URL of serial number change, length cannot exceed 1024; cancel the notification when the name is the same and the URL is empty|
|encode|string|data encoding mode: json or proto|

**Response message:**

```json
{
  "id": int32,
  "result": {
    "isOK": bool,
    "msg": "string"
  },
  "error": null
}
```

**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|isOK|bool|whether setting successful|
|msg|string|error message|

**Example:**

Request:
```json
{
	"method": "Chain33.AddSeqCallBack",
	"params": [
		{
			"name": "test",
			"URL": "http://127.0.0.1:9999/",
			"encode": "json"
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

## 1.11 Enumerate Block Sequence Number Callbacks

**Request message:**
```json
{
	"jsonrpc":"2.0",
	"method": "Chain33.ListSeqCallBack",
	"params": [
		null
	],
	"id": 0
}
```

**Parameter description：**

No parameter.

**Response message:**

```json
{
  "id": 0,
  "result": {
    "items": [
      {
        "name": "string",
        "URL": "string",
        "encode": "string"
      }
    ]
  },
  "error": null
}
```

**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|items|json|list of callback information|

**Example:**

Request:
```json
{
	"method": "Chain33.ListSeqCallBack",
	"params": [
		null
	],
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
        "encode": "json"
      }
    ]
  },
  "error": null
}
```

## 1.12 Get of the Latest Sequence Number Value for a Callback

**Request message:**

```json
{
	"jsonrpc":"2.0",
	"method": "Chain33.GetSeqCallBackLastNum",
	"params": [
		{
			"data": "string"
		}
	],
	"id": 0
}
```

**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|data|string|callback name|

**Response message:**

```json
{
  "id": 0,
  "result": {
    "data": int64
  },
  "error": null
}
```

**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|data|string|serial name|

**Example:**

Request:
```json
{
	"method": "Chain33.GetSeqCallBackLastNum",
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