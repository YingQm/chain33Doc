# Development Environment Preparation

[TOC]

## 1 Development Environment Installation

### 1.1 Go Environment Installation

Go Language installation package download address: <a href="https://golang.google.cn/dl/" target="_blank">https://golang.google.cn/dl/</a>

The recommended installation version is 1.13.4, and the corresponding package name of each operating system is:

Operating system |  Package name
---|---
Windows | go1.13.4.windows-amd64.msi
Linux | go1.13.4.linux-amd64.tar.gz
Mac | go1.13.4.darwin-amd64.tar.gz

#### Linux/Mac Installation

Take Linux for example

- Download binary packages: go1.13.4.linux-amd64.tar.gz

- Uncompress the downloaded binary package to /usr/local 

```shell
tar -C /usr/local -xzf go1.13.4.linux-amd64.tar.gz
```

- Add /usr/local/go/bin to PATH Environment Variables, and set GOPATH Environment Variables.

```shell
export PATH=$PATH:/usr/local/go/bin
export GOPATH=~/gopath
```

#### Windows Installation

Open the corresponding MSI file for installation

Default installation is in c:\Go directory，add c:\Go\bin to PATH Environment Variables

Set GOPATH environment variables, such as D:\ GOPATH at the same time

### 1.2 Git Environmental Installation

Install the latest version of Git

#### Installation on Linux 

Install using the basic package management tools included with the Linux release version

Fedora-based release version using yum

```shell
sudo yum install git
```

Debian release version based use apt-get

```shell
sudo apt-get install git
```

#### Installation on Windows 

Open Git official download address <a href="http://git-scm.com/download/win" target="_blank">http://git-scm.com/download/win</a>, download will start automatically and install manually after downloading

#### Installation on  Mac

Open Git official download address <a href="http://git-scm.com/download/mac" target="_blank">http://git-scm.com/download/mac</a>, download and install

### 1.3 IDE Installation

#### LiteIDE

LiteIDE is an open source, cross-platform, lightweight Go language integrated development environment

Installation package download address: <a href="https://sourceforge.net/projects/liteide/files" target="_blank">https://sourceforge.net/projects/liteide/files</a>

Select the appropriate installation package according to the operating system and uncompress it to complete the installation

#### VSCode

VSCode is an open source, cross-platform lightweight code editor, integrated with Go language development plug-ins

Installation package download address: <a href="https://code.visualstudio.com/Download" target="_blank">https://code.visualstudio.com/Download</a>

Select the appropriate installation package according to the operating system

> Install the Go language plug-in

In the VSCode interface, use the shortcut Ctrl+Shift+x to open the extension command panel, type "go" to search, and then select "go for Visual Studio Code" plug-in to install

Open the menu item File ->Preferences-> Settings, open the settins.json file to modify User Settings, and you can set the commonly used configuration of Go

```ini
{
    "go.goroot": "D:\\Go",
    "go.gopath": "D:\\gopath"
}
```

#### GoLand

GoLand is an ergonomic commercial IDE designed by JetBrains to provide Go developers with paid software

Download from official website: <a href="https://www.jetbrains.com/go/" target="_blank">https://www.jetbrains.com/go/</a>

## 2 Code Download

Use the Git command to download code locally, taking Linux as an example:

```shell
mkdir -p $GOPATH/src/github.com/33cn
git clone https://github.com/33cn/chain33.git $GOPATH/src/github.com/33cn/chain33
git clone https://github.com/33cn/plugin.git $GOPATH/src/github.com/33cn/plugin
```

You can switch to the trunk branch

```shell
cd $GOPATH/src/github.com/33cn/plugin
git checkout master
```

## 3 Environment Configuration

Chain33 runtime environment is customized by its configuration files, you can refer to the configuration file in the code <a href="https://github.com/33cn/chain33/blob/master/cmd/chain33/chain33.toml" target="_blank">cmd/chain33/chain33.toml</a>,Following is a list of commonly used environmental configurations

### 3.1 Local Environment Configuration

Local environment means that Chain33 runs on the local private network and is only used for local testing

Here we introduce how to build a private Chain33 blockchain network

