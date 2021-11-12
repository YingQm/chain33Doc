## GRPC 平行链接口
[TOC]

### 1 平行链资产转移接口
**调用接口**
```
rpc CreateTransaction(CreateTxIn) returns (UnsignTx) {}
```
**参数：**
```
message CreateTxIn {
    bytes  execer     = 1;
    string actionName = 2;
    bytes  payload    = 3;
}

message CrossAssetTransfer {
    string assetExec    = 1;
    string assetSymbol  = 2;
    int64  amount       = 3;
    //default signed addr
    string toAddr       = 4;
    string note         = 5;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|method|string|Chain33.CreateTransaction|
|execer|string|交易执行器，需填具体平行链title+paracross|
|assetExec|string|资产原生合约，比如coins,token|
|assetSymbol|string|资产符号，比如bty, ccny|
|amount|int64|转移资产数量，精确到10^8|
|toAddr|string|可选，目标地址，缺省为交易签名地址|
|note|string|可选，转移备注|

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

### 2 平行链跨资产转到合约接口
>跨链转移进来的资产放在paracross合约下，默认为原生合约

**调用接口**
```
rpc CreateTransaction(CreateTxIn) returns (UnsignTx) {}
```
**参数：**
```
message CreateTxIn {
    bytes  execer     = 1;
    string actionName = 2;
    bytes  payload    = 3;
}

message AssetsTransferToExec {
    string cointoken = 1;
    int64  amount    = 2;
    bytes  note      = 3;
    string execName  = 4;
    string to        = 5;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|execer|string|主链填paracross，平行链需要把title加上|
|execName|string|目标合约名称，如果平行链上转需要填平行链的执行器名字|
|to|string|目标合约地址，示例是user.p.dog.trade的地址|
|amount|int|转移数量|
|cointoken|string|转移资产符号,默认原生合约就是paracross，所以只填符号即可|

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


### 3 平行链绑定挖矿命令
**调用接口**
```
rpc CreateTransaction(CreateTxIn) returns (UnsignTx) {}
```
**参数：**
```
message CreateTxIn {
    bytes  execer     = 1;
    string actionName = 2;
    bytes  payload    = 3;
}

message ParaBindMinerCmd{
    int32  bindAction   = 1;  // 1: bind, 2:unbind
    int64  bindCoins    = 2;  // bind coins count
    string targetNode   = 3;  // super node addr
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|method|string|Chain33.CreateTransaction|
|execer|string|必须是平行链的执行器user.p.para.paracross,title:user.p.para.按需调整|
|actionName|string|ParaBindMiner|
|bindAction|string|绑定:1，解绑定:2|
|bindCoins|int|绑定挖矿冻结币的份额，需冻结平行链原生代币，解绑定不需要此配置|
|targetNode|string|绑定目标共识节点，需要是共识账户组的成员|

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
