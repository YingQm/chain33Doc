## Wallet接口
[TOC]
### 1 账户管理
#### 1.1 钱包加锁 Lock
**调用接口**
```
rpc Lock(ReqNil) returns (Reply) {}
```
**参数：**
```
message ReqNil {}
```

**参数说明：**
nil

**返回数据：**
```
message Reply {
    bool  isOk = 1;
    bytes msg  = 2;
}
```
**参数说明：**

|参数|类型|说明|
|----|----|----|
|isok|bool|在成功时，返回 true；失败时，返回 false|
|msg|string|在成功时，为空；失败时，返回错误信息|

#### 1.2 钱包解锁 UnLock
**调用接口**
```
rpc UnLock(WalletUnLock) returns (Reply) {}
```
**参数：**
```
message WalletUnLock {
    string passwd         = 1;
    int64  timeout        = 2;
    bool   walletOrTicket = 3;
}
```

**参数说明：**

|参数|类型|是否必填|说明|
|----|----|----|----|
|passwd|string|是|解锁密码|
|walletOrTicket|bool|否|true，只解锁ticket买票功能，false：解锁整个钱包|
|timeout|int64|否|钱包解锁时间，0，一直解锁，非0值，超时之后继续锁定|

**返回数据：**
同上

#### 1.3 设置/修改钱包密码 SetPasswd
**调用接口**
```
rpc SetPasswd(ReqWalletSetPasswd) returns (Reply) {}
```
**参数：**
```
message ReqWalletSetPasswd {
    string oldPass = 1;
    string newPass = 2;
}
```

**参数说明：**

|参数|类型|是否必填|说明|
|----|----|----|----|
|oldPass|string|是|第一次设置密码时，oldPass 为空|
|newPass|string|是|待设置的新密码 必须是8个字符（包含8个）以上的数字和字母组合|

**返回数据：**
同上

#### 1.4 设置账户标签 SetLabl
**调用接口**
```
rpc SetLabl(ReqWalletSetLabel) returns (WalletAccount) {}
```
**参数：**
```
message ReqWalletSetLabel {
    string addr  = 1;
    string label = 2;
}
```

**参数说明：**

|参数|类型|是否必填|说明|
|----|----|----|----|
|addr|string|是|账户地址|
|label|string|是|待设置的账户标签|

