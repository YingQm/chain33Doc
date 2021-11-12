# Parallel Chain Upgrade, Release6.1 Upgrade to Release6.2
[TOC]

## 1 Background
 The bitcoin main network is expected to conduct the second hard fork on June 20, 2019, adding the following function points:
1. Consensus speed increased (from 15 seconds to 5 seconds)
2. Reduce the storage space (it is expected that the space can be compressed to about 10G about a month after the completion of synchronization)
3. Other functional optimizations
The old version will not be available after June 20, 2019, so all the old versions in the current network need to be upgraded centrally in advance.

## 2 Synchronization Scheme
In order not to affect the existing business, and the upgrade time is relatively abundant, it is suggested not to the old version of the main chain and parallel chain, let the business continues to run.

#### 2.1 Main Chain Synchronization Scheme

 Directly take the latest version, decompress and synchronize a new copy of the data.
 Note: if the upgrade is on the old version, the reconstruction of blockchain storage is expected to take several hours, which will affect the current business. So it is not recommended to upgrade on the old main chain.

  1. Use the latest version of the main chain
```shell
      wget https://bty.oss-ap-southeast-1.aliyuncs.com/chain33/mainChain_v6.2.0.tar.gz
```

  2. Start the chain33 process in the current directory
    Note: if both the new and old main chain processes are running on the same machine (with enough hard disk space), make sure that the JSONRPC and GRP ports that the new main chain listens for are changed, or they will conflict. Change the following 8801,8802 to other ports
```shell
   jrpcBindAddr=":8801"
   grpcBindAddr=":8802"

   nohup ./chain33 -f chain33.toml > console.log 2>&1 &
```

  3.  Wait for main chain synchronization (about 8 hours is expected)
```shell
         # Determine the synchronization status, and return true to indicate completion of synchronization
       ./chain33-cli net is_sync

        # Check node synchronization
      ./chain33-cli net peer_info
```

#### 2.2 Parallel Chain Synchronization Scheme (after the completion of main chain synchronization)
   
   Due to the transformation of block structure of parallel chain, upgrading on the original version is not supported, and data needs to be re-synchronized. Calculate with the height of 100,000 blocks, the synchronization time is more than 1 hour. In order not to affect the business, it is suggested to synchronize a new parallel chain node, and then quickly switch.

###### 1.  Record the current height of the parallel chain (known as paraHeight, as used later) and the value of statehash.
```shell
    >executive command:
    ./chain33-cli --rpc_laddr="http://parallel chain IP: parallel chain port" block last_header
	
    >Record height and statehash values:
    {
    "version": 0,
    "stateHash": "0x70d1e798415c9aa6a141c4cd6dfb2b612fd0b0987bbdece6858fe79aa7888c92",
    "height": 28820,
	}
```
   
###### 2.Download the parallel chain version
```shell
   wget https://bty.oss-ap-southeast-1.aliyuncs.com/chain33/paraChain_v6.2.0.tar.gz
```

###### 3. To modify the configuration file, the following items need to be modified based on the following configuration file:
```shell
1. Must be changed to your own chain name
Title="user.p.devtest."

2. Changes are needed only if coins are used. If only tokens are issued, the following three configurations remain the same.
CoinSymbol="bty"  // Token name, changed to your own name (support upper and lower case letters)
genesis="1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs" // Change genesis(address of initial token) to your own address.
genesisAmount=100000000 // Issue amount, default is 100 million, modify to your actual number

3. If multiple parallel chains are on the same server, this port is distinguished from the others
jrpcBindAddr=":8801"

4. If multiple parallel chains are on the same server, this port should be distinguished from the others
grpcBindAddr=":8802"

5. Change the IP and port of your main chain
ParaRemoteGrpcClient = "localhost:8802"

6. You have to change the starting height of your parallel chain
startHeight=2000000

7. You have to change the super administrator address to your own chain
superManager

8. Must be modified to match the your current parallel chain configuration 
tokenApprs

9.  parameter under [fork.system], indicating the height at which some functions are in effect while other parameters remain unchanged. The following parameters are recommended to be modified to values greater than the height of the parallel chain (paraHeight+100).
ForkCheckBlockTime=28920
ForkTxGroupPara=28920
ForkChainParamV2=28920
ForkMultiSignAddress=28920
ForkStateDBSet=28920
ForkLocalDBAccess=28920
ForkBlockCheck=28920
ForkBase58AddressCheck=28920
ForkEnableParaRegExec=28920
```

###### 4. Start the service after the modification
```shell
nohup ./chain33 -f chain33.para.toml > console.log 2>&1 &
```

###### 5. After the parallel chain synchronization is complete, execute the following command to verify that statehash at the same height before and after the upgrade is consistent. If not, feedback to R&D for confirmation
```shell
./chain33-cli --rpc_laddr="http://parallel chain IP: parallel chain port" block get -s 28820 -e 28820
```