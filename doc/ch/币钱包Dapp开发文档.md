### 使用框架：
Android：https://github.com/wendux/DSBridge-Android
IOS：https://github.com/wendux/DSBridge-IOS
参考文档：
https://www.npmjs.com/package/@33cn/wallet-api

### 1.获取托管账户token：getToken
入参：无
返回数据：token

### 2.获取托管账户手机号：getPhone
入参：无
返回数据：手机号

### 3.获取当前语言：getLang
入参：无
返回数据："zh-CN"  "en-US"


### 4.获取当前钱包BTY地址：getCurrentBTYAddress
入参：无
返回数据：地址

### 5.返回上一个网页：closeCurrentWebview
入参：无
返回数据：无

### 6.微信分享：wechatShare
入参：无
返回数据：无

### 7.朋友圈分享：friendCircleShare
入参：无
返回数据：无

### 8.设置标题：setTitle
入参：
```java
{
	"title": "支付",
}
```
返回数据：无

### 9.普通签名：sign
入参：
```java
{
	"createHash": "fwjeofwioeurou32ouo324",
	"exer": "user.p.x.xx",
	"withhold": 1, (1：代扣 -1：不代扣)
}
```
返回数据：
```java
{
	"signHash": "fwjeofwioeurou32ouo324",
}
```


### 10.交易组签名：signTxGroup
入参：
```java
{
	"createHash": "fwjeofwioeurou32ouo324",
	"exer": "user.p.x.xx",
	"withhold": 1, (1：代扣 -1：不代扣)
}
```
返回数据：
```java
{
	"signHash": "fwjeofwioeurou32ouo324",
}
```

### 11.缓存私钥：configPriv
入参：
```java
{
	"cachePriv": 1（0:默认 1：缓存私钥 -1：清除私钥）
}
```
返回数据：
入参：
```java
{
	"status": 1（1：执行成功 -1：执行失败）
}
```

### 12.调起扫码：scanQRCode
入参：无
返回数据：扫码结果

### 13.获取设备id：getDeviceId
入参：无
返回：设备ID

### 14.gotoWallet 跳转钱包
入参：无
返回：无

