[TOC]
# 1 Private Chain Network Construction
## 1.1 Install Go Environment and Git Environment
 Check whether golang and git were installed or not,if the following is displayed, neither of them were installed.
```shell
~$ go version
The program 'go' is currently not installed. You can install it by typing:
sudo apt install golang-go
~$ git
The program 'git' is currently not installed. You can install it by typing:
sudo apt install git
```

- Go environment installation refer to <a href="https://chain.33.cn/document/81#1.1%20Go%20%E7%8E%AF%E5%A2%83%E5%AE%89%E8%A3%85">HERE</a>


- Git environment installation refer to <a href="https://chain.33.cn/document/81#1.2%20Git%20%E7%8E%AF%E5%A2%83%E5%AE%89%E8%A3%85">HERE</a>

## 1.2 Download the Plugin Source Code and Compile the Executable File
Code downloading refer to<a href="https://chain.33.cn/document/81#2%20%E4%BB%A3%E7%A0%81%E4%B8%8B%E8%BD%BD"> here</a>, the execution results are shown as follows:
```shell
mkdir -p $GOPATH/src/github.com/33cn
git clone https://github.com/33cn/plugin.git $GOPATH/src/github.com/33cn/
cd plugin
make
```

After successful compilation, two executables, chain33 and chain33-cli, will be generated under the build directory.
- In order to prevent the two nodes from obtaining equal votes when they participate in the selection of the main node, the number of nodes is usually configured to be odd numbers of 3,5,7, etc. Three nodes are configured here.

Copy this two files to a certain directory on the three nodes, such as /home/ubuntu/chain33, which needs to be created first.

```shell
mkdir -p /home/ubuntu/chain33
scp chain33 /home/ubuntu/chain33/
scp chain33 ubuntu@192.168.0.107:/home/ubuntu/chain33/
scp chain33 ubuntu@192.168.0.116:/home/ubuntu/chain33/
scp chain33-cli /home/ubuntu/chain33/
scp chain33-cli ubuntu@192.168.0.107:/home/ubuntu/chain33/
scp chain33-cli ubuntu@192.168.0.116:/home/ubuntu/chain33/
```

## 1.3 Modify Configuration Files

Copy ../raft/chain33.test.tomlto the current directory,configuration item explanation refer to<a href="https://chain.33.cn/document/123"> HERE</a>

```shell
cp ../chain33.test.toml .
```

Our four nodes are seed nodes, so we set isSeed in [p2p] as true, and add the node IP :port to the seeds and [consensus.sub.raft] peersURL strings in ip:port[p2p]and save them, noting that the two port numbers are different.

```plain
[p2p]
seeds=["192.168.0.105:13802","192.168.0.107:13802","192.168.0.116:13802"]
isSeed=true

[consensus.sub.raft]
Note: the value of nodeID must be in the same order as the IP of the node where the profile is located in peersURL, starting from 1, nodeID=1 on 192.168.0.105, nodeID=2 on 192.168.0.107, and so on
nodeID=x
peersURL="http://192.168.0.105:9021,http://192.168.0.107:9021,http://192.168.0.116:9021"
```

Copy the configured configuration file chain33.testx.toml to the /home/ubuntu/chain33 directory of the corresponding node

```shell
scp chain33.test1.toml ubuntu@192.168.0.105:/home/ubuntu/chain33/
scp chain33.test2.toml ubuntu@192.168.0.107:/home/ubuntu/chain33/
scp chain33.test3.toml ubuntu@192.168.0.116:/home/ubuntu/chain33/
```

## 1.4 Start the Program on Each Node

Log in to each node and enter the following command to start the blockchain program:

```shell
nohup ./chain33 -f chain33.testx.toml >> log.out 2>&1 &
```

> Note: by default, raft produces an empty block at 2-minute intervals.

## 1.5 View the Node From Chain33-cli
### 1.5.1 Check Node Synchronization Status, and if True, the Block is Synchronized

```shell
./chain33-cli net is_sync
```

### 1.5.2 Send Transaction to Test Whether the Blockchain is Working Properly
- First create a wallet and account, refer to<a href="https://chain.33.cn/document/80#1.3%20%E5%88%9B%E5%BB%BA%E9%92%B1%E5%8C%85%E4%BB%A5%E5%8F%8A%E8%B4%A6%E6%88%B7" > HERE</a>,the execution results are shown as follows:

