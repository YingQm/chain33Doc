## 1 Balance Inquiry
[TOC]
### 1.1 Query Address Balance

#### Request Message Format 1
```json
Request message:
{
    "id":int32,
    "method":"Chain33.GetBalance",
    "params":[
		{
			"addresses":[
				"string"
			],
			"execer":"string"
		}
	]
}
```
**Parameter description：**

|Parameter|Type|If Necessary|Description|
|----|----|----|----|
|addresses|[]string|yes|list of addresses to query|
|execer|string|yes| actuator name, the coins query for the available main tokens, and the ticket query for the main tokens being mined|

#### Request Message Format 2
```json
Request message:
{
    "id":int32,
    "method":"Chain33.GetBalance",
    "params":[
		{
			"addresses":[
				"string"
			],
			"execer":"string",
			"asset_exec": "string",
			"asset_symbol" : "string"
		}
	]
}
```
**Parameter description：**

|Parameter|Type|If Necessary|Description|
|----|----|----|----|
|addresses|[]string|yes|list of addresses to query|
|execer|string|yes|actuator name, name of the contract on which the asset is located|
|asset_exec|string|yes| original contract name of the asset, such as bty generated in coins contract，tokens are generated in the token contract, assets across the chain in the paracross contract|
|asset_symbol|string|yes|asset name,such as bty, various symbol of token. bty across the chain is called coins.bty, token across the chain is called token.symbol |

#### Response message
```json
Response message：
{
    "id":int32,
    "result":[
		{
			"currency":int32,
			"balance":int64,
			"frozen":int64,
			"addr":"string"
		}
	],
    "error":null
}
```
**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|currency|int32|currency type, 0 is bty|
|balance|int64|available balance of account|
|frozen|int64|frozen balance of the account|
|addr|string|account address|
### 1.2 Query Address token Balance
```json
Request message:
{
    "id":int32,
    "method":"token.GetTokenBalance",
    "params":[
		{
			"addresses":[
				"string"
			],
			"execer":"string",
			"tokenSymbol":"string"
		}
	]
}
```
**Parameter description：**

|Parameter|Type|If Necessary|Description|
|----|----|----|----|
|addresses|[]string|yes|list of addresses to query|
|execer|string|yes| token queries the available balance, trade queries the token in the trading contract, if it is querying the balance on the parallel chain, then need to specify an executor execer for a specific parallel chain, for example：user.p.xxx.token .|
|tokenSymbol|string|yes|token symbol name|

```json
Response message:
{
    "id":int32,
    "result":
		{
			"currency":int32,
			"balance":int64,
			"frozen":int64,
			"addr":"string"
		}
	],
    "error":null
}
```
**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|currency|int32|currency type, 0 is bty|
|balance|int64|available balance of account|
|frozen|int64|frozen balance of the account|
|addr|string|account address|

### 1.3 Check Address Balance of All Contract Addresses
```json
Request message:
{
    "id":int32,
    "method":"Chain33.GetAllExecBalance",
    "params":[
		{
			"addr":"string"
		}
	]
}
```
**Parameter description：**

|Parameter|Type|If Necessary|Description|
|----|----|----|----|
|addr|string|yes|addresses to query|

```json
Response message:
{
    "id":int32,
    "result":[
		{
			"addr":"string",
			"ExecAccount":[
				{
					"Execer":"string",
					"Account":{
						"currency":int32,
						"balance":int64,
						"frozen":int64,
						"addr":"string"
					}
				}
			]
		}
	],
    "error":null
}
```
**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|addr|string|account address|
|ExecAccount.Execer|string|actuator name|
|ExecAccount.Account|json|account balance information|