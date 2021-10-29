# autonomy 接口
[TOC]
## 1 自治系统参数默认值以及范围
### 1.1 可修改参数：
```
    // 默认公示周期,以区块高度计算,换算成时间大概一周
    publicPeriod         int32 = 17280 * 7  
    // 最小公示周期
	minPublicPeriod      int32 = 17280 * 7
	// 最大公示周期
	maxPublicPeriod      int32 = 17280 * 14
	
    // 默认重大项目公示金阈值
	largeProjectAmount         = types.Coin * 100 * 10000 
	// 最小重大项公示金目阈值
	minLargeProjectAmount      = types.Coin * 100 * 10000
	// 最大重大项公示金目阈值
	maxLargeProjectAmount      = types.Coin * 300 * 10000
	
	// 默认提案金
	proposalAmount             = types.Coin * 500         
	// 最小提案金
	minProposalAmount          = types.Coin * 20
	// 最大提案金
	maxProposalAmount          = types.Coin * 2000
	
	// 默认董事会成员赞成率，以%计
	boardApproveRatio   int32 = 51                       
	// 最小董事会赞成率
	minBoardApproveRatio      = 50
	// 最大董事会赞成率
	maxBoardApproveRatio      = 66
	
	// 默认全体持票人否决率，以%计
	pubOpposeRatio      int32 = 33                     
	// 最小全体持票人否决率
	minPubOpposeRatio   int32 = 33
	// 最大全体持票人否决率
	maxPubOpposeRatio   int32 = 50
	
	// 可以调整，但是可能需要进行范围的限制：参与率最低设置为 50%， 最高设置为 80%，赞成率，最低 50.1%，最高80%
	// 不能设置太低和太高，太低就容易作弊，太高则有可能很难达到
	// 最小全体持票人参与率
	minPubAttendRatio = 50
	// 最大全体持票人参与率
	maxPubAttendRatio = 80

	// 最小全体持票人赞成率
	minPubApproveRatio = 50
	// 最大全体持票人赞成率
	maxPubApproveRatio = 80
```
### 1.2 不可修改参数：
```
    // 董事会成员数范围
    minBoards                 = 20
	maxBoards                 = 40                  
```

## 1 提案董事会成员
### 1.1 proposal board

**请求报文：**
```json
{
    "jsonrpc":"2.0",
    "method": "Chain33.CreateTransaction",
    "params": [
        {
            "execer": "autonomy",
            "actionName": "PropBoard",
            "payload": {
                "year" : 2019,
                "month" : 8,
                "day" : 29,
                "update" : false,
                "boards" : ["14KEKbYtKKQm4wMthSK9J4La4nAiidGozt", "1EbDHAXpoiewjPLX9uqoz38HsKqMXayZrF", "1KcCVZLSQYRUwE5EXTsAoQs9LuJW6xwfQa"],
                "startBlockHeight" : 100,
                "endBlockHeight" : 1000,
                "realEndBlockHeight" : 0
            }
        }    
    ]
}
```
**参数说明：**

|参数|类型|是否必须|说明|
|----|----|----|----|
|year|int32|否|提案年|
|month|int32|否|提案月|
|day|int32|否|提案日|
|update|bool|否|替换或者更新boards；替换(false); 更新(true)|
|boards|[]string|是|提案董事会成员|
|startBlockHeight|int64|是|开始投票高度|
|endBlockHeight|int64|是|结束投票高度|
|realEndBlockHeight|int64|否|实际投票结束高度，不需要填写|

* endBlockHeight > startBlockHeight + 720 (自治系统中所有涉及提案都需要满足)

**响应报文：**
```json
{
    "id": int32,
    "result": "string",
    "error": null
}
```
**参数说明：**

|参数|类型|说明|
|----|----|----|
|result|string|交易十六进制编码后的字符串|

### 1.2 revoke proposal board

**请求报文：**
```json
{
    "jsonrpc":"2.0",
    "method": "Chain33.CreateTransaction",
    "params": [
        {
            "execer": "autonomy",
            "actionName": "RvkPropBoard",
            "payload": {
                "proposalID" : "0x5047974ad5b275d5173367b76cea1d9509fd669e266c8456a1c12f14b347e7dd"
            }
        }
    ]
}
```
**参数说明：**

|参数|类型|是否必须|说明|
|----|----|----|----|
|proposalID|string|是|提案ID，即PropBoard的交易hash|

**响应报文：**
```json
{
    "id": int32,
    "result": "string",
    "error": null
}
```
**参数说明：**

|参数|类型|说明|
|----|----|----|
|result|string|交易十六进制编码后的字符串|

### 1.3 vote proposal board

**请求报文：**
```json
{
    "jsonrpc":"2.0",
    "method": "Chain33.CreateTransaction",
    "params": [
        {
            "execer": "autonomy",
            "actionName": "VotePropBoard",
            "payload": {
                "proposalID" : "0x5047974ad5b275d5173367b76cea1d9509fd669e266c8456a1c12f14b347e7dd",
                "approve": true,
                "originAddr": ["14KEKbYtKKQm4wMthSK9J4La4nAiidGozt", "1EbDHAXpoiewjPLX9uqoz38HsKqMXayZrF", "1KcCVZLSQYRUwE5EXTsAoQs9LuJW6xwfQa"]
            }
        }
    ]
}
```
**参数说明：**

