## Trade 接口

[TOC]

代码位置: `github.com/33cn/plugin/plugin/dapp/trade/proto`
在下面查询相关接口中，返回的卖单都一个一种格式，买单也是一种格式，只在第一个卖单或买单查询中列出其格式，不重复。

**卖单买单状态说明：**

|状态|名称|说明|
|----|----|----|
|1|TradeOrderStatusOnSale|在售|
|2|TradeOrderStatusSoldOut|售完|
|3|TradeOrderStatusRevoked|卖单被撤回|
|4|TradeOrderStatusExpired|订单超时(目前不支持订单超时)|
|5|TradeOrderStatusOnBuy|求购|
|6|TradeOrderStatusBoughtOut|购买完成|
|7|TradeOrderStatusBuyRevoked|买单被撤回|

Buy/Sell ID 在创建交易时不需要带上前缀 "mavl-trade-sell-" 或 "mavl-trade-buy-"

### 1 生成买入指定卖单卖出的token的交易（未签名）CreateRawTradeBuyTx
**调用接口**
```
rpc CreateRawTradeBuyTx(TradeForBuy) returns (UnsignTx) {}
```
**参数：**
```
message TradeForBuy {
    string sellID      = 1;
    int64  boardlotCnt = 2;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|sellID|string|卖单id|
|boardlotCnt|int64|购买数量，单位手|

**返回数据：**
```
message UnsignTx {
    bytes data = 1;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|data|bytes|交易十六进制编码后的数据|

### 2 生成撤销卖出token(卖单)的交易（未签名） CreateRawTradeRevokeTx
**调用接口**
```
rpc CreateRawTradeRevokeTx(TradeForRevokeSell) returns (UnsignTx) {}
```
**参数：**
```
message TradeForRevokeSell {
    string sellID = 1;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|sellID|string|卖单id|
|fee|int64|交易的手续费|

**返回数据：**
```
message UnsignTx {
    bytes data = 1;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|data|bytes|交易十六进制编码后的数据|

### 3 生成 买入token的交易（未签名） CreateRawTradeBuyLimitTx
**调用接口**
```
rpc CreateRawTradeBuyLimitTx(TradeForBuyLimit) returns (UnsignTx) {}
```
**参数：**
```
message TradeForBuyLimit {
    string tokenSymbol       = 1;
    int64  amountPerBoardlot = 2;
    int64  minBoardlot       = 3;
    int64  pricePerBoardlot  = 4;
    int64  totalBoardlot     = 5;
    string assetExec         = 6;
    string priceExec         = 7;
    string priceSymbol       = 8;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|tokenSymbol|string|token标识符|
|assetExec|string|资产来源的执行器名称|
|amountPerBoardlot|int64|每一手成交的数量|
|minBoardlot|int64|一次购买最少成交的数量|
|pricePerBoardlot|int64|一手成交的价格|
|totalBoardlot|int64|总共的出售的手数|
|priceExec|string|标价资产的合约|
|priceSymbol|string|标价资产的名字|

**返回数据：**
```
message UnsignTx {
    bytes data = 1;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|data|bytes|交易十六进制编码后的数据|

### 4 生成卖出指定买单的token的交易（未签名） CreateRawTradeSellMarketTx
**调用接口**
```
rpc CreateRawTradeSellMarketTx(TradeForSellMarket) returns (UnsignTx) {}
```
**参数：**
```
message TradeForSellMarket {
    string buyID       = 1;
    int64  boardlotCnt = 2;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|buyID|string|买单id|
|boardlotCnt|int64|购买数量，单位手|

**返回数据：**
```
message UnsignTx {
    bytes data = 1;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|data|bytes|交易十六进制编码后的数据|

### 5 生成撤销买入token(买单)的交易（未签名） CreateRawTradeRevokeBuyTx
**调用接口**
```
rpc CreateRawTradeRevokeBuyTx(TradeForRevokeBuy) returns (UnsignTx) {}
```
**参数：**
```
message TradeForRevokeBuy {
    string buyID = 1;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|buyID|string|买单id|

**返回数据：**
```
message UnsignTx {
    bytes data = 1;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|data|bytes|交易十六进制编码后的数据|
