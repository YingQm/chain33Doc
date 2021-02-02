## 1 Mempool Interface
[TOC]
### 1.1 GetMempool
**Request message:**
```json
{
     "jsonrpc":"2.0",
     "id":int32,
     "method":"Chain33.GetMempool",
     "params":[]
}
```

**Response message:**
```json
{
    "id":int32,
    "result":
    {
        "txs":
        [
            {
                "execer":"string",
                "payload":"string",
                "fee":int64,
                "feefmt":"string",
                "amount":int64,
                "amountfmt":"string",
                "expire":int64,
                "nonce":int64,
                "to":"string",
                "signature":{"ty":int32,"pubkey":"string","signature":"string"}
            }
        ]
    }
}
```
**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|txs|array|list of transactions in the cache|
|execer|string|actuator name|
|payload|string|raw load in the transaction|
|fee|int64|this transaction fee, original unit, conversion relationship with the base currency unit is 10^8|
|feefmt|string|transaction fee for human readable string|
|amount|int64|amount of this transaction|
|amountfmt|string|this transaction amount for human readable string|
|expire|int32|transaction expiration time|
|nonce|int32|transaction identification code|
|to|string|destination address|
|signature|-|transaction signature|
