# Introduction to DApp Development
[TOC]

# 1 Generation of DApp

App(Application), what we usually call software, has undergone several generations of evolution in the limited decades since the birth of computers. It can be summarized as follows:

![App Development History](https://public.zhaobi.tech/web/storage/upload/20190717/b8831d163089f33cf374db7e4d3b97c8.jpg "App Development History")

- **Stand-Alone App:**

    All the elements that make up the App are stored in one separate node, which can be used without the network, is the earliest form of App. Such as DOS system, single game, etc.;

- **Network App:**

    It be simply understood as the classic Client/Server model, App consists of these two parts and can exist on more than one different node.For example, traditional online games like CS, Red Alert;

- **Distributed App:**

    The components of App are scattered to N nodes, and the normal use of the App will not be affected if a few nodes die. Such as WeChat, Taobao, etc.;

- **P2P App:**

    Based on the application of P2P network, the composition or content of App is dispersed to N nodes, which communicate directly with each other.At present, there are common modes like BitTorrent download, blockchain application, etc.;

**Comparative Analysis of the Background and Advantages and Disadvantages of App in Each Stage:**

||Advantage|Disadvantage|Background of Creation|
|--------|--------|--------|--------|
|Stand-Alone App|Simple to use<br/>Need not connect to the Internet|Limited use, media transmission is limited<br/>Information isolation, cannot be shared|No Internet Connection<br/>Network limited<br/>Simple logic|
|Network App|Easy to use<br/>With the aid of the network, easy to spread<br/>Information shared, attract users|Single network, low reliability<br/>Single point of bottleneck exist<br/>High capacity expansion costs|Slow speed network<br/>Large volume of data<br/>Low reliability|
|Distributed App|Spread fast<br/>All data connect<br/>Capacity expansion costs are low<br/>High reliability|Monopoly data.<br/>Mechanism opacity<br/>Credibility depends heavily on third parties|High speed network<br/>Massive data<br/>High reliability<br/>Company or industry monopoly|
|P2P App|All network connect<br/>Transparency of processing mechanism<br/>Data disclosure and credibility<br/>Self-governance, independent of third parties|In the early stage of development, immature<br/>Low processing performance<br/>Small amount of data to process|High speed network<br/>Massive data<br/>High reliability<br/>Data public and reliable|

**Definition of DApp: **

DApp(Decentralized Application), is another way of calling it opposite to the traditional centralized application.It's essentially an "intelligent contract," but with an interface wrapped around it to make it easier for end users to use. Traditional App components can be simply understood as:

> **App = Frontend + Server**

Then DApp can be simply understood as:

> **DApp = Frontend + Contracts**

The Server of traditional App can be a single node/distributed/cloud service node. It is centrally controlled, owned by one or more specific companies/organizations/individuals, as a centralized model. Its owner can control the whole logic of the application, so it is called "centralized application".

However, Contracts at DApp are procedural logic that can be deployed over blockchain networks. It runs on all the nodes in the blockchain network, all the nodes have exactly the same logic, and the owner can be anyone.Once the contract is deployed, its behavior will not be controlled by any particular person, so it is called a "decentralized application."

## 2 DApp Design and Development

A typical DApp consists of the following:

![DApp Composition](https://public.zhaobi.tech/web/storage/upload/20181114/c33a38f7419b1f47291ac80d520e0e98.png "DApp Composition")

- **Front End：**

    The client can be a mobile App, a webpage, or even a command line. Generally, it is the RPC service interface directly connected to the blockchain node.

- **Server(optional):**

    Similar to the service node of centralized application, it mainly encapsulates DApp's own service interface, with the lower layer docking blockchain and the upper layer docking client.

- **Blockchain End:**

    Conventional blockchain nodes provide blockchain operation interface services to the front end or service end, such as sending transactions, query results and other actions;


**A Normal DApp Development Process is Shown in the Figure Below:**

![DApp Development Process](https://public.zhaobi.tech/web/storage/upload/20190717/514d2828bc87366fe929289d6a682128.jpg "DApp Development Process")

In fact, it mainly includes the development of front-end and contract. The contract is deployed on the blockchain network, which is the main execution logic of DApp and the front-end is the user interface.

Even if the front end is not used, the command line interface of blockchain can still call the contract and realize the complete logic of DApp. However, the threshold for users is too high, so generally, formal DApp will provide the front end.

## 3 Development of DApp in Chain33

Chain33 was designed as a highly extensible blockchain development platform that supports extension customization except very little inherent core logic.The expansion capability of the system can be divided into two major categories:

**The first category is the expansion and customization of system capabilities:**

    Chain33 provides the underlying plug-in management mechanism, basically all the capabilities of the system exist as a plug-in, the plug-in implementation can be replaced,Developers can use the system plugins provided by the system itself, or they can develop new functional plugins. These plugins' capabilities cover everything from encryption and decryption, consensus, storage, wallet, executor, command line, etc.


**The second category is the development of extended applications:**

    Chain33 also provides a separate framework for DApp, based on the plug-in mechanism, to facilitate DApp development by focusing developers on the core contract logic (that is, the executor logic) and adding RPC interfaces and command-line interfaces (the latter two are not required).

Check the position of DApp in the system of Chain33:

![chain33 arch](https://public.zhaobi.tech/web/storage/upload/20181114/263b976261a440e456fcebe0a2bb7c04.png "chain33 arch")

As shown in the upper left part of the figure above, Chain33 provides the DApp Framework with three elements: the executor, the command line, and RPC, where the executor is the contract logic of the DApp.

The command line provides command wrappers from the command line, which is optional.

RPC is the unique external service interface of packaging DApp.In general, Chain33 framework provides common interfaces for creating, sending, query. DApp can also develop its own RPC interface for special needs.

