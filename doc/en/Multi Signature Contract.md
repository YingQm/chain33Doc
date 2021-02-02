# Multi Signature Contract：
[TOC]
## Multi Signature Contract's Function
### 1. Multi Signature Contract's Creation：
Set the default owner and weight, specify the daily quota for the asset, and request the value of the weight
### 2. Modification of Multi Signature Account Attributes：
   。Owner's add/del/modify/replace
   。Modification of asset daily limits
   。Modification of request weight 
### 3. Transfer of Multi Signature Account：
   。When rolling in, the "to" address must be a multi-signed address, and the "from" address must be a non-multi-signed address.
   。When rolling out, the "to" address must be a non-multi-signed address, and the "from" address must be a multi-signed address. 传出 transaction 需要校验权重

## Multi Signature Contract's Command Line：

### Multi Signature Contract's Command Line Description：

#### account
```
cli multisig  account
Available Commands:
  address     get multisig account address
  assets      get assets of multisig account
  count       get multisig account count
  create      Create a multisig account transaction
  creator     get all multisig accounts created by the address
  dailylimit  Create a modify assets dailylimit transaction
  owner       get multisig accounts by the owner
  info        get multisig account info
  unspent     get assets unspent today amount
  weight      Create a modify required weight transaction

```
#### owner
```
cli multisig  owner
Available Commands:
  add         Create a add owner  transaction
  del         Create a del owner transaction
  modify      Create a modify owner weight transaction
  replace     Create a replace owner transaction
```
#### tx
```
cli multisig  tx
Available Commands:
  confirm          Create a confirm transaction
  confirmed_weight get the weight of the transaction confirmed.
  count            get multisig tx count
  info             get multisig account tx info
  transfer_in      Create a transfer to multisig account transaction
  transfer_out     Create a transfer from multisig account transaction
  txids            get multisig txids
```
### Multi Signature Contract's Command Line Description：
```
1. Multi signature contract's creation：generates a multisigned account address multisig-addr based on the txhash
   cli send multisig account create -d 10 -e coins -s BTY -a "owner-1 owner-2" -w "20 10" -r 15 -k private-key

2. Check the number of accounts created:
   cli multisig account count

3. Account index gets multiple siignature account addresses
   cli multisig account address -e 0 -s 0

4. Get account details through the multi-signature account addr
   cli multisig account info -a multisig-addr

5. Transfer to multisig contract
   cli send bty transfer -a 50 -n test  -t multisig-exec-addr -k addr3

6. Transfer to multiple signature address in multisig contract
   cli send multisig tx transfer_in -a 40 -e coins -s BTY  -t multisig-addr -n test -k addr3

7. View multiple signature address assets
   cli multisig  account assets  -a multisig-addr

8. Transfer from multiple signature address in multisig contracts
   cli send multisig  tx transfer_out  -a 11 -e coins -s BTY -f multisig-addr -t addr3 -n test -k owner-1

9. Query transaction count
   cli multisig  tx count  -a multisig-addr

10. Query transaction txid
   cli multisig   tx txids  -a multisig-addr -s 0 -e 0

11. Query transaction information
   cli multisig  tx info  -a multisig-addr -i 0

12. Add a new owner-3 to the multiple signature account
   cli send multisig owner add  -a multisig-addr -o owner-3 -w 5 -k  owner-1

13. Delete an existed owner-3 in the multiple signature account
   cli send multisig  owner del  -a multisig-addr -o owner-3  -k owner-1

14. Replace existed owner-3 in the multiple signature account with owner-4
   cli send multisig  owner replace  -a multisig-addr -n owner-4 -o owner-2 -k  owner-1

15. Modify existed owner-4 weight in the multiple signature account
   cli send multisig  owner modify  -a multisig-addr -o owner-4 -w 11 -k owner-1

16. Modify multiple signature account dailylimit
   cli send multisig  account dailylimit -a multisig-addr -e coins -s BTY -d 12 -k owner-1

17. Modify multiple signature account request weight
   cli send multisig  account weight -a multisig-addr -w 16 -k owner-1

18. Revocation of confirmation of a multiple signature account transaction
   cli send   multisig tx confirm  -a multisig-addr -i 8 -c f  -k owner-1

19. Confirm a multiple signature account transaction
   cli send multisig tx confirm  -a multisig-addr -i 8 -k owner-1

20. Get all multiple signature accounts created at the specified address
   cli multisig account creator -a addr

21. Gets the daily balance of the specified asset on the specified account
   cli multisig  account unspent  -a multisig-addr -e coins -s BTY

22. Gets all multiple signature addresses owned by owner. Returns all multiple signature addresses owned by this wallet when no address is specified
   cli  multisig account owner -a 166po3ghRbRu53hu8jBBQzddp7kUJ9Ynyf
   
```

