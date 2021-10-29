# 部署调用EVM合约（通过chain33命令行实现）

[TOC]


### 1.1 创建部署交易
```
命令行参数：
./chain33-cli evm create
Usage:
  chain33-cli evm create [flags]

Flags:
  -b, --abi string         abi string used for create constructor parameter(optional, not needed if no parameter for constructor)
  -s, --alias string       human readable contract alias name(optional)
  -c, --code string        contract binary code
      --expire string      transaction expire time (optional) (default "120s")
  -f, --fee float          contract gas fee (optional)
  -h, --help               help for create
  -n, --note string        transaction note info (optional)
  -p, --parameter string   (optional)parameter for constructor and should be input as constructor(xxx,xxx,xxx)
```
**参数说明：**
    
|参数|类型|是否必填|说明|
|----|----|----|----|----|
|abi|string|否|部署合约abi字符串，只有需要填充构造函数参数时才需要|
|alias|string|否|部署合约别名|
|code|string|是|部署合约字节码|
|fee|int64|否|部署合约需要的交易费，可以通过EstimateGas来获取，也可以不填|
|note|string|否|备注信息|
|parameter|string|否|部署合约时构造函数参数，以字符串格式“constructor(xxx,xxx,xxx)”输入|

**执行结果：**
未签名的部署交易字符串

**备注：**
该交易字符串，经过签名就可以发送

### 1.2 创建调用交易
```
命令行参数：
Usage:
  chain33-cli evm call [flags]

Flags:
  -a, --amount float       the amount transfer to the contract (optional)
  -e, --exec string        evm contract address
  -f, --fee float          contract gas fee (optional)
  -h, --help               help for call
  -n, --note string        transaction note info (optional)
  -p, --parameter string   tx input parameter as:approve(13nBqpmC4VaJpEZ6J6G9NUM1Y55FQvw558, 100000000)
  -t, --path string        abi path(optional), default to .(current directory) (default "./")

```
**参数说明：**
    
|参数|类型|是否必填|说明|
|----|----|----|----|----|
|amount|小数，精确到0.0001|否|交易执行过程中，数量为amount的BTY从交易发起者账户中转账到该合约账户中|
|exec|string|是|合约地址|
|fee|int64|否|部署合约需要的交易费，可以通过EstimateGas来获取，也可以不填|
|note|string|否|备注信息|
|parameter|string|是|调用合约输入参数，以字符串格式，如“approve(13nBqpmC4VaJpEZ6J6G9NUM1Y55FQvw558, 100000000)”输入|
|path|string|是|本地用来存放abi字符串信息的文件目录，命令就可以从本地读取来进行调用参数的abi序列化，abi文件以contractAddress.abi的格式来保存|


**执行结果：**
未签名的调用交易字符串

**备注：**
该交易字符串，经过签名就可以发送

### 1.3 估算gas（部署交易或者调用交易执行时需要的支付的gas）
```
命令行参数：
Usage:
  chain33-cli evm estimate [flags]

Flags:
  -c, --caller string   contract creator or caller
  -h, --help            help for estimate
  -x, --tx string       tx string(should be signatured)
```
**参数说明：**
    
|参数|类型|是否必填|说明|
|----|----|----|----|----|
|caller|string|是|交易调用地址|
|tx|string|是|未签名交易字符串|


**执行结果：**
需要支付的gas

### 1.4 查询
```
命令行参数：
Usage:
  chain33-cli evm query [flags]

Flags:
  -a, --address string   evm contract address
  -c, --caller string    the caller address
  -h, --help             help for query
  -b, --input string     call params (abi format) like foobar(param1,param2)
  -t, --path string      abi path(optional), default to .(current directory) (default "./")

```
**参数说明：**
    
|参数|类型|是否必填|说明|
|----|----|----|----|----|
|address|string|是|合约地址|
|caller|string|是|交易调用地址|
|input|string|是|查询输入参数，使用格式“foobar(param1,param2)”|
|path|string|是|本地用来存放abi字符串信息的文件目录，命令就可以从本地读取来进行调用参数的abi序列化，abi文件以contractAddress.abi的格式来保存|

**执行结果：**
查询结果信息

### 1.5 evm合约内部转账
```
命令行参数：
chain33-cli evm transfer [flags]

Flags:
  -a, --amount float      the amount transfer to the contract, precision to 0.0001
  -c, --caller string     the caller address
  -h, --help              help for transfer
  -r, --receiver string   receiver address
```
**参数说明：**
    
|参数|类型|是否必填|说明|
|----|----|----|----|----|
|amount|小数，精确到0.0001|是|转账额度|
|caller|string|是|转账交易发起人地址|
|receiver|string|是|接收地址|

**执行结果：**
在evm合约内部进行BTY的转账


