[TOC]

This section introduces how to build a parallel chain quickly, to achieve the issue and transfer ability of token by JAVA-SDK.
The following commands are all executed on Windows，and are similar on Linux except for the name of the main program on chain33 and the name of command-line tool.

# 1.Deploy Chain33 Parallel Chain
Refer to the instructions in the link below：
Parallel chain deployment: [https://github.com/andyYuanFZM/chain33_para_deploy](https://github.com/andyYuanFZM/chain33_para_deploy)  

# 2.System Configuration for Token
After finishing the previous step, use the chain33-cli.exe command-line tool operation on the parallel chain. Since the following operations only need to be performed once after he chain is deployed, so here the command line is used to demonstrate them.

Before issuing tokens, the following two steps are required:
## 2.1 Configure the Super Administrator for this Chain
The role of the super administrator is to add system configuration, such as the following token-blacklist and token-finisher configuration.
In chain33.toml, modify the following two configurations to change the addresses to the ones you want to set. 
(you can directly use the private key provided by the official without modification, and there is a small amount of BTY in it that can be used to pay the service fee: 3990969DF92A5914F7B71EEB9A4E58D6E255F32BF042FEA5318FC8B3D50EE6E8).
```shell
[exec.sub.manage]
superManager=[
    "1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs",
]

[exec.sub.token]
saveTokenTxList=true
tokenApprs = [
        "1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs",
]
```

## 2.2 Configure Token-Finisher and Token-Blacklist
Token-finisher: the reviewer address of the token is used to review the information (name, amount) of the token after the token is pre-created.
Token-blacklist：token blacklist, indicating which names cannot be created on the chain, such as BTC,ETH, and so on.

```shell
#configure token-finisher, -c：fixed fill with“token-finisher”，-o：add(represent adding)， -v：token-finisher address, --paraName: correspond to the name of the parallel chain
./chain33-cli.exe --paraName "user.p.developer." config config_tx -c token-finisher -o add -v 1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs
#signiture transaction, -k: private key of the blockchain super administrator 
./chain33-cli.exe  wallet sign -k 3990969DF92A5914F7B71EEB9A4E58D6E255F32BF042FEA5318FC8B3D50EE6E8 -d "data generated in the previous step"
#send transactions
./chain33-cli.exe  wallet send -d "data generated after signiture in the previous step"

#query results
./chain33-cli.exe  --paraName "user.p.developer." config query_config -k token-finisher

#configure token-blacklist， -c: fixed fill with“token-blacklist ”，-o  add(represent adding)，-v Black list names, like BTY here
./chain33-cli.exe --paraName "user.p.developer."  config config_tx -c token-blacklist -o add -v BTY
./chain33-cli.exe wallet sign -k 3990969DF92A5914F7B71EEB9A4E58D6E255F32BF042FEA5318FC8B3D50EE6E8 -d "data generated in the previous step"
./chain33-cli.exe  wallet send -d "data generated after signiture in the previous step"

#query results
./chain33-cli.exe --paraName "user.p.developer." config query_config -k token-blacklist 
```
Note that only after token-finisher and token-blacklist are configured successfully can you proceed to the next process of issuing token.

# 3. Using JAVA-SDK
JAVA-SDK is used to store data on chain and token distribution function. The usage of private chain/league chain/public chain/parallel chain is different, only the usage of public chain/parallel chain is introduced here.

## 3.1 Token Pre-Creation
Invoke RpcClient.createRawTokenPreCreateTx()

**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|name|string|annotation name for token|
|symbol|string|token name, only capital letters are supported, and the same symbol is not allowed for the same chain|
|introduction|string|token introduction|
|ownerAddr|string|token owner, storage address after token generated|
|total|long|token amount, say 500, the system supports a maximum of $90 billion|
|price|long|token issuing cost, just fill with 0|
|fee|long|commission charges, private chain/league chain is 0|

Then invoke RpcClient.createNoBalanceTx()

**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|txHex|string|transaction generated in the previous step txhex|
|payAddr|string|address corresponding to the withhold commission fee|

## 3.2 Token Accomplished
Invoke RpcClient.createRawTokenFinishTx()

**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|fee|long|commission charges, private chain/league chain is 0|
|symbol|string|token name, only capital letters are supported, and the same symbol is not allowed for the same chain|
|ownerAddr|string|token owner, storage address after token generated|

Then invoke RpcClient.createNoBalanceTx()

**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|txHex|string|transaction generated in the previous step txhex|
|payAddr|string|address corresponding to the withhold commission fee|

## 3.3 Token Transfer
Invoke RpcClient.createRawTransaction()

**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|to|long|commission charges, private chain/league chain is 0|
|amount|long|send amount|
|fee|long|commission charges|
|note|string|remark|
|isToken|boolean|whether it is a transfer of token type|
|isWithdraw|boolean|whether it is a withdrawal transaction|
|tokenSymbol|string|token symbol|

Then invoke RpcClient.createNoBalanceTx()

**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|txHex|string|transaction generated in the previous step txhex|
|payAddr|string|address corresponding to the withhold commission fee|

Detailed implementation can be referred to the following link:
Use example: <a href="https://github.com/andyYuanFZM/chain33-sdk-java/blob/sdk_test/src/test/java/cn/chain33/javasdk/client/TokenParaTest.java" target="_blank">JAVA-SDK Use Example</a>
