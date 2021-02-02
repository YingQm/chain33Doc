[TOC]
# 1 League Chain Network Construction
## 1.1 Install Go Environment, Git Environment and expect
 Check whether golang and git were installed or not,if the following is displayed, neither of them were installed.
```shell
~$ go version
The program 'go' is currently not installed. You can install it by typing:
sudo apt install golang-go
~$ git
The program 'git' is currently not installed. You can install it by typing:
sudo apt install git
~$ expect
The program 'expect' is currently not installed. You can install it by typing:
sudo apt install expect
```

- Go environment installation refer to <a href="https://chain.33.cn/document/81#1.1%20Go%20%E7%8E%AF%E5%A2%83%E5%AE%89%E8%A3%85">HERE</a>


- Git environment installation refer to <a href="https://chain.33.cn/document/81#1.2%20Git%20%E7%8E%AF%E5%A2%83%E5%AE%89%E8%A3%85">HERE</a>

- expect installation
```shell
sudo apt install expect
```
 Verify expect installation
```shell
~$ expect -f
expect: option requires an argument -- 'f'
usage: expect [-div] [-c cmds] [[-f] cmdfile] [args]
```

## 1.2 Download the Plugin Source Code and Compile to Generate an Executable
The code download refer to <a href="https://chain.33.cn/document/81#2%20%E4%BB%A3%E7%A0%81%E4%B8%8B%E8%BD%BD">HERE</a>, execution result are shown below:
```shell
mkdir -p $GOPATH/src/github.com/33cn
git clone https://github.com/33cn/plugin.git $GOPATH/src/github.com/33cn/
cd plugin
make
```

Two executable files, chain33 and chain33-cli will generate under the build directory.

## 1.3 Generate 4-Node Profile
Tendermint league chain requires two profiles in addition to the chain33 profile, genesis.json and priv_validator.json.

> Genesis.json is used to configure the basic information of blockchain, including block time, chain ID, public key information, weight, name, etc.
```json
{
  "genesis_time": "0001-01-01T00:00:00Z",
  "chain_id": "test-chain-Ep9EcD",
  "validators": [
    {
      "pub_key": {
        "type": "ed25519",
        "data": "220ACBE680DF2473A0CB48987A00FCC1812F106A7390BE6B8E2D31122C992A19"
      },
      "power": 10,
      "name": ""
    }
  ],
  "app_hash": ""
}
```
> Priv_validator.json is used to configure the consensus validator information, including address, public key, and private key, the height of the last consensus, number of rounds, and phase, shown as follows:

```json
{
  "address": "02A13174B92727C4902DB099E51A3339F48BD45E",
  "pub_key": {
    "type": "ed25519",
    "data": "220ACBE680DF2473A0CB48987A00FCC1812F106A7390BE6B8E2D31122C992A19"
  },
  "last_height": 0,
  "last_round": 0,
  "last_step": 0,
  "priv_key": {
    "type": "ed25519",
    "data": "B3DC4C0725884EBB7264B92F1D8D37584A64ADE1799D997EC64B4FE3973E08DE220ACBE680DF2473A0CB48987A00FCC1812F106A7390BE6B8E2D31122C992A19"
  }
}
```

For user convenience, use the chain33-cli command-line tool to generate a profile under the current directory that specifies the number of consensus validation nodes.

- Generate 4-Node Profile
```shell
./chain33-cli valnode init_keyfile -n 4
```

- Check to see if genesis_file.json,priv_validator_x.json(x:0-3) has been generated
```shell
ls
...  genesis_file.json  priv_validator_0.json  priv_validator_1.json  priv_validator_2.json  priv_validator_3.json ...
```

## 1.4 Send Relevant File to the Specified Node

### 1.4.1 Modify Profile

configuration item interpretation refer to <a href="https://chain.33.cn/document/123">HERE</a>

- Copy ../tendermint/chain33.test.toml to the current directory
```shell
cp ../chain33.test.toml .
```
- Here our four nodes are both seed nodes, so set isSeed in [p2p] to true, and add node ip:port to the seeds and validatorNodes array in [p2p] and save them. Note these two port numbers are different.
```plain
[p2p]
seeds=["192.168.0.105:13802","192.168.0.107:13802","192.168.0.116:13802","192.168.0.137:13802"]
isSeed=true

[consensus.sub.tendermint]
validatorNodes=["192.168.0.105:46656","192.168.0.107:46656","192.168.0.116:46656","192.168.0.137:46656"]
```

