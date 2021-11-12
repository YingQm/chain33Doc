# 1.创建钱包
### 1.1 创建助记词 createMnem
**入参说明：**


| 参数 | 类型 | 是否必填 | 说明 |
| :-----:| :----: | :----: |
| mnemLangType | int | 是 | 1：中文助记词 2：英文助记词 |


**返回数据：**
助记词

### 1.2 创建钱包（地址、私钥、公钥） createWallet
**入参说明：**

| 参数 | 类型 | 是否必填 | 说明 |
| :-----:| :----: | :----: |
| mnem | string | 是 | 助记词 |
| chain | string | 是 | 主链，例如：“BTC” |

**返回数据：**

| 参数 | 类型  | 说明 |
| :-----:| :----: | :----: |
| address | string  | 地址 |
| priv | string | 私钥|
| pub | string  | 公钥|



### 1.3 私钥转地址 privToAddr
**入参说明：**

| 参数 | 类型 | 是否必填 | 说明 |
| :-----:| :----: | :----: |
| chain | string | 是 | 主链，例如：“BTC” |
| priv | string | 是 | 私钥 |

**返回数据：**
币种地址

### 1.4 公钥转地址 pubToAddr
**入参说明：**

| 参数 | 类型 | 是否必填 | 说明 |
| :-----:| :----: | :----: |
| chain | string | 是 | 主链，例如：“BTC” |
| pub | string | 是 | 公钥 |

**返回数据：**
币种地址

# 2.交易相关

### 2.1 获取余额 getBalance
**入参说明：**

| 参数 | 类型 | 是否必填 | 说明 |
| :-----:| :----: | :----: |
| addr | string | 是 | 币种地址 |
| chain | string | 是 | 主链名称，例如：“BTC” |
| tokenSymbol | string | 是 | token名称，例如ETH下的“YCC” |
| goNoderUrl | string | 是 | 服务器节点 |

**返回数据：**
币种余额data数据
````java
{
	"id": 1,
	"result": {
		"address": "0x632d8B07CDE8B2dcc3645148d2fa76647565664",
		"balance": "0.02091716"
	},
	"error": null
}
````

### 2.2 获取交易记录 getTranList
**入参说明：**

| 参数 | 类型 | 是否必填 | 说明 |
| :-----:| :----: | :----: |
| addr | string | 是 | 币种地址 |
| chain | string | 是 | 主链名称，例如：“BTC” |
| tokenSymbol | string | 是 | token名称，例如ETH下的“YCC” |
| type | int | 是 | 交易账单类型（0全部 1入账，2出账） |
| page | string | 是 | 页数 |
| count | string | 是 | 一页请求的条数|
| goNoderUrl | string | 是 | 服务器节点 |

**返回数据：**
返回：交易记录data数据

| 参数 | 类型 | 说明 |
| :-----:| :----: | :----: |
| blocktime | string |  交易时间 |
| fee | string |  手续费 |
| from | string |  转出地址 |
| height | string | 区块高度 |
| note | string | 备注 |
| status | string | 状态 （-1：失败，0：确认中，1：完成） |
| to | string | 转入地址 |
| txid | string |  交易txid |
| type | string | 交易账单类型（0全部 1入账，2出账） |
| value | string |  交易数量 |
```java
{
	"id": 1,
	"result": [{
		"blocktime": 1605774673,
		"fee": "0.007",
		"from": "1P7P4v3kL39zugQgDDLRqxdddddddfKs",
		"height": 11097152,
		"note": "",
		"status": "1",
		"to": "1KgE3vayiqZKhfhMftN7vtddddMk941",
		"txid": "0x3b4f885b01370509be01e258f2ddddd7fc01f65d578d9156a6887f3667c8d",
		"type": "receive",
		"value": "3"
	}, {
		"blocktime": 1602750506,
		"fee": "0.007",
		"from": "1KgE3vayiqZKhfhMftddddHoMk941",
		"height": 10499717,
		"note": "",
		"status": "1",
		"to": "1NkcL7c2LLESnZQgi2dddddKByemsPa5",
		"txid": "0x4fc738785a0e792660858f65d5a9dddddccbc37b1229bd4c5d32fed1c7",
		"type": "send",
		"value": "0.1"
	}]
		"error": null
}
```

### 2.3 获取单笔交易详情 getTranByTxid
**入参说明：**

| 参数 | 类型 | 是否必填 | 说明 |
| :-----:| :----: | :----: |
| txid | string | 是 | 交易txid |
| chain | string | 是 | 主链名称，例如：“BTC” |
| tokenSymbol | string | 是 | token名称，例如ETH下的“YCC” |
| goNoderUrl | string | 是 | 服务器节点 |

**返回数据：**

| 参数 | 类型 | 说明 |
| :-----:| :----: | :----: |
| blocktime | string |  交易时间 |
| fee | string |  手续费 |
| from | string |  转出地址 |
| height | string | 区块高度 |
| status | string | 状态 （-1：失败，0：确认中，1：完成） |
| to | string | 转入地址 |
| txid | string |  交易txid |
| type | string | 交易账单类型（0全部 1入账，2出账） |
| value | string |  交易数量 |
```java
{
	"id": 1,
	"result": {
		"blocktime": 1605774673,
		"fee": "0.007",
		"from": "1P7P4v3kL39zugQgDDLRqxzGjQd7aEbfKs",
		"height": 11097152,
		"status": "1",
		"to": "1KgE3vayiqZKhfhMftN7vt2gDv9HoMk941",
		"txid": "0x3b4f885b01370509be01e258f277276dc37fc01f65d578d9156a6887f3667c8d",
		"type": "send",
		"value": "3"
	},
	"error": null
}
```