## Multiple Signature Contract RPC Interface Description：

### account

#### 1. Create Multiple Signature Account(unsigned)：

> Request message：

```
request: http.post
{
    "jsonrpc":"2.0",
    "id":int32,
    "method":"multisig.MultiSigAccCreateTx",
    "params":[{"owners":[{"ownerAddr":string,"weight":uint64}],
                "RequiredWeight":uint64,
                "dailyLimit":{"symbol":string,"execer":string,"dailyLimit":uint64}]
}
```

> Parameter description：

Parameter|Type|Description
---|---|---
owners|[]*Owner|the owner array(ownerAddr:string,weight:uint64), at least two of the owner
requiredWeight|uint64|the request weight of transaction executed, which cannot be greater than the sum of all owners' weights
dailyLimit|*SymbolDailyLimit|The daily quota value of the asset(execer:string,symbol:string,dailyLimit:uint64)
   
> Response message：return hexadecimal encoded transaction strings

```
response:
{   __
    "id":int32,
    "error":null,
    "result": "string"
}
```

#### 2. Multiple Signature Account Modify RequiredWeight Value(unsigned)：

> Request message：

```
request: http.post
{
    "jsonrpc":"2.0",
    "id":int32,
    "method":"multisig.MultiSigAccOperateTx",
    "params":[{"multiSigAccAddr":string,
                "newRequiredWeight":uint64,
                "operateFlag":bool}]
}
```
> Parameter description：

Parameter|Type|Description
---|---|---
multiSigAccAddr|string|multiple signature account address
newRequiredWeight|uint64|new request weight value
operateFlag|bool|account operation type：true  modify RequiredWeight value
   
> operation type：return hexadecimal encoded transaction strings

```
response:
{   
    "id":int32,
    "error":null,
    "result": "string"
}
```

#### 3. Multiple Signature Account Modify DailyLimit (unsigned)：

> Request message：

```
request: http.post
{
    "jsonrpc":"2.0",
    "id":int32,
    "method":"multisig.MultiSigAccOperateTx",
    "params":[{"multiSigAccAddr":string,
                "dailyLimit":{"symbol":string,"execer":string,"dailyLimit":uint64},
                "operateFlag":bool}]
}
```

> Parameter description：

Parameter|Type|Description
---|---|---
multiSigAccAddr|string|multiple signature account address
dailyLimit|*SymbolDailyLimit|daily quota value of the asset(execer:string,symbol:string,dailyLimit:uint64)
operateFlag|bool|account operation type：false  modify DailyLimit value
   
> Response message：return hexadecimal encoded transaction strings

```
response:
{   
    "id":int32,
    "error":null,
    "result": "string"
}
```

#### 4. Get the Number of Created Multiple Signature Accounts：

> Request message：

```
request: http.post
{
    "jsonrpc":"2.0",
    "id":int32,
    "method":"Chain33.Query",
    "params":[{"execer" : "multisig",
               "funcName" : "MultiSigAccCount",
               "payload" : nil}]
}

```
   
> Response data：

```
{
   "id" : 0,
   "error" : null,
   "result" : {"data" : "0"}
}
```

> Parameter description：

Parameter|Type|Description
---|---|---
data|Int64|multiple signature account number


#### 5. Get Multiple Signature Address：

> Request message：

```
request: http.post
{
    "jsonrpc":"2.0",
    "id":int32,
    "method":"Chain33.Query",
    "params":[{"execer" : "multisig",
               "funcName" : "MultiSigAccounts",
               "payload" : {"start":int64,"end":int64}}]
}

```

> Parameter description：

Parameter|Type|Description
---|---|---
start|int64|multiple signature account index，Start from 0
end|int64|multiple signature account index，end>=start && end< MultiSigAccCount value

> Response data：

