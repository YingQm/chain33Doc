## 1 Transaction Interface
[TOC]

### 1.1 Construct and Send Transaction
To send a transaction, you need to go through three steps:construct transaction->transaction signature->send transaction；

**Construct Transaction：** fill in the key information to construct a complete trading data;
**Transaction Signature：** signing the transaction data, is to mark the owner identity of the transaction,also prevents trading data from being tampered with;
**Send Transaction：** Send the transaction data to the blockchain for execution；

Below introduces three interfaces:

#### 1.1.1 Construct Transaction CreateRawTransaction
**Request message:**
```json
{
    "jsonrpc":"2.0",
    "id":int32,
    "method":"Chain33.CreateRawTransaction",
    "params":[{"to":"string","amount":int64,"fee":int64,"note":"string","isToken":bool,"isWithdraw":bool,"tokenSymbol":"string","execName":"string"}]  
}
```
**Parameter description：**

|Parameter|Type|If Necessary|Description|
|----|----|----|----|
|to|string|yes|send to address|
|amount|int64|yes|send the amount, note that the base unit is 10^8|
|fee|int64|yes|commission fee, note that the base unit is 10^8|
|note|string|no|note|
|isToken|bool|no|token symbol（do not fill in this if it is not token transfer, basic token transfer including parallel chain as well)|
|isWithdraw|bool|yes|whether it is a withdrawal transaction|
|tokenSymbol|string|no|token symbol（do not fill in this if it is not token transfer）|
|execName|string|yes|TransferToExec(transfer to contract) or Withdraw(withdrawal from contract), if want to construct transfers on parallel chains, leave this parameter empty|
|execer|string|-|actuator name, if it is a base token for a parallel chain, write user.p.xx.coins here

**Response message:**
```json
response
{
    "id":int32,
    "result":"string"
}
```
**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|result|string|hexadecimal string encoding of the transaction object|


**Example：**
Request:
```json
{
	"id":1,
	"method":"Chain33.CreateRawTransaction",
	"params":[{
		"to":"1ALB6hHJCayUqH5kfPHU3pz8aCUMw1QiT3",
		"amount":10000,"fee":2000000,
		"note":"for test",
 		"isToken" : bool, 
		"tokenSymbol" : string
	}]
}
```
Response:
```json
{
	"id":1,	"result":"0a05636f696e73121118010a0d10904e1a08666f7220746573742080897a309dfabda9e8dffbce383a2231414c423668484a436179557148356b6650485533707a386143554d773151695433",
	"error":null
}
```

#### 1.1.2 Transaction Signature SignRawTx

**Request message:**
```json
{
    "jsonrpc":"2.0",
    "id":int32,
    "method":"Chain33.SignRawTx",
    "params":[{"addr":"string", "privkey":"string","txHex":"string","expire":"string", "index":int32}]  
}
```

**Parameter description：**

|Parameter|Type|If Necessary|Description|
|----|----|----|----|
|addr|string|no|addr and key can be entered either way，if addr is used, it relies on the private key signature stored in the wallet|
|privkey|string|no|signature private key，addr and key can be entered either way|
|txHex|string|yes|original transaction data generated in the previous step|
|expire|string|yes|for expiration time,"300ms","-1.5h"or"2h45m" all works，and the unit of effective time are "ns", "us"(or "µs"),"ms","s","m","h"|
|index|int32|no|If signature transaction group, then it is the serial number of the transaction to be signed, starting from 1. If it is less than or equal to 0, it is all the transactions in the signature group.|

**Response message:**
```json
{
    "id":int32,
    "result":{"string"},
    "error":null
}
```

**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|result|string|hexadecimal string after the transaction signature|

#### 1.1.3 Send Transaction SendTransaction
**Request message:**
```json
request: http.post
{
    "jsonrpc":"2.0",
    "id":int32,
    "method":"Chain33.SendTransaction",
    "params":[{"data":"string"}]
}
```

**Parameter description：**

|Parameter|Type|If Necessary|Description|
|----|----|----|----|
|data|string|yes|the transaction data signed from the previous step|

**Response message:**
```json
response
{
   "id":int32,
   "result":{"string"} 
}
```
**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|result|string|the transaction hash generated after the transaction is sent (this hash can be used to query the transaction status and history later)|

#### 1.1.4  Structure and Send Transaction Free of Commission Fee CreateNoBalanceTransaction (Parallel chain)
In parallel chain operating environment，to send a transaction without commission charge is permitted. The specific steps are as follows:
create transaction -> **parallel chain transaction package** -> transaction signature -> send transaction

