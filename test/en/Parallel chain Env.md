```bash
The following is the configuration of the parallel chain environment and the description of the meaning of each parameter:
# 1.CoinSymbol (genesis: address of the initial token, genesisAmount: amount of the initial token)
# 2.Support parallel chain fork switch: EnableParaFork
# 3.Whether the storedb upgrade should re-execute localdb, the parallel chain upgrade needs to be turned on: enableReExecLocal
# 4.Support parallel chain mempool configuration, name="para"
# 5.Parallel chain storage supports kvmvccmavl, which takes effect after 100,000 height by default
# 6.Increase system fork configuration and fork configuration for each actuator

Title="user.p.devtest."
CoinSymbol="bty"
EnableParaFork=true

[log]
# Log level, support debug(dbug)/info/warn/error(eror)/crit
loglevel = "info"
logConsoleLevel = "info"
# Log file name, where all generated log files are placed, 
logFile = "logs/chain33.log"
# Maximum value of a single log file (unit: megabyte)
maxFileSize = 300
# Maximum number of saved history log files 
maxBackups = 100
# Maximum number of saved history log messages (unit: days)
maxAge = 28
# Whether log file names use local time (if not, then use UTC time)
localTime = true
# Whether the history log file is compressed (compressed format is gz)
compress = true
# Whether to print the call source file and line number
callerFile = false
# Whether to print the calling method
callerFunction = false

[blockchain]
# Number of cached blocks
defCacheSize=512
# The maximum number of blocks to apply for at one time when synchronizing blocks
maxFetchBlockNum=128
# The time interval between requesting a synchronized block from the opposite node
timeoutSeconds=5
# Batch synchronization block is the number of blocks acquired at one time
batchBlockNum=128
# Database type used
driver="leveldb"
# Database file directory
dbPath="paradatadir"
# Database cache size
dbCache=64
# Strong consistency
isStrongConsistency=true
# Whether it is a single node
singleMode=true
# Whether need to write to disk immediately when bulk writing to a database. You can set false for non-ssd computers to improve performance.
batchsync=false
# Whether to record the sequence of adding or deleting blocks, if the node act as the main chain node and provides service for the parallel chain node, it needs to be set to true
isRecordBlockSequence=false
# Whether it is a parallel chain node
isParaChain = true
# Whether to turn on the tx quick query index
enableTxQuickIndex=true
# Whether storedb upgrade should re-execute localdb, bityuan main chain upgrade does not need to be enabled, and parallel chain upgrade needs to be enabled
enableReExecLocal=true

[p2p]
seeds=[]
enable=false
isSeed=false
serverStart=true
innerSeedEnable=true
useGithub=true
innerBounds=300
msgCacheSize=10240
driver="leveldb"
dbPath="paradatadir/addrbook"
dbCache=4
grpcLogFile="grpc33.log"

[rpc]
jrpcBindAddr=":8801"
grpcBindAddr=":8802"
whitelist=["*"]
jrpcFuncWhitelist=["*"]
grpcFuncWhitelist=["*"]

[mempool]
# Mempool queue name, can be matched, timeline, score, price, para
name="para"
poolCacheSize=10240
minTxFee=100000

[consensus]
name="para"
genesisBlockTime=1514533394
genesis="1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs"
minerExecs=["paracross"]    #Allocation of mining contracts

[mver.consensus]
#Fund account address
fundKeyAddr = "1BQXS6TxaYYG5mADaWij4AxhZZUTpw95a5"
#User reward
coinReward = 18
#Development fund reward
coinDevFund = 12
#ticket price
ticketPrice = 10000
#Difficulty of mining
powLimitBits = "0x1f00ffff"
#The maximum range of adjusting   of difficulty each time, if set to 4, the range is (1/4-4), do not increase the difficulty more than 4 times at one time, or reduce the difficulty to 1/4 of the original, as this parameter is set in order to avoid sudden burst of difficulty
retargetAdjustmentFactor = 4
#Indicates that if the block time is greater than the current time 16s, then the block will be judged as invalid.
futureBlockTime = 16
#Ticket freeze time
ticketFrozenTime = 5    #5s only for test
ticketWithdrawTime = 10 #10s only for test
ticketMinerWaitTime = 2 #2s only for test
#The maximum number of transactions contained by block 
maxTxNumber = 1600      #160
#Adjust the interval of difficulty(difficulty is not adjusted for each block, but every targetTimespan/targetTimePerBlock)
targetTimespan = 2304
#Target time for each block package
targetTimePerBlock = 16

[consensus.sub.para]
minerstart=false
#Here IP is changed to the actual address
ParaRemoteGrpcClient = "localhost:8802"
#Specifies that synchronization starts at a block height of the main chain
startHeight=2240000
#Packing time interval, unit of second
writeBlockSeconds=5
#Every few blocks of the main chain are not related to the transaction, and the empty blocks are packaged on the parallel chain
emptyBlockInterval=50
#The number of blocks that wait for the parallel chain consensus message to be attached to the main chain and succeed, beyond which the consensus message will be reposted, minimum 2
waitBlocks4CommitMsg=2
#After the switch of the main chain node in the cloud, the parallel chain ADAPTS to the new block of the main chain node, and backtrack to find the depth of the same blockhash as recorded by itself
searchHashMatchedBlockDepth=10000
#Creation address quota
genesisAmount=100000000
#The backbone supports the parallel chain consensus tx fork height, which needs to be strictly consistent with the backbone and cannot be modified
MainForkParacrossCommitTx=2270000
# Parallel chain since the consensus on the corresponding height of main chain, need greater than or equal to MainForkParacrossCommitTx = 2270000, 1 don't open it
MainParaSelfConsensusForkHeight=-1

[store]
name="kvmvccmavl"
driver="leveldb"
storedbVersion="2.0.0"
dbPath="paradatadir/mavltree"
dbCache=128
enableMavlPrefix=false
enableMVCC=false
enableMavlPrune=false
pruneHeight=10000

[store.sub.mavl]
enableMavlPrefix=false
enableMVCC=false
enableMavlPrune=false
pruneHeight=10000
enableMemTree=true
enableMemVal=true

[store.sub.kvmvccmavl]
enableMVCCIter=true
enableMavlPrefix=false
enableMVCC=false
enableMavlPrune=false
pruneHeight=10000
enableMemTree=true
enableMemVal=true

[wallet]
minFee=100000
driver="leveldb"
dbPath="parawallet"
dbCache=16
signType="secp256k1"
minerdisable=true

[exec]
isFree=true
minExecFee=100000
enableStat=false
enableMVCC=false

[exec.sub.manage]
superManager=[
    "1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs",
]

[exec.sub.token]
saveTokenTxList=true
tokenApprs = [
        "1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs",
]

[exec.sub.paracross]
# Parallel chain superaccounts can vote directly after the consensus stops the corresponding backbone height of n empty blocks, which is only valid for the backbone
paraConsensusStopBlocks=30000

[fork.system]
ForkChainParamV1= 0
ForkCheckTxDup=0
ForkBlockHash= 1
ForkMinerTime= 0
ForkTransferExec=0
ForkExecKey=0
ForkTxGroup=0
ForkResetTx0=0
ForkWithdraw=0
ForkExecRollback=0
ForkCheckBlockTime=0
ForkTxHeight=0
ForkTxGroupPara=0
ForkChainParamV2=0
ForkMultiSignAddress=0
ForkStateDBSet=0
ForkLocalDBAccess=0
ForkBlockCheck=0
ForkBase58AddressCheck=0
ForkEnableParaRegExec=100000

[fork.sub.coins]
Enable=0

[fork.sub.ticket]
Enable=0
ForkTicketId =0
ForkTicketVrf =0

[fork.sub.retrieve]
Enable=0
ForkRetrive=0

[fork.sub.hashlock]
Enable=0

[fork.sub.manage]
Enable=0
ForkManageExec=0

[fork.sub.token]
Enable=0
ForkTokenBlackList= 0
ForkBadTokenSymbol= 0
ForkTokenPrice=0
ForkTokenSymbolWithNumber=0
ForkTokenCheck= 100000

[fork.sub.trade]
Enable=0
ForkTradeBuyLimit= 0
ForkTradeAsset= 0
ForkTradeID = 0

[fork.sub.paracross]
Enable=0
ForkParacrossWithdrawFromParachain=0
ForkParacrossCommitTx=0

[fork.sub.evm]
Enable=0
ForkEVMState=0
ForkEVMABI=0
ForkEVMFrozen=0
ForkEVMKVHash=0

[fork.sub.blackwhite]
Enable=0
ForkBlackWhiteV2=0

[fork.sub.cert]
Enable=0

[fork.sub.guess]
Enable=0

[fork.sub.lottery]
Enable=0

[fork.sub.oracle]
Enable=0

[fork.sub.relay]
Enable=0

[fork.sub.norm]
Enable=0

[fork.sub.pokerbull]
Enable=0

[fork.sub.privacy]
Enable=0

[fork.sub.game]
Enable=0

[fork.sub.multisig]
Enable=0

[fork.sub.unfreeze]
Enable=0
ForkTerminatePart=0
ForkUnfreezeIDX= 0

[fork.sub.store-kvmvccmavl]
ForkKvmvccmavl=100000

[pprof]
listenAddr = "localhost:6061"P

```