```
{
   "id" : 0,
   "error" : null,
   "result" : {
    "address": [
        "3GfnDQxxUEmVrkBCk7RfgvTkLrBLEVEzGV"
    ]}
}
```

> Parameter description：

Parameter|Type|Description
---|---|---
address|[]string|multiple signature account address list


#### 6. Get Multiple Signature Account Message：

> Request message：

```
request: http.post
{
    "jsonrpc":"2.0",
    "id":int32,
    "method":"Chain33.Query",
    "params":[{"execer" : "multisig",
               "funcName" : "MultiSigAccountInfo",
               "payload" : {"multiSigAccAddr":string}}]
}

```
> Parameter description：

Parameter|Type|Description
---|---|---
multiSigAccAddr|string|multiple signature account address


> Response data：

```
{
   "id" : 0,
   "error" : null,
   "result" : {
    "createAddr": "1DkrXbz2bK6XMpY4v9z2YUnhwWTXT6V5jd",
    "multiSigAddr": "3GfnDQxxUEmVrkBCk7RfgvTkLrBLEVEzGV",
    "owners": [
        {
            "ownerAddr": "1C5xK2ytuoFqxmVGMcyz9XFKFWcDA8T3rK",
            "weight": 20
        },
        {
            "ownerAddr": "1LDGrokrZjo1HtSmSnw8ef3oy5Vm1nctbj",
            "weight": 10
        }
    ],
    "dailyLimits": [
        {
            "symbol": "BTY",
            "execer": "coins",
            "dailyLimit": uint64,
            "spentToday": uint64,
            "lastday": int64
        }
    ],
	"txCount": 1,
    "requiredWeight": 15}
}
```

> Parameter description：

Parameter|Type|Description
---|---|---
createAddr|string|multiple signature account creator address
multiSigAddr|string|this multiple signature account address
ownerAddr|string|owner address
weight|uint64|owner weight
execer|string|asset
symbol|string|asset identification
dailyLimit|uint64|asset daily limit
spentToday|uint64|Assets spent that day
lastDay|int64|start time the very day
txCount|uint64|multiple signature account transaction amount
requiredWeight|uint64|multiple signature account weight required to execute transaction



#### 7. Query the Multiple Signature Account Specified Asset's Balance Without Code of the Day：

> Request message：

```
request: http.post
{
    "jsonrpc":"2.0",
    "id":int32,
    "method":"Chain33.Query",
    "params":[{"execer" : "multisig",
               "funcName" : "MultiSigAccUnSpentToday",
               "payload" : {
				"multiSigAddr":string,
				"assets":{"execer":string,"symbol":string},
				"isAll":bool}}]
}

```

> Parameter description：

Parameter|Type|Description
---|---|---
multiSigAddr|string|multiple signature account address
assets|*Assets|asset information("execer":string,"symbol":string)
isAll|bool|whether all assets，true: all assets, false: only query for specified assets

> Response data：

```
{
   "id" : 0,
   "error" : null,
   "result" : {
    "unSpentAssets":[
    {
		"assets":{
        	"symbol": "BTY",
        	"execer": "coins",
        	"amount": uint64
		}
    },
    {
		"assets":{
        	"symbol": "HYB",
        	"execer": "token",
        	"amount": uint64
		}
    }]}
}
```

> Parameter description：

Parameter|Type|Description
---|---|---
execer|string|multiple signature account asset executor name
symbol|string|multiple signature account asset identification
amount|uint64|multiple signature account specified 


#### 8. Query Specified Asset Information Multiple Signature Account：

> Request message：

```
request: http.post
{
    "jsonrpc":"2.0",
    "id":int32,
    "method":"Chain33.Query",
    "params":[{"execer" : "multisig",
               "funcName" : "MultiSigAccAssets",
               "payload" : {
				"multiSigAddr":string,
				"assets":{"execer":string,"symbol":string},
				"isAll":bool}}]
}

```

> Parameter description：

Parameter|Type|Description
---|---|---
multiSigAddr|string|multiple signature account address
assets|*Assets|asset information("execer":string,"symbol":string)
isAll|bool|whether all assets，true: all assets with no need to fill in the specific assets information, false: only query for specified assets

> Response data：