|参数|类型|是否必须|说明|
|----|----|----|----|
|proposalID|string|是|提案ID，即PropBoard的交易hash|
|approve|bool|是|是否同意该提案，true：同意；false: 不同意|
|originAddr|[]string|否|如果有绑定挖矿的可以将挖矿地址填入进行投票|

**响应报文：**
```json
{
    "id": int32,
    "result": "string",
    "error": null
}
```
**参数说明：**

|参数|类型|说明|
|----|----|----|----|
|result|string|交易十六进制编码后的字符串|

### 1.4 terminate proposal board

**请求报文：**
```json
{
    "jsonrpc":"2.0",
    "method": "Chain33.CreateTransaction",
    "params": [
        {
            "execer": "autonomy",
            "actionName": "TmintPropBoard",
            "payload": {
                "proposalID" : "0x5047974ad5b275d5173367b76cea1d9509fd669e266c8456a1c12f14b347e7dd"
            }
        }
    ]
}
```
**参数说明：**

|参数|类型|是否必须|说明|
|----|----|----|----|
|proposalID|string|是|提案ID，即PropBoard的交易hash|

**响应报文：**
```json
{
    "id": int32,
    "result": "string",
    "error": null
}
```
**参数说明：**

|参数|类型|说明|
|----|----|----|----|
|result|string|交易十六进制编码后的字符串|

### 1.5 query proposal board
#### 1.5.1 通过proposalID查询提案
**请求报文：**
```json
{
    "method": "Chain33.Query",
    "params": [
        {
            "execer": "autonomy",
            "funcName": "GetProposalBoard",
            "payload": {
                "data" : "0x5047974ad5b275d5173367b76cea1d9509fd669e266c8456a1c12f14b347e7dd"
            }
        }
    ]
}
```
**参数说明：**

|参数|类型|是否必须|说明|
|----|----|----|----|
|data|string|是|提案ID，即PropBoard的交易hash|

#### 1.5.2 通过状态或者地址以及状态地址查询提案

**请求报文：**
```json
{
    "method": "Chain33.Query",
    "params": [
        {
            "execer": "autonomy",
            "funcName": "ListProposalBoard",
            "payload": {
                "status" : 1,
                "addr" : "", 
                "count" : 1,
                "direction" : 0,
                "height" : -1,
                "index" : -1
            }
        }
    ]
}
```
**参数说明：**

|参数|类型|是否必须|说明|
|----|----|----|----|
status|int32|是|提案状态
addr|string|否|提案地址
count|int32|是|查询数量
direction|int32|是|查询方向，0降序 1升序
height|int64|否|查询量大翻页查询时候需要输入从某个高度开始
index|int32|否|查询量大翻页查询时候需要输入从某个index开始

* status 1-提案状态 2-提案撤销状态 3-投票状态 4-提案结束状态

**响应报文：**
```json
{
    "id": int32,
    "result": {
      "propBoards" : [
        {
            "propBoard": {
                "year" : 2019,
                "month" : 8,
                "day" : 29,
                "boards" : ["14KEKbYtKKQm4wMthSK9J4La4nAiidGozt", "1EbDHAXpoiewjPLX9uqoz38HsKqMXayZrF", "1KcCVZLSQYRUwE5EXTsAoQs9LuJW6xwfQa"],
                "startBlockHeight" : 100,
                "endBlockHeight" : 1000
            },
            "curRule": {
                "boardApproveRatio" : 66,
                "pubOpposeRatio" : 33,
                "proposalAmount" : 10000000,
                "largeProjectAmount" : 100000000,
                "publicPeriod" : 120960
            },
            "board" : {
                "boards" : ["12cjnN5D4DPdBQSwh6vjwJbtsW4EJALTMv","1Luh4AziYyaC5zP3hUXtXFZS873xAxm6rH"],
                "revboards" : ["1NNaYHkscJaLJ2wUrFNeh6cQXBS4TrFYeB"],
                "amount" : 10000000,
                "startHeight" : 100
            },
            "voteResult": {
                "totalVotes" : 100,
                "approveVotes" : 70,
                "opposeVotes" : 20,
                "pass" : true
            },
            "status" : 1,
            "address" : "1EDnnePAZN48aC2hiTDzhkczfF39g1pZZX",
            "height" : 100,
            "index" : 1,
            "proposalID" : "0x5047974ad5b275d5173367b76cea1d9509fd669e266c8456a1c12f14b347e7dd"
        }
      ]
    },
    "error": null
}
```
**参数说明：**

|参数|类型|说明|
|----|----|----|----|
|propBoard|json|参见(1)|
|curRule.boardApproveRatio|int32|董事会赞成率|
|curRule.pubOpposeRatio|int32|全体持票人否决率|
|curRule.proposalAmount|int64|提案金|
|curRule.largeProjectAmount|int64|重大项目阈值|
|curRule.publicPeriod|int32|公示期|
|board.boards|[]string|有投票权的boards|
|board.revboards|[]string|无投票权的boards|
|board.amount|int64|该boards在当前周期已经审批的项目金|
|board.startHeight|int64|当前周期的起始区块高度|
|voteResult.totalVotes|int32|总票数|
|voteResult.approveVotes|int32|赞成票|
|voteResult.opposeVotes|int32|反对票|
|voteResult.pass|bool|是否通过，true-通过 false-未通过|
|status|int32|提案状态|
|address|string|提案地址|
|height|int64|提案高度|
|index|int32|提案index|
|proposalID|string|提案ID|