### 1.4.1 Send Files to Nodes
- Copy chain33, chain33-cli, chain33.test.toml, genesis_file.json, priv_validator_x（0-3).json to the directory of the specified node;
```shell
scp chain33 chain33-cli chain33.test.toml genesis_file.json priv_validator_0.json username@node1Ip: specified path
scp chain33 chain33-cli chain33.test.toml genesis_file.json priv_validator_1.json username@node2Ip: specified path
scp chain33 chain33-cli chain33.test.toml genesis_file.json priv_validator_2.json username@node3Ip: specified path
scp chain33 chain33-cli chain33.test.toml genesis_file.json priv_validator_3.json username@node4Ip: specified path
```

### 1.4.2 Rename File priv_validator_x.json and genesis_file.json
- Login each nodes, rename the priv_validator_x.json to priv_validator.json
- Login each nodes, rename genesis_file.json under directory to genesis_file.json

## 1.5 Start the Program on Each Node
- Log in to each node and enter the following command to start the blockchain program:

```shell
nohup ./chain33 -f chain33.test.toml >> log.out 2>&1 &
```
## 1.6 Check Node Execution by chain33-cli
### 1.6.1 Check the node block synchronization status, if true, the block is synchronized
```shell
./chain33-cli net is_sync
```

### 1.6.2 Send the Transaction to Test if the Blockchain is Operating Normally
- Start by creating a wallet and an account, refer to <a href="https://chain.33.cn/document/80#1.3%20%E5%88%9B%E5%BB%BA%E9%92%B1%E5%8C%85%E4%BB%A5%E5%8F%8A%E8%B4%A6%E6%88%B7" >HERE</a>, and the execution results are shown below:

```shell
./chain33-cli account list
{
    "wallets": [
        {
            "acc": {
                "balance": "0.0000",
                "frozen": "0.0000",
                "addr": "1JfGzjz4ikQWuLyDGPL8DP9hVNUgDXaDLY"
            },
            "label": "node award"
        },
        {
            "acc": {
                "balance": "100000000.0000",
                "frozen": "0.0000",
                "addr": "1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs"
            },
            "label": "genesis"
        },
        {
            "acc": {
                "balance": "0.0000",
                "frozen": "0.0000",
                "addr": "1EqCTLRGPXYHDDUBrVUuoeqQyTnpSAMgXM"
            },
            "label": "test"
        }
    ]
}
```
- Send transfer transaction from genesis account to test account, refer to <a href="https://chain.33.cn/document/80#1.4.2%20%E5%8F%91%E9%80%81%E8%BD%AC%E8%B4%A6%E4%BA%A4%E6%98%93" >HERE</a>,and the execution results are shown below:

```shell
./chain33-cli send bty transfer -a 1000 -t 1EqCTLRGPXYHDDUBrVUuoeqQyTnpSAMgXM -n "first transfer" -k 1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs
0x040224c373b189ccd7a6e2c5a123a5a9f743e4905ad112f0cf5957145db7bdd4
```

- Search for trading results, refer to <a href="https://chain.33.cn/document/80#1.4.3%20%E6%9F%A5%E8%AF%A2%E4%BA%A4%E6%98%93%E7%BB%93%E6%9E%9C">HERE</a>, and the execution results are shown below:

```shell
./chain33-cli tx query -s 0x040224c373b189ccd7a6e2c5a123a5a9f743e4905ad112f0cf5957145db7bdd4
{
    "tx": {
        "execer": "coins",
        "payload": {
            "transfer": {
                "cointoken": "",
                "amount": "100000000000",
                "note": "first transfer",
                "to": "1EqCTLRGPXYHDDUBrVUuoeqQyTnpSAMgXM"
            },
            "ty": 1
        },
       .........
        "fee": "0.0010",
        "expire": 1550563096,
        "nonce": 3159930318345275859,
        "to": "1EqCTLRGPXYHDDUBrVUuoeqQyTnpSAMgXM",
        "from": "1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs",
        "hash": "0x040224c373b189ccd7a6e2c5a123a5a9f743e4905ad112f0cf5957145db7bdd4"
    },
    ............
    "height": 1,
    "index": 1,
    "blocktime": 1550562976,
    "amount": "1000.0000",
    "fromaddr": "1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs",
    "actionname": "transfer",
    "assets": [
        {
            "exec": "coins",
            "symbol": "BTY",
            "amount": 100000000000
        }
    ]
}

```

