[TOC]
# Part 1: Interface Description
## 1 Event Publishing
### 1.1 Transaction Generates the Published Event（unsigned）

**Request message:**

```json
{
   "jsonrpc":"2.0",
  "method": "Chain33.CreateTransaction",
  "params": [
    {
      "execer": "oracle",
      "actionName": "EventPublish",
      "payload": {
        "type": "string",
        "subType": "string",
        "time": int64,
        "content": "string",
        "introduction": "string"
      }
    }
  ],
  "id": int32
}
```
**Parameter description:**

|Parameter|Type|Description|
|----|----|----|
|type|string|event type|
|subType|string|event subtype|
|time|int64|estimated time of result publication, UTC time|
|content|string|event content, may represent in json format|
|introduction|string|event introduction|

**Response message:**

```json
{
  "id": int32,
  "result": "string",
  "error": null
}
```

**Parameter description:**

|Parameter|Type|Description|
|----|----|----|
|result|string|hexadecimal encoded transaction strings|

**Example**
Request:
```json
{
  "method": "Chain33.CreateTransaction",
  "params": [
    {
      "execer": "oracle",
      "actionName": "EventPublish",
      "payload": {
        "type": "football",
        "subType": "Premier League",
        "time": 1548084600,
        "content": "test",
        "introduction": "test2"
      }
    }
  ],
  "id": 0
}
```
Response:
```json
{
  "id": 0,
  "result": "0a066f7261636c65123138010a2d1208666f6f7462616c6c1a0e5072656d696572204c656167756520f8ca97e2052a04746573743205746573743220a08d06309a95a2ce81b6aabf1d3a22314350794a7152427a4c4b537a504c44416845454d64666f53464450513965477448",
  "error": null
}
```

### 1.2 Transaction Signature (TSIG) SignRawTx

**Request message**

```json
{
  "method": "Chain33.SignRawTx",
  "params": [
    {
      "addr": "14KEKbYtKKQm4wMthSK9J4La4nAiidGozt",
      "txHex": "0a066d616e61676512410a3f0a146f7261636c652d7075626c6973682d6576656e74122231344b454b6259744b4b516d34774d7468534b394a344c61346e41696964476f7a741a0361646420a08d0630f98bbebaaae3dfe8183a223151344e687572654a784b4e4266373164323642394a336642516f5163666d657a32",
      "expire": "120s"
    }
  ],
  "id": 0
}
```

**Parameter description**

|Parameter|Type|Description|
|----|----|----|
|addr|string|select only one parameter to input  between addr and privkey is permitted, but if addr is used then it relies on the private key signature stored in the wallet|
|privkey|string|select only one parameter to input between addr and privkey is permitted, but if privkey is used then directly sign|
|txHex|string|the original transaction data generated in the previous step|
|expire|string|expiration time may be input as "300ms"，"-1.5h" or "2h45m"，and units of effective time are "ns", "us" (or "µs"), "ms", "s", "m", "h"|

**Response message**

```json
{
  "id": 0,
  "result": "0a066d616e61676512410a3f0a146f7261636c652d7075626c6973682d6576656e74122231344b454b6259744b4b516d34774d7468534b394a344c61346e41696964476f7a741a036164641a6d0801122102504fa1c28caaf1d5a20fefb87c50a49724ff401043420cb3ba271997eb5a43871a463044022027c7ba260166723b65e3b94e3ea8df3692740005a37060031cbc2064a30cebfe022058f5dda61e133005fc87b90fc1f46b0f18b9c172873d6b44a0d9bcf23986f62320a08d06288be0e2e00530f98bbebaaae3dfe8183a223151344e687572654a784b4e4266373164323642394a336642516f5163666d657a32",
  "error": null
}
```

**Parameter description:**

|Parameter|Type|Description|
|----|----|----|
|result|string|hexadecimal string after the transaction has been signed|

### 1.3 Transaction Sending SendTransaction