### 1.6 query active board

**请求报文：**
```json
{
    "method": "Chain33.Query",
    "params": [
        {
            "execer": "autonomy",
            "funcName": "GetActiveBoard",
            "payload": {
                "data" : "1"
            }
        }    
    ]
}
```
**参数说明：**

|参数|类型|是否必须|说明|
|----|----|----|----|
|data|string|是|"1"|

**响应报文：**
```json
{
    "id": int32,
    "result": {
        "boards" : ["12cjnN5D4DPdBQSwh6vjwJbtsW4EJALTMv","1Luh4AziYyaC5zP3hUXtXFZS873xAxm6rH"],
        "revboards" : ["1NNaYHkscJaLJ2wUrFNeh6cQXBS4TrFYeB"],
        "amount" : 10000000,
        "startHeight" : 100
    },
    "error": null
}
```
**参数说明：**

|参数|类型|说明|
|----|----|----|----|
|boards|[]string|有投票权的boards|
|revboards|[]string|无投票权的boards|
|amount|int64|该boards在当前周期已经审批的项目金|
|startHeight|int64|当前周期的起始区块高度|

## 2 提案项目
### 2.1 proposal project

**请求报文：**
```json
{
    "jsonrpc":"2.0",
    "method": "Chain33.CreateTransaction",
    "params": [
        {
            "execer": "autonomy",
            "actionName": "PropProject",
            "payload": {
                "year" : 2019,
                "month" : 8,
                "day" : 29,
                "firstStage" : "",
                "lastStage" : "",
                "production" : "",
                "description" : "",
                "contractor" : "",
                "amount" : 10000000,
                "amountDetail" : "",
                "toAddr" : "1EbDHAXpoiewjPLX9uqoz38HsKqMXayZrF",
                "startBlockHeight" : 100,
                "endBlockHeight" : 1000,
                "realEndBlockHeight" : 0,
                "projectNeedBlockNum" : 100000
            }
        }    
    ]
}
```
**参数说明：**

|参数|类型|是否必须|说明|
|----|----|----|----|
|year|int32|否|提案年|
|month|int32|否|提案月|
|day|int32|否|提案日|
|firstStage|string|否|第一阶段提案项目hash|
|lastStage|string|否|上一阶段提案项目hash|
|production|string|否|项目地址|
|description|string|否|项目阶段性简述|
|contractor|string|否|承包人|
|amount|int64|是|项目经费|
|amountDetail|string|否|经费细则|
|toAddr|string|是|收款地址|
|startBlockHeight|int64|是|开始投票高度|
|endBlockHeight|int64|是|结束投票高度|
|realEndBlockHeight|int64|否|实际投票结束高度，不需要填写|
|projectNeedBlockNum|int64|否|项目耗时预估（以区块计算）|

* endBlockHeight > startBlockHeight + 720 (自治系统中所有涉及提案都需要满足)

**响应报文：**
```json
{
    "id": int32,
    "result": "string",
    "error": null
}
```
**参数说明：**

|参数|类型|说明|
|----|----|----|----|
|result|string|交易十六进制编码后的字符串|

### 2.2 revoke proposal project

**请求报文：**
```json
{
    "jsonrpc":"2.0",
    "method": "Chain33.CreateTransaction",
    "params": [
        {
            "execer": "autonomy",
            "actionName": "RvkPropProject",
            "payload": {
                "proposalID" : "0x5047974ad5b275d5173367b76cea1d9509fd669e266c8456a1c12f14b347e7dd"
            }
        }
    ]
}
```
**参数说明：**

|参数|类型|是否必须|说明|
|----|----|----|----|
|proposalID|string|是|提案ID，即PropProject的交易hash|

**响应报文：**
```json
{
    "id": int32,
    "result": "string",
    "error": null
}
```
**参数说明：**

|参数|类型|说明|
|----|----|----|----|
|result|string|交易十六进制编码后的字符串|

### 2.3 vote proposal project

**请求报文：**
```json
{
    "jsonrpc":"2.0",
    "method": "Chain33.CreateTransaction",
    "params": [
        {
            "execer": "autonomy",
            "actionName": "VotePropProject",
            "payload": {
                "proposalID" : "0x5047974ad5b275d5173367b76cea1d9509fd669e266c8456a1c12f14b347e7dd",
                "approve": true
            }
        }
    ]
}
```
**参数说明：**

|参数|类型|是否必须|说明|
|----|----|----|----|
|proposalID|string|是|提案ID，即PropProject的交易hash|
|approve|bool|是|是否同意该提案，true：同意；false: 不同意|

**响应报文：**
```json
{
    "id": int32,
    "result": "string",
    "error": null
}
```
**参数说明：**

|参数|类型|说明|
|----|----|----|----|
|result|string|交易十六进制编码后的字符串|

### 2.4 pub vote proposal project

