[TOC]

This section mainly describes how to build a league chain based on chain33 and implement data verification, token issuance, transfer and other capabilities on the chain.

# 1.Deploy Chain33 League Chain
Refer to the instructions in the following link: 
League chain deployment: [https://github.com/andyYuanFZM/chain33_tender_deploy](https://github.com/andyYuanFZM/chain33_tender_deploy)  

# 2.System Configuration for Token
After finishing the previous step, use the chain33-cli command-line tool operation on the parallel chain node. Since the following operations only need to be performed once after the chain is deployed, so here the command line is used to demonstrate them.

Before issuing tokens, the following two steps are required:
## 2.1 Configure the Super Administrator for this Chain
The role of the super administrator is to add system configuration, such as the following token-blacklist and token-finisher configuration.
In chain33.toml, modify the following two configurations to change the addresses to the ones you want to set. 
(create your own address and keep the private key yourself is best; if you do not want to change it, we provide the private key corresponding to the following address: 3990969DF92A5914F7B71EEB9A4E58D6E255F32BF042FEA5318FC8B3D50EE6E8 ）。
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
Token-finisher: the reviewer address of the token, is used to review the information (name, amount) of the token after the token is pre-created.
Token-blacklist：token blacklist, indicating which names cannot be created on the chain, such as BTC,ETH, and so on.

```shell
#configure token-finisher, -c：fixed fill with“token-finisher”，-o：add(represent adding)， -v：token-finisher address, --paraName: correspond to the name of the parallel chain
./chain33-cli.exe --paraName "user.p.developer." config config_tx -c token-finisher -o add -v 1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs
#signiture transaction, -k: private key of the blockchain super administrator 
./chain33-cli.exe  wallet sign -k 3990969DF92A5914F7B71EEB9A4E58D6E255F32BF042FEA5318FC8B3D50EE6E8 -d [data generated in the previous step]
#send transactions
./chain33-cli.exe  wallet send -d [data generated after signiture in the previous step]

#query results
./chain33-cli.exe  --paraName "user.p.developer." config query_config -k token-finisher

#configure token-blacklist， -c: fixed fill with“token-blacklist ”，-o  add(represent adding)，-v Black list names, like BTY here
./chain33-cli.exe --paraName "user.p.developer."  config config_tx -c token-blacklist -o add -v BTY
./chain33-cli.exe wallet sign -k 3990969DF92A5914F7B71EEB9A4E58D6E255F32BF042FEA5318FC8B3D50EE6E8 -d [data generated in the previous step]
./chain33-cli.exe  wallet send -d [data generated after signiture in the previous step]

#query results
./chain33-cli.exe --paraName "user.p.developer." config query_config -k token-blacklist 

#token pre-create
./chain33-cli token precreate -f 0.001 -i Devcoin -n "DEVELOP COINS" -a "token receiver, it can be yourself or someone else" -p 0 -s "COINSDEVX" -t 19900000000
./chain33-cli wallet sign -k 3990969DF92A5914F7B71EEB9A4E58D6E255F32BF042FEA5318FC8B3D50EE6E8 -d [data generated in the previous step]
./chain33-cli wallet send -d [data generated after signiture in the previous step]

#Query, only when this step is completed can you enter the following process
./chain33-cli token get_precreated

#token finish 
./chain33-cli token finish -s COINSDEVX -f 0.001 -a [token receiver address]
./chain33-cli wallet sign -k 3990969DF92A5914F7B71EEB9A4E58D6E255F32BF042FEA5318FC8B3D50EE6E8 -d [data generated in the previous step]
./chain33-cli wallet send -d [data generated after signiture in the previous step]

#Query
./chain33-cli token get_finish_created

#Query based on address
./chain33-cli token token_balance -a [token receiver address]  -s COINSDEVX -e token
```
Note that only after token-finisher and token-blacklist are configured successfully can you proceed to the next process of issuing token.

# 3. Using JAVA-SDK
JAVA-SDK is used to realize data stored on chain and token distribution function. The usage of private chain/league chain/public chain/parallel chain is different, only the usage of public chain/parallel chain is introduced here.


## 3.1 Store on Chain
Invoke TransactionUtil.createTx()

**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|privateKey|string|signer's private key|
|execer|string|called contract name: user.write|
|payLoad|string|content stored on chain, in json format|
|fee|long|commission charges, private chain/league chain is 0|

## 3.2 Token Pre-Creation
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

## 3.3 Token Accomplished
Invoke RpcClient.createRawTokenFinishTx()

**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|fee|long|commission charges, private chain/league chain is 0|
|symbol|string|token name, only capital letters are supported, and the same symbol is not allowed for the same chain|
|ownerAddr|string|token owner, storage address after token generated|

Detailed implementation can be referred to the following link:
Use example: <a href="https://github.com/andyYuanFZM/chain33-sdk-java/blob/sdk_test/src/test/java/cn/chain33/javasdk/client/TokenTest.java" target="_blank">JAVA-SDK Use Example</a>


