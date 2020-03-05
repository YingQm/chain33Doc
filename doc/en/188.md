## 1 Interface Contract

- All RPC interfaces are HTTP protocols.
- All the data transmitted by the message are in JSON format.
- The RPC interfaces of this system are all POST method requests.

### 1.1 Request Format
**Request message structure:**
```json
{
    "jsonrpc":"2.0",
    "id":int32,
    "method":"Chain33.Method",
    "params":[]
}
```

**Description of each parameter:**

|Parameter|Type|If Necessary|Description|
|----|----|----|----|
|id|int32|yes|interface id temporarily out of use|
|method|string|yes|requested method name of RPC|
|params|array|no|additional parameter, default to null|


### 1.2 Response Format
**Response message structure:**
```json
{
    "id":int32,
    "result":{},
    "error":null
}
```
**Description of each parameter:**

|Parameter|Type|Description|
|----|----|----|
|id|int32|correspond to the request id|
|result|string or json|returned data ,different format returned by different methods,pure string or data in json format|
|error|string|fill in error information on error, empty when there is no error|
