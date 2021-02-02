# Video Course
[TOC]

#### Lesson 1: DApp Introduction and Chain33 Development Environment Depolyment

> Introduce the basic concepts of DApp and smart contract, the logic of rock-paper-scissors contracts, and how to set up a single-node development environment for debugging on the Windows based operating system.
> Video address: <a href="https://www.bilibili.com/video/av36690009/" target="_blank">DApp Introduction and Construction of Chain33 Development Environment</a>
> Some of the commands used in lesson 1.

```bash
	#Generate seed. Note: remember the generated seed so that you can retrieve your wallet if you accidentally delete it.
	./chain33-cli.exe seed generate -l 0
	#Save the seed, the wallet password followed by -p. Note: passwords can be customized, remember them. You will use them later when unlocking your wallet.
	./chain33-cli.exe seed save -s [seed value generated in the previous step] -p tech1234
	#Unlock wallet.
	./chain33-cli.exe wallet unlock -p tech1234 -t 0 
	#Import the genesis account address, which is specified in the configuration file.
	./chain33-cli.exe account import_key -k 3990969DF92A5914F7B71EEB9A4E58D6E255F32BF042FEA5318FC8B3D50EE6E8  -l genesis
	#Create a new account labeled testA
	./chain33-cli.exe account create -l testA
	#The genesis account initiates a transfer to the account A.
	./chain33-cli send coins transfer -a 1000 -t 1FbuCnz6Bnw3EiECrv9QYKcnYhP19JL5gb -n "test for transfer bty" -k 3990969DF92A5914F7B71EEB9A4E58D6E255F32BF042FEA5318FC8B3D50EE6E8
	#Query the transaction
	./chain33-cli.exe tx query_hash -s [transaction hash generated in the previous step]
```

#### Lesson 2: Write a Rock-Paper-Scissors Contract in GO

> Describe the process of developing the rock-paper-scissors contract using GO on Chain33.
> Video address: <a href="https://www.bilibili.com/video/av36842971/" target="_blank">Rock-Paper-Scissors Contract Development Introduction</a>

#### Lesson 3:Rock-Paper-Scissors Contract Invoking

> Introduce rock-paper-scissors-contract invoking.
> Video address: <a href="https://www.bilibili.com/video/av37268467/" target="_blank">Rock-Paper-Scissors Contract Invoking</a>.
> Some of the commands used in lesson 3.

```bash
	#Get contract address
	curl --data-binary '{"jsonrpc":"2.0", "id": 1, "method":"Chain33.ConvertExectoAddr","params":[{"execname":"fingerguessing"}] }' \
		-H 'content-type:text/plain;' \
		http://localhost:8801

	#transfer amount into the contract
	#Construct transaction that transfer coins into contract
	curl --data-binary '{"jsonrpc":"2.0", "id": 1, "method":"Chain33.CreateRawTransaction","params":[{"to":"1MwyBkj94REkZadQveucgsH9PRzpSSxTyx","amount":1000000000}] }' \
		-H 'content-type:text/plain;' \
		http://localhost:8801

	#Sign transaction, which signs the hash value returned in the previous step
	 curl --data-binary '{"jsonrpc":"2.0", "id": 1, "method":"Chain33.SignRawTx","params":[{"addr":"1FbuCnz6Bnw3EiECrv9QYKcnYhP19JL5gb", "expire":"2h", "txHex":"Data generated in the previous step"}] }' \
		-H 'content-type:text/plain;' \
		http://localhost:8801

	#Send transaction
	 curl --data-binary '{"jsonrpc":"2.0", "id": 1, "method":"Chain33.SendTransaction","params":[{"data":"Data generated in the previous step"}] }' \
		-H 'content-type:text/plain;' \
		http://localhost:8801

	#Query the amount of user A at the contract address
	 curl --data-binary '{"jsonrpc":"2.0", "id": 1, "method":"Chain33.GetBalance","params":[{"addresses":["1FbuCnz6Bnw3EiECrv9QYKcnYhP19JL5gb"],"execer":"fingerguessing"}] }' \
		-H 'content-type:text/plain;' \
		http://localhost:8801

	#Create rock-paper-scissors game steps
	#Build game
	curl --data-binary '{"jsonrpc":"2.0", "id": 1, "method":"Chain33.CreateTransaction","params":[{"execer":"fingerguessing", "actionName":"createGame", "payload":{"amount": 200000000,"hashType":"sha256","hashValue":"001c470a12512811dfc5d1cd5c60deb2ee6acafb1ca153a0ca26e19d1b5995a7"}}] }' \
		-H 'content-type:text/plain;' \
		http://localhost:8801

	#Sign transaction, private key signature of user A, called in the same way as the signature method described above
	#Send the transaction, call it in the same way as above

	#Match rock-paper-scissors game steps
	#Construct transaction
	curl --data-binary '{"jsonrpc":"2.0", "id": 1, "method":"Chain33.CreateTransaction","params":[{"execer":"fingerguessing", "actionName":"matchGame", "payload":{"gameId": "0xae020e911efad0f7ed1a297b915d906c2a0bb9f357b973cd6fe5cce9fcbce471","guess":2}}] }' \
		-H 'content-type:text/plain;' \
		http://localhost:8801

	#Sign transaction, private key signature of user B, called in the same way as the signature method described above
	#Send the transaction, call it in the same way as above

	#User A draws rock-paper-scissors game steps
	#Construct transaction
	curl --data-binary '{"jsonrpc":"2.0", "id": 1, "method":"Chain33.CreateTransaction","params":[{"execer":"fingerguessing", "actionName":"closeGame", "payload":{"gameId": "0xf7275f95c7de6e06fd93567e4c565386ef93a048f07357ea0d08b1484bfd24d3","secret":"123456","result":1}}] }' \
		-H 'content-type:text/plain;' \
		http://localhost:8801

	#Sign transaction, the private key signature of user A, the same calling way as above
	#Send the transaction, call it in the same way as above
```