**请求报文：**
```json
{
    "jsonrpc":"2.0",
    "method": "Chain33.CreateTransaction",
    "params": [
        {
            "execer": "autonomy",
            "actionName": "PubVotePropProject",
            "payload": {
                "proposalID" : "0x5047974ad5b275d5173367b76cea1d9509fd669e266c8456a1c12f14b347e7dd",
                "oppose": true,
                "originAddr": ["14KEKbYtKKQm4wMthSK9J4La4nAiidGozt", "1EbDHAXpoiewjPLX9uqoz38HsKqMXayZrF", "1KcCVZLSQYRUwE5EXTsAoQs9LuJW6xwfQa"]
            }
        }
    ]
}
```
**参数说明：**

|参数|类型|是否必须|说明|
|----|----|----|----|
|proposalID|string|是|提案ID，即PropProject的交易hash|
|oppose|bool|是|是否反对该提案，true：反对；false: 不反对|
|originAddr|[]string|否|如果有绑定挖矿的可以将挖矿地址填入进行投票|

**响应报文：**
```json
{
    "id": int32,
    "result": "string",
    "error": null
}
```
**参数说明：**

|参数|类型|说明|
|----|----|----|----|
|result|string|交易十六进制编码后的字符串|

### 2.5 terminate proposal project

**请求报文：**
```json
{
    "jsonrpc":"2.0",
    "method": "Chain33.CreateTransaction",
    "params": [
        {
            "execer": "autonomy",
            "actionName": "TmintPropProject",
            "payload": {
                "proposalID" : "0x5047974ad5b275d5173367b76cea1d9509fd669e266c8456a1c12f14b347e7dd"
            }
        }
    ]
}
```
**参数说明：**

|参数|类型|是否必须|说明|
|----|----|----|----|
|proposalID|string|是|提案ID，即PropProject的交易hash|

**响应报文：**
```json
{
    "id": int32,
    "result": "string",
    "error": null
}
```
**参数说明：**

|参数|类型|说明|
|----|----|----|----|
|result|string|交易十六进制编码后的字符串|

### 2.5 query proposal project

#### 2.5.1 通过proposalID查询提案

**请求报文：**
```json
{
    "method": "Chain33.Query",
    "params": [
        {
            "execer": "autonomy",
            "funcName": "GetProposalProject",
            "payload": {
                "data" : "0x5047974ad5b275d5173367b76cea1d9509fd669e266c8456a1c12f14b347e7dd"
            }
        }
    ]
}
```
**参数说明：**

|参数|类型|是否必须|说明|
|----|----|----|----|
data|string|是|提案ID，即PropProject的交易hash

#### 2.5.2 通过状态或者地址以及状态地址查询提案

**请求报文：**
```json
{
    "method": "Chain33.Query",
    "params": [
        {
            "execer": "autonomy",
            "funcName": "ListProposalProject",
            "payload": {
                "status" : 1,
                "addr" : "", 
                "count" : 1,
                "direction" : 0,
                "height" : -1,
                "index" : -1
            }
        }
    ]
}
```
**参数说明：**

|参数|类型|是否必须|说明|
|----|----|----|----|
|status|int32|是|提案状态|
|addr|string|否|提案地址|
|count|int32|是|查询数量|
|direction|int32|是|查询方向，0降序 1升序|
|height|int64|否|查询量大翻页查询时候需要输入从某个高度开始|
|index|int32|否|查询量大翻页查询时候需要输入从某个index开始|

* status 1-提案状态 2-提案撤销状态 3-董事会投票状态 4-全体持票人投票状态 5-提案结束状态

**响应报文：**
```json
{
  "id": int32,
  "result": {
      "propProjects" : [
        {
            "propProject": {
                "year" : 2019,
                "month" : 8,
                "day" : 29,
                "projects" : ["14KEKbYtKKQm4wMthSK9J4La4nAiidGozt", "1EbDHAXpoiewjPLX9uqoz38HsKqMXayZrF", "1KcCVZLSQYRUwE5EXTsAoQs9LuJW6xwfQa"],
                "startBlockHeight" : 100,
                "endBlockHeight" : 1000
            },
            "curRule": {
                "boardApproveRatio" : 66,
                "pubOpposeRatio" : 33,
                "proposalAmount" : 10000000,
                "largeProjectAmount" : 100000000,
                "publicPeriod" : 120960
            },
            "boards" : ["", "", ""],
            "boardVoteRes": {
                "totalVotes" : 30,
                "approveVotes" : 20,
                "opposeVotes" : 10,
                "pass" : true
            },
            "pubVote" : {
                "publicity" : true,
                "totalVotes" : 100,
                "opposeVotes" : 10,
                "pubPass" : true
            },
            "status" : 1,
            "address" : "1EDnnePAZN48aC2hiTDzhkczfF39g1pZZX",
            "height" : 100,
            "index" : 1,
            "proposalID" : "0x5047974ad5b275d5173367b76cea1d9509fd669e266c8456a1c12f14b347e7dd"
        }
      ]
  },
  "error": null
}
```
**参数说明：**

