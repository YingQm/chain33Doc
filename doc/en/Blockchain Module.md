# Blockchain Module

[TOC]

## 1 Module Introduction

Blockchain module is a component that processes blocks, including storing block information, adding blocks to the main or side chains, and synchronizing blocks. At the same time, it provides interfaces to query block information and block chain status.

## 2 Logical Architecture and Context

### 2.1 Blockchain Context

![Blockchain Context](https://public.33.cn/web/storage/upload/20190717/10d07c1870f0b3acf65c75354b9e2b45.png)

- Interaction with Consensus module: handle blocks the Consensus module packaged, and the request of Consensus module to query block information

- Interaction with P2P module: deal with the broadcast blocks received by P2P modules, send blocks to P2P modules for broadcasting, and handle the requests of P2P modules to inquire block information

- Interaction with Mempool and Executor modules: handle requests from these two modules to query the blockchain status

### 2.2 Blockchain Logical Construction

Blockchain module consists of three sub-modules: message receiving module, block synchronization module and block storage module

> Message receiving module

Accept queries for information about blocks and blockchain status from other modules

> Block synchronization module

After the node starts, compared the latest block height of peer nodes with its own height. If its own height is lower than the latest height of peer nodes, the block will initiate the synchronization request to catch up with the main chain

> Block storage module

Store block information to the database in different types

## 3 Process Logic

> Here is the processing logic for the three modules

### 3.1 Message Receiving Module

Includes the following message:

#### block related information

- EventGetBlocks:  get block information
- EventGetHeaders:  get block header information
- EventAddBlock: add blocks synchronized from peers
- EventAddBlockHeaders:  add block headers synchronized from peers
- EventAddBlockDetail: add blocks from consensus module
- EventBroadcastAddBlock: add block broadcast from peers
- EventGetBlockHeight: get the latest block height
- EventGetLastHeader:  get the latest block header information
- EventGetLastBlock: get the latest block information

#### Blockchain browser related messages

- EventGetTransactionByAddr: get hash values of all transactions at the address by the account address
- EventGetTransactionByHash: get corresponding information by transaction hash
- EventGetBlockOverview: get header information for this block and list of transaction hashes using block hash values
- EventGetAddrOverview: get the coins received by the account, the current balance of the account and the number of transactions involved by the account address
- EventGetBlockHash: get block hash from block height
- EventQueryTx: query specific transaction information including txproof proof by the transaction hash 

#### Parallel chain related messages

- EventGetLastBlockSequence: get the sequence of the node corresponding to the latest block
- EventGetSeqByHash:  get the sequence corresponding to the block hash
- EventAddParaChainBlockDetail: add consensus block from parallel chain 
- EventDelParaChainBlockDetail: delete consensus block from parallel chain 
- EventLocalGet: query for stored Key-Value pairs

#### Other messages

- EventIsSync: query the synchronization status of blockchain
- EventIsNtpClockSync: query the NTP network time synchronization status
- EventLocalPrefixCount: query the number of keys with a specified prefix

### 3.2 Block Synchronization Module

Includes timing processing logic and immediate processing logic

#### Timing process

1. FetchPeerList:  periodically fetch peer information in the network from the P2P module and save it to the local peerList
2. SynBlocksFromPeers: periodically request specified blocks from a peerList
3. CheckTipBlockHash: check periodically whether the latest height block hash of this node is consistent with the corresponding height block hash in the peerlist
4. CheckBestChain: periodically detect and obtain an optimal chain list, ensuring that block request peers and this node are all on the same chain
5. RecoveryFaultPeer: periodically detect the fault peer node's and recove

#### Real-Time Processing

Receive and process blocks from three sources: blocks packaged by consensus modules, broadcast blocks, and synchronized blocks

Process the entrance function ProcessBlock(), the process is as follows:

- check whether the block already exists on the main/side chain of the node
- check whether the block already exists on the orphan chain of the node
- check whether the parent block already exists on the main/side chain of the node
- try to block to the main/side chain
- try to the process orphaned blocks in an orphan chain whose parent block is this block

### 3.3 Block Storage Module

#### Store data content

All storage formats are in Key-Value form, including the following data contents:

> Block related

1. key("blockLastHeight"): store the latest block height
2. key("Hash:%v", blockhash): store block height
3. key("Body:%v", blockhash): store block body
4. key("Header:%v", blockhash):store block header
5. key("TD:%v", blockhash): store block body
6. key("Height:%v", height): store block hash corresponding to the height of the block
7. key("HH:%v", height): store block header corresponding to block height 
8. key("LastSequence"): store the latest sequence
9. key("Seq:%v", sequence): store sequence corresponding block hash
10. key("HashToSeq:%v", blockhash): stores the sequence corresponding to block hash

> Transaction related

1. key("TxAddrHash:%s:%s", addr, heightindex): store hash list of transactions related to the address
2. key("TxAddrDirHash:%s:%d:%s", addr, flag, heightindex): store hash list of transactions for an address-related category
3. key("AddrTxsCount:%s", addr): store number of transactions in which the address participates

#### Data access interface

> Get and store the  information of the latest block

- UpdateHeight
- UpdateLastBlock
- LastHeader
- LastBlock

> Get and store block information

- LoadBlockByHeight
- LoadBlockByHash
- GetHeightByBlockHash
- GetBlockHashByHeight
- GetBlockHeaderByHeight
- GetBlockHeaderByHash
- GetTdByBlockHash
- SaveTdByBlockHash

> Store and delete blocks and transactions

- SaveBlock
- DelBlock
- GetTx
- AddTxs
- DelTxs