```shell
./chain33-cli account list
{
    "wallets": [
        {
            "acc": {
                "balance": "0.0000",
                "frozen": "0.0000",
                "addr": "1EVnGWTrC6WcaGSU8D8cuXxkFcRTPJ1Tox"
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
                "addr": "1GqcbERCs872VCVb35znGk6jhYUsRc4rvm"
            },
            "label": "test"
        }
    ]
}
```
- Send transaction from genesis account to test account, refer to<a href="https://chain.33.cn/document/80#1.4.2%20%E5%8F%91%E9%80%81%E8%BD%AC%E8%B4%A6%E4%BA%A4%E6%98%93" > HERE</a>,the execution results are shown as follows:

```shell
./chain33-cli send bty transfer -a 1000 -t 1GqcbERCs872VCVb35znGk6jhYUsRc4rvm -n "first transfer" -k 1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs
0xb545a3b856105476e0fc29901ca0d0d6af3fe0fa2b6466d6fb3c2e2bc0392f7d
```

- Query transaction results, refer to<a href="https://chain.33.cn/document/80#1.4.3%20%E6%9F%A5%E8%AF%A2%E4%BA%A4%E6%98%93%E7%BB%93%E6%9E%9C"> HERE</a>,the execution results are shown as follows:

```shell
./chain33-cli tx query -s 0xb545a3b856105476e0fc29901ca0d0d6af3fe0fa2b6466d6fb3c2e2bc0392f7d
{
    "txs": [
        {
            "tx": {
                "execer": "coins",
                "payload": {
                    "transfer": {
                        "cointoken": "",
                        "amount": "100000000000",
                        "note": "first transfer",
                        "to": "1GqcbERCs872VCVb35znGk6jhYUsRc4rvm"
                    },
                    "ty": 1
                },
                ............
                "fee": "0.0010",
                "expire": 1550732383,
                "nonce": 7996280053722898816,
                "to": "1GqcbERCs872VCVb35znGk6jhYUsRc4rvm",
                "from": "1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs",
                "hash": "0xb545a3b856105476e0fc29901ca0d0d6af3fe0fa2b6466d6fb3c2e2bc0392f7d"
            },
            ............
            "height": 3,
            "index": 0,
            "blocktime": 1550732269,
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
    ]
}

```
- Query the node information, the same height means the block chain works normally.

```shell
./chain33-cli net peer_info
{
    "peers": [
        {
            "addr": "192.168.0.116",
            "port": 13802,
            "name": "03d7981d1c5f7e2497ddfb30b3910881748cddc900508488485e327f487d2075f0",
            "mempoolSize": 0,
            "self": false,
            "header": {
                "version": 0,
                "parentHash": "0x4593f41033c40f4068c45ef1cdda309434a2a7f8095be3dfbfc695b83bc51c35",
                "txHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "stateHash": "0xd031c20b2adb75dd42536333cf8d2eed7e6b8a20693971076a446106630a1178",
                "height": 4,
                "blockTime": 1550732390,
                "txCount": 0,
                "hash": "0xb469c9f4e03e3bdff903f23515ab26f9cc3616542589f989f5fe04148ec8f6e8",
                "difficulty": 0
            }
        },
        {
            "addr": "192.168.0.107",
            "port": 13802,
            "name": "02eaed19dd47a011022052ba9a6f923f60ff00b5bb338d558ea9ffad0ea122b584",
            "mempoolSize": 0,
            "self": false,
            "header": {
                "version": 0,
                "parentHash": "0x4593f41033c40f4068c45ef1cdda309434a2a7f8095be3dfbfc695b83bc51c35",
                "txHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "stateHash": "0xd031c20b2adb75dd42536333cf8d2eed7e6b8a20693971076a446106630a1178",
                "height": 4,
                "blockTime": 1550732390,
                "txCount": 0,
                "hash": "0xb469c9f4e03e3bdff903f23515ab26f9cc3616542589f989f5fe04148ec8f6e8",
                "difficulty": 0
            }
        },
        {
            "addr": "192.168.0.105",
            "port": 13802,
            "name": "039a54c0b5fa2d0de1bc263796acd08316e535af2c40568f41459d1804560cc612",
            "mempoolSize": 0,
            "self": true,
            "header": {
                "version": 0,
                "parentHash": "0x4593f41033c40f4068c45ef1cdda309434a2a7f8095be3dfbfc695b83bc51c35",
                "txHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "stateHash": "0xd031c20b2adb75dd42536333cf8d2eed7e6b8a20693971076a446106630a1178",
                "height": 4,
                "blockTime": 1550732390,
                "txCount": 0,
                "hash": "0xb469c9f4e03e3bdff903f23515ab26f9cc3616542589f989f5fe04148ec8f6e8",
                "difficulty": 0
            }
        }
    ]
}
```