**Response message**
```json
{
  "method": "Chain33.SendTransaction",
  "params": [
    {
      "data": "0a066d616e61676512410a3f0a146f7261636c652d7075626c6973682d6576656e74122231344b454b6259744b4b516d34774d7468534b394a344c61346e41696964476f7a741a036164641a6d0801122102504fa1c28caaf1d5a20fefb87c50a49724ff401043420cb3ba271997eb5a43871a463044022027c7ba260166723b65e3b94e3ea8df3692740005a37060031cbc2064a30cebfe022058f5dda61e133005fc87b90fc1f46b0f18b9c172873d6b44a0d9bcf23986f62320a08d06288be0e2e00530f98bbebaaae3dfe8183a223151344e687572654a784b4e4266373164323642394a336642516f5163666d657a32"
    }
  ],
  "id": 0
}
```
**Parameter description**

|Parameter|Type|Description|
|----|----|----|
|data|string|transaction data signed in the previous step|

**Response message**
```json
{
  "id": 0,
  "result": "0x06fc2a38f886027e115c5e278d2d598bba26a0d3066dc881bdac6069753c906a",
  "error": null
}
```

**Parameter description**

|Parameter|Type|Description|
|----|----|----|
|result|string|transaction hash generated after the transaction has send（can be used to query transaction status and history)|

## 2 Abort Event
### 2.1 Generate Event-Aborted Transaction（unsigned）

**Response message**
```json
{
  "method": "Chain33.CreateTransaction",
  "params": [
    {
      "execer": "oracle",
      "actionName": "EventAbort",
      "payload": {
        "eventID": "0x2edd12dee5724526d06517ce52704470b24b89dc918497d62c152dcfe8ddd5fd"
      }
    }
  ],
  "id": 0
}
```
**Parameter description**

|Parameter|Type|Description|
|----|----|----|
|eventID|string|event ID of the published event|

**Response message**
```json
{
  "id": 0,
  "result": "0a066f7261636c65124838041244124230783265646431326465653537323435323664303635313763653532373034343730623234623839646339313834393764363263313532646366653864646435666420a08d0630f38a8189ec8694c7133a22314350794a7152427a4c4b537a504c44416845454d64666f53464450513965477448",
  "error": null
}
```

**Parameter description**

|Parameter|Type|Description|
|----|----|----|
|result|string|hexadecimal encoded transaction strings|

## 3 Pre-publish Event Results
### 3.1 Create Transaction of the Pre-Published Event Results（unsigned）

**Response message**
```json
{
  "method": "Chain33.CreateTransaction",
  "params": [
    {
      "execer": "oracle",
      "actionName": "ResultPrePublish",
      "payload": {
        "eventID": "0xfa3e8d786df3085e71bcff1615847d2f353c45545724c785a9729db1c6106b13",
        "source": "............",
        "result": "0:0"
      }
    }
  ],
  "id": 0
}
```

**Parameter description**

|Parameter|Type|Description|
|----|----|----|
|eventID|string|event ID of the published event|
|source|string|source of the published results, such as a sports channel|
|result|string|result of the published event, such as match scores|

**Response message**
```json
{
  "id": 0,
  "result": "0a066f7261636c65125b38021a5712423078666133653864373836646633303835653731626366663136313538343764326633353363343535343537323463373835613937323964623163363130366231331a0ce696b0e6b5aae4bd93e882b22203303a3020a08d0630c5a8c388cc82fc954f3a22314350794a7152427a4c4b537a504c44416845454d64666f53464450513965477448",
  "error": null
}
```

**Parameter description**

|Parameter|Type|Description|
|----|----|----|
|result|string|hexadecimal encoded transaction strings|

## 4 Abort Result of Pre-Published Event
### 4.1 Generates Transactions that Abort Pre-Published Result (unsigned）

**Response message**
```json
{
  "method": "Chain33.CreateTransaction",
  "params": [
    {
      "execer": "oracle",
      "actionName": "ResultAbort",
      "payload": {
        "eventID": "0x1c3dc77998a4efa1b3b3bd527b83714da8c6b668d26002f06de6144277cb6ddd"
      }
    }
  ],
  "id": 0
}
```