|参数|类型|说明|
|----|----|----|----|
|propProject|json|参见(1)|
|curRule.boardApproveRatio|int32|董事会赞成率|
|curRule.pubOpposeRatio|int32|全体持票人否决率|
|curRule.proposalAmount|int64|提案金|
|curRule.largeProjectAmount|int64|重大项目阈值|
|curRule.publicPeriod|int32|公示期|
|boards|[]string|投票该提案的董事会成员|
|boardVoteRes.totalVotes|int32|总票数|
|boardVoteRes.approveVotes|int32|赞成票|
|boardVoteRes.opposeVotes|int32|反对票|
|boardVoteRes.pass|bool|是否通过，true-通过 false-未通过|
|pubVote.publicity|int32|全体持票数|
|pubVote.totalVotes|int32|赞成票|
|pubVote.opposeVotes|int32|反对票，反对票率决定是否通过|
|pubVote.pubPass|bool|最总是否通过，true-通过 false-未通过|
|status|int32|提案状态|
|address|string|提案地址|
|height|int64|提案高度|
|index|int32|提案index|
|proposalID|string|提案ID|

## 3 提案系统参数修改
### 3.1 proposal rule

**请求报文：**
```json
{
    "jsonrpc":"2.0",
    "method": "Chain33.CreateTransaction",
    "params": [
        {
            "execer": "autonomy",
            "actionName": "PropRule",
            "payload": {
                "year" : 2019,
                "month" : 8,
                "day" : 29,
                "ruleCfg" : {
                    "boardApproveRatio" : 66,
                    "pubOpposeRatio" : 33,
                    "proposalAmount" : 10000000,
                    "largeProjectAmount" : 100000000,
                    "publicPeriod" : 120960
                },
                "startBlockHeight" : 100,
                "endBlockHeight" : 1000,
                "realEndBlockHeight" : 0
            }
        }    
    ]
}
```
**参数说明：**

|参数|类型|是否必须|说明|
|----|----|----|----|
|year|int32|否|提案年|
|month|int32|否|提案月|
|day|int32|否|提案日|
|ruleCfg.boardApproveRatio|int32|否|董事会赞成率|
|ruleCfg.pubOpposeRatio|int32|否|全体持票人否决率|
|ruleCfg.proposalAmount|int64|否|提案金|
|ruleCfg.largeProjectAmount|int64|否|重大项目阈值|
|ruleCfg.publicPeriod|int32|否|公示期|
|startBlockHeight|int64|是|开始投票高度|
|endBlockHeight|int64|是|结束投票高度|
|realEndBlockHeight|int64|否|实际投票高度，不需要填写|

* endBlockHeight > startBlockHeight + 720 (自治系统中所有涉及提案都需要满足)

**响应报文：**
```json
{
    "id": int32,
    "result": "string",
    "error": null
}
```
**参数说明：**

|参数|类型|说明|
|----|----|----|----|
|result|string|交易十六进制编码后的字符串|

### 3.2 revoke proposal rule

**请求报文：**
```json
{
    "jsonrpc":"2.0",
    "method": "Chain33.CreateTransaction",
    "params": [
        {
            "execer": "autonomy",
            "actionName": "RvkPropRule",
            "payload": {
                "proposalID" : "0x5047974ad5b275d5173367b76cea1d9509fd669e266c8456a1c12f14b347e7dd"
            }
        }
    ]
}
```
**参数说明：**

|参数|类型|是否必须|说明|
|----|----|----|----|
|proposalID|string|是|提案ID，即PropRule的交易hash|

**响应报文：**
```json
{
    "id": int32,
    "result": "string",
    "error": null
}
```
**参数说明：**

|参数|类型|说明|
|----|----|----|
|result|string|交易十六进制编码后的字符串|

### 3.3 vote proposal rule

**请求报文：**
```json
{
    "jsonrpc":"2.0",
    "method": "Chain33.CreateTransaction",
    "params": [
        {
            "execer": "autonomy",
            "actionName": "VotePropRule",
            "payload": {
                "proposalID" : "0x5047974ad5b275d5173367b76cea1d9509fd669e266c8456a1c12f14b347e7dd",
                "approve": true,
                "originAddr": ["14KEKbYtKKQm4wMthSK9J4La4nAiidGozt", "1EbDHAXpoiewjPLX9uqoz38HsKqMXayZrF", "1KcCVZLSQYRUwE5EXTsAoQs9LuJW6xwfQa"]
            }
        }
    ]
}
```
**参数说明：**

|参数|类型|是否必须|说明|
|----|----|----|----|
|proposalID|string|是|提案ID，即PropRule的交易hash|
|approve|bool|是|是否同意该提案，true：同意；false: 不同意|
|originAddr|[]string|否|如果有绑定挖矿的可以将挖矿地址填入进行投票|

**响应报文：**
```json
{
    "id": int32,
    "result": "string",
    "error": null
}
```
**参数说明：**

|参数|类型|说明|
|----|----|----|----|
|result|string|交易十六进制编码后的字符串|

### 3.4 terminate proposal rule

**请求报文：**
```json
{
    "jsonrpc":"2.0",
    "method": "Chain33.CreateTransaction",
    "params": [
        {
            "execer": "autonomy",
            "actionName": "TmintPropRule",
            "payload": {
                "proposalID" : "0x5047974ad5b275d5173367b76cea1d9509fd669e266c8456a1c12f14b347e7dd"
            }
        }
    ]
}
```
**参数说明：**

