[TOC]

---
# 1.  Solidity of DApp Development 
*   Remix is an open source Solidity development environment that provides basic functions such as compiling, deploying to local or test networks, and executing contracts. Solidity is the official programming language designed and supported by Ethereum to write smart contracts.
---
## 1.1 Remix Environment Built
First. use online environment  
>	<a href="https://remix.ethereum.org/" target="_blank" title="Online Remix Url">Online Remix Url</a>,use online IDE to develop smart contract,it's the simplest way if the network speed is ok.
  
![在线地址图片](https://public.33.cn/web/storage/upload/20181115/7d0284e64a0da8703415097351eca36d.png)

Second. set up the offline environment locally

>   Download the official packaged<a href="https://github.com/ethereum/browser-solidity/blob/gh-pages/remix-7013ed1.zip" target="_blank" title="offline version"> offline version</a>, after local decompression, use the browser open index.html

![offline env diagram](https://public.33.cn/web/storage/upload/20181115/2f3ddb8fa4da1dbf252e119d963b22b0.png)

Third. set up the online environment locally

>  Install the local online environment using the following NPM command

**Installation command:**
Install the NPM and node.js (see https://docs.npmjs.com/getting-started/installing-node), Remix-ide has been as a module of NPM:
    npm install remix-ide -g
    remix-ide
Or you can clone the entire github library (you need to install wget first) :

    git clone https://github.com/ethereum/remix-ide.git
    cd remix-ide
    npm install
    npm run setupremix  # this will clone https://github.com/ethereum/remix for you and link it to remix-ide. Only execute this step if you want to contribute on Remix development
    npm start

---
>	Specific operation can refer to: https://github.com/ethereum/remix-ide

---
## 1.2 Example Introduction and Environment Use

---
### 1.2.1 Write Contract Code
>	**step1：**Click the `+` sign in the upper left corner of online remix, Cteate New File in the Browser Storage Explorer, name does not matter, and extension is "xxx.sol".

![+](https://public.33.cn/web/storage/upload/20181112/60afc760f6af446f33cd24875b3afa68.png)
    
>	**step2:**Here is a simple case code, which reads as follows:  

---
    pragma solidity ^0.4.18;
    contract SimpleStorage {
    uint storedData;
    function set(uint x) public {
        storedData = x;
    }
    function get() constant public returns (uint) {
        return storedData;}
}

---
### 1.2.2 Compiled Intelligent Contract

>	**step3: **Click the button on the right of the IDE screen, Start to compile. If there are no errors, the screenshot below shows:

![Start to compile](https://public.33.cn/web/storage/upload/20181112/2efb1ec9902b26fea2e695e11e3e5491.png)

>	**step4: **Click the`run`button, and then click`Create` to Create a string of code for the contract deployment. You can see the interface used by the contract

![合约部署](https://public.33.cn/web/storage/upload/20181112/c1dfd1550734b7bea8579e308a759baf.png "合约部署")

    In the screenshot, '3' is shown as the input code for the contract code interface deployment:0x608060405234801561001057600080fd5b5060df8061001f6000396000f3006080604052600436106049576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff16806360fe47b114604e5780636d4ce63c146078575b600080fd5b348015605957600080fd5b5060766004803603810190808035906020019092919050505060a0565b005b348015608357600080fd5b50608a60aa565b6040518082815260200191505060405180910390f35b8060008190555050565b600080549050905600a165627a7a72305820400d8ac26862c8658a699fc570c2a260485d7d8747b8bb9541264fdf2e7d9aeb0029

### 1.2.3 Call Contract Method
   
>	**step5:**In this case, there are only two contract methods, set and get. If you want to call the set method of the contract, you just need to fill in the parameter value to the right, and then click on the method name to get the input code of the calling method.
input code of set：0x60fe47b10000000000000000000000000000000000000000000000000000000000000064  
input code of get：0x6d4ce63c

![调用合约方法](https://public.33.cn/web/storage/upload/20181112/800c6b194a04b3caacb8e74e2dbb9fd5.png "调用合约方法")

---
## 1.3 Deploy Smart Contracts Using Cli Debugging Tools
Cli is our debugging command, which makes it easy to use. Here's how to use the cli command to deploy the smart contract on the Chain33 chain and invoke the methods in the smart contract

---
>	**step1:**Deploy the smart contract on chain of Chain33 using the cli command:

    ./chain33-cli evm create -i "contract code" -c "contract owner's address" -s "contract alias"
    
    root@ubuntu055-3:/home/lcj0# ./chain33-cli evm create -i 0x608060405234801561001057600080fd5b5060df8061001f6000396000f3006080604052600436106049576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff16806360fe47b114604e5780636d4ce63c146078575b600080fd5b348015605957600080fd5b5060766004803603810190808035906020019092919050505060a0565b005b348015608357600080fd5b50608a60aa565b6040518082815260200191505060405180910390f35b8060008190555050565b600080549050905600a165627a7a72305820400d8ac26862c8658a699fc570c2a260485d7d8747b8bb9541264fdf2e7d9aeb0029 -c 15nn4D2ppUj8tmyHfdm8g4EvtqpBYUS7DM  -n "create" -s "test"
---
>	**step2：**The contract code above is the binary code generated by deploying in Remix. After successful command call, a transaction hash is generated and then used to query the transaction:

    ./chain33-cli tx query -s "transaction hash"

    root@ubuntu055-3:/home/lcj0# ./chain33-cli tx query -s 0xd11c94a0b8c03033a6b39b1ad38c4979c79099577f0ac7892079332e4b901f83
    
   *    The results returned can be seen as follows: where the name contract name is used when contract transfer or retrieval operations are involved; addr contract address, to which all operations facing the contract are operations;

---
    "ty": 601,
    "tyname": "LogContractData",
    "log": {
        "creator": "15nn4D2ppUj8tmyHfdm8g4EvtqpBYUS7DM",
        "name": "user.evm.0xd11c94a0b8c03033a6b39b1ad38c4979c79099577f0ac7892079332e4b901f83",
        "alias": "test",
        "addr": "1C8NhUNVtVqY3jhvoBHccFxNEZLvc6hjdW",
        "code": "0x6080604052600436106049576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff16806360fe47b114604e5780636d4ce63c146078575b600080fd5b348015605957600080fd5b5060766004803603810190808035906020019092919050505060a0565b005b348015608357600080fd5b50608a60aa565b6040518082815260200191505060405180910390f35b8060008190555050565b600080549050905600a165627a7a72305820400d8ac26862c8658a699fc570c2a260485d7d8747b8bb9541264fdf2e7d9aeb0029"

---
>	**step3:**Call the contract method set

    ./chain33-cli evm call -i "Input generated in Remix" -e "name of the contract" -c "caller address"
    
    ./chain33-cli evm call -i 0x60fe47b10000000000000000000000000000000000000000000000000000000000000064 -e "user.evm.0xd11c94a0b8c03033a6b39b1ad38c4979c79099577f0ac7892079332e4b901f83" -c 15nn4D2ppUj8tmyHfdm8g4EvtqpBYUS7DM
   
---
>	**step4:**When the call set is complete, the transaction hash is returned, and the result of the call using this hash query contains the following information: "caller", who has consumed "usedGas", and null, the initial value of storedData defined in solidity

    ./chain33-cli tx query -s 0x883afecd195596caab14d0923035378391b8f2e2b809b7f6ef0734da74d13297
    
    "ty": 603,
    "tyname": "LogCallContract",
    "log": {
        "caller": "15nn4D2ppUj8tmyHfdm8g4EvtqpBYUS7DM",
        "contractName": "",
        "contractAddr": "1C8NhUNVtVqY3jhvoBHccFxNEZLvc6hjdW",
        "usedGas": "20205",
        "ret": null
            }

---
>	**step5:**Call the contract method get

    ./chain33-cli evm call -i 0x6d4ce63c -e "user.evm.0xd11c94a0b8c03033a6b39b1ad38c4979c79099577f0ac7892079332e4b901f83" -c 15nn4D2ppUj8tmyHfdm8g4EvtqpBYUS7DM

---
>	**step6:** The query result value changes, you can see that the ret value for storedData changes after passing in the set method parameter to"0x0000000000000000000000000000000000000000000000000000000000000064"

    ./chain33-cli tx query -s 0x7d1bf3465ff10e48cd46c9bf6e81f81d979c6deb51befaee2fd649e768bb205f
    
    {
        "ty": 603,
        "tyname": "LogCallContract",
        "log": {
            "caller": "15nn4D2ppUj8tmyHfdm8g4EvtqpBYUS7DM",
            "contractName": "",
            "contractAddr": "1C8NhUNVtVqY3jhvoBHccFxNEZLvc6hjdW",
            "usedGas": "274",
            "ret": "0x0000000000000000000000000000000000000000000000000000000000000064"
             }

---
## 1.4 Call the JSONRPC Interface to Deploy the Smart Contract


**1** Using the input code generated by solidity contract creation, the relevant JSONRPC interface is invoked to deploy the contract on Chain33 chain. The following is an introduction to the relevant JSONRPC interface.In Chain33.Unlock I used the python call interface, and I will show the python call method below.
1)First determine the status of the wallet and call the Chain33.GetWalletStatus interface. If the wallet is locked, call the Chain33.Unlock interface to unlock the wallet

    request: http.post
    {
        "jsonrpc":"2.0",
        "id":int32,
        "method":"Chain33.UnLock",
        "params":[{"passwd":"string","walletorticket":bool,"timeout":int32}]
    }
• timeout: unlock time, default 0, means unlock forever; a non-zero value indicating that the wallet continues to be locked after a timeout, in seconds.
• walletorticket： True, unlock only the ticket function, false, unlock the entire wallet.

---
>	    The actual python script shown below, the json_payload inside is the method of the interface, session.post('http://localhost:8901', json = json_payload). The Chain33 network node that calls the requests module to construct the post data to be passed to port 8901

---
	#!/usr/bin/python
	# -*-coding:UTF-8 -*-
	import requests
    
    def Unlock(passwd,walletorticket = False,timeout = 0):
    session = requests.session()
    json_payload = {"jsonrpc": "2.0", "id": 2, "method": "Chain33.UnLock", "params": [{"passwd":passwd,"walletorticket":walletorticket,"timeout":timeout}]}
    reponse = session.post('http://localhost:8901', json = json_payload)
    dic = reponse.json()
    if (dic['error'] == None):
        if (dic['result']['msg'] == ''):
            print "Wallet unlocked successfully：{}".format(dic['result']['isOK'])
        else:
            print "Wallet unlocked failed：{}".format(dic['result']['msg'])
    else:
        print dic['error']
    
---
2）Construct deployment corresponding transaction contract, call interface "method" : "Chain33. CreateTransaction", the hash generated for signature

     http.post
     {"jsonrpc": "2.0",
    "id": int32,
    "method": "Chain33.CreateTransaction", 
    "params": [{"execer": "evm", "actionName": "CreateCall", "payload": {"code": "string",                  "note": "string",  "Fee":int64, "isCreate": bool}}]
    }
• code: remix compiled input code (in step3 above)
• note  
• fee: 1000000，to prevent Gas shortage
• isCreate: whether or not to create a contract, here fill in true

---
3）The transaction generated by the step on the signature, calls the Chain33.SignRawTx interface (corresponding contract deployer on your own main chain), and generates the hash that is sent to the Chain33 chain after the signature
   
    http.post
    {"jsonrpc":"2.0",
    "id":int32,
    "method":"Chain33.SignRawTx",
    "params":[{"addr":"string", "key":"string","txhex":"string","expire":"string", "index":int32}]
    }
• addr and key can only be entered either way
• expire：expiration time type such as "300 ms," 1.5 "h" m "string, effective unit of time for" ns ", "us", "ms", "s", "m", "h"  
• index: if the signature trading group, it is the trading serial number to be signed, starting from 1; if it is less than or equal to 0, it is all the transactions in the signature group 
• txhex：the hash string generated for the previous step

---
4）Send the signed transaction from the previous step, calling the Chain33.SendTransaction interface,
Return a string of hash values after execution. This hash value combined with prefix user.p.developer.user.evm. constituted the address of the contract, the game is as follows:
user.p.developer.user.evm.0x318638f8b0a53b4145605215a15fd33714084f6776c854634fbe9c3cd043bf47
    
     http.post
      {"jsonrpc":"2.0",
        "id":int32,
        "method":"Chain33.SendTransaction",
        "params":[{"data":"string"}]
      }
• data: the signed data

---
5）After this step, the contract is deployed on the blockchain. You can call the Chain33.GetTxByHashes interface to query the results.

    http.post
    {
        "jsonrpc":"2.0",
        "id":int32,
        "method":"Chain33.GetTxByHashes",
        "params":[{"hashes":["hashId0","hashId3","hashId2"]}] 
    }

----
**2** Using the input code generated by solidity method to invoke the contract method, invoke the method in the deployed contract on chain of Chain33 by the associated JSONRPC interface to invoke the method in the deployed contract

---
1）First determine the status of the wallet and call the Chain33.GetWalletStatus interface. If the wallet is locked, call the Chain33.Unlock interface to unlock the wallet

---
2）Construct call methods corresponding to the transaction contract, call interface "method" : "Chain33. CreateTransaction", the hash generated for signature

     http.post{"jsonrpc": "2.0", 
               "id": 2, 
               "method": "Chain33.CreateTransaction", 
               "params": [{"execer": "evm", "actionName": "CreateCall", "payload": {"code": evm_call_code, "isCreate": False,  "name": user_evm_name, "amount": 0}}]
               }
• evm_call_code：method corresponds to input code (in step5 above) 
• "isCreate"：whether to create, here fill in false
• "name":create the contract to generate the caller name, for example: user.p.developer.user.evm.0x318638f8b0a53b4145605215a15fd33714084f6776c854634fbe9c3cd043bf47

>   Call "method": "Chain33. CreateTransaction" : generated hash:

    0a54757365722e65766d2e757365722e65766d2e30783635326439356634303566363536323562636163616330626132323666323866333766396638623465656135663431353034616164663462616538376664373812462244095ea7b30000000000000000000000000000000000000000000000000000000000000021000000000000000000000000000000000000000000000000000000000000006420a08d0630eeccfec4f8c5a4fd093a2231444b5054554354704e7a5774743968476e62416d3547737462726767746f454234

---
3）The transaction generated by the step on the signature, calling the Chain33.SignRawTx interface (with its corresponding contract deployer on its own main chain), generates the hash that is sent to the Chain33 chain after the signature
>   Call the signature interface, "method":" chain33.signrawtx "to generate the signed hash: 

    0a54757365722e65766d2e757365722e65766d2e30783635326439356634303566363536323562636163616330626132323666323866333766396638623465656135663431353034616164663462616538376664373812462244095ea7b3000000000000000000000000000000000000000000000000000000000000002100000000000000000000000000000000000000000000000000000000000000641a6e080112210239522964b148480e65ce1965a18fd47e405b48596fac0f03e5e9e5a7cbe0b15f1a473045022100fd948c4d425d0052a652aa88e559df73380cda0215403853e2be028a5ba556240220077be7c71cb374868e3313896e36d8a43367cc421f5c13e8725683cec2fba15a20a08d0628d5ecd8dc0530eeccfec4f8c5a4fd093a2231444b5054554354704e7a5774743968476e62416d3547737462726767746f454234 
    
---
4）Send the signed transaction from the previous step, call the Chain33.SendTransaction interface, and return a string of hash values.
>   Call "method":" Chain33.SendTransaction "to generate the sent transaction hash for queryresults on the Chain33 chain, or on the blockchain browser.

    0x54eb29276e923d1dcea8f569ef5279302f823376a3a7bb3de23ef25c6a855c43 
    
---
5）After this step, the contract is deployed on the blockchain. You can call the Chain33.GetTxByHashes interface to query the results.