#### Lesson 4: Parallel Chain Deployment and Issuing Token on Parallel Chain

> Introduce the concept of parallel chain, such as how to build a parallel chain and how to issue tokens on parallel chain.
> Video address: <a href="https://www.bilibili.com/video/av37367891/" target="_blank">Issuing Token on Parallel Chain</a>
> Steps for issuing tokens on parallel chains (command-line mode)
> In the most simplified configuration, deploying a main chain node + multiple parallel chains (different parallel chains are distinguished by ports) only need one server. The server is configured with 4 core CPU and 8G memory,

```bash
#Download the main chain, uncompress and execute (if a main chain that can be linked already exists, there is no need to create the main chain node again, supporting one main chain node to hang down multiple parallel chain nodes at the same time）：
wget https://bty.oss-ap-southeast-1.aliyuncs.com/chain33/mainChain.tar.gz
tar -zxvf mainChain.tar.gz 
cd mainChain
nohup ./chain33 -f chain33.toml >>  bty.out&

#Check the synchronization state. This step will synchronously execute the block from the main chain, which will take some time. At present, the main network block has exceeded 1 million, which is expected to be completed in 6 hours.
#Check the result of block synchronization by executing the following command, and return true indicates the completion of synchronization:
./chain33-cli  net is_sync

#Check the block synchronization by executing the following command:
./chain33-cli  net peer_info

#Run parallel chain nodes, this step needs to be completed after the main chain node synchronization

#Download the parallel chain and uncompress it
wget https://bty.oss-ap-southeast-1.aliyuncs.com/chain33/paraChain.tar.gz
tar -zxvf paraChain.tar.gz 

#Modify configuration files
cd paraChain/

Modify the chain33.toml configuration file, here only list the configuration items that need to be modified
# Set title as the name of your own parallel chain. Note the last one. Do not omit it.
Title="user.p.devtest."
# Json/RPC addresses linked to the main chain correspond to the IP and port of the main chain respectively
mainnetJrpcAddr="http://172.26.8.152:8801"
# Grpc address linked to the main chain corresponds to the IP and port of the main chain respectively
ParaRemoteGrpcClient = "172.26.8.152:8802"
# Synchronization starting from a block at a specified height of the main chain.
startHeight=1000000
#Super administrator address, matched with its own private key (note that this address should own BTY for the payment of fees)
superManager=[
    "15WgpzXZWM5QrVadD4hb4eMNWkhQ85HpfX",
]
#Match the token creator address with the address that holds the private key (same as the one above)
tokenApprs = [
        "15WgpzXZWM5QrVadD4hb4eMNWkhQ85HpfX",
]

# Start parallel chain
nohup ./chain33 -f chain33.para.toml >> para.out&


#Query block synchronization information on parallel chains
./chain33-cli --rpc_laddr="http://localhost:8901" block last_header

#Configure token-finisher
./chain33-cli --rpc_laddr="http://localhost:8901" --paraName "user.p.devtest." config config_tx -c token-finisher -o add -v [token-finisher address, just fill in the superManager address above is also permitted]
./chain33-cli --rpc_laddr="http://localhost:8901"    wallet sign -k [private key corresponding to superManager] -d [data generated in the previous step]
./chain33-cli --rpc_laddr="http://localhost:8901"   wallet send -d [Signed data generated in the previous step]

#Configure token-blacklist
./chain33-cli --rpc_laddr="http://localhost:8901" --paraName "user.p.devtest." config config_tx -c token-blacklist -o add -v BTY
./chain33-cli --rpc_laddr="http://localhost:8901"  wallet sign -k [private key corresponding to superManager] -d [data generated in the previous step]
./chain33-cli --rpc_laddr="http://localhost:8901"  wallet send -d [Signed data generated in the previous step]

#Query the results of the last two steps, note that the following process can only be entered if the last two steps are configured successfully
./chain33-cli --rpc_laddr="http://localhost:8901"   --paraName "user.p.devtest." config query_config -k token-blacklist 
./chain33-cli --rpc_laddr="http://localhost:8901"  --paraName "user.p.devtest." config query_config -k token-finisher

#Token pre-create
./chain33-cli --rpc_laddr="http://localhost:8901" --paraName "user.p.devtest."  token precreate -f 0.001 -i Devcoin -n "DEVELOP COINS" -a [token receiver, it can be yourself or someone else] -p 0 -s "COINSDEVX" -t 19900000000
./chain33-cli --rpc_laddr="http://localhost:8901" wallet sign -k [token-finisher private key] -d [data generated in the previous step]
./chain33-cli --rpc_laddr="http://localhost:8901"  wallet send -d [Signed data generated in the previous step]

#Query, only when this step is completed can you enter the following process
./chain33-cli --rpc_laddr="http://localhost:8901" --paraName "user.p.devtest." token  get_precreated

#Token finish 
./chain33-cli --rpc_laddr="http://localhost:8901" --paraName "user.p.devtest." token finish -s COINSDEVX -f 0.001 -a [token receiver address]
./chain33-cli --rpc_laddr="http://localhost:8901" wallet sign -k [token-finisher private key] -d [data generated in the previous step]
./chain33-cli --rpc_laddr="http://localhost:8901"  wallet send -d [Signed data generated in the previous step]

#Query
./chain33-cli --rpc_laddr="http://localhost:8901"  --paraName "user.p.devtest."  token get_finish_created

#Query based on address 
./chain33-cli --rpc_laddr="http://localhost:8901"  --paraName "user.p.devtest." token token_balance -e "user.p.devtest.token" -a [token receiver address]  -s COINSDEVX
```