**Parameter description**

|Parameter|Type|Description|
|----|----|----|
|eventID|string|event ID of published event|

**Response message**
```json
{
  "id": 0,
  "result": "0a066f7261636c65124838052a44124230783163336463373739393861346566613162336233626435323762383337313464613863366236363864323630303266303664653631343432373763623664646420a08d0630f8ae9da2a9c198b3113a22314350794a7152427a4c4b537a504c44416845454d64666f53464450513965477448",
  "error": null
}
```
**Parameter description**

|Parameter|Type|Description|
|----|----|----|
|result|string|hexadecimal encoded transaction strings|

## 5 Formal Publish of Event Results
### 5.1Generate a Formal Publish Event Result of Transaction（unsigned）

**Response message**
```json
{
  "method": "Chain33.CreateTransaction",
  "params": [
    {
      "execer": "oracle",
      "actionName": "ResultPublish",
      "payload": {
        "eventID": "0xd0181ccc942c72d1a2d1bd10c520751fc743693c8131e59119063b324fa96796",
        "source": "............",
        "result": "1:1"
      }
    }
  ],
  "id": 0
}
```

**Parameter description**

|Parameter|Type|Description|
|----|----|----|
|eventID|string|event ID of published event|
|source|string|source of the published results, such as a sports channel|
|result|string|result of the published event, such as match scores|

**Response message**
```json
{
  "id": 0,
  "result": "0a066f7261636c65125b3803225712423078643031383163636339343263373264316132643162643130633532303735316663373433363933633831333165353931313930363362333234666139363739361a0ce6909ce78b90e4bd93e882b22203313a3120a08d0630989ee891e7f987a0353a22314350794a7152427a4c4b537a504c44416845454d64666f53464450513965477448",
  "error": null
}
```

**Parameter description**

|Parameter|Type|Description|
|----|----|----|
|result|string|hexadecimal encoded transaction strings|

## 6 Query Interface
### 6.1 Query Status by Event ID of Published Event 

**Response message**
```json
{
  "method": "Chain33.Query",
  "params": [
    {
      "execer": "oracle",
      "funcName": "QueryOraclesByIDs",
      "payload": {
        "eventID": [
          "0xd0181ccc942c72d1a2d1bd10c520751fc743693c8131e59119063b324fa96796"
        ]
      }
    }
  ],
  "id": 0
}
```

**Parameter description**

|Parameter|Type|Description|
|----|----|----|
|eventID|json|array of event IDs that need to query information|

**Response message**
```json
{
  "id": 0,
  "result": {
    "status": [
      {
        "eventID": "0xd0181ccc942c72d1a2d1bd10c520751fc743693c8131e59119063b324fa96796",
        "addr": "14KEKbYtKKQm4wMthSK9J4La4nAiidGozt",
        "type": "football",
        "subType": "Premier League",
        "time": "1548084600",
        "content": "test007",
        "introduction": "test007-intr",
        "status": {
          "opAddr": "14KEKbYtKKQm4wMthSK9J4La4nAiidGozt",
          "status": 5
        },
        "source": "............",
        "result": "1:1",
        "preStatus": {
          "opAddr": "14KEKbYtKKQm4wMthSK9J4La4nAiidGozt",
          "status": 3
        }
      }
    ]
  },
  "error": null
}
```

**Parameter description**

|Parameter|Type|Description|
|----|----|----|
|status.eventID|string|event ID|
|status.addr|string|event address|
|status.type|string|event type|
|status.subType|string|sub-type of the published event|
|status.time|int64|estimated time of result publication, UTC time|
|status.content|string|event content, may represent in json format|
|status.introduction|string|event introduction|
|status.status|json|current status, including operator address, current status value;0: initial state, 1: event published, 2: event cancelled, 3: event result pre-published, 4: event pre-published result cancelled, 5: event result published|
|status.source|string|source of the published results, such as a sports channel|
|status.result|string|published event results, such as game scores|
|status.preStatus|json|previous state, including operator address and current state value|

