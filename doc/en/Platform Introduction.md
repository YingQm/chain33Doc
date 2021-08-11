# Platform Introduction

Chain33 platform is a pluggable and easily upgraded blockchain architecture that supports consensus, database, executor, etc.
Chain33 creatively supports a layered architecture, where the main chain is responsible for transaction clearing,  intelligent contracts and virtual machines are separated from the main chain and executed independently on parallel chains, and multiple parallel chains coexist to improve computing efficiency. And the parallel chains are interconnected through the main chain.

Chain33 has the following features:
- Underlying framework of blockchain based on Go language
- Modules are independent, divided into block chain, consensus, executor, P2P, Mempool, wallet, data storage, RPC and other modules
- Strong scalability, consensus, executor, data storage and other modules can be plugged and unplugged
- Parallel chain technology makes it easier for the public chain to expand horizontally.

# Introduction to the Public Chain Architecture of Chain33

Application layer: compatible with Ethereum intelligent contract, and supports original capabilities such as issuing tokens, asset transaction, wallet retrieval, hash locking, etc.,and support for user expandable executor (contracts).
Consensus layer: the consensus algorithm can be inserted, supporting public chain consensus of POS and DPOS, Tendermint and PBFT alliance chain consensus, Raft private chain consensus, parallel chain consensus, etc.
Data layer: data storage mode supports extensibility. Currently, it supports MPT, MAVL, KVDB and MVCCKVDB.

![Chain33 public chain architecture](https://public.33.cn/web/storage/upload/20190717/f4d67b4b79383b0f323addeed2b95b7d.jpg "Chain33 public chain architecture")

# Introduction to the Parallel Chain Architecture of Chain33
## Parallel Chain Topology

![Parallel Chain Topology](https://public.33.cn/web/storage/upload/20190717/f4fe00ee3ad55501f345808b074f0c7c.jpg "Parallel Chain Topology")

Parallel chain expansion network is simpler, more intuitive and more powerful than subdivision scheme. It is not only an application of DApp, but directly owns its own blockchain ecology. It is more efficient and simpler than cross-chain trading. In general, it is more scalable, more efficient and safer.

![slice](https://public.33.cn/web/storage/upload/20190717/2915218feff514dead57e97757de9b74.jpg "slice")


A parallel chain consists of multiple chains with the bottom layer of Chain33  
The transaction is sent to the main chain to be packaged by consensus, then synchronized to the parallel chain to be executed, and finally the execution result is written back to the main chain for save 
This separates consensus from transaction execution, while the parallel transaction execution improves TPS

# Development Roadmap

![Evelution Route](https://public.33.cn/web/storage/upload/20190718/3c0077d108aa954343d55d56490fb1d9.png "Evelution Route")