Compared with ordinary transaction, it has one more step of **parallel chain transaction wrapper** . The corresponding interface is as follows

**Request message:**
```json
{
    "jsonrpc":"2.0",
    "id":int32,
    "method":"Chain33.CreateNoBalanceTransaction",
    "params":[{"txHex":"string","payAddr":int64,"privkey":int64,"expire":"string"}]  
}
```

**Parameter description：**

|Parameter|Type|If Necessary|Description|
|----|----|----|----|
|txHex|string|yes|unsigned raw transaction data|
|payAddr|string|yes|PayAddr and privkey can enter only one of the addresses to be used for payment. If payAddr is used, it relies on the signature of the private key stored in the wallet|
|privkey|string|no| private key corresponding to payAddr.If payAddr has been imported into a parallel chain, only send the address is permitted|

**Response message:**
```json
response
{
    "id":int32,
    "result":"string"
}
```
**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|result|string|unsigned raw transaction data|

#### 1.1.5 Error Message

|code|output|description| 
|----|----|----|
|txExistErr|transaction exists|this transaction is already existed in mempool|
|lowFeeErr|low transaction fee|transaction fee is too low|
|manyTxErr|too many transactions| more than 10 transactions in the same account in mempool|
|signErr|wrong signature|signature error|
|lowBalanceErr|low balance|insufficient balance|
|bigMsgErr|message too big|message too big|
|expireErr|message expired|message expired|
|loadAccountsErr|loadacconts error|matching account error|
|emptyTxErr|empty transaction|transaction is empty|
|dupTxErr|duplicated transaction|repeated transaction|
|memNotReadyErr|mempool not ready|mempool not ready|
|memFullErr|mempool is full|mempool is full|

### 1.2 Query Transaction Information Based on Hash QueryTransaction
**Request message:**
```json
{
    "jsonrpc":"2.0",
    "id":int32,
    "method":"Chain33.QueryTransaction",
    "params":[{"hash":"string"}]
}
```
**Parameter description：**

|Parameter|Type|If Necessary|Description|
|----|----|----|----|
|hash|string|yes|transaction hash|

**Response message:**
```json
{
    "id":int32,
    "result":
    {
        "tx":
        {
            "execer":"string",
            "payload":"string",
            "fee":int64,
            "expire":int32,
            "nonce":int32,
            "to":"string",
            "signature":{"ty":int32,"pubkey":"string","signature":"string"}
        },
        "receipt":{"ty":int32,"logs":[{"ty":int32,"log":"string"}]},
        "proofs":["string"],
        "height":int64,
        "index":int32,
        "blockTime":int64,
        "amount":int64,
        "fromAddr":"string"
        "actionName": "string"
    }
}

```
**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|result.tx|json|transaction basic information|
|result.receipt|json|transaction execution result information|
|result.actionName|string|operation name, different actuators may have different values, such as coins（transfer，withdraw，genesis），ticket（genesis，open，close，miner）|
|result.receipt.ty|int32|receipt.ty == 1 represent failed execution；receipt.ty == 2 represent successful execution|

### 1.3 Get Transaction Information Based on Address GetTxByAddr
**Request message:**
```json
{
    "jsonrpc":"2.0",
    "id":int32,
    "method":"Chain33.GetTxByAddr",
    "params":[
        {"addr":"string",
        "flag":int32,
        "count":int32,
        "direction":int32,
        "height":int64,
        "index":int64}
     ] 
}
```
**Parameter description：**

|Parameter|Type|If Necessary|Description|
|----|----|----|----|
|addr|string|yes|account address to query|
|count|int32|yes|number of data bars returned|
|direction|int32|yes|direction of inquiry; 0: forward query, block height from low to high; -1: reverse query;|
|flag|int32|no|transaction type；0: all transactions involving addr, 1：addr as the sender；2：addr as the receiver；|
|height|int64|no|transaction height in block, -1：represents taking backwards from the most recent；大于等于0的值，从具体的高度+具体index开始取|
|index|int64|no|index of transaction in block, between 0--100000|

**Response message:**
```json
{
    "id":int32,
    "result":
    {
        "txInfos": 
        [
            {
                "hash": "string",
                "height": int64,
                "index": int64,
                "assets": [ 
                      {
                         "exec": "string", 
						 "symbol": "string",
						 "amount":int64
                      } 
                 ]
            }
        ]
    }
}
```
**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|txInfos|json|transaction array；including transaction information of asset, height；|
|txInfos.hash|string|transaction id, specific transaction information can be obtained through the QueryTransaction interface|
|txInfos.assets|array|asset information, lists the assets associated with the transaction  the entire array may be null|


**Example：**
Request:
```json
{
    "jsonrpc":"2.0",
    "id":int32,
    "method":"Chain33.GetTxByAddr",
    "params":[
        {"addr":"1JZqMjcbETCENx2JAsWSQwCGXu25icLpz4",
        "flag":0,
        "count":10,
        "direction":0,
        "height":-1,
        "index":0}
     ] 
}
```
Response:
```json
{
    "id":int32,
    "result":
    {
        "txInfos": 
        [
            {
                "hash": "0xf5eeeaf0471f126078567418bfdfb944e82471fdd41fc32b6bed8c0807d16259",
                "height": 3705,
                "index": 4987,
                "assets": [ 
                      {
                         "exec": "coins", "symbol": "BTY"
                      } 
                 ]
            }
        ]
    }
}
```

### 1.4 Get Transaction Information in Bulk Based on the Hash Array GetTxByHashes
**Request message:**
```json
{
    "jsonrpc":"2.0",
    "id":int32,
    "method":"Chain33.GetTxByHashes",
    "params":[{"hashes":["string"], "disableDetail":bool}] 
}
```
**Parameter description：**

|Parameter|Type|If Necessary|Description|
|----|----|----|----|
|hashes|string array|yes|transactionID list, use comma","to divide|
|disableDetail|bool|no|whether hided transaction details, default is false|

**Response message:**
```json
{
    "id":int32,
    "result":
    {
        "txs": 
        [
            {
                "tx": {}
        ]
    }
}
```
**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|tx|json|one transaction detailed information, please refer to QueryTransaction interface|

### 1.5 Get Transaction String by Hash GetHexTxByHash
**Request message:**
```json
{
    "id":int32,
    "method":"Chain33.GetHexTxByHash",
    "param":[{"hash":"string"}]
}
```

**Parameter description：**

|Parameter|Type|If Necessary|Description|
|----|----|----|----|
|hash|string|yes|transaction hash|

**Response message:**
```json
{
    "id":int32,
    "result":"string"    
}
```
**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|result|string|hexadecimal encoded data of transaction object|

### 1.6 Get Address Related Overview Information GetAddrOverview
**Request message:**
```json
{
    "jsonrpc":"2.0",
    "id":int32,
    "method":"Chain33.GetAddrOverview",
    "params":[{"addr":"string","flag":int32,"count":int32,"direction":int32,"height":int64,"height":int64,"index":int64}] 
}
```
**Parameter description：**

|Parameter|Type|If Necessary|Description|
|----|----|----|----|
|addr|string|yes|address information to query|
> Note: the parameter structure of this interface and GetTxByAddr are common, but this interface only used addr parameters, other parameters are meaningless;

**Response message:**
```json
  response
{
    "id":int32,
    "result":
    {
    	"reciver": 10000000000,
        "balance": 9899000000,
        "txCount": 101
	}
}
```
**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|reciver|int64|total amount received|
|txCount|int64|transaction count|
|balance|int64|current balance|

### 1.7 Convert Contract Name to Actual Address ConvertExectoAddr
**Request message:**
```json
{
    "jsonrpc":"2.0",
    "id":int32,
    "method":"Chain33.ConvertExectoAddr",
    "params":[{"execname":"string"}] 
}
```
**Parameter description：**

|Parameter|Type|If Necessary|Description|
|----|----|----|----|
|execname|string|yes|actuator name. If you need to transfer money to the actuator , some interfaces need to be called to convert the executor name to the actual address|

**Response message:**
```json
{
    "id":int32,
    "result":"string"   
}
```
**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|result|string|transformational address string|

### 1.8 Create Transaction Group CreateRawTxGroup
**Request message:**
```json
{
    "jsonrpc":"2.0",
    "id":int32,
    "method":"Chain33.CreateRawTxGroup",
    "params":[{"txs":["string"]}] 
}
```
**Parameter description：**

|Parameter|Type|If Necessary|Description|
|----|----|----|----|
|txs|string array|yes|transaction array in hexadecimal format|

**Response message:**
```json
{
    "id":int32,
    "result":"string"   
}
```
**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|result|string|transaction group object's hexadecimal string|