## 交易三部曲：构造、签名、发送
### 2.4 构造 createTran
**入参说明：**

| 参数 | 类型 | 是否必填 | 说明 |
| :-----:| :----: | :----: |
| chain | string | 是 | 主链名称，例如：“BTC” |
| fromAddr | string | 是 | 出币地址 |
| toAddr | string | 是 | 入币地址 |
| amount | double | 是 | 数量 |
| fee | double | 是 | 手续费|
| note | string | 是 | 备注|
| tokenSymbol | string | 是 | token名称，例如ETH下的“YCC” |
| goNoderUrl | string | 是 | 服务器节点 |

**返回数据：**
构造的data数据，用于签名
```java
{
	"error": null,
	"id": 1,
	"result": {
		"execer": "Y29pbnM=",
		"payload": "GAEKCgoDQlRZEICt4gQ=",
		"fee": 700000,
		"nonce": 7832532200213791736,
		"to": "1P7P4v3kL39zugQgDDLRqxdddd7aEbfKs"
	}
}
```

### 2.5 签名 signTran
**入参说明：**

| 参数 | 类型 | 是否必填 | 说明 |
| :-----:| :----: | :----: |
| chain | string | 是 | 主链名称，例如：“BTC” |
| unSignData | string | 是 | 构造后的数据（result） |
| priv | string | 是 | 私钥 |

**返回数据：**
签名后的数据
```java
0a05636f696e73120e18010a0a0a034254591080ade2041a6d0801122103ac71dc39543350e02dce483ce83022b17f4399ed857ed15d4d0c6a92001d51121a46304402201c8ecff7b378f9e50edde928a9f683272142fe202190b7017fbffd88393aa
```

### 2.6 发送交易 sendTran
**入参说明：**

| 参数 | 类型 | 是否必填 | 说明 |
| :-----:| :----: | :----: |
| chain | string | 是 | 主链名称，例如：“BTC” |
| tokenSymbol | string | 是 | token名称，例如ETH下的“YCC” |
| signData | string | 是 | 签名后的数据 |
| goNoderUrl | string | 是 | 服务器节点 |

**返回数据：**

| 参数 | 类型 | 说明 |
| :-----:| :----: | :----: |
| result | string |  交易txid |

```java
{
	"id": 1,
	"result": "0xeba51c32447bd1dfa287b85ad41b012ee310ddd4b6a335a568bd3710d834",
	"error": null
}

```
### 2.7 平行链构造+签名 pcTran
**入参说明：**

| 参数 | 类型 | 是否必填 | 说明 |
| :-----:| :----: | :----: |
| to | string | 是 | 入币地址 |
| tokenSymbol | string | 是 | coins币：链名.coins（xx.coins）；token币：链名.币名(xx.x) |
| execer | string | 是 | 执行器：coins币：user.p.链名.coins ；token币：user.p.链名.token|
| txpriv | string | 是 | 本地BTY的私钥 |
| amount | string | 是 | 数量 |
| note | string | 是 | 备注 |
| feePriv | string | 是 |代扣手续费的私钥 |
| coinsForFee | string | 是 |coinsForFee 为true,代扣coins币作为手续费 |
| tokenfee | string | 是 | 代扣多少coins作为手续费，例如：0.001 |
| tokenfeeAddr | string | 是 | 代扣的手续费接收地址 |
| fee | string | 是 | 代扣BTY作为整个交易的手续费，单笔交易最低0.001，交易组建议0.003 |


**返回数据：**

| 参数 | 类型 | 说明 |
| :-----:| :----: | :----: |
| txId | string |  交易txid |
| signedTx | string |  签名后的数据（签名后使用它作为sendTran的入参发送交易） |




# 简单接入：
#### 1.将lib-wallet.aar放置于libs文件夹
#### 2.app下的build.gradle文件中配置引入aar
```java
   implementation(name: 'lib-wallet', ext: 'aar')
```
#### 3.通过appSecret初始化GoWallet


```java
package com.fzm.walletsdk

import android.os.Bundle
import android.util.Log
import androidx.appcompat.app.AppCompatActivity
import com.fzm.lib_wallet.GoWallet


class MainActivity : AppCompatActivity() {

    val appkeySecret = "aba2c4d118fdc3aefd69c3bcb00ebca17cdefddddddd"

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        val goWallet = GoWallet.init(this, appkeySecret)
        if (goWallet != null) {
            val zhMnme = goWallet.createMnem(1)
            val enMnme = goWallet.createMnem(2)
            val wallet = goWallet.createWallet(zhMnme, "BTC")
            Log.v("wallet：", "${wallet.address},${wallet.priv},${wallet.pub}")

            val addr = goWallet.privToAddr("BTC", wallet.priv)
            val addr2 = goWallet.pubToAddr("BTC", wallet.pub)

            Log.v("walletnew：", "${addr},${addr2}")
        }
    }
}

```



