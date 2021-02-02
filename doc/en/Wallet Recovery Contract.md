# Wallet Recovery Contract
[TOC]
### 1 Generated Transaction (unsigned)
#### 1.1 Backup Main Address CreateRawRetrieveBackupTx
**Request message：**
```json
request: http.post
{
    "jsonrpc":"2.0",
    "method":"retrieve.CreateRawRetrieveBackupTx",
    "params":[{"backupAddr":"1E5saiXVb9mW8wcWUUZjsHJPZs5GmdzuSY","defaultAddr":"14KEKbYtKKQm4wMthSK9J4La4nAiidGozt","delayPeriod": 61}]
}
```
**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|backupAddr|string|backup address|
|defaultAddr|string|main account address|
|delayPeriod|int32|delay period|

**Response message:**
```json
response:
{
  "id": int32,
  "result": "string",
  "error": null
}
```
**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|result|string|hexadecimal encoded transaction strings|

#### 1.2 Backup Address Preparation CreateRawRetrievePrepareTx
**Request message：**
```json
request: http.post
{
    "jsonrpc":"2.0",
    "method":"retrieve.CreateRawRetrievePrepareTx",
    "params":[{"backupAddr":"1E5saiXVb9mW8wcWUUZjsHJPZs5GmdzuSY","defaultAddr":"14KEKbYtKKQm4wMthSK9J4La4nAiidGozt"}]
}
```
**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|backupAddr|string|backup address|
|defaultAddr|string|main account address|

**Response message:**
```json
response:
{
  "id": int32,
  "result": "string",
  "error": null
}
```

**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|result|string|hexadecimal encoded transaction strings|

#### 1.3 Backup Address Take Effect CreateRawRetrievePerformTx
**Request message：**
```json
request: http.post
{
    "jsonrpc":"2.0",
    "method":"retrieve.CreateRawRetrievePerformTx",
    "params":[{"backupAddr":"1E5saiXVb9mW8wcWUUZjsHJPZs5GmdzuSY","defaultAddr":"14KEKbYtKKQm4wMthSK9J4La4nAiidGozt"}]
}
```
**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|backupAddr|string|backup address|
|defaultAddr|string|main account address|

**Response message:**
```json
response:
{
  "id": int32,
  "result": "string",
  "error": null
}
```

**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|result|string|hexadecimal encoded transaction strings|

#### 1.4 Cancel the Backup (Ready but not yet in effect) CreateRawRetrieveCancelTx
**Request message：**
```json
request: http.post
{
    "jsonrpc":"2.0",
    "method":"retrieve.CreateRawRetrieveCancelTx",
    "params":[{"backupAddr":"1E5saiXVb9mW8wcWUUZjsHJPZs5GmdzuSY","defaultAddr":"14KEKbYtKKQm4wMthSK9J4La4nAiidGozt"}]
}
```
**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|backupAddr|string|backup address|
|defaultAddr|string|main account address|

**Response message:**
```json
response:
{
  "id": int32,
  "result": "string",
  "error": null
}
```

**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|result|string|hexadecimal encoded transaction strings|

### 2 Status Query
#### 2.1 Query Backup Address Status 
**Request message：**
```json
request: http.post
requst
{
    "jsonrpc":"2.0",
    "method":"Chain33.Query",
    "params":[
    {
        "execer":"retrieve",
        "funcName":"GetRetrieveInfo",
        "payload":{
            "backupAddress":"1E5saiXVb9mW8wcWUUZjsHJPZs5GmdzuSY", 
            "defaultAddress":"14KEKbYtKKQm4wMthSK9J4La4nAiidGozt"
        }
    }]
}
```
**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|execer|string|actuators name|
|funcName|string|query function name|
|backupAddr|string|backup address|
|defaultAddr|string|main account address|
 
 **Response message:**
```json
response:
{
    "id":int32,
    "result":
    {
        "backupAddress":"1EDnnePAZN48aC2hiTDzhkczfF39g1pZZX",
        "defaultAddress":"1PUiGcbsccfxW3zuvHXZBJfznziph5miAo",
        "delayPeriod":"61",
        "prepareTime":"0",
        "remainTime":"0",
        "status":3
    },
    "error":null
}
```

**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|backupAddress|string|backup address|
|defaultAddress|string|main account address|
|delayPeriod|string|delay period|
|prepareTime|string|prepare time|
|remainTime|string|time of remaining in effect|
|status|int32|current status (1: the address is backed up; 2: the backup address is ready to take effect; 3: the backup address is effective)|
