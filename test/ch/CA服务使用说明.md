# CA服务使用说明

### 1. 简介
chain33-ca是chain33联盟链自带的CA服务节点，可向区块链用户签发认证证书，向区块链节点提供证书链认证，提供区块链用户权限管理和证书管理。

### 2. 准备环境

#### 2.1 下载软件包
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

#### 2.2 配置文件
根据实际场景修改管理员公钥，证书相关的配置
```text
[server]
# CA服务端口
bindAddr = ":11901"
# 签名类型，支持"auth_ecdsa", "auth_sm2"
signType = "auth_ecdsa"
# CA文件目录
certdir = "certdir"
# 管理员公钥
admin = ""

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
# 配置初始节点的ip
ip = ["127.0.0.1", "127.0.0.2"]
```

#### 2.3 节点启动
```bash
nohup ./chain33-ca -f chain33.ca.toml > ca.log 2>&1 &
```

查看进程是否启动
```bash
ps -ef | grep -v grep | grep chain33-ca
```


### 3. 使用案例

#### 3.1 用户身份证书
用户在chain33联盟链发送交易交易前，先通过管理员在chain33-ca添加用户权限，用户再向chain33-ca申请身份证书，证书信息作为交易的一部分发送到区块链节点，节点通过chain33-ca提供的证书链校验用户证书的有效性。
![证书使用](https://public.33.cn/web/storage/upload/20200910/890cec56a90a7cb4f5fb2758d3368934.png)

#### 3.1.1 chain33配置

将CA服务certdir目录下的文件复制到cryptoPath配置的目录
```
[exec.sub.cert]
# 是否启用证书验证和签名
enable=true
# 加密文件路径，使用
cryptoPath="certdir"
# 带证书签名类型，支持"auth_ecdsa", "auth_sm2"
signType="auth_ecdsa"
```

#### 3.1.2 客户端

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

#### 3.2 联盟链动态增加注销节点

#### 3.2.1 CA服务配置
配置联盟链初始节点的ip
```
# 证书信息
[cert]
cn = "chain33-ca-server"
contry = "CN"
locality = "HZ"
province = "ZJ"
expire = 100
# CRL过期时间,单位小时
crlexpire = 24
# 配置初始节点的ip
ip = ["127.0.0.1", "127.0.0.2"]
```
#### 3.2.2 生成联盟链初始节点证书
每个节点生成一份证书和key，拷贝到节点chain33目录
```go
// 生成用户信息
userName := "user"
identity := "101"
priv, err := secp256r1.GeneratePrivateKey()
if err != nil {
    assert.Fail(t, err.Error())
}
pub := secp256r1.PubKeyFromPrivate(priv)

// 注册用户
res1, err := jsonclient.CertUserRegister(userName, identity, types.ToHex(pub), "", caAdminPriv)
if err != nil {
    assert.Fail(t, err.Error())
}
assert.Equal(t, true, res1)

// 申请证书
res2, err := jsonclient.CertEnroll(identity, "", caAdminPriv)
if err != nil {
    assert.Fail(t, err.Error())
}

_ = ioutil.WriteFile("user.cert", res2.Cert, 666)
_ = ioutil.WriteFile("user.key", res2.Key, 666)
```

#### 3.2.3 初始节点配置
`enableTLS`配置true，将CA服务器cacert目录下的证书文件复制到`caCert`配置的路径，`certFile`和`keyFile`配置3.2.1生成的证书和key对应的路径，`caServer`配置CA服务器
```
[p2p.sub.gossip]
seeds=[]
isSeed=false
serverStart=true
innerSeedEnable=true
useGithub=true
innerBounds=300
#是否启用ssl/tls 通信，默认不开启
enableTLS=true
#如果需要CA配合认证，则需要配置caCert,caServer
caCert=""
certFile=""
keyFile=""
# ca服务端接口http://ip:port
caServer=""
```

#### 3.2.4 新增节点
参考3.2.1生成新增节点的证书，将证书拷贝到新增节点，并配置chain33，启动新增节点发送交易

#### 3.2.5 注销节点
注销指定节点对应的证书
```go
identity := "new101"

// 证书注销
res, err := jsonclient.CertRevoke("", identity, "", caAdminPriv)
if err != nil {
    assert.Fail(t, err.Error())
}
```

被注销的节点交易发送失败


更多的接口说明，请参考[chain33-ca接口文档](https://github.com/33cn/chain33-ca/blob/master/README.md)和[chain33-sdk 证书服务](https://github.com/33cn/chain33-sdk-java/blob/master/%E8%81%94%E7%9B%9F%E9%93%BE%E6%8E%A5%E5%8F%A3%E8%AF%B4%E6%98%8E.md#%E8%AF%81%E4%B9%A6%E6%9C%8D%E5%8A%A1%E6%8E%A5%E5%8F%A3)