# 食品溯源案例

[TOC]

## 1 平行链环境搭建
具体过程参见 [平行链环境搭建](https://chain.33.cn/document/130)

运行（这里以Linux系统为例）：

```shell
$ cd $GOPATH/chain33
$ nohup ./chain33 -f chain33.para.toml >> log.out 2>&1 &
```

创建钱包并导入创世地址私钥（已经创建钱包的话就无需进行这一步了）：

```shell
# 生成随机数种子，建议可以手工生成并保存好，后继可以使用此种子恢复钱包
$ ./chain33-cli --rpc_laddr="http://localhost:8901" --paraName="user.p.para." seed generate -l 0

# 保存种子，并设置钱包密码为"Password123"，注意：密码可以自定义，并且牢牢记住，后面解锁钱包时会用到
$ ./chain33-cli --rpc_laddr="http://localhost:8901" --paraName="user.p.para." seed save -p "Password123" -s "上一步中生成的seed"

# 使用我们刚刚设置的密码解锁钱包（钱包新创建后默认为锁定状态）
$ ./chain33-cli --rpc_laddr="http://localhost:8901" --paraName="user.p.para." wallet unlock -p "Password123"

# 导入创世地址私钥（这个私钥对应地址：1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs，这个地址中有代币）
$ ./chain33-cli  --rpc_laddr="http://localhost:8901" --paraName="user.p.para." account import_key -k 3990969DF92A5914F7B71EEB9A4E58D6E255F32BF042FEA5318FC8B3D50EE6E8 -l genesis

# 查看账户
$ ./chain33-cli --rpc_laddr="http://localhost:8901" --paraName="user.p.para." account list
```
>注意：平行链节点执行指令时，需要添加`--rpc_laddr`以及`--paraName`后缀，rpc_laddr表示平行链节点启动的IP和监听端口，paraName表示平行链的名称（参见平行链配置文件中的Title）

查询节点是否已经和主链同步 (平行链需要从主链上拉取区块，所以同步需要花一些时间)：

```shell
$ ./chain33-cli --rpc_laddr="http://localhost:8901" --paraName="user.p.para." para is_sync
true
```

查看区块同步的状态：

```shell
$ ./chain33-cli --rpc_laddr="http://localhost:8901" --paraName="user.p.para." block last_header
{
    "version": 0,
    "parentHash": "0x905d3c3ab62718381436720382e436a52976b6798896c77c97cb4e751e3a67c9",
    "txHash": "0x765a8babc9b63f7a5c608afb0943001741f3591f676026cd67dd99f6b3ad5122",
    "stateHash": "0xeb240fe1248028e9c7271ae2838ea3970bb880031764c8154c8bce2d16262cb7",
    "height": 57,
    "blockTime": 1546501778,
    "txCount": 1,
    "hash": "0xac2be112305b231b9851a34f6db7bde1745a2b7c9c3a684c736dc59baf3e6e51",
    "difficulty": 0
}
```

## 2 合约编译
使用solidity编译器进行合约的编译，可使用以下工具：

[Remix-IDE](http://remix.ethereum.org/#appVersion=0.7.7&optimize=false&version=soljson-v0.4.23+commit.124ca40d.js)

[Intellij-Solidity](https://plugins.jetbrains.com/plugin/9475-intellij-solidity)

### 2.1 Remix-IDE

创建新的solidity合约，并选择编译器版本进行编译。

![remix_prepare](https://public.33.cn/web/storage/upload/20190226/23cc7ad57c6c3c5d76bc7b665e7114a2.png "remix_prepare")

编译成功后，可以使用ABI、Bytecode进行合约的创建。

![remix_compare](https://public.33.cn/web/storage/upload/20190226/6de5d85d0fb53a47930b742f41cd57c6.png "remix_compare")

* Remix生成的abi存在换行、空格等字符，chain33实现的evm不能直接使用，还需要进行进一步的格式化操作：去除换行、空格。
* Chrome浏览器不支持编译后abi、bin文件的拷贝，因此尽量使用Edge或者IE浏览器。

考虑到以上两点，因此推荐使用Intellij-Solidity插件进行编译。

注意：
* 在合约中定义结构体时：
* 不要定义过多元素，否则编译器会报stack too deep异常。
* 不要嵌套结构体，目前chain33内部实现的evm虚拟机不支持嵌套结构体类型。


### 2.2 Intellij-Solidity

#### 2.2.1 插件安装
打开IntelliJ IDEA，在File->Settings->Plugins选项卡中，查找IntelliJ-Solidity插件进行安装。

![intelliJ_solidity](https://public.33.cn/web/storage/upload/20190226/4a61b115ef65e813c75c306e1f0209eb.png "intelliJ_solidity")

#### 2.2.2 solc安装
本地没有安装genth节点，可以直接获取chain33官方编译好的版本或者使用代码进行本地编译；
如果本地已有genth节点，可以直接使用节点自带solc。

##### 2.2.2.1 进行solc本地编译
获取最新solidity代码进行编译，github地址: https://github.com/ethereum/solidity
具体安装过程参见 [Solidity官方文档](https://solidity.readthedocs.io/en/latest/installing-solidity.html#building-from-source)

##### 2.2.2.2 获取solc编译版本
根据自己的系统环境，去github上面 [获取编译好的solc](https://github.com/ethereum/solidity/releases/tag/v0.4.23)
Linux系统环境选择solc-static-linux项进行下载，将其重命名为solc后，添加到系统环境变量
Windows系统环境选择solidity-windows.zip项进行下载，解压后将solc.exe等命令添加到系统环境变量
具体可自选，推荐选用0.5以下版本，链接给的是v0.4.23版本。

#### 2.2.3 合约的编译
获取食品溯源合约 [food.sol](https://github.com/harrylee2015/L/blob/master/share/solidity/food.sol)
打开IntelliJ IDEA，使用Build->Compile Solidity编译合约，编译后的结果可以在项目栏中看到。

![compile_solidity](https://public.33.cn/web/storage/upload/20190226/e286d4e377ffecd8271eec3ef4a36f4e.png "compile_solidity")

也可以通过命令行来进行合约的编译：

```shell
# 这里以Linux系统为例
$ mkdir -p $GOPATH/chain33
$ cp food.sol $GOPATH/chain33/food.sol
$ cd $GOPATH/chain33
$ solc --abi food.sol > Food.abi
$ solc --bin food.sol > Food.bin
```

使用生成的abi、bin文件进行合约的创建

## 3 合约创建
```shell
# 进入目录
$ cd $GOPATH/chain33
# 使用chain33-cli中已有命令行进行合约的创建
$ ./chain33-cli --rpc_laddr="http://localhost:8901" --paraName="user.p.para." evm create --sol food.sol -c 1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs -f 0.1
# 输出样例
0x83f7f41a2b7b095539d104bc2935bfdb043f3620b43d3362037fb62ad08d616d（这个hash要保存好，后续命令将会使用到）

# 根据返回的hash，查看合约创建详细信息
# 这里将输出重定向到了query_tx.txt文件中，可以打开该文件进行查看
$ ./chain33-cli --rpc_laddr="http://localhost:8901" --paraName="user.p.para." tx query -s "上一步返回的hash（这个hash要保存好，后续命令将会使用到）" > query_tx.txt
```

合约也可以使用前面生成的abi、bin文件来创建：

```shell
# 使用abi文件创建合约，因为参数较长所以省略了一些，命令执行后返回的hash要保存好，后续命令将会使用到
$ ./chain33-cli --rpc_laddr="http://localhost:8901" --paraName="user.p.para." evm create -c 1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs -f 0.1 -b '[{"constant":false,"inputs":[name":"_id","type":"string"},{"name":"_shopDate","type":"uint256"}],......,"type":"function"}]'

# 使用bin文件创建合约，因为参数较长所以省略了一些，命令执行后返回的hash要保存好，后续命令将会使用到
$ ./chain33-cli --rpc_laddr="http://localhost:8901" --paraName="user.p.para." evm create -c 1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs -f 0.1 -i '60606040526000805560006001556000600255341561001d57600080fd5b613c688061002c6000396000f300606060405260043610610107576000357c010000000000000000000000000000000000000000000000......72305820312fdba79b13b73f35f86d697bdf484ccf71d5f18456270446f3a7cf1af948db0029'
```

输出参考 [合约创建](https://github.com/harrylee2015/L/blob/master/share/solidity/food_trace.md#3-%E5%90%88%E7%BA%A6%E7%9A%84%E5%88%9B%E5%BB%BA)

## 4 案例实现
实现一个食品溯源的流程，实现产地，生产，流通等环节溯源。

实际溯源的环节是一个非常复杂的过程，这边精简为以下几个环节： 农牧场，食品厂，超市，食品质检部门，用户
产品具备的属性，以生猪为例各环节操作：

### 4.1 信息录入

#### 4.1.1 添加猪肉信息
农牧场出栏

|出栏批次|名称|重量|出栏日期|产地|
|----|----|----|----|----|
|00001|pig001|500|20190221|NanJing|

```shell
# 使用addPigInfo进行猪肉信息的录入
# 其中0x83f7f41a2b7b095539d104bc2935bfdb043f3620b43d3362037fb62ad08d616d为前面提示的需要保存的hash，用户需要将其替换成自己保存的hash
$ ./chain33-cli --rpc_laddr="http://localhost:8901" --paraName="user.p.para." evm call -c 1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs -e "user.p.para.user.evm.0x83f7f41a2b7b095539d104bc2935bfdb043f3620b43d3362037fb62ad08d616d" -f 0.01 -b "addPigInfo(\"1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs\",\"pig001\",\"00001\",\"500\",\"20190210\",\"NanJing\")"

# 通过hash查看猪肉信息是否成功添加
$ ./chain33-cli --rpc_laddr="http://localhost:8901" --paraName="user.p.para." tx query -s "上一步返回的hash"

# 使用getPigNumber()函数查看信息是否成功录入
# 其中0x83f7f41a2b7b095539d104bc2935bfdb043f3620b43d3362037fb62ad08d616d为前面提示的需要保存的hash，用户需要将其替换成自己保存的hash
$ ./chain33-cli --rpc_laddr="http://localhost:8901" --paraName="user.p.para." evm call -c 1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs -e "user.p.para.user.evm.0x83f7f41a2b7b095539d104bc2935bfdb043f3620b43d3362037fb62ad08d616d"  -f 0.01 -b "getPigNumber()"

# 通过hash查看getPigNumber()函数结果
$ ./chain33-cli --rpc_laddr="http://localhost:8901" --paraName="user.p.para." tx query -s "上一步返回的hash"
```

[输出参考](https://github.com/harrylee2015/L/blob/master/share/solidity/food_trace.md#411-%E7%8C%AA%E8%82%89%E4%BF%A1%E6%81%AF%E5%BD%95%E5%85%A5)

#### 4.1.2 添加食品信息
食品厂生产（比如火腿)

|食品编号(比如二维码)|名称|重量|生产日期|包装日期|保质期|猪肉出栏批次|
|----|----|----|----|----|----|----|----|
|001|food001|500|20190215|20190220|20210215|00001|

```shell
# 使用addFoodInfo()进行食品信息的录入
# 其中0x83f7f41a2b7b095539d104bc2935bfdb043f3620b43d3362037fb62ad08d616d为前面提示的需要保存的hash，用户需要将其替换成自己保存的hash
$ ./chain33-cli --rpc_laddr="http://localhost:8901" --paraName="user.p.para." evm call -c 1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs -e "user.p.para.user.evm.0x83f7f41a2b7b095539d104bc2935bfdb043f3620b43d3362037fb62ad08d616d" -f 0.01 -b "addFoodInfo(\"1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs\", \"001\", \"food001\", \"500\", \"20190215\", \"20190220\", \"20210215\", \"00001\", \"\", \"\")"

# 通过hash查看食品信息是否成功添加
$ ./chain33-cli --rpc_laddr="http://localhost:8901" --paraName="user.p.para." tx query -s "上一步返回的hash"

# 使用getFoodNumber()函数查看信息是否成功录入
# 其中0x83f7f41a2b7b095539d104bc2935bfdb043f3620b43d3362037fb62ad08d616d为前面提示的需要保存的hash，用户需要将其替换成自己保存的hash
$ ./chain33-cli --rpc_laddr="http://localhost:8901" --paraName="user.p.para." evm call -c 1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs -e "user.p.para.user.evm.0x83f7f41a2b7b095539d104bc2935bfdb043f3620b43d3362037fb62ad08d616d" -f 0.01 -b "getFoodNumber()"

# 通过hash查看getFoodNumber()函数结果
$ ./chain33-cli --rpc_laddr="http://localhost:8901" --paraName="user.p.para." tx query -s "上一步返回的hash"
```

[输出参考](https://github.com/harrylee2015/L/blob/master/share/solidity/food_trace.md#412-%E9%A3%9F%E5%93%81%E4%BF%A1%E6%81%AF%E5%BD%95%E5%85%A5)

#### 4.1.3 添加质检信息
食品质检部门抽检

|食品编号(比如二维码)|检测时间|检测结果|检测说明|
|----|----|----|----|
|food001|20190226|Qualified|The food is good.|

```shell
# 使用addCheckInfo()进行质检信息的录入
# 其中0x83f7f41a2b7b095539d104bc2935bfdb043f3620b43d3362037fb62ad08d616d为前面提示的需要保存的hash，用户需要将其替换成自己保存的hash
$ ./chain33-cli --rpc_laddr="http://localhost:8901" --paraName="user.p.para." evm call -c 1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs -e "user.p.para.user.evm.0x83f7f41a2b7b095539d104bc2935bfdb043f3620b43d3362037fb62ad08d616d" -f 0.01 -b "addCheckInfo(\"1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs\", \"food001\", \"20190226\", \"Qualified\", \"The food is good.\")"

# 通过hash查看质检信息是否成功添加
$ ./chain33-cli --rpc_laddr="http://localhost:8901" --paraName="user.p.para." tx query -s "上一步返回的hash"

# 使用getCheckInfoNumber()函数查看信息是否成功录入
# 其中0x83f7f41a2b7b095539d104bc2935bfdb043f3620b43d3362037fb62ad08d616d为前面提示的需要保存的hash，用户需要将其替换成自己保存的hash
$ ./chain33-cli --rpc_laddr="http://localhost:8901" --paraName="user.p.para." evm call -c 1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs -e "user.p.para.user.evm.0x83f7f41a2b7b095539d104bc2935bfdb043f3620b43d3362037fb62ad08d616d" -f 0.01 -b "getCheckInfoNumber()"

# 通过hash查看getCheckInfoNumber()函数结果
$ ./chain33-cli --rpc_laddr="http://localhost:8901" --paraName="user.p.para." tx query -s "上一步返回的hash"
```

[输出参考](https://github.com/harrylee2015/L/blob/master/share/solidity/food_trace.md#413-%E8%B4%A8%E6%A3%80%E4%BF%A1%E6%81%AF%E5%BD%95%E5%85%A5)

#### 4.1.4 添加超市上架信息

|食品编号(比如二维码)|上架日期|
|----|----|
|food001|20190304|

```shell
# 使用updateShopDate()进行超市上架信息的录入
# 其中0x83f7f41a2b7b095539d104bc2935bfdb043f3620b43d3362037fb62ad08d616d为前面提示的需要保存的hash，用户需要将其替换成自己保存的hash
$ ./chain33-cli --rpc_laddr="http://localhost:8901" --paraName="user.p.para." evm call -c 1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs -e "user.p.para.user.evm.0x83f7f41a2b7b095539d104bc2935bfdb043f3620b43d3362037fb62ad08d616d" -f 0.01 -b "updateShopDate(\"food001\", \"20190304\")"

# 通过hash查看超市上架信息是否成功添加
$ ./chain33-cli --rpc_laddr="http://localhost:8901" --paraName="user.p.para." tx query -s "上一步返回的hash"
```

[输出参考](https://github.com/harrylee2015/L/blob/master/share/solidity/food_trace.md#414-%E4%B8%8A%E6%9E%B6%E4%BF%A1%E6%81%AF%E5%BD%95%E5%85%A5)

#### 4.1.5 添加用户评分信息

|食品编号|用户评分|
|----|----|
|food001|90|

```shell
# 使用updateScore()进行评分信息的录入
# 其中0x83f7f41a2b7b095539d104bc2935bfdb043f3620b43d3362037fb62ad08d616d为前面提示的需要保存的hash，用户需要将其替换成自己保存的hash
$ ./chain33-cli --rpc_laddr="http://localhost:8901" --paraName="user.p.para." evm call -c 1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs -e "user.p.para.user.evm.0x83f7f41a2b7b095539d104bc2935bfdb043f3620b43d3362037fb62ad08d616d" -f 0.01 -b "updateScore(\"food001\", \"90\")"

# 通过hash查看评分信息是否成功添加
$ ./chain33-cli --rpc_laddr="http://localhost:8901" --paraName="user.p.para." tx query -s "上一步返回的hash"
```

[输出参考](https://github.com/harrylee2015/L/blob/master/share/solidity/food_trace.md#415-%E8%AF%84%E5%88%86%E4%BF%A1%E6%81%AF%E5%BD%95%E5%85%A5)

### 4.2 信息查询

#### 4.2.1 猪肉信息查询

```shell
# 使用pigId查询猪肉信息
# 其中0x83f7f41a2b7b095539d104bc2935bfdb043f3620b43d3362037fb62ad08d616d为前面提示的需要保存的hash，用户需要将其替换成自己保存的hash
$ ./chain33-cli --rpc_laddr="http://localhost:8901" --paraName="user.p.para." evm call -c 1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs -e "user.p.para.user.evm.0x83f7f41a2b7b095539d104bc2935bfdb043f3620b43d3362037fb62ad08d616d" -f 0.01 -b "getPigInfoByID(\"00001\")"
$ ./chain33-cli --rpc_laddr="http://localhost:8901" --paraName="user.p.para." tx query -s "上一步返回的hash"
```

[输出参考](https://github.com/harrylee2015/L/blob/master/share/solidity/food_trace.md#423-%E7%81%AB%E8%85%BF%E5%8E%9F%E6%9D%90%E6%96%99%E7%8C%AA%E8%82%89%E4%BF%A1%E6%81%AF%E6%9F%A5%E8%AF%A2)

#### 4.2.2 食品信息查询

```shell
# 使用foodId查询食品（火腿）信息
# 其中0x83f7f41a2b7b095539d104bc2935bfdb043f3620b43d3362037fb62ad08d616d为前面提示的需要保存的hash，用户需要将其替换成自己保存的hash
$ ./chain33-cli --rpc_laddr="http://localhost:8901" --paraName="user.p.para." evm call -c 1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs -e "user.p.para.user.evm.0x83f7f41a2b7b095539d104bc2935bfdb043f3620b43d3362037fb62ad08d616d" -f 0.01 -b "getFoodInfoByID(\"food001\")"
$ ./chain33-cli --rpc_laddr="http://localhost:8901" --paraName="user.p.para." tx query -s "上一步返回的hash"
```

[输出参考](https://github.com/harrylee2015/L/blob/master/share/solidity/food_trace.md#421-%E7%81%AB%E8%85%BF%E4%BF%A1%E6%81%AF%E6%9F%A5%E8%AF%A2)

#### 4.2.3 质检信息查询

```shell
# 使用foodId查询质检信息
# 其中0x83f7f41a2b7b095539d104bc2935bfdb043f3620b43d3362037fb62ad08d616d为前面提示的需要保存的hash，用户需要将其替换成自己保存的hash
$ ./chain33-cli --rpc_laddr="http://localhost:8901" --paraName="user.p.para." evm call -c 1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs -e "user.p.para.user.evm.0x83f7f41a2b7b095539d104bc2935bfdb043f3620b43d3362037fb62ad08d616d" -f 0.01 -b "getCheckInfoByID(\"food001\")"
$ ./chain33-cli --rpc_laddr="http://localhost:8901" --paraName="user.p.para." tx query -s "上一步返回的hash"
```

[输出参考](https://github.com/harrylee2015/L/blob/master/share/solidity/food_trace.md#422-%E8%B4%A8%E6%A3%80%E4%BF%A1%E6%81%AF%E6%9F%A5%E8%AF%A2)