|参数|类型|是否必须|说明|
|----|----|----|----|
|proposalID|string|是|提案ID，即PropRule的交易hash|

**响应报文：**
```json
{
    "id": int32,
    "result": "string",
    "error": null
}
```
**参数说明：**

|参数|类型|说明|
|----|----|----|----|
|result|string|交易十六进制编码后的字符串|

### 3.5 query proposal rule

#### 3.5.1 通过proposalID查询提案

**请求报文：**
```json
{
    "method": "Chain33.Query",
    "params": [
        {
            "execer": "autonomy",
            "funcName": "GetProposalRule",
            "payload": {
                "data" : "0x5047974ad5b275d5173367b76cea1d9509fd669e266c8456a1c12f14b347e7dd"
            }
        }
    ]
}
```
**参数说明：**

|参数|类型|是否必须|说明|
|----|----|----|----|
|data|string|是|提案ID，即PropRule的交易hash|

#### 3.5.2 通过状态或者地址以及状态地址查询提案

**请求报文：**
```json
{
    "method": "Chain33.Query",
    "params": [
        {
            "execer": "autonomy",
            "funcName": "ListProposalRule",
            "payload": {
                "status" : 1,
                "addr" : "", 
                "count" : 1,
                "direction" : 0,
                "height" : -1,
                "index" : -1
            }
        }
    ]
}
```
**参数说明：**

|参数|类型|是否必须|说明|
|----|----|----|----|
|status|int32|是|提案状态|
|addr|string|否|提案地址|
|count|int32|是|查询数量|
|direction|int32|是|查询方向，0降序 1升序|
|height|int64|否|查询量大翻页查询时候需要输入从某个高度开始|
|index|int32|否|查询量大翻页查询时候需要输入从某个index开始|

* status 1-提案状态 2-提案撤销状态 3-投票状态 4-提案结束状态

**响应报文：**
```json
{
  "id": int32,
  "result": {
      "propRules" : [
        {
            "propRule": {
                "year" : 2019,
                "month" : 8,
                "day" : 29,
                "ruleCfg" : {
                    "boardApproveRatio" : 66,
                    "pubOpposeRatio" : 33,
                    "proposalAmount" : 10000000,
                    "largeProjectAmount" : 100000000,
                    "publicPeriod" : 120960
                },
                "startBlockHeight" : 100,
                "endBlockHeight" : 1000,
                "realEndBlockHeight" : 900
            },
            "curRule": {
                "boardApproveRatio" : 66,
                "pubOpposeRatio" : 33,
                "proposalAmount" : 10000000,
                "largeRuleAmount" : 100000000,
                "publicPeriod" : 120960
            },
            "voteResult": {
                "totalVotes" : 100,
                "approveVotes" : 70,
                "opposeVotes" : 20,
                "pass" : true
            },
            "status" : 1,
            "address" : "1EDnnePAZN48aC2hiTDzhkczfF39g1pZZX",
            "height" : 100,
            "index" : 1,
            "proposalID" : "0x5047974ad5b275d5173367b76cea1d9509fd669e266c8456a1c12f14b347e7dd"
        }
      ]
  },
  "error": null
}
```
**参数说明：**

|参数|类型|说明|
|----|----|----|----|
|propRule|json|参见(1)|
|curRule|json|参见(1)|
|voteResult.totalVotes|int32|总票数|
|voteResult.approveVotes|int32|赞成票|
|voteResult.opposeVotes|int32|反对票|
|voteResult.pass|bool|是否通过，true-通过 false-未通过|
|status|int32|提案状态|
|address|string|提案地址|
|height|int64|提案高度|
|index|int32|提案index|
|proposalID|string|提案ID|

### 3.6 query active rule

**请求报文：**
```json
{
    "method": "Chain33.Query",
    "params": [
        {
            "execer": "autonomy",
            "funcName": "GetActiveRule",
            "payload": {
                "data" : "1"
            }
        }
    ]
}
```
**参数说明：**

|参数|类型|是否必须|说明|
|----|----|----|----|
|data|string|是|"1"|

**响应报文：**
```json
{
  "id": int32,
  "result": {
        "boardApproveRatio" : 66,
        "pubOpposeRatio" : 33,
        "proposalAmount" : 10000000,
        "largeRuleAmount" : 100000000,
        "publicPeriod" : 120960
  },
  "error": null
}
```
**参数说明：**

|参数|类型|说明|
|----|----|----|----|
|boardApproveRatio|int32|董事会赞成率|
|pubOpposeRatio|int32|全体持票人否决率|
|proposalAmount|int64|提案金|
|largeProjectAmount|int64|重大项目阈值|
|publicPeriod|int32|公示期|

## 4 提案董事会成员修改
### 4.1 proposal change