### 1.6.3 Check the Status of Node Consensus Synchronization. If true, the Node Consensus Synchronization is Normal
```shell
./chain33-cli valnode is_sync
```

### 1.6.4 Check the Current State of the Node, Including Address, Public Key, Weight, Current Cumulative Value

> Note: the node with the largest cumulative value gets the right to propose and package of the next height or the next round. If the maximum cumulative value of multiple nodes is equal, the node with the address of the highest dictionary order gets the right.

```shell
./chain33-cli valnode nodes
[
    {
        "Address": "N8YIgjPnD9FlSYhJcaverfpJ8Ek=",
        "PubKey": "DYz9SWwgwU/I8KFVgzMYyvdXptlEGMAAuUVLGhcqJ+E=",
        "VotingPower": 10,
        "Accum": -20
    },
    {
        "Address": "WuW4f/7jm6UGlRJ4DXCv4Ryt5Yc=",
        "PubKey": "09Fpp0+3uetv//fGSOG3xKSw6ZIsxLSmsBhcDTUelIQ=",
        "VotingPower": 10,
        "Accum": -20
    },
    {
        "Address": "dA6vreo61lcoX6UCzfn8uriiYgM=",
        "PubKey": "wk5aSXzS3m6L0ZeL0jA56oFnxPHMqLsX85RfFT3Boxc=",
        "VotingPower": 10,
        "Accum": 20
    },
    {
        "Address": "dUxa2Rzk4FtJo/KP+WDNdOcfHvY=",
        "PubKey": "JvVmZNQsyjTMWfjbPDWj//obpmK/WwgOc3Q4YSudPPE=",
        "VotingPower": 10,
        "Accum": 20
    }
]

```
### 1.6.5 Query Node Status
```shell
./chain33-cli net peer_info
{
    "peers": [
        {
            "addr": "192.168.0.137",
            "port": 13802,
            "name": "035bd8a1f1aba3ef53cac434530d611d5e8a9527980ab3a5410c5f2fddb1a83194",
            "mempoolSize": 0,
            "self": false,
            "header": {
                "version": 0,
                "parentHash": "0xc8799befacd9709a5f4dfa68d6fd53a37ccce83352997a132adfed7f46747757",
                "txHash": "0xd7dabfb237a791aa9d907d10f4e2d8578943b407a0af2443a7ac50492afcd1ec",
                "stateHash": "0xafec60a0a5931b30ddd0cf849fea1a72ef8687d41030a3aa8adb83c947f78129",
                "height": 1,
                "blockTime": 1550562976,
                "txCount": 2,
                "hash": "0x9ebd6aebcb764d6d381a948ff4534edd7e3fa214a4361a43311b9bf880be2c08",
                "difficulty": 0
            }
        },
        {
            "addr": "192.168.0.107",
            "port": 13802,
            "name": "0294cfe779fbf34225ec89d278f80658d93a4e82075a4ca1ec0b4456b63ecbc6f1",
            "mempoolSize": 0,
            "self": false,
            "header": {
                "version": 0,
                "parentHash": "0xc8799befacd9709a5f4dfa68d6fd53a37ccce83352997a132adfed7f46747757",
                "txHash": "0xd7dabfb237a791aa9d907d10f4e2d8578943b407a0af2443a7ac50492afcd1ec",
                "stateHash": "0xafec60a0a5931b30ddd0cf849fea1a72ef8687d41030a3aa8adb83c947f78129",
                "height": 1,
                "blockTime": 1550562976,
                "txCount": 2,
                "hash": "0x9ebd6aebcb764d6d381a948ff4534edd7e3fa214a4361a43311b9bf880be2c08",
                "difficulty": 0
            }
        },
        {
            "addr": "192.168.0.116",
            "port": 13802,
            "name": "0373d41c98e896bebfe37f7e831e848da1889f88574a7622d112511caf07c7d299",
            "mempoolSize": 0,
            "self": false,
            "header": {
                "version": 0,
                "parentHash": "0xc8799befacd9709a5f4dfa68d6fd53a37ccce83352997a132adfed7f46747757",
                "txHash": "0xd7dabfb237a791aa9d907d10f4e2d8578943b407a0af2443a7ac50492afcd1ec",
                "stateHash": "0xafec60a0a5931b30ddd0cf849fea1a72ef8687d41030a3aa8adb83c947f78129",
                "height": 1,
                "blockTime": 1550562976,
                "txCount": 2,
                "hash": "0x9ebd6aebcb764d6d381a948ff4534edd7e3fa214a4361a43311b9bf880be2c08",
                "difficulty": 0
            }
        },
        {
            "addr": "192.168.0.105",
            "port": 13802,
            "name": "03da6dec2f03958caa104fa79c58c49d95c343118b49ab959791d144d7b69db71b",
            "mempoolSize": 0,
            "self": true,
            "header": {
                "version": 0,
                "parentHash": "0xc8799befacd9709a5f4dfa68d6fd53a37ccce83352997a132adfed7f46747757",
                "txHash": "0xd7dabfb237a791aa9d907d10f4e2d8578943b407a0af2443a7ac50492afcd1ec",
                "stateHash": "0xafec60a0a5931b30ddd0cf849fea1a72ef8687d41030a3aa8adb83c947f78129",
                "height": 1,
                "blockTime": 1550562976,
                "txCount": 2,
                "hash": "0x9ebd6aebcb764d6d381a948ff4534edd7e3fa214a4361a43311b9bf880be2c08",
                "difficulty": 0
            }
        }
    ]
}
```
### 1.6.6 Query Consensus Information at a Certain Height
```shell
./chain33-cli valnode info -t 1
{
    #Condition committed at current height(in this case height 1)
    "SeenCommit": {
        "BlockID": {
            "Hash": "GjOepWMTxSLZeZ196ciNiS4e3kU="
        },
        #Precommit condition
        "Precommits": [
            {
                "ValidatorAddress": "N8YIgjPnD9FlSYhJcaverfpJ8Ek=",
                "Height": 1,
                "Timestamp": 1550562976822045939,
                "Type": 2,
                "BlockID": {
                    "Hash": "GjOepWMTxSLZeZ196ciNiS4e3kU="
                },
                "Signature": "PPw6MYBO7FMgHOWheKVZzxQ1slPizzCq+aivr+cqqnrjKoQv4sLF0OhRiNiGSP9FBQEo/cKFR3laevuwo5SxBA=="
            },
            {
                "ValidatorAddress": "WuW4f/7jm6UGlRJ4DXCv4Ryt5Yc=",
                "ValidatorIndex": 1,
                "Height": 1,
                "Timestamp": 1550562976830780017,
                "Type": 2,
                "BlockID": {
                    "Hash": "GjOepWMTxSLZeZ196ciNiS4e3kU="
                },
                "Signature": "Gz8yGVSa3TLOaETLpZuqlt5t6ue8EOevXcLNgGMk2A9OoNOhDjGQ81tMyif1r1utnuFZ5Dr2tOV6FUUV80eQBw=="
            },
            {},
            {
                "ValidatorAddress": "dUxa2Rzk4FtJo/KP+WDNdOcfHvY=",
                "ValidatorIndex": 3,
                "Height": 1,
                "Timestamp": 1550562949920064092,
                "Type": 2,
                "BlockID": {
                    "Hash": "GjOepWMTxSLZeZ196ciNiS4e3kU="
                },
                "Signature": "9L409a9Gu2tf+ahkPDxDgGGY1z7pGiS6RO2FNwLMmEh3I//nn9d2OyK08TKbd5RXwm0+3es3I4zw2ulamKCSBQ=="
            }
        ]
    },
    #Condition committed at last height(in this case height 0)
    "LastCommit": {},
    #Current consensus status
    "State": {
        "ChainID": "chain33-l5m0ho",
        "LastBlockHeight": 1,
        "LastBlockTotalTx": 1,
        "LastBlockTime": 1550562976729168766,
        #Status of current consensus verification nodes
        "Validators": {
            "Validators": [
                {
                    "Address": "N8YIgjPnD9FlSYhJcaverfpJ8Ek=",
                    "PubKey": "DYz9SWwgwU/I8KFVgzMYyvdXptlEGMAAuUVLGhcqJ+E=",
                    "VotingPower": 10,
                    "Accum": -20
                },
                {
                    "Address": "WuW4f/7jm6UGlRJ4DXCv4Ryt5Yc=",
                    "PubKey": "09Fpp0+3uetv//fGSOG3xKSw6ZIsxLSmsBhcDTUelIQ=",
                    "VotingPower": 10,
                    "Accum": -20
                },
                {
                    "Address": "dA6vreo61lcoX6UCzfn8uriiYgM=",
                    "PubKey": "wk5aSXzS3m6L0ZeL0jA56oFnxPHMqLsX85RfFT3Boxc=",
                    "VotingPower": 10,
                    "Accum": 20
                },
                {
                    "Address": "dUxa2Rzk4FtJo/KP+WDNdOcfHvY=",
                    "PubKey": "JvVmZNQsyjTMWfjbPDWj//obpmK/WwgOc3Q4YSudPPE=",
                    "VotingPower": 10,
                    "Accum": 20
                }
            ],
            #The proposer of the next height(in this case height 2),Accum is the calculated result in the selection of proposer, which will be used for the comparison in the next selection
            "Proposer": {
                "Address": "WuW4f/7jm6UGlRJ4DXCv4Ryt5Yc=",
                "PubKey": "09Fpp0+3uetv//fGSOG3xKSw6ZIsxLSmsBhcDTUelIQ=",
                "VotingPower": 10,
                "Accum": -20
            }
        },
        #The newly generated height(in this case height 1) node validate consensus situation
        "LastValidators": {
            "Validators": [
                {
                    "Address": "N8YIgjPnD9FlSYhJcaverfpJ8Ek=",
                    "PubKey": "DYz9SWwgwU/I8KFVgzMYyvdXptlEGMAAuUVLGhcqJ+E=",
                    "VotingPower": 10,
                    "Accum": -30
                },
                {
                    "Address": "WuW4f/7jm6UGlRJ4DXCv4Ryt5Yc=",
                    "PubKey": "09Fpp0+3uetv//fGSOG3xKSw6ZIsxLSmsBhcDTUelIQ=",
                    "VotingPower": 10,
                    "Accum": 10
                },
                {
                    "Address": "dA6vreo61lcoX6UCzfn8uriiYgM=",
                    "PubKey": "wk5aSXzS3m6L0ZeL0jA56oFnxPHMqLsX85RfFT3Boxc=",
                    "VotingPower": 10,
                    "Accum": 10
                },
                {
                    "Address": "dUxa2Rzk4FtJo/KP+WDNdOcfHvY=",
                    "PubKey": "JvVmZNQsyjTMWfjbPDWj//obpmK/WwgOc3Q4YSudPPE=",
                    "VotingPower": 10,
                    "Accum": 10
                }
            ],
            #The newly generated height(in this case height 1),Accum is the calculated result in the selection of proposer, which will be used for the comparison in the next selection
            "Proposer": {
                "Address": "N8YIgjPnD9FlSYhJcaverfpJ8Ek=",
                "PubKey": "DYz9SWwgwU/I8KFVgzMYyvdXptlEGMAAuUVLGhcqJ+E=",
                "VotingPower": 10,
                "Accum": -30
            }
        },
        #The last height consensus validator changed 
        "LastHeightValidatorsChanged": 1,
        #Consensus parameters
        "ConsensusParams": {
            "BlockSize": {
                "MaxBytes": 22020096,
                "MaxTxs": 100000,
                "MaxGas": -1
            },
            "TxSize": {
                "MaxBytes": 10240,
                "MaxGas": -1
            },
            "BlockGossip": {
                "BlockPartSizeBytes": 65536
            },
            "EvidenceParams": {
                "MaxAge": 100000
            }
        },
         #The last height consensus parameters changed 
        "LastHeightConsensusParamsChanged": 1
    },
    #The newly generated proposal information for height(in this case height 1)
    "Proposal": {
        "height": 1,
        "timestamp": 1550562976729939670,
        "POLRound": -1,
        "POLBlockID": {},
        "signature": "1YieRBNBu0L1vWspJAj7/Hd1cDLTvjKvghLoX1mIvKmzkqrT3UehfPWtY4p3UxgVngFz256Zz6pbeZIAowRLDA==",
        "blockhash": "GjOepWMTxSLZeZ196ciNiS4e3kU="
    },
    #The newly generated height(in this case height 1)block information
    "block": {
        "header": {
            "chainID": "chain33-l5m0ho",
            "height": 1,
            "time": 1550562976729168766,
            "numTxs": 1,
            "lastBlockID": {},
            "totalTxs": 1,
            "validatorsHash": "t+4pc+omQBGNlI4ZkoIgKRkjxff8TbljwDKKWirwVvc=",
            "consensusHash": "/GlQqG9MV+dJNFIoxo0NOSvVUDU="
        },
        "evidence": {},
        #Commit information at a higher height (in this case, a height of 0)
        "lastCommit": {},
        #The newly generated height(in this case height 1)proposes the node address
        "proposerAddr": "N8YIgjPnD9FlSYhJcaverfpJ8Ek="
    }
}

```