```
{
   "id" : 0,
   "error" : null,
   "result" : {
	"accAssets":[
    {
        "assets": 
		{
			"execer":"coins" 
			"symbol":"BTY"
		}
        "account": 
		{
			"frozen":int64
			"currency":int32
			"balance":int64
			"addr":string
		}
        "recvAmount": uint64
    }]}
}
```

> Parameter description：

Parameter|Type|Description
---|---|---
execer|string|asset actuator name
symbol|string|asset identification
frozen|int64|frozen assets
currency|int32|coins identification
balance|int64|balance
addr|string|checked account address
recvAmount|uint64|Query account received amount for this asset


#### 9. Query List of Multiple Signature Account Created by the Specified Address：

> Request message：

```
request: http.post
{
    "jsonrpc":"2.0",
    "id":int32,
    "method":"Chain33.Query",
    "params":[{"execer" : "multisig",
               "funcName" : "MultiSigAccAllAddress",
               "payload" : {"multiSigAccAddr":string,}}]
}

```
> Parameter description：

Parameter|Type|Description
---|---|---
multiSigAccAddr|string|creator address

> Response data：return multiple signature account address list

```
{
   "id" : 0,
   "error" : null,
   "result" : {
    "address": [
        "3GfnDQxxUEmVrkBCk7RfgvTkLrBLEVEzGV"
    ]
}
}
```

> Parameter description：

Parameter|Type|Description
---|---|---
address|string|multiple signature address list

#### 10. Query Multiple Signature Account List of Owner Address：

> Request message：

```
request: http.post
{
    "jsonrpc":"2.0",
    "id":int32,
    "method":"multisig.MultiSigAddresList",
    "params":[{"data":string}]
}

```
> Parameter description：

Parameter|Type|Description
---|---|---
data|string|owner address, get the multiple signature account list of all addresses of this wallet when no address is specified:

> Response data：return multiple signature account address list

```
{
   "id" : 0,
   "error" : null,
   "result" : {
    "items": [
        {
            "multiSigAddr": "3MrcA7jcWNdLYmrbuS5eEVoPbx8BWPGB5F",
            "ownerAddr": "1C5xK2ytuoFqxmVGMcyz9XFKFWcDA8T3rK",
            "weight": 20
        },
        {
            "multiSigAddr": "3MrcA7jcWNdLYmrbuS5eEVoPbx8BWPGB5F",
            "ownerAddr": "1KHwX7ZadNeQDjBGpnweb4k2dqj2CWtAYo",
            "weight": 5
        },
        {
            "multiSigAddr": "3MrcA7jcWNdLYmrbuS5eEVoPbx8BWPGB5F",
            "ownerAddr": "1LDGrokrZjo1HtSmSnw8ef3oy5Vm1nctbj",
            "weight": 10
        }
    ]
}
}
```

> Parameter description：

Parameter|Type|Description
---|---|---
multiSigAddr|string|multiple signature address
ownerAddr|string|owner address, or empty string""
weight|uint64|owner address weight in this multiple signature account 


### owner

#### 1. Add Owner in Multiple Signature Account(unsigned)：

> Request message：

```
request: http.post
{
    "jsonrpc":"2.0",
    "id":int32,
    "method":"multisig.MultiSigOwnerOperateTx",
    "params":[{
		"multiSigAccAddr":string,
		"newOwner":string,
        "newWeight":uint64,
		"operateFlag":uint64
	}]
}
```

> Parameter description：

Parameter|Type|Description
---|---|---
multiSigAccAddr|string|multiple signature account address
newOwner|string|owner address need to be added
newWeight|uint64|owner weight that needs to be added
operateFlag|uint64|owner operation type：1

   
> Response message：return hexadecimal encoded transaction strings

```
response:
{   
    "id":int32,
    "error":null,
    "result": "string"
}
```

#### 2. multiple signature account删除owner(unsigned)：

> Request message：

```
request: http.post
{
    "jsonrpc":"2.0",
    "id":int32,
    "method":"multisig.MultiSigOwnerOperateTx",
    "params":[{
		"multiSigAccAddr":string,
		"oldOwner":string,
		"operateFlag":uint64
	}]
}
```

> Parameter description：

Parameter|Type|Description
---|---|---
multiSigAccAddr|string|multiple signature account address
oldOwner|string|owner address need to be deleted
operateFlag|uint64|owner operation type：2

   
> Response message：return hexadecimal encoded transaction strings