![Local Environment](https://public.zhaobi.tech/web/storage/upload/20190717/d9146257f02dd91fa2090d9855cffde4.png)

First, modify the configuration file. All three nodes have the same configuration file. Here are just some of the differences of cmd/chain33/chain33.toml 

```ini
# This node connects to the local private network
Title="local"

[p2p]
# Node information in the local private network
seeds=["10.0.2.11:13802", "10.0.2.12:13802", "10.0.2.13:13802"]
# Whether to add the system's built-in nodes to the seeds list
innerSeedEnable=false
# Whether to add the node on the official github to the seeds list
useGithub=false

[rpc]
jrpcBindAddr=":8801"
grpcBindAddr=":8802"
whitelist=["*"]
enableTLS=false

[consensus]
# Creation address changed to private address
# The creation address can use the address in this example, the corresponding private key is 3990969DF92A5914F7B71EEB9A4E58D6E255F32BF042FEA5318FC8B3D50EE6E8 
genesis="1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs"

# Only leave the following two items, and delete all other consensus related configurations
[consensus.sub.solo]
genesis="1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs"
hotkeyAddr="1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs"
```

Then start Chain33 on three nodes

```shell
nohup ./chain33 -f chain33.toml &> console.out&
```

### 3.2 Test Chain Configuration

Test chain refers to BTY test network, the block transaction query website is: <a href="https://testnet.bityuan.com" target="_blank">https://testnet.bityuan.com</a>

The configuration file is <a href="https://github.com/33cn/chain33/blob/master/cmd/chain33/chain33.toml" target="_blank">cmd/chain33/chain33.toml</a>

```ini
Title="chain33"
# Access test chain
TestNet=true
```

### 3.3 Main Chain Configuration

Main chain refers to BTY public network, the block transaction query website is: <a href="https://mainnet.bityuan.com" target="_blank">https://mainnet.bityuan.com</a>

The configuration file is  <a href="https://github.com/33cn/chain33/blob/master/cmd/chain33/bityuan.toml" target="_blank">cmd/chain33/bityuan.toml</a>

```ini
# Access main chain
Title="bityuan"
```

### 3.4 Parallel Chain Configuration

#### 3.4.1 Configuration Files

The parallel chain is attached to the main chain, and the parallel chain node needs to be connected to the main chain node, where the isRecordBlockSequence configuration item on the main chain node needs to be set

Here is the configuration of the main chain nodes, here only shows how they differ from  cmd/chain33/bityuan.toml

```ini
[blockchain]
# Whether to store   block sequence
isRecordBlockSequence=true
```

<a href="https://github.com/33cn/plugin/blob/master/chain33.para.toml" target="_blank">plugin/chain33.para.toml</a> is the configuration file for the parallel chain nodes, with the following parameters:
Title: the name of the parallel chain, user.p. is the fixed prefix, developer can be modified according to users own requirements
startHeight: Starting from the certain height of the main chain to synchronize the data, for the newly built parallel chain, it is recommended to start from the height closest to the highest of the main chain to reduce the synchronization time
```ini
Title="user.p.developer."

[consensus.sub.para]
ParaRemoteGrpcClient = "118.31.177.1:8802"
#Specify a block starting at a certain height of the main chain, and if multiple parallel chain nodes are deployed, make sure the heights in both profiles are the same.
#Recommended configuration, can be equipped with the current height of the main chain and slightly smaller, use blockchain browser to see the current height of the main network
# https://mainnet.bityuan.com/all/index
# For example, the current configuration is 284110, and here can be configured into 284100. It is not recommended to make a big difference, which will generate a lot of meaningless empty blocks
startHeight=1620000
```

#### 3.4.2 Chain33 Chain environment

- The simplest parallel chain requires two nodes (which can support multiple VMs),such as node A (IP: 192.168.0.104) and node B (IP: 192.168.0.159). Node A is the main chain node, which links the main chain network and parallel chain nodes. Node B is a parallel chain node, which is used to request blocks in the main network from node A, and take out the transactions belonging to this parallel chain, package them on the parallel chain for execution.
- The ports used by nodes A and B are 8801,8802,8901,8902,13802. Ensure normal access to these ports.
  
- Main chain node (node A): 8801，8802，13802端口
  
    8801:   JsonRpc Service port

    8802:   Grpc Service port

    13802: P2P service ports between nodes

- Parallel chain node (node A): 8901， 8902 Port
  
    8901:   JsonRpc Service port

    8902:   Grpc Service port


![env diagram](https://public.zhaobi.tech/web/storage/upload/20190717/00b56b768239a2d14b45bcb4607f4b67.jpg "env diagram")

### 3.4.3 Run Main/Parallel Chain Nodes

---
> Run the main chain node

Step 1: download the compiled main chain program, and uncompress it into the main chain A node directory
Step 2: start the process command

    nohup ./chain33 -f chain33.bty.toml >>  bty.out&
Step 3: check synchronization

    root@ubuntu055-1:/home/lcj1# ./chain33-cli net is_sync
	true

Step 4: view the main network information

	   root@ubuntu055-3:/home/lcj0# ./chain33-cli net peer_info
	{
		"peers": [
			{
				"addr": "192.168.0.104",
				"port": 13802,
				"name": "02df13954f1f8732295a02b552673b04aeea04eb3843a621f4c90f64efc05896ea",
				"mempoolSize": 0,
				"self": true,
				"header": {
					"version": 0,
					"parentHash": "0x5ec3c1f9bb1f7c5fc213f83266266723fa40d11eacd9164a92dec225cd95d440",
					"txHash": "0xc73f1f2c809257d0222b16198c6d85d74e25d6d9ab72a2c99e88922f234d6a00",
					"stateHash": "0x6d29c939e6c1002ce06c3c32ded6cead08dd4cd67218ede45b4936e10d8ac84d",
					"height": 643,
					"blockTime": 1542163168,
					"txCount": 1,
					"hash": "0xd035c763d267d9070fa2e4d921dc03150897ed7c977d0abc34ae1c2768ab039a",
					"difficulty": 0
				}
			}
		]
	}
---
> Run parallel chain nodes

Step 1: download the compiled parallel chain program, uncompress it into the parallel chain B node directory, and modify the configuration file

> mainnetJrpcAddr=http://192.168.0.104:8801  

> `ParaRemoteGrpcClient` change to the IP address of the actual main chain node A. This configuration makes the parallel chain to request the block to port 8802 of main chain node A
> ParaRemoteGrpcClient = "192.168.0.1:8802"

Step 2: start the process command

	nohup ./chain33 -f chain33.para.toml >> para.out&

Step 3: check synchronization

	./chain33-cli net is_sync
	true

### 3.4.4 Cli Command Demo

- You can use the cli debug command on chain33 to manipulate the relevant interfaces for a quick start

---
    Available Commands:
        account     Account management
        block       Get block header or body info
        close       Close chain33
        coins       Construct system coins transactions
        config      Configuration
        evm         EVM contracts operation
        exec        Executor operation
        help        Help about any command
        mempool     Mempool management
        net         Net operation
        privacy     Privacy transaction management
        relay       Cross chain relay management
        retrieve    Wallet retrieve operation
        seed        Seed management
        send        Send transaction in one move
        stat        Coin statistic
        ticket      Ticket management
        token       Token management
        trade       Token trade management
        tx          Transaction management
        version     Get node version
        wallet      Wallet management
        
- Only part of the commands are shown here

-  **Create wallet**，`the seeds must be kept and not disclosed to others`  
step1:`create seeds`

---
    root@ubuntu055-3:/home/lcj0# ./chain33-cli seed generate -l 0
    {
    "seed": "page patch story blouse ill sense despair mail praise prosper session among offer cheese wood"   
    }

---  
 step2:`save seeds`，when creating the wallet -p is followed by the password for the wallet

---
    root@ubuntu055-3:/home/lcj0# ./chain33-cli seed save -p fzm123456 -s "page patch story blouse ill sense despair mail praise prosper session among offer cheese wood"
    {
    "isOK": true,
    "msg": ""
    }  
  
---- 
*   **Check wallet status**  

---
    root@ubuntu055-3:/home/lcj0# ./chain33-cli wallet status
    {
        "isWalletLock": true,
        "isAutoMining": false,
        "isHasSeed": true,
        "isTicketLock": true
    }

*   **Unlock wallet**, the password after -p is the password that was set when the wallet was created above

---
    root@ubuntu055-3:/home/lcj0# ./chain33-cli wallet unlock -p fzm123456
    {
        "isOK": true,
        "msg": ""
    }  
    
*   **Create account address**, where -l is followed by label

---
    root@ubuntu055-3:/home/lcj0# ./chain33-cli account create -l test
    {
        "acc": {
            "balance": "0.0000",
            "frozen": "0.0000",
            "addr": "1HEuPSPCk9ZvyBzsp5e9y5nvySs2Qxijek"
        },
        "label": "test"
    }
    
*   **Address balance query**, where -a queries the address -e executor contract, the following is the command to view the balance of the coins contract

---
    root@ubuntu055-3:/home/lcj0# ./chain33-cli account balance -a 15nn4D2ppUj8tmyHfdm8g4EvtqpBYUS7DM -e coins
    {
        "balance": "500.0590",
        "frozen": "0.0000",
        "addr": "15nn4D2ppUj8tmyHfdm8g4EvtqpBYUS7DM"
    }
    
*   **Export of wallet private key**，-a account address in the wallet

----
    root@ubuntu055-3:/home/lcj0# ./chain33-cli account dump_key -a 15nn4D2ppUj8tmyHfdm8g4EvtqpBYUS7DM
    {
     "data": "0x1d265f4dbb202b4fc5e24ffdc96852a6e0834dbee7eb4eebd476b171f7cb0baa"
    }
    
---
*   **Import of wallet private key**，-k private key corresponding to the address -l account label
    
---
    root@ubuntu055-3:/home/lcj0# ./chain33-cli account import_key -k 0x1d265f4dbb202b4fc5e24ffdc96852a6e0834dbee7eb4eebd476b171f7cb0baa -l test222
        {
            "acc": {
                "balance": "500.0590",
                "frozen": "0.0000",
                "addr": "15nn4D2ppUj8tmyHfdm8g4EvtqpBYUS7DM"
            },
            "label": "test222"
        }
        
*   **bty send_exec Build a transaction that transfers to the specified executor at the specified address**

---
Step1: construct the transaction, -t "transfer target account", -a "transfer amount", -n "note record", and return a string of hash to be signed

    root@ubuntu055-3:/home/lcj0# ./chain33-cli coins transfer -t 1HEuPSPCk9ZvyBzsp5e9y5nvySs2Qxijek -n "bty transfer to " -a 1
    
    0a05636f696e73123f18010a3b1080c2d72f1a10627479207472616e7366657220746f20222231484575505350436b395a7679427a737035653979356e76795373325178696a656b20a08d0630b6bde8c09df69dfb523a2231484575505350436b395a7679427a737035653979356e76795373325178696a656b

Step2: sign transaction, -a "signed account - transferee" -d "unsigned transaction string" -a "signed address "/-k" signed private key "-e" timeout (default: 120 seconds) ", returns a list of signed hashes that need to be sent to the chain

    root@ubuntu055-3:/home/lcj0# ./chain33-cli wallet sign -a 15nn4D2ppUj8tmyHfdm8g4EvtqpBYUS7DM -d 0a05636f696e73123f18010a3b1080c2d72f1a10627479207472616e7366657220746f20222231484575505350436b395a7679427a737035653979356e76795373325178696a656b20a08d0630b6bde8c09df69dfb523a2231484575505350436b395a7679427a737035653979356e76795373325178696a656b 
    
    0a05636f696e73123f18010a3b1080c2d72f1a10627479207472616e7366657220746f20222231484575505350436b395a7679427a737035653979356e76795373325178696a656b1a6d08011221024e8bcbc6bc079df8f12de07cfd5ea002c425b665c86da19257af8d35ac0c55631a4630440220567a97dde98ee4ea6afb6bd96ed212976f632dbba82286d9fcd33c4b38f4d2e702206b012ed3b0d60cf518d33d632ab07f5fbbbae7a9559416d7e523e67ed865c39a20a08d06288eaa85df0530b6bde8c09df69dfb523a2231484575505350436b395a7679427a737035653979356e76795373325178696a656b  
    
---    
Step3: send transaction, -d "hash string returned after signature"

    root@ubuntu055-3:/home/lcj0# ./chain33-cli wallet send -d 0a05636f696e73123f18010a3b1080c2d72f1a10627479207472616e7366657220746f20222231484575505350436b395a7679427a737035653979356e76795373325178696a656b1a6d08011221024e8bcbc6bc079df8f12de07cfd5ea002c425b665c86da19257af8d35ac0c55631a4630440220567a97dde98ee4ea6afb6bd96ed212976f632dbba82286d9fcd33c4b38f4d2e702206b012ed3b0d60cf518d33d632ab07f5fbbbae7a9559416d7e523e67ed865c39a20a08d06288eaa85df0530b6bde8c09df69dfb523a2231484575505350436b395a7679427a737035653979356e76795373325178696a656b
    
    0x87484aaa79e7116783ebda48ff86a1f54386835908eb2c03a942b552a46132fe

**Step4: Query specific transaction information based on the transaction hash**  

        root@ubuntu055-3:/home/lcj0# ./chain33-cli tx query -s 0x87484aaa79e7116783ebda48ff86a1f54386835908eb2c03a942b552a46132fe
    {
        "tx": {
            "execer": "coins",
            "payload": {
                "Value": {
                    "Transfer": {
                        "amount": 100000000,
                        "note": "bty transfer to ",
                        "to": "1HEuPSPCk9ZvyBzsp5e9y5nvySs2Qxijek"
                    }
                },
                "ty": 1
            },
            "rawpayload": "0x18010a3b1080c2d72f1a10627479207472616e7366657220746f20222231484575505350436b395a7679427a737035653979356e76795373325178696a656b",
            "signature": {
                "ty": 1,
                "pubkey": "0x024e8bcbc6bc079df8f12de07cfd5ea002c425b665c86da19257af8d35ac0c5563",
                "signature": "0x30440220567a97dde98ee4ea6afb6bd96ed212976f632dbba82286d9fcd33c4b38f4d2e702206b012ed3b0d60cf518d33d632ab07f5fbbbae7a9559416d7e523e67ed865c39a"
            },
            "fee": "0.0010",
            "expire": 1541494030,
            "nonce": 5978097161099419318,
            "to": "1HEuPSPCk9ZvyBzsp5e9y5nvySs2Qxijek",
            "from": "15nn4D2ppUj8tmyHfdm8g4EvtqpBYUS7DM"
        },
        "receipt": {
            "ty": 2,
            "tyname": "ExecOk",
            "logs": [
                {
                    "ty": 2,
                    "tyname": "LogFee",
                    "log": {
                        "prev": {
                            "currency": 0,
                            "balance": "50005900000",
                            "frozen": "0",
                            "addr": "15nn4D2ppUj8tmyHfdm8g4EvtqpBYUS7DM"
                        },
                        "current": {
                            "currency": 0,
                            "balance": "50005800000",
                            "frozen": "0",
                            "addr": "15nn4D2ppUj8tmyHfdm8g4EvtqpBYUS7DM"
                        }
                    },
                    "rawlog": "0x0a2b10e0f5d5a4ba01222231356e6e3444327070556a38746d794866646d38673445767471704259555337444d122b10c0e8cfa4ba01222231356e6e3444327070556a38746d794866646d38673445767471704259555337444d"
                },
                {
                    "ty": 3,
                    "tyname": "LogTransfer",
                    "log": {
                        "prev": {
                            "currency": 0,
                            "balance": "50005800000",
                            "frozen": "0",
                            "addr": "15nn4D2ppUj8tmyHfdm8g4EvtqpBYUS7DM"
                        },
                        "current": {
                            "currency": 0,
                            "balance": "49905800000",
                            "frozen": "0",
                            "addr": "15nn4D2ppUj8tmyHfdm8g4EvtqpBYUS7DM"
                        }
                    },
                    "rawlog": "0x0a2b10c0e8cfa4ba01222231356e6e3444327070556a38746d794866646d38673445767471704259555337444d122b10c0a6f8f4b901222231356e6e3444327070556a38746d794866646d38673445767471704259555337444d"
                },
                {
                    "ty": 3,
                    "tyname": "LogTransfer",
                    "log": {
                        "prev": {
                            "currency": 0,
                            "balance": "0",
                            "frozen": "0",
                            "addr": "1HEuPSPCk9ZvyBzsp5e9y5nvySs2Qxijek"
                        },
                        "current": {
                            "currency": 0,
                            "balance": "100000000",
                            "frozen": "0",
                            "addr": "1HEuPSPCk9ZvyBzsp5e9y5nvySs2Qxijek"
                        }
                    },
                    "rawlog": "0x0a24222231484575505350436b395a7679427a737035653979356e76795373325178696a656b12291080c2d72f222231484575505350436b395a7679427a737035653979356e76795373325178696a656b"
                }
            ]
        },
        "height": 4751,
        "index": 0,
        "blocktime": 1541493930,
        "amount": "1.0000",
        "fromaddr": "15nn4D2ppUj8tmyHfdm8g4EvtqpBYUS7DM",
        "actionname": "transfer"
    }
	

## 4 Deploy 4 Nodes on a Single Docker Machine
> The following operations are based on ubuntu16.04

### 4.1 Docker Installation
```bash
curl -fsSL https://get.docker.com/ | sh
```

> Version verification:
```bash
docker -v  
Docker version 17.11.0-ce, build 1caf76c
```

### 4.2 Install Docker-compose
```bash
curl -L https://get.daocloud.io/docker/compose/releases/download/1.21.0/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose  
chmod +x /usr/local/bin/docker-compose
```

### 4.3 Download Chain33 Program
```bash
wget https://github.com/33cn/plugin/releases/download/v6.1.0/chain33_6.1.0_linux.tar.gz
tar -zxvf chain33_6.1.0_linux.tar.gz
```

### 4.4 Configure Dockerfile
```bash
FROM ubuntu:16.04

WORKDIR /root
COPY chain33 chain33
COPY chain33-cli chain33-cli
COPY chain33.toml ./

CMD ["/root/chain33", "-f", "/root/chain33.toml"]
```

### 4.5 Configure Docker-compose.yml File
```bash
version: '3'

services:
  chain33:
    build:
      context: .

  chain32:
    build:
      context: .

  chain31:
    build:
      context: .

  chain30:
    build:
      context: .
```

### 4.6 Write the Startup Script Docker-compose.sh
```bash
#!/usr/bin/env bash

set -e
set -o pipefail

# os: ubuntu16.04 x64

PWD=$(cd "$(dirname "$0")" && pwd)
export PATH="$PWD:$PATH"

NODE3="${1}_chain33_1"
CLI="docker exec ${NODE3} /root/chain33-cli"
NODE2="${1}_chain32_1"
NODE1="${1}_chain31_1"
NODE4="${1}_chain30_1"

containers=("${NODE1}" "${NODE2}" "${NODE3}" "${NODE4}")

sedfix=""
if [ "$(uname)" == "Darwin" ]; then
sedfix=".bak"
fi

function init() {
# update test environment
sed -i $sedfix 's/^Title.*/Title="local"/g' chain33.toml
sed -i $sedfix 's/^TestNet=.*/#TestNet=true/g' chain33.toml
sed -i $sedfix 's/^FixTime=.*/#FixTime=false/g' chain33.toml

# p2p
sed -i $sedfix 's/^seeds=.*/seeds=["chain33:13802","chain32:13802","chain31:13802","chain30:13802"]/g' chain33.toml
sed -i $sedfix '0,/^enable=.*/s//enable=true/' chain33.toml
sed -i $sedfix 's/^isSeed=.*/isSeed=true/g' chain33.toml
sed -i $sedfix 's/^innerSeedEnable=.*/innerSeedEnable=false/g' chain33.toml
sed -i $sedfix 's/^useGithub=.*/useGithub=false/g' chain33.toml

# rpc
sed -i $sedfix 's/^jrpcBindAddr=.*/jrpcBindAddr="0.0.0.0:8801"/g' chain33.toml
sed -i $sedfix 's/^grpcBindAddr=.*/grpcBindAddr="0.0.0.0:8802"/g' chain33.toml
sed -i $sedfix 's/^whitelist=.*/whitelist=["localhost","127.0.0.1","0.0.0.0"]/g' chain33.toml

# consensus
#sed -i $sedfix 's/^name="ticket"/name="solo"/g' chain33.toml
#sed -i $sedfix '/^minerstart=true/a[consensus.sub.solo]' chain33.toml
#sed -i $sedfix 's/^genesis=.*/genesis="1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs"/g' chain33.toml

}

function start() {
# docker-compose ps
docker-compose ps

# remove exsit container
docker-compose down

# create and run docker-compose container
docker-compose -f docker-compose.yml up --build -d

local SLEEP=10
echo "=========== sleep ${SLEEP}s ============="
sleep ${SLEEP}
docker-compose ps
}

function main() {
echo "================main begin======================"
init
start
echo "================main end========================"
}
# run script
main
```

>  The file directory structure is as follows:
```bash
root@ubuntu054:/data/solo# ls
chain33  chain33-cli  chain33.toml  docker-compose.sh  docker-compose.yml  Dockerfile
```

### 4.7 Startup environment
> Execution

```bash
./docker-compose.sh 
```

### 4.8 Check Container Startup 
```bash
root@ubuntu054:/data/solo# docker ps -a
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS               NAMES
3484b6eb112d        solo_chain32        "/root/chain33 -f /r…"   14 minutes ago      Up 14 minutes                           solo_chain32_1
1c3cda51d636        solo_chain31        "/root/chain33 -f /r…"   14 minutes ago      Up 14 minutes                           solo_chain31_1
0616f1a12413        solo_chain33        "/root/chain33 -f /r…"   14 minutes ago      Up 14 minutes                           solo_chain33_1
bb5bd85e38b7        solo_chain30        "/root/chain33 -f /r…"   14 minutes ago      Up 14 minutes                           solo_chain30_1
```

### 4.9 Environment Testing
> Check synchronization status
```bash
root@ubuntu054:/data/solo# docker exec solo_chain32_1 /root/chain33-cli net is_sync
true
```

> Check Peer-info
```bash
root@ubuntu054:/data/solo# docker exec solo_chain32_1 /root/chain33-cli net peer_info
{
    "peers": [
        {
            "addr": "172.19.0.4",
            "port": 13802,
            "name": "02204102b9dd74a14f71a151a4626038f60e2fe3f23b3fcdc865913d594d74b579",
            "mempoolSize": 0,
            "self": false,
            "header": {
                "version": 0,
                "parentHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "txHash": "0x22db70a26130f2fe4758fd65bf016949c1c46f5642b4a556f8a0ff7a41350898",
                "stateHash": "0xeb240fe1248028e9c7271ae2838ea3970bb880031764c8154c8bce2d16262cb7",
                "height": 0,
                "blockTime": 1514533394,
                "txCount": 1,
                "hash": "0xc8799befacd9709a5f4dfa68d6fd53a37ccce83352997a132adfed7f46747757",
                "difficulty": 0
            }
        },
        {
            "addr": "172.19.0.3",
            "port": 13802,
            "name": "0284e9e17e200cf7d5dd2ff6c81dbf6ef0ccf85418db494c654dfb6de9b863457c",
            "mempoolSize": 0,
            "self": false,
            "header": {
                "version": 0,
                "parentHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "txHash": "0x22db70a26130f2fe4758fd65bf016949c1c46f5642b4a556f8a0ff7a41350898",
                "stateHash": "0xeb240fe1248028e9c7271ae2838ea3970bb880031764c8154c8bce2d16262cb7",
                "height": 0,
                "blockTime": 1514533394,
                "txCount": 1,
                "hash": "0xc8799befacd9709a5f4dfa68d6fd53a37ccce83352997a132adfed7f46747757",
                "difficulty": 0
            }
        },
        {
            "addr": "172.19.0.2",
            "port": 13802,
            "name": "02493c1f49dc139e38cd4180b231e0305b12506b0c5831032da9e0ac4e90996ee3",
            "mempoolSize": 0,
            "self": false,
            "header": {
                "version": 0,
                "parentHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "txHash": "0x22db70a26130f2fe4758fd65bf016949c1c46f5642b4a556f8a0ff7a41350898",
                "stateHash": "0xeb240fe1248028e9c7271ae2838ea3970bb880031764c8154c8bce2d16262cb7",
                "height": 0,
                "blockTime": 1514533394,
                "txCount": 1,
                "hash": "0xc8799befacd9709a5f4dfa68d6fd53a37ccce83352997a132adfed7f46747757",
                "difficulty": 0
            }
        },
        {
            "addr": "172.19.0.5",
            "port": 13802,
            "name": "033571c89f018e0c7acb410d4589ee3a6876162ded94b398eee61ba0f42a1a78ea",
            "mempoolSize": 0,
            "self": true,
            "header": {
                "version": 0,
                "parentHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "txHash": "0x22db70a26130f2fe4758fd65bf016949c1c46f5642b4a556f8a0ff7a41350898",
                "stateHash": "0xeb240fe1248028e9c7271ae2838ea3970bb880031764c8154c8bce2d16262cb7",
                "height": 0,
                "blockTime": 1514533394,
                "txCount": 1,
                "hash": "0xc8799befacd9709a5f4dfa68d6fd53a37ccce83352997a132adfed7f46747757",
                "difficulty": 0
            }
        }
    ]
}
```