**请求报文：**
```json
{
    "jsonrpc":"2.0",
    "method": "Chain33.CreateTransaction",
    "params": [
        {
            "execer": "autonomy",
            "actionName": "PropChange",
            "payload": {
                "year" : 2019,
                "month" : 8,
                "day" : 29,
                "changes" : [
                    {
                        "cancel" : true,
                         "addr" : "14KEKbYtKKQm4wMthSK9J4La4nAiidGozt"
                    },
                    {
                        "cancel" : true,
                        "addr" : "1EbDHAXpoiewjPLX9uqoz38HsKqMXayZrF"
                    }, 
                    {
                        "cancel" : false,
                        "addr" : "1KcCVZLSQYRUwE5EXTsAoQs9LuJW6xwfQa"
                    }
                ],
                "startBlockHeight" : 100,
                "endBlockHeight" : 1000,
                "realEndBlockHeight" : 0
            }
        }    
    ]
}
```
**参数说明：**

|参数|类型|是否必须|说明|
|----|----|----|----|
|year|int32|否|提案年|
|month|int32|否|提案月|
|day|int32|否|提案日|
|changes.cancel|bool|是|撤销或者添加董事会，true-撤销，false-添加|
|changes.addr|string|是|撤销或者添加董事会的地址|
|startBlockHeight|int64|是|开始投票高度|
|endBlockHeight|int64|是|结束投票高度|
|realEndBlockHeight|int64|否|实际投票结束高度，不需要填写|

* endBlockHeight > startBlockHeight + 720 (自治系统中所有涉及提案都需要满足)

**响应报文：**
```json
{
    "id": int32,
    "result": "string",
    "error": null
}
```
**参数说明：**

|参数|类型|说明|
|----|----|----|----|
|result|string|交易十六进制编码后的字符串|

### 4.2 revoke proposal change

**请求报文：**
```json
{
    "jsonrpc":"2.0",
    "method": "Chain33.CreateTransaction",
    "params": [
        {
            "execer": "autonomy",
            "actionName": "RvkPropChange",
            "payload": {
                "proposalID" : "0x5047974ad5b275d5173367b76cea1d9509fd669e266c8456a1c12f14b347e7dd"
            }
        }
    ]
}
```
**参数说明：**

|参数|类型|是否必须|说明|
|----|----|----|----|
|proposalID|string|是|提案ID，即PropChange的交易hash|

**响应报文：**
```json
{
    "id": int32,
    "result": "string",
    "error": null
}
```
**参数说明：**

|参数|类型|说明|
|----|----|----|----|
|result|string|交易十六进制编码后的字符串|

### 4.3 vote proposal change

**请求报文：**
```json
{
    "jsonrpc":"2.0",
    "method": "Chain33.CreateTransaction",
    "params": [
        {
            "execer": "autonomy",
            "actionName": "VotePropChange",
            "payload": {
                "proposalID" : "0x5047974ad5b275d5173367b76cea1d9509fd669e266c8456a1c12f14b347e7dd",
                "approve": true
            }
        }
    ]
}
```
**参数说明：**

|参数|类型|是否必须|说明|
|----|----|----|----|
|proposalID|string|是|提案ID，即PropChange的交易hash|
|approve|bool|是|是否同意该提案，true：同意；false: 不同意|

**响应报文：**
```json
{
    "id": int32,
    "result": "string",
    "error": null
}
```
**参数说明：**

|参数|类型|说明|
|----|----|----|----|
|result|string|交易十六进制编码后的字符串|

### 4.4 terminate proposal change

**请求报文：**
```json
{
    "jsonrpc":"2.0",
    "method": "Chain33.CreateTransaction",
    "params": [
        {
            "execer": "autonomy",
            "actionName": "TmintPropChange",
            "payload": {
                "proposalID" : "0x5047974ad5b275d5173367b76cea1d9509fd669e266c8456a1c12f14b347e7dd"
            }
        }
    ]
}
```
**参数说明：**

|参数|类型|是否必须|说明|
|----|----|----|----|
|proposalID|string|是|提案ID，即PropChange的交易hash|

**响应报文：**
```json
{
    "id": int32,
    "result": "string",
    "error": null
}
```
**参数说明：**

|参数|类型|说明|
|----|----|----|----|
|result|string|交易十六进制编码后的字符串|

### 4.5 query proposal change

#### 4.5.1 通过proposalID查询提案

**请求报文：**
```json
{
    "method": "Chain33.Query",
    "params": [
        {
            "execer": "autonomy",
            "funcName": "GetProposalChange",
            "payload": {
                "data" : "0x5047974ad5b275d5173367b76cea1d9509fd669e266c8456a1c12f14b347e7dd"
            }
        }
    ]
}
```
**参数说明：**

|参数|类型|是否必须|说明|
|----|----|----|----|
|data|string|是|提案ID，即PropChange的交易hash|

#### 4.5.2 通过状态或者地址以及状态地址查询提案

**请求报文：**
```json
{
    "method": "Chain33.Query",
    "params": [
        {
            "execer": "autonomy",
            "funcName": "ListProposalChange",
            "payload": {
                "status" : 1,
                "addr" : "", 
                "count" : 1,
                "direction" : 0,
                "height" : -1,
                "index" : -1
            }
        }
    ]
}
```
**参数说明：**

|参数|类型|是否必须|说明|
|----|----|----|----|
|status|int32|是|提案状态|
|addr|string|否|提案地址|
|count|int32|是|查询数量|
|direction|int32|是|查询方向，0降序 1升序|
|height|int64|否|查询量大翻页查询时候需要输入从某个高度开始|
|index|int32|否|查询量大翻页查询时候需要输入从某个index开始|

