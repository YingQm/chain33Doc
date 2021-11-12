## Unfreeze

[TOC]

> 定期解冻合约帮助用户锁定一定量的币， 按在指定的规制解冻给受益人，
> 适用于分期付款， 分期支付形式的员工激励等情景。

**合约提供了3类操作**
  1. 创建定期解冻合约：创建时需要指定支付的资产和总量，以及定期解冻的形式。
  1. 受益人提币：受益人提走解冻了的资产。
  1. 发起人终止合约： 发起人可以终止合约的履行。

**解冻的形式目前支持两种**
  1. 固定数额解冻：指定时间间隔，解冻固定的资产。
  1. 按剩余量的固定比例解冻：指定时间间隔，按剩余量的固定比例解冻。 这种方式，越到后面解冻的越少。

---
> 说明：在合约创建时，就可以解冻一次。
  举例：一个固定数额解冻和合约，总量为100，一个月解冻10。创建时可以由受益人提走10，第一个月后又可以提走10。
  在受益人没有及时提币的情况下，受益人在一段时间之后可以一次性提走本该解冻的所有的币。
  即解冻的币是按指定形式解冻的，和受益人的提币时间和次数等都不会影响解冻的进程。

### 1 查询合约状态 GetUnfreeze

**调用接口**
```
rpc QueryUnfreeze(ReqString) returns (Unfreeze) {}
```
**参数：**
```
message ReqString {
    string data = 1;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|data|string|合约的ID，可以查询创建冻结合约时得到，同创建冻结合约的交易ID的十六进制，是对应的unfreezeID去掉前缀 "mavl-unfreeze-"。|

**返回数据：**
```
message Unfreeze {
    string unfreezeID = 1;
    int64 startTime = 2;
    string assetExec   = 3;
    string assetSymbol = 4;
    int64 totalCount = 5;
    string initiator = 6;
    string beneficiary = 7;
    int64 remaining = 8;
    string means = 9;
    oneof  meansOpt {
        FixAmount      fixAmount      = 10;
        LeftProportion leftProportion = 11;
    }
    bool terminated = 12;
}

// 按时间固定额度解冻
message FixAmount {
    int64 period = 1;
    int64 amount = 2;
}

// 固定时间间隔按余量百分比解冻
message LeftProportion {
    int64 period        = 1;
    int64 tenThousandth = 2;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|unfreezeID |string|解冻交易ID（唯一识别码），这里合约的ID， 可以查询创建冻结合约时，得到， 同创建冻结合约的交易ID的十六进制。是对应的unfreezeID去掉前缀 "mavl-unfreeze-"|
|startTime | string | 合约生效时间， UTC 秒数|
|assetExec |string|资产所在执行器名 |
|assetSymbol |string|资产标识 |
|totalCount | string| 冻结资产总数 |
|initiator |string| 合约创建者/发币人地址 |
|beneficiary |string| 合约受益人/收币人地址 |
|remaining | string | 合约中剩余资产总数 |
|means | string | 合约解冻算法名/解冻方式（百分比；固额） |
|meansOpt.fixAmount|FixAmount| 按时间固定额度解冻 |
|meansOpt.leftProportion|LeftProportion|固定时间间隔按余量百分比解冻|
|terminated|bool|是否已经终止|

### 2 查询合约可提币量 GetUnfreezeWithdraw

**调用接口**
```
rpc GetUnfreezeWithdraw(ReqString) returns (ReplyQueryUnfreezeWithdraw) {}
```
**参数：**
```
message ReqString {
string data = 1;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|data|string|合约的ID，可以查询创建冻结合约时得到，同创建冻结合约的交易ID的十六进制，是对应的unfreezeID去掉前缀 "mavl-unfreeze-"。|

**返回数据：**
```
message ReplyQueryUnfreezeWithdraw {
    string unfreezeID      = 1;
    int64  availableAmount = 2;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|unfreezeID|string|具体数据，这里合约的ID，是对应创建合约的交易Hash加上前缀 "mavl-unfreeze-"|
|availableAmount|int64|合约中解冻了的但还没有被提走的资产数目 |