```
response:
{   
    "id":int32,
    "error":null,
    "result": "string"
}
```


#### 3. Multiple Signature Account Owner Weight Change(unsigned)：

> Request message：

```
request: http.post
{
    "jsonrpc":"2.0",
    "id":int32,
    "method":"multisig.MultiSigOwnerOperateTx",
    "params":[{
		"multiSigAccAddr":string,
		"oldOwner":string,
		"newWeight":uint64,
		"operateFlag":uint64
	}]
}
```

> Parameter description：

Parameter|Type|Description
---|---|---
multiSigAccAddr|string|multiple signature account address
oldOwner|string|owner address which need to be deleted
newWeight|uint64|new weight value
operateFlag|uint64|owner operation type：3

   
> Response message：return hexadecimal encoded transaction strings

```
response:
{   
    "id":int32,
    "error":null,
    "result": "string"
}
```

#### 4. Replace Multiple Signature Account Owner(unsigned)：

> Request message：

```
request: http.post
{
    "jsonrpc":"2.0",
    "id":int32,
    "method":"multisig.MultiSigOwnerOperateTx",
    "params":[{
		"multiSigAccAddr":string,
		"oldOwner":string,
		"newOwner":string,
		"operateFlag":uint64
	}]
}
```

> Parameter description：

Parameter|Type|Description
---|---|---
multiSigAccAddr|string|multiple signature account address
oldOwner|string|owner address which need to be deleted
newOwner|string|new owner address
operateFlag|uint64|owner operation type：4

   
> Response message：return hexadecimal encoded transaction strings

```
response:
{   
    "id":int32,
    "error":null,
    "result": "string"
}
```

### tx

#### 1. Multiple Signature Account Asset Rolling in(unsigned)：

> Request message：

```
request: http.post
{
    "jsonrpc":"2.0",
    "id":int32,
    "method":"multisig.MultiSigAccTransferInTx",
    "params":[{
		"symbol":string,
		"execname":string,
		"note":string,
		"to":string,
		"amount":int64
	}]
}
```

> Parameter description：

Parameter|Type|Description
---|---|---
symbol|string|asset identification, for example: BTY
execname|string|asset actuator names, for example:
to|string|collect account address, must be multiple signature address
note|string|transfer instructions
amount|int64|the amount of assets transferred in

> Response message：return hexadecimal encoded transaction strings

```
response:
{   
    "id":int32,
    "error":null,
    "result": "string"
}
```

#### 2. Multiple Signature Account Asset Rolling out(unsigned)：

> Request message：

```
request: http.post
{
    "jsonrpc":"2.0",
    "id":int32,
    "method":"multisig.MultiSigAccTransferOutTx",
    "params":[{
		"symbol":string,
		"execname":string,
		"note":string,
		"to":string,
		"from":string,
		"amount":int64
	}]
}
```

> Parameter description：

Parameter|Type|Description
---|---|---
symbol|string|asset identification, for example: BTY
execname|string|Asset actuator names, for example: coins
from|string|charge off account address，must be multiple signature address
to|string|collect account address, must be multiple signature address
note|string|transfer instructions
amount|int64|the amount of assets transferred in

> Response message：return hexadecimal encoded transaction strings

```
response:
{   
    "id":int32,
    "error":null,
    "result": "string"
}
```

#### 3. Multiple Signature Account Transaction Confirmation(unsigned)：

> Request message：

```
request: http.post
{
    "jsonrpc":"2.0",
    "id":int32,
    "method":"multisig.MultiSigConfirmTx",
    "params":[{
		"multiSigAccAddr":string,
		"txId":uint64,
		"confirmOrRevoke":bool
	}]
}
```
> Parameter description：

Parameter|Type|Description
---|---|---
multiSigAccAddr|string|multiple signature address
txId|uint64|To be confirmed or revoked transaction index, start from 0
confirmOrRevoke|bool|confirm/cancel transaction . true：confirm transaction 

> Response message：return hexadecimal encoded transaction strings

```
response:
{   
    "id":int32,
    "error":null,
    "result": "string"
}
```

#### 4. Get Number of Multiple Signature Account Transaction：

> Request message：

