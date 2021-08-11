# CA服务使用说明

### 简介
chain33-ca是chain33联盟链自带的CA服务节点，可向区块链用户签发认证证书，向区块链节点提供证书链认证，提供区块链用户权限管理和证书管理。

### 准备环境

#### 下载软件包
```bash
wget https://bty33.oss-cn-shanghai.aliyuncs.com/chain33-Ca.tar.gz
```

下载后解压到任意指定目录
```bash
tar -xzvf chain33-Ca.tar.gz 
cd chain33-Ca
```

软件包包含
```text
chain33-ca       -- chain33-ca节点程序
chain33.ca.toml  -- 配置文件
```

#### 配置文件
根据实际场景修改管理员公钥，证书相关的配置
```text
[server]
# CA服务端口
bindAddr = ":11901"
# 签名类型，支持"auth_ecdsa", "auth_sm2"
signType = "auth_sm2"
# CA文件目录
certdir = "certdir"
# 管理员公钥
admin = "0234e18d439e708f4295d61c9dc0ad396c267268837a0e9a7a92a5dfbd562964bd"

[db]
# db类型
driver = "leveldb"
# 数据源
dbPath = "caserver"

# 证书信息
[cert]
cn = "chain33-ca-server"
contry = "CN"
locality = "HZ"
province = "ZJ"
expire = 100
# CRL过期时间,单位小时
crlexpire = 24
```

#### 节点启动
```bash
nohup ./chain33-ca -f chain33.ca.toml > ca.log 2>&1 &
```

查看进程是否启动
```bash
ps -ef | grep -v grep | grep chain33-ca
```


### 使用方法
用户在chain33联盟链发送交易交易前，先通过管理员在chain33-ca添加用户权限，用户再向chain33-ca申请身份证书，证书信息作为交易的一部分发送到区块链节点，节点通过chain33-ca提供的证书链校验用户证书的有效性。
![证书使用](https://public.33.cn/web/storage/upload/20200910/890cec56a90a7cb4f5fb2758d3368934.png)

结合chain33-sdk

```java
// chain33-ca节点
static RpcClient certclient = new RpcClient("http://127.0.0.1:11901");

// 管理员注册用户
boolean result = certclient.certUserRegister(UserName, Identity, UserPub, AdminKey);

// 用户申请证书
CertObject.CertEnroll cert = certclient.certEnroll(Identity, UserKey);

// 构造交易
CertService.CertAction.Builder builder = CertService.CertAction.newBuilder();
builder.setTy(CertUtils.CertActionNormal);
byte[] reqBytes = builder.build().toByteArray();

String transactionHash = TransactionUtil.createTxWithCert(UserKey, "cert", reqBytes, SignType.SM2, cert.getCert(), "ca 
test".getBytes());

// 发送交易
String hash = chain33client.submitTransaction(transactionHash);
```

更多的接口说明，请参考[chain33-ca接口文档](https://github.com/33cn/chain33-ca/blob/master/README.md)和[chain33-sdk 证书服务](https://github.com/33cn/chain33-sdk-java/blob/master/%E8%81%94%E7%9B%9F%E9%93%BE%E6%8E%A5%E5%8F%A3%E8%AF%B4%E6%98%8E.md#%E8%AF%81%E4%B9%A6%E6%9C%8D%E5%8A%A1%E6%8E%A5%E5%8F%A3)