### 6.2 Query Status by Event ID of Event Status

**Response message:**
```json
{
  "method": "Chain33.Query",
  "params": [
    {
      "execer": "oracle",
      "funcName": "QueryEventIDsByStatus",
      "payload": {
        "status": 4,
        "addr": "",
        "type": "",
        "eventID": ""
      }
    }
  ],
  "id": 0
}
```

**Parameter description:**

|Parameter|Type|If Necessary|Description|
|----|----|----|----|
|status|int32|yes|event status|
|addr|string|no||
|type|string|no|event type|
|eventID|string|depends on the case|eventID, the first query is empty, if the number of results is more than one page, set eventID to the last ID of the last query result, so as to find the data of the next page|

**Response message:**
```json
{
  "id": 0,
  "result": {
    "eventID": [
      "0x45aca020ca26b2e0f92590c0662978194221a6b791a97e748f599221df3f2786",
      "0x437d5ca35bbc78a8bdf72978c018270883a923fce38664be0de1e6dc569e277f"
    ]
  },
  "error": null
}
```

**Parameter description:**

|Parameter|Type|Description|
|----|----|----|
|eventID|json|array of event IDs that matches the criteria|

### 6.3 Query the Event ID Based on the User Address Where the Event was Created and the Status of the Event
**Response message**
```json
{
  "method": "Chain33.Query",
  "params": [
    {
      "execer": "oracle",
      "funcName": "QueryEventIDsByAddrAndStatus",
      "payload": {
        "status": 2,
        "addr": "14KEKbYtKKQm4wMthSK9J4La4nAiidGozt",
        "type": "",
        "eventID": ""
      }
    }
  ],
  "id": 0
}
```

**Parameter description**

|Parameter|type|If Necessary|Description|
|----|----|----|----|
|status|int32|yes|event status|
|addr|string|no|the address where creates the event|
|type|string|no|event type|

**Response message**
```json
{
  "id": 0,
  "result": {
    "eventID": [
      "0xdd6b4ebfb7560e803cc4500490d2b7e6818296eed19d938446f2230eaa04a5e1",
      "0x1aae4290800019f6ba97ac45acba334aa919faff1a37c4adffce5eb12c6d3a06",
      "0x2edd12dee5724526d06517ce52704470b24b89dc918497d62c152dcfe8ddd5fd"
    ]
  },
  "error": null
}
```

**Parameter description**

|Parameter|Type|Description|
|----|----|----|
|eventID|json|array of event IDs that matches the criteria|
### 6.4 Query the Event ID Based on the Type of Created Event and the State of the Event

**Response message**
```json
{
  "method": "Chain33.Query",
  "params": [
    {
      "execer": "oracle",
      "funcName": "QueryEventIDsByTypeAndStatus",
      "payload": {
        "status": 1,
        "addr": "",
        "type": "football",
        "eventID": ""
      }
    }
  ],
  "id": 0
}
```

**Parameter description**

|Parameter|Type|If Necessary|Description|
|----|----|----|----|
|status|int32|yes|event status|
|addr|string|no|the address where creates the event|
|type|string|yes|event type|
|eventID|string|depends on the case|eventID, the first query is empty, if the number of results is more than one page, set eventID to the last ID of the last query result, so as to find the data of the next page|
**Response message**
```json
{
  "id": 0,
  "result": {
    "eventID": [
      "0xdd6b4ebfb7560e803cc4500490d2b7e6818296eed19d938446f2230eaa04a5e1",
      "0x1aae4290800019f6ba97ac45acba334aa919faff1a37c4adffce5eb12c6d3a06",
      "0x2edd12dee5724526d06517ce52704470b24b89dc918497d62c152dcfe8ddd5fd"
    ]
  },
  "error": null
}
```

**Parameter description**

|Parameter|Type|Description|
|----|----|----|
|eventID|json|array of event IDs that matches the criteria|