**返回数据：**
```
message WalletAccount {
    Account acc   = 1;
    string  label = 2;
}

// Account 的信息
message Account {
    int32 currency = 1;
    int64 balance = 2;
    int64 frozen = 3;
    string addr = 4;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|acc|Account|账户信息|
|acc.currency|int32|货币类型, coins标识，目前只有0 一个值|
|acc.balance|int64|可用余额，1e8 表示 1 个 BTY|
|acc.frozen|int64|冻结金额|
|acc.addr|string|账户地址|
|label|string|是|账户标签|

#### 1.5 创建账户 NewAccount
**调用接口**
```
rpc NewAccount(ReqNewAccount) returns (WalletAccount) {}
```
**参数：**
```
message ReqNewAccount {
    string label = 1;
}
```

**参数说明：**

|参数|类型|是否必填|说明|
|----|----|----|----|
|label|string|是|账户标签|

**返回数据：**
```
message WalletAccountStore {
    string privkey   = 1;
    string label     = 2;
    string addr      = 3;
    string timeStamp = 4;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|privkey|int32|账户私钥|
|label|string|账户标签|
|addr|string|账户地址|
|timeStamp|string|创建账户时的时标|

#### 1.6 获取账户列表 GetAccounts
**调用接口**
```
rpc GetAccounts(ReqNil) returns (WalletAccounts) {}
```
**参数：**
nil

**返回数据：**
```
message WalletAccounts {
    repeated WalletAccount wallets = 1;
}

message WalletAccountStore {
    string privkey   = 1;
    string label     = 2;
    string addr      = 3;
    string timeStamp = 4;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|privkey|int32|账户私钥|
|label|string|账户标签|
|addr|string|账户地址|
|timeStamp|string|创建账户时的时标|

#### 1.7 合并账户余额 MergeBalance
**调用接口**
```
rpc MergeBalance(ReqWalletMergeBalance) returns (ReplyHashes) {}
```
**参数：**
```
message ReqWalletMergeBalance {
    string to = 1;
}
```

**参数说明：**

|参数|类型|是否必填|说明|
|----|----|----|----|
|to|string|是|合并钱包上的所有余额到一个账户地址|

**返回数据：**
```
message ReplyHashes {
    repeated bytes hashes = 1;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|hashes|[]bytes|交易的 hash 列表|

#### 1.8 导入私钥 ImportPrivkey
**调用接口**
```
rpc ImportPrivkey(ReqWalletImportPrivkey) returns (WalletAccount) {}
```
**参数：**
```
message ReqWalletImportPrivkey {
    string privkey = 1;
    string label   = 2;
}
```

**参数说明：**

|参数|类型|是否必填|说明|
|----|----|----|----|
|privkey|string|是|私钥|
|label|string|是|导入账户标签|

**返回数据：**
```
message WalletAccount {
    Account acc   = 1;
    string  label = 2;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|label|string|账户标签|
|acc|Account|账户详情|

#### 1.9 导出私钥 DumpPrivkey
**调用接口**
```
rpc DumpPrivkey(ReqString) returns (ReplyString) {}
```
**参数：**
```
message ReqString {
    string data = 1;
}
```

**参数说明：**

|参数|类型|是否必填|说明|
|----|---|----|----|
|data|string|是|待导出私钥的账户地址|

**返回数据：**
```
message ReplyString {
    string data = 1;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|data|string|私钥|

### 2 交易相关
#### 2.1 设置交易费用 SetTxFee
**调用接口**
```
rpc SetTxFee(ReqWalletSetFee) returns (Reply) {}
```
**参数：**
```
message ReqWalletSetFee {
    int64 amount = 1;
}
```
**参数说明：**

|参数|类型|是否必填|说明|
|----|----|----|----|
|amount|int64|是|手续费|

**返回数据：**
```
message Reply {
    bool  isOk = 1;
    bytes msg  = 2;
}
```
**参数说明：**

|参数|类型|说明|
|----|----|----|
|isok|bool|在成功时，返回 true；失败时，返回 false|
|msg|string|在成功时，为空；失败时，返回错误信息|

#### 2.2 发送交易 SendToAddress
**调用接口**
```
rpc SendToAddress(ReqWalletSendToAddress) returns (ReplyHash) {}
```
**参数：**
```
message ReqWalletSendToAddress {
    string from        = 1;
    string to          = 2;
    int64  amount      = 3;
    string note        = 4;
    bool   isToken     = 5;
    string tokenSymbol = 6;
}
```

**参数说明：**

|参数|类型|是否必填|说明|
|----|----|----|----|
|from|string|是|来源地址|
|to|string|是|发送到地址|
|amount|int64|是|发送金额|
|note|string|是|备注|
|isToken|bool|是|是否是token类型的转账（非token转账这个不用填）|
|tokenSymbol|string|是|toekn的symbol（非token转账这个不用填）|

**返回数据：**
```
message ReplyHash {
    bytes hash = 1;
}
```
**参数说明：**

|参数|类型|说明|
|----|----|----|
|hash|bytes|交易hash|

#### 2.3 获取钱包交易列表 WalletTxList
程序员小哥哥正在努力研发中...
<div style='display: none'>

**调用接口**
```

```
**参数：**
```

```
```json
{
    "jsonrpc":"2.0",
    "id":int32,
    "method":"Chain33.WalletTxList",
    "params":[{"fromTx":"string","count":int32,"direction":int32}]
}
```
**参数说明：**

|参数|类型|是否必填|说明|
|----|----|----|----|
|fromTx|string|是|Sprintf("%018d", height*100000 + index)，表示从高度 height 中的 index 开始获取交易列表；第一次传参为空，获取最新的交易|
|count|int32|是|获取交易列表的个数|
|direction|int32|是|查找方式；0，获取最新的交易数据，倒叙排序，在交易列表中时间高度是递减的；1，正序排序，按照时间，区块高度增加的方向获取交易列表|
|mode|int32|是|获取交易列表的个数|
|sendRecvPrivacy|int32|否||
|address|string|否||
|tokenname|string|否||

**返回数据：**
```

```
```json
{
    "id":0,
    result":
    {
        "txDetails":
        [
            {
                "tx":
                {
                    "execer":"coins",
                    "payload":"0x18010a061080c8afa025",
                    "signature":
                    {
                        "ty":0,
                        "pubkey":"0x02504fa1c28caaf1d5a20fefb87c50a49724ff401043420cb3ba271997eb5a4387",
                        "signature":"0x304402200319c88c5cc349d6c75671f880e6dba2fc46268fe92f9b62ac4b4b52f63cdb700220153374f999044073fb3d12ba686eeb1f237291e3586eafdc4151f44030f86258"
                    },
                    "fee":1000000,
                    "expire":0,
                    "nonce":6281838661429879825,
                    "to":"1Dx744a6KQpDmv76sFMeR7W5SaQGREA2Bu"
                },
                "receipt":
                {
                    "ty":3,
                    "logs":
                    [
                        {
                            "ty":2,
                            "log":"0x08c0cebafefbcf2a1080cafdfdfbcf2a18c0fbc2ffffffffffff01"
                        },
                        {
                            "ty":3,
                            "log":"0x0880cafdfdfbcf2a108082ceddd6cf2a1880b8d0dfdaffffffff01"
                        },
                        {
                            "ty":3,
                            "log":"0x1080c8afa0251880c8afa025"
                        }
                    ]
                },
                "height":21706,
                "index":75,
                "blockTime":1516110740,
                "amount":10000000000,
                "fromAddr":"14KEKbYtKKQm4wMthSK9J4La4nAiidGozt",
                "txHash":"0xc33717bad521f075966a1ed3835904d0acab863493e9cce5d3cd08e7df934751"
                "actionName": "genesis"
            }
        ]
    }
}
```
**参数说明：**

|参数|类型|说明|
|----|----|----|
|execer|string|当其值等于 "coins" 表示交易与钱包相关，其他过滤|
|payload|string|交易内容，需要解析|
|signature|Signature|交易签名|
|fee|int64|交易手续费|
|expire|int64|交易过期区块高度或者时间，大于 1e9 时，表示时间，否则表示高度|
|nonce|int64|随机数|
|to|string|接收地址|
|receipt|ReceiptLog|中当 ty 等于 2 时，交易有效|
|height|int64|交易所在区块高度|
|index|int64|用于获取交易|
|txhash|string|交易哈希|
|actionname|string|coins（transfer，withdraw，genesis），ticket（genesis，open，close，miner 挖矿所得）|

</div>

### 3 交易签名 SignRawTx
**调用接口**
```
rpc SignRawTx(ReqSignRawTx) returns (ReplySignRawTx) {}
```
**参数：**
```
message ReqSignRawTx {
    string addr    = 1;
    string privkey = 2;
    string txHex   = 3;
    string expire  = 4;
    int32  index   = 5;
    // 签名的模式类型
    // 0：普通交易
    // 1：隐私交易
    // int32  mode  = 6;
    string token = 7;
    int64  fee   = 8;
    // bytes  newExecer = 9;
    string newToAddr = 10;
}
```
**参数说明：**

|参数|类型|是否必填|说明|
|----|----|----|----|
|addr|string|是|签名地址|
|privkey|string|是|签名私钥，addr与key可以只输入其一|
|txHex|string|是|交易原始数据|
|expire|string|是|过期时间，可输入如"300ms"，"-1.5h"或者"2h45m"的字符串，有效时间单位为"ns", "us" (or "µs"), "ms", "s", "m", "h"|
|index|int32|是|若是签名交易组，则为要签名的交易序号，从1开始，小于等于0则为签名组内全部交易|
|fee|int64|否|交易费，单位1/10^8 BTY, 为0时将自动设置合适交易费|
|token|string|否|-|
|newToAddr|string|否|-|

**返回数据：**
```
message ReplySignRawTx {
    string txHex = 1;
}
```

**参数说明：**

|参数|类型|说明|
|----|----|----|
|txhex|string|签名后的交易二进制码|

### 4 seed相关
#### 4.1 生成随机的 GenSeed
**调用接口**
```
rpc GenSeed(GenSeedLang) returns (ReplySeed) {}
```
**参数：**
```
message GenSeedLang {
    int32 lang = 1;
}
```
**参数说明：**

|参数|类型|是否必填|说明|
|----|----|----|----|
|lang|int32|是|lang=0:英语，lang=1:简体汉字|

**返回数据：**
```
message ReplySeed {
    string seed = 1;
}
```
**参数说明：**

|参数|类型|说明|
|----|----|----|
|seed|string|seed字符串|

#### 4.2 保存seed并用密码加密 SaveSeed
**调用接口**
```
rpc SaveSeed(SaveSeedByPw) returns (Reply) {}
```
**参数：**
```
message SaveSeedByPw {
    string seed   = 1;
    string passwd = 2;
}
```
**参数说明：**

|参数|类型|是否必填|说明|
|----|----|----|----|
|seed|string|是|种子要求16个单词或者汉字，参考genseed输出格式，需要空格隔开|
|passwd|string|是|加密密码，必须大于或等于8个字符的字母和数字组合|

**返回数据：**
```
message Reply {
    bool  isOk = 1;
    bytes msg  = 2;
}
```
**参数说明：**

|参数|类型|说明|
|----|----|----|
|isok|bool|在成功时，返回 true；失败时，返回 false|
|msg|string|在成功时，为空；失败时，返回错误信息|

#### 4.3 通过钱包密码获取钱包的seed原文 GetSeed
**调用接口**
```
rpc GetSeed(GetSeedByPw) returns (ReplySeed) {}
```
**参数：**
```
message GetSeedByPw {
    string passwd = 1;
}
```
**参数说明：**

|参数|类型|是否必填|说明|
|----|----|----|----|
|passwd|string|是|加密密码|

**返回数据：**
```
message ReplySeed {
    string seed = 1;
}
```
**参数说明：**

|参数|类型|说明|
|----|----|----|
|seed|string|返回seed字符串|

### 5 获取钱包状态 GetWalletStatus
**调用接口**
```
rpc GetWalletStatus(ReqNil) returns (WalletStatus) {}
```
**参数：**
nil

**返回数据：**
```
message WalletStatus {
    bool isWalletLock = 1;
    bool isAutoMining = 2;
    bool isHasSeed    = 3;
    bool isTicketLock = 4;
}
```
**参数说明：**

|参数|类型|说明|
|----|----|----|
|isWalletLock|bool| 钱包解锁状态时，返回false；锁定状态时，返回true|
|isAutoMining|bool| true为自动开启挖矿|
|isHasSeed|bool| true为已经存在seed|
|isTicketLock|bool| ticket解锁状态时，返回false；锁定状态时，返回true|