```
request: http.post
{
    "jsonrpc":"2.0",
    "id":int32,
    "method":"Chain33.Query",
    "params":[{"execer" : "multisig",
               "funcName" : "MultiSigAccTxCount",
               "payload" : {"multiSigAccAddr":string}}]
}

```

> Parameter description：

Parameter|Type|Description
---|---|---
multiSigAccAddr|string|multiple signature account address

 
> Response data：

```
{
   "id" : 0,
   "error" : null,
   "result" : {"data" : "0"}
}
```

> Parameter description：

Parameter|Type|Description
---|---|---
data|Int64|number of multiple signature account address


#### 5. Get Interval Multiple Signature Transaction Index atSpecified Status of a Specified ：

> Request message：

```
request: http.post
{
    "jsonrpc":"2.0",
    "id":int32,
    "method":"Chain33.Query",
    "params":[{"execer" : "multisig",
               "funcName" : "MultiSigTxids",
               "payload" : 
				{"multiSigAddr":string,
				"fromTxId":uint64,"toTxId":uint64,
				"pending":bool,"executed":bool
				}}]
}

```
> Parameter description：

Parameter|Type|Description
---|---|---
multiSigAddr|string|multiple signature account address
fromTxId|uint64|multiple signature account transaction index value，fromTxId>=0
toTxId|uint64|multiple signature account transaction index, toTxId< MultiSigAccTxCount number of transactions acquired
pending|bool|unexecuted transaction 
executed|bool|executed transaction 

> Response data：

```
{
   "id" : 0,
   "error" : null,
   "result" :{
    "multiSigAddr": "3GfnDQxxUEmVrkBCk7RfgvTkLrBLEVEzGV",
    "txids": [
        0,
        1
    ]
}
}
```

> Parameter description：

Parameter|Type|Description
---|---|---
txids|[]uint64|multiple signature account transaction index


#### 6. Get Multiple Signature Transaction Information：

> Request message：
```
request: http.post
{
    "jsonrpc":"2.0",
    "id":int32,
    "method":"Chain33.Query",
    "params":[{"execer" : "multisig",
               "funcName" : "MultiSigTxInfo",
               "payload" : {"multiSigAddr":string,"txId":uint64}}]
}

```
> Parameter description：

Parameter|Type|Description
---|---|---
multiSigAddr|string|multiple signature account address
txId|uint64|multiple signature account transaction index value，fromTxId>=0


> Response data：

```
{
   "id" : 0,
   "error" : null,
   "result" {
   	 "txHash": "d952237fd9a825218b767058946a1047dbdbe166c74e274792d341e81088fbc4",
   	 "executed": true,
   	 "txType": 3,
   	 "multiSigAddr": "3GfnDQxxUEmVrkBCk7RfgvTkLrBLEVEzGV",
   	 "confirmedOwner": [
     {
            "ownerAddr": "1C5xK2ytuoFqxmVGMcyz9XFKFWcDA8T3rK",
            "weight": 20
     }]}
}
```

> Parameter description：

Parameter|Type|Description
---|---|---
txHash|string|multiple signature account transaction hash value
executed|bool|multiple signature account transaction execution status, true: executed, false: not executed
txType|uint64|multiple signature account type 1：owner property related transactions 2:account property related transactions 3: transfer related transactions
multiSigAddr|string|multiple signature account multiple signature account address
confirmedOwner|[]*Owner|owner list in confirmation of this multiple signature account
ownerAddr|string|multiple signature account owner address
weight|uint64|multiple signature account owner weight 



#### 7. Get Validated Weight Information of Specified Transaction：

> Request message

```
request: http.post
{
    "jsonrpc":"2.0",
    "id":int32,
    "method":"Chain33.Query",
    "params":[{"execer" : "multisig",
               "funcName" : "MultiSigTxConfirmedWeight",
               "payload" : {"multiSigAddr":string,txId":uint64}}]
}

```
> Parameter description：

Parameter|Type|Description
---|---|---
multiSigAddr|string|multiple signature account address 
txId|uint64|multiple signature account transaction index value，0 <= fromTxId < MultiSigAccTxCount number of transactions acquired

> Response data：

```
{
   "id" : 0,
   "error" : null,
   "result" :{
    "data": 20
	}
}
```

Parameter description：

Parameter|Type|Description
---|---|---
data|uint64|multiple signature account weight of the confirmed transaction 