* status 1-提案状态 2-提案撤销状态 3-投票状态 4-提案结束状态

**响应报文：**
```json
{
  "id": int32,
  "result": {
      "propChanges" : [
        {
            "propChange": {
                "year" : 2019,
                "month" : 8,
                "day" : 29,
                "changes" : [
                    {
                        "cancel" : true,
                         "addr" : "14KEKbYtKKQm4wMthSK9J4La4nAiidGozt"
                    },
                    {
                        "cancel" : true,
                        "addr" : "1EbDHAXpoiewjPLX9uqoz38HsKqMXayZrF"
                    }, 
                    {
                        "cancel" : false,
                        "addr" : "1KcCVZLSQYRUwE5EXTsAoQs9LuJW6xwfQa"
                    }
                ],
                "startBlockHeight" : 100,
                "endBlockHeight" : 1000,
                "realEndBlockHeight" : 900
            },
            "curRule": {
                "changeApproveRatio" : 66,
                "pubOpposeRatio" : 33,
                "proposalAmount" : 10000000,
                "largeProjectAmount" : 100000000,
                "publicPeriod" : 120960
            },
            "board" : {
                "boards" : ["12cjnN5D4DPdBQSwh6vjwJbtsW4EJALTMv","1Luh4AziYyaC5zP3hUXtXFZS873xAxm6rH"],
                "revboards" : ["1NNaYHkscJaLJ2wUrFNeh6cQXBS4TrFYeB"],
                "amount" : 10000000,
                "startHeight" : 100
            },
            "voteResult": {
                "totalVotes" : 100,
                "approveVotes" : 70,
                "opposeVotes" : 20,
                "pass" : true
            },
            "status" : 1,
            "address" : "1EDnnePAZN48aC2hiTDzhkczfF39g1pZZX",
            "height" : 100,
            "index" : 1,
            "proposalID" : "0x5047974ad5b275d5173367b76cea1d9509fd669e266c8456a1c12f14b347e7dd"
        }
      ]
    },
    "error": null
}
```
**参数说明：**

|参数|类型|说明|
|----|----|----|----|
|propChange|json|参见(1)|
|curRule.changeApproveRatio|int32|董事会赞成率|
|curRule.pubOpposeRatio|int32|全体持票人否决率|
|curRule.proposalAmount|int64|提案金|
|curRule.largeProjectAmount|int64|重大项目阈值|
|curRule.publicPeriod|int32|公示期|
|board.boards|[]string|有投票权的boards|
|board.revboards|[]string|无投票权的boards|
|board.amount|int64|该boards在当前周期已经审批的项目金|
|board.startHeight|int64|当前周期的起始区块高度|
|voteResult.totalVotes|int32|总票数|
|voteResult.approveVotes|int32|赞成票|
|voteResult.opposeVotes|int32|反对票|
|voteResult.pass|bool|是否通过，true-通过 false-未通过|
|status|int32|提案状态|
|address|string|提案地址|
|height|int64|提案高度|
|index|int32|提案index|
|proposalID|string|提案ID|

## 5 评论提案
### 5.1 comment proposal

**请求报文：**
```json
{
    "jsonrpc":"2.0",
    "method": "Chain33.CreateTransaction",
    "params": [
        {
            "execer": "autonomy",
            "actionName": "PropBoard",
            "payload": {
                "proposalID" : "",
                "repHash" : "",
                "comment" : ""
            }
        }
    
    ]
}
```
**参数说明：**

|参数|类型|是否必须|说明|
|----|----|----|----|
|proposalID|string|是|所要评论的提案|
|repHash|string|否|所要回复的评论|
|comment|string|是|评论|


**响应报文：**
```json
{
    "id": int32,
    "result": "string",
    "error": null
}
```
**参数说明：**

|参数|类型|说明|
|----|----|----|----|
|result|string|交易十六进制编码后的字符串|

### 5.2 query proposal comment

通过提案ID查询所对应评论

**请求报文：**
```json
{
    "method": "Chain33.Query",
    "params": [
        {
            "execer": "autonomy",
            "funcName": "ListProposalComment",
            "payload": {
                "proposalID" : "", 
                "count" : 1,
                "direction" : 0,
                "height" : -1,
                "index" : -1
            }
        }
    ]
}
```
**参数说明：**

|参数|类型|是否必须|说明|
|----|----|----|----|
|proposalID|string|否|提案ID|
|count|int32|是|查询数量|
|direction|int32|是|查询方向，0降序 1升序|
|height|int64|否|查询量大翻页查询时候需要输入从某个高度开始|
|index|int32|否|查询量大翻页查询时候需要输入从某个index开始|

**响应报文：**
```json
{
  "id": int32,
  "result": {
      "rltCmt" : [
        {
            "repHash" : "",
            "comment" : "",
            "height" : 100,
            "index" : 1,
            "hash" : "0x5047974ad5b275d5173367b76cea1d9509fd669e266c8456a1c12f14b347e7dd"
        }
      ]
  },
  "error": null
}
```
**参数说明：**

|参数|类型|说明|
|----|----|----|
|repHash|string|回复的评论(hash)|
|comment|string|评论|
|height|int64|提案高度|
|index|int32|提案index|
|hash|string|评论的hash|