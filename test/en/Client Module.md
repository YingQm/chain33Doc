# Client Module

[TOC]

## 1 Module Introduction
Cli modules can call the implemented services in Chain33 directly through the PRC interface. The Cli module can be simply understood as a front-end application.

PRC provides various system services to external applications by providing a series of protocols. In Chain33, GPRC services with protobuf protocol definition and jsonPRC services with Json definition protocol are mainly adopted to provide the same system services for different front-end applications.


## 2 Logical Architecture and Context
### 2.1 Relationship Between Cli Module and Chain33

![](https://public.33.cn/web/storage/upload/20190717/2a4dc288adf69248ef64ed74fa5ad591.jpg)

1 Call the corresponding PRC interface depending on the instructions entered

2 After the PRC module receives the PRC request, it sends the message to the specified module by setting the topic

3 After the individual modules are processed, the results are returned to the PRC module

4 Finally the PRC module constructs the structure required by the Cli from the information in the response, and return.

### 2.2 Process Logic
#### 2.2.1  Instruction Addition
Cobra is used in Chain33 to create the instruction set, and rootCmd is the uniform entry point for all instruction sets.

```go
var rootCmd = &cobra.Command{
	Use:   "Chain33-cli",
	Short: "Chain33 client tools",
}
```

 RootCmd involves two elements in the cobra.Command structure: commands and flags

```go
type Command struct {
	...
	// commands is the list of commands supported by this program.
	commands []*Command
	...

	// flags is full set of flags.
	flags *flag.FlagSet
	...
}
```

 * Commands：Represents an action or instruction to be executed, while each instruction can contain sub-commands.
 * Flags: Actions that instructions can perform or filter

 Commands add by AddCommand:

```go
// AddCommand adds one or more commands to this parent command.
func (c *Command) AddCommand(cmds ...*Command) {
	for i, x := range cmds {
		...
		c.commands = append(c.commands, x)
		...
	}
}
```

 Flags set by AddFlag：

```go
// AddFlag will add the flag to the FlagSet
func (f *FlagSet) AddFlag(flag *Flag) {
}
```

 Flag can be set as required by function MarkFlagRequired: 

```go
func (c *Command) MarkFlagRequired(name string) error {
	return MarkFlagRequired(c.Flags(), name)
}
```

#### 2.2.2 Call of Instruction

```go
type PRCCtx struct {
	Addr   string			// Peer PRC addresses
	Method string			// Call function
	Params interface{}		// Incoming parameters
	Res    interface{}		// Response
	cb     Callback			// Callback function
}
```

PRCCtx creation

```go
func NewPRCCtx(laddr, method string, params, res interface{}) *PRCCtx {
	return &PRCCtx{
		Addr:   laddr,
		Method: method,
		Params: params,
		Res:    res,
	}
}
```

PRCCtx execution

```go
func (c *PRCCtx) Run() {
	result, err := c.RunResult()
	if err != nil {
		fmt.Fprintln(os.Stderr, err)
		return
	}
	data, err := json.MarshalIndent(result, "", "    ")
	if err != nil {
		fmt.Fprintln(os.Stderr, err)
		return
	}
	fmt.Println(string(data))
}
```

#### 2.2.3 Instruction Processing Logic
PRC interface currently supported by Chain33 

```go
type QueueProtocolAPI interface {
	Version() (*types.Reply, error)
	Close()
	NewMessage(topic string, msgid int64, data interface{}) queue.Message
	Notify(topic string, ty int64, data interface{}) (queue.Message, error)
	// +++++++++++++++ mempool interfaces begin
	// Synchronously send the transaction information to the specified module to get the reply message types.EventTx
	SendTx(param *types.Transaction) (*types.Reply, error)
	// types.EventTxList
	GetTxList(param *types.TxHashList) (*types.ReplyTxList, error)
	// types.EventGetMempool
	GetMempool() (*types.ReplyTxList, error)
	// types.EventGetLastMempool
	GetLastMempool() (*types.ReplyTxList, error)
	// types.EventQuery
	Query(param *types.Query) (*types.Message, error)
	// --------------- mempool interfaces end

	// +++++++++++++++ execs interfaces begin
	// types.EventBlockChainQuery
	BlockChainQuery(param *types.BlockChainQuery) (*types.ResUTXOGlobalIndex, error)
	// --------------- execs interfaces end

	// +++++++++++++++ p2p interfaces begin
	// types.EventPeerInfo
	PeerInfo() (*types.PeerList, error)
	// types.EventGetNetInfo
	GetNetInfo() (*types.NodeNetInfo, error)
	// --------------- p2p interfaces end

	// +++++++++++++++ consensus interfaces begin
	// types.EventGetTicketCount
	GetTicketCount() (*types.Int64, error)
	// --------------- consensus interfaces end

	// +++++++++++++++ wallet interfaces begin
	// types.EventLocalGet
	LocalGet(param *types.LocalDBGet) (*types.LocalReplyValue, error)
	// types.EventLocalList
	LocalList(param *types.LocalDBList) (*types.LocalReplyValue, error)
	// types.EventWalletGetAccountList
	WalletGetAccountList(req *types.ReqAccountList) (*types.WalletAccounts, error)
	// types.EventNewAccount
	NewAccount(param *types.ReqNewAccount) (*types.WalletAccount, error)
	// types.EventWalletTransactionList
	WalletTransactionList(param *types.ReqWalletTransactionList) (*types.WalletTxDetails, error)
	// types.EventWalletImportprivkey
	WalletImportprivkey(param *types.ReqWalletImportPrivKey) (*types.WalletAccount, error)
	// types.EventWalletSendToAddress
	WalletSendToAddress(param *types.ReqWalletSendToAddress) (*types.ReplyHash, error)
	// types.EventWalletSetFee
	WalletSetFee(param *types.ReqWalletSetFee) (*types.Reply, error)
	// types.EventWalletSetLabel
	WalletSetLabel(param *types.ReqWalletSetLabel) (*types.WalletAccount, error)
	// types.EventWalletMergeBalance
	WalletMergeBalance(param *types.ReqWalletMergeBalance) (*types.ReplyHashes, error)
	// types.EventWalletSetPasswd
	WalletSetPasswd(param *types.ReqWalletSetPasswd) (*types.Reply, error)
	// types.EventWalletLock
	WalletLock() (*types.Reply, error)
	// types.EventWalletUnLock
	WalletUnLock(param *types.WalletUnLock) (*types.Reply, error)
	// types.EventGenSeed
	GenSeed(param *types.GenSeedLang) (*types.ReplySeed, error)
	// types.EventSaveSeed
	SaveSeed(param *types.SaveSeedByPw) (*types.Reply, error)
	// types.EventGetSeed
	GetSeed(param *types.GetSeedByPw) (*types.ReplySeed, error)
	// types.EventGetWalletStatus
	GetWalletStatus() (*types.WalletStatus, error)
	// types.EventWalletAutoMiner
	WalletAutoMiner(param *types.MinerFlag) (*types.Reply, error)
	// types.EventDumpPrivkey
	DumpPrivkey(param *types.ReqStr) (*types.ReplyStr, error)
	// types.EventCloseTickets
	CloseTickets() (*types.ReplyHashes, error)
	// types.EventSignRawTx
	SignRawTx(param *types.ReqSignRawTx) (*types.ReplySignRawTx, error)
	GetFatalFailure() (*types.Int32, error)
	// Privacy Begin
	// types.EventShowPrivacyAccountSpend
	ShowPrivacyAccountSpend(param *types.ReqPrivBal4AddrToken) (*types.UTXOHaveTxHashs, error)
	// types.EventShowPrivacyPK
	ShowPrivacyKey(param *types.ReqStr) (*types.ReplyPrivacyPkPair, error)
	// types.EventPublic2privacy
	Publick2Privacy(param *types.ReqPub2Pri) (*types.Reply, error)
	// types.EventPrivacy2privacy
	Privacy2Privacy(param *types.ReqPri2Pri) (*types.Reply, error)
	// types.EventPrivacy2public
	Privacy2Public(param *types.ReqPri2Pub) (*types.Reply, error)
	// types.EventCreateUTXOs
	CreateUTXOs(param *types.ReqCreateUTXOs) (*types.Reply, error)
	// types.EventCreateTransaction creating a transaction with the assistance of server
	CreateTrasaction(param *types.ReqCreateTransaction) (*types.Transaction, error)
	// types.EventPrivacyAccountInfo
	ShowPrivacyAccountInfo(param *types.ReqPPrivacyAccount) (*types.ReplyPrivacyAccount, error)
	// types.EventPrivacyTransactionList
	PrivacyTransactionList(param *types.ReqPrivacyTransactionList) (*types.WalletTxDetails, error)
	// types.EventRescanUtxos
	RescanUtxos(param *types.ReqRescanUtxos) (*types.RepRescanUtxos, error)
	// types.EventEnablePrivacy
	EnablePrivacy(param *types.ReqEnablePrivacy) (*types.RepEnablePrivacy, error)
	// Privacy End
	// --------------- wallet interfaces end

	// +++++++++++++++ blockchain interfaces begin
	// types.EventGetBlocks
	GetBlocks(param *types.ReqBlocks) (*types.BlockDetails, error)
	// types.EventQueryTx
	QueryTx(param *types.ReqHash) (*types.TransactionDetail, error)
	// types.EventGetTransactionByAddr
	GetTransactionByAddr(param *types.ReqAddr) (*types.ReplyTxInfos, error)
	// types.EventGetTransactionByHash
	GetTransactionByHash(param *types.ReqHashes) (*types.TransactionDetails, error)
	// types.EventGetHeaders
	GetHeaders(param *types.ReqBlocks) (*types.Headers, error)
	// types.EventGetBlockOverview
	GetBlockOverview(param *types.ReqHash) (*types.BlockOverview, error)
	// types.EventGetAddrOverview
	GetAddrOverview(param *types.ReqAddr) (*types.AddrOverview, error)
	// types.EventGetBlockHash
	GetBlockHash(param *types.ReqInt) (*types.ReplyHash, error)
	// types.EventIsSync
	IsSync() (*types.Reply, error)
	// types.EventIsNtpClockSync
	IsNtpClockSync() (*types.Reply, error)
	// types.EventGetLastHeader
	GetLastHeader() (*types.Header, error)
	//types.EventGetLastBlockSequence:
	GetLastBlockSequence() (*types.Int64, error)
	//types.EventGetBlockSequences:
	GetBlockSequences(param *types.ReqBlocks) (*types.BlockSequences, error)
	//types.EventGetBlockByHashes:
	GetBlockByHashes(param *types.ReqHashes) (*types.BlockDetails, error)
	// --------------- blockchain interfaces end

	// +++++++++++++++ store interfaces begin
	StoreGet(*types.StoreGet) (*types.StoreReplyValue, error)
	StoreGetTotalCoins(*types.IterateRangeByStateHash) (*types.ReplyGetTotalCoins, error)
	// --------------- store interfaces end

	// +++++++++++++++ other interfaces begin
	// close Chain33
	CloseQueue() (*types.Reply, error)
	// --------------- other interfaces end
}
```

Service initialization:

```go
func New(client queue.Client, option *QueueProtocolOption) (QueueProtocolAPI, error) {
	if client == nil {
		return nil, types.ErrInvalidParam
	}
	q := &QueueProtocol{}
	q.client = client
	if option != nil {
		q.option = *option
	} else {
		q.option.SendTimeout = 600 * time.Second
		q.option.WaitTimeout = 600 * time.Second
	}
	return q, nil
}
```

Wait for response:

```go
func (q *QueueProtocol) query(topic string, ty int64, data interface{}) (queue.Message, error) {
	client := q.client
	msg := client.NewMessage(topic, ty, data)
	err := client.SendTimeout(msg, true, q.option.SendTimeout)
	if err != nil {
		return queue.Message{}, err
	}
	return client.WaitTimeout(msg, q.option.WaitTimeout)
}
```

Topic is the key value used by each module when it registers in the message queue, which is defined as follows:

```go
const (
	mempoolKey = "mempool" // Unpacked Mempool
	p2pKey     = "p2p"     //
	consensusKey = "consensus" // Consensus system
	executorKey   = "execs"      // Transaction actuator
	walletKey     = "wallet"     // Wallet
	blockchainKey = "blockchain" // Block
	storeKey      = "store"
)
```

Ty is the type of the event, defined as follows:

```go
// event
const (
	EventTx                   = 1
	EventGetBlocks            = 2
	EventBlocks               = 3
	EventGetBlockHeight       = 4
	EventReplyBlockHeight     = 5
	EventQueryTx              = 6
	EventTransactionDetail    = 7
	EventReply                = 8
	EventTxBroadcast          = 9
	EventPeerInfo             = 10
	EventTxList               = 11
	EventReplyTxList          = 12
	EventAddBlock             = 13
	EventBlockBroadcast       = 14
	EventFetchBlocks          = 15
	EventAddBlocks            = 16
	EventTxHashList           = 17
	EventTxHashListReply      = 18
	EventGetHeaders           = 19
	EventHeaders              = 20
	EventGetMempoolSize       = 21
	EventMempoolSize          = 22
	EventStoreGet             = 23
	EventStoreSet             = 24
	EventStoreGetReply        = 25
	EventStoreSetReply        = 26
	EventReceipts             = 27
	EventExecTxList           = 28
	EventPeerList             = 29
	EventGetLastHeader        = 30
	EventHeader               = 31
	EventAddBlockDetail       = 32
	EventGetMempool           = 33
	EventGetTransactionByAddr = 34
	EventGetTransactionByHash = 35
	EventReplyTxInfo          = 36
	//wallet event
	EventWalletGetAccountList  = 37
	EventWalletAccountList     = 38
	EventNewAccount            = 39
	EventWalletAccount         = 40
	EventWalletTransactionList = 41
	//EventReplyTxList           = 42
	EventWalletImportprivkey = 43
	EventWalletSendToAddress = 44
	EventWalletSetFee        = 45
	EventWalletSetLabel      = 46
	//EventWalletAccount       = 47
	EventStoreDel           = 47
	EventWalletMergeBalance = 48
	EventReplyHashes        = 49
	EventWalletSetPasswd    = 50
	EventWalletLock         = 51
	EventWalletUnLock       = 52
	EventTransactionDetails = 53
	EventBroadcastAddBlock  = 54
	EventGetBlockOverview   = 55
	EventGetAddrOverview    = 56
	EventReplyBlockOverview = 57
	EventReplyAddrOverview  = 58
	EventGetBlockHash       = 59
	EventBlockHash          = 60
	EventGetLastMempool     = 61
	EventWalletGetTickets   = 62
	EventMinerStart         = 63
	EventMinerStop          = 64
	EventWalletTickets      = 65
	EventStoreMemSet        = 66
	EventStoreRollback      = 67
	EventStoreCommit        = 68
	EventCheckBlock         = 69
	//seed
	EventGenSeed      = 70
	EventReplyGenSeed = 71
	EventSaveSeed     = 72
	EventGetSeed      = 73
	EventReplyGetSeed = 74
	EventDelBlock     = 75
	//local store
	EventLocalGet            = 76
	EventLocalReplyValue     = 77
	EventLocalList           = 78
	EventLocalSet            = 79
	EventGetWalletStatus     = 80
	EventCheckTx             = 81
	EventReceiptCheckTx      = 82
	EventQuery               = 83
	EventReplyQuery          = 84
	EventFlushTicket         = 85
	EventFetchBlockHeaders   = 86
	EventAddBlockHeaders     = 87
	EventWalletAutoMiner     = 88
	EventReplyWalletStatus   = 89
	EventGetLastBlock        = 90
	EventBlock               = 91
	EventGetTicketCount      = 92
	EventReplyGetTicketCount = 93
	EventDumpPrivkey         = 94
	EventReplyPrivkey        = 95
	EventIsSync              = 96
	EventReplyIsSync         = 97

	EventCloseTickets            = 98
	EventGetAddrTxs              = 99
	EventReplyAddrTxs            = 100
	EventIsNtpClockSync          = 101
	EventReplyIsNtpClockSync     = 102
	EventDelTxList               = 103
	EventStoreGetTotalCoins      = 104
	EventGetTotalCoinsReply      = 105
	EventQueryTotalFee           = 106
	EventSignRawTx               = 107
	EventReplySignRawTx          = 108
	EventSyncBlock               = 109
	EventGetNetInfo              = 110
	EventReplyNetInfo            = 111
	EventErrToFront              = 112
	EventFatalFailure            = 113
	EventReplyFatalFailure       = 114
	EventBindMiner               = 115
	EventReplyBindMiner          = 116
	EventDecodeRawTx             = 117
	EventReplyDecodeRawTx        = 118
	EventGetLastBlockSequence    = 119
	EventReplyLastBlockSequence  = 120
	EventGetBlockSequences       = 121
	EventReplyBlockSequences     = 122
	EventGetBlockByHashes        = 123
	EventReplyBlockDetailsBySeqs = 124
	EventDelParaChainBlockDetail = 125
	EventAddParaChainBlockDetail = 126
	EventGetSeqByHash            = 127
	EventLocalPrefixCount        = 128
	// Token
	EventBlockChainQuery        = 212
	EventTokenPreCreate         = 200
	EventReplyTokenPreCreate    = 201
	EventTokenFinishCreate      = 202
	EventReplyTokenFinishCreate = 203
	EventTokenRevokeCreate      = 204
	EventReplyTokenRevokeCreate = 205
	EventSellToken              = 206
	EventReplySellToken         = 207
	EventBuyToken               = 208
	EventReplyBuyToken          = 209
	EventRevokeSellToken        = 210
	EventReplyRevokeSellToken   = 211
	// config
	EventModifyConfig      = 300
	EventReplyModifyConfig = 301

	// privacy
	EventPublic2privacy = iota + 400
	EventReplyPublic2privacy
	EventPrivacy2privacy
	EventReplyPrivacy2privacy
	EventPrivacy2public
	EventReplyPrivacy2public
	EventShowPrivacyPK
	EventReplyShowPrivacyPK
	EventShowPrivacyAccountSpend
	EventReplyShowPrivacyAccountSpend
	EventCreateUTXOs
	EventReplyCreateUTXOs
	EventCreateTransaction
	EventReplyCreateTransaction
	EventPrivacyAccountInfo
	EventReplyPrivacyAccountInfo
	EventPrivacyTransactionList
	EventReplyPrivacyTransactionList
	EventRescanUtxos
	EventReplyRescanUtxos
	EventEnablePrivacy
	EventReplyEnablePrivacy

	// monitor
	EventAddMonitorMetric = iota + 500
)
```

## 3 Instruction Introduction

### 3.1 account
Account management

```bash
Usage:
	Chain33-cli account [command]

Available Commands:
	balance     Get balance of a account address
	create      Create a new account with label
	dump_key    Dump private key for account address
	import_key  Import private key with label
	list        Get account list
	set_label   Set label for account address
```

#### 3.1.1 account balance: Query Account Balance
cli account balance -a "query address" -e "actuator address"

```bash
[lyn@localhost build]$ ./Chain33-cli account balance -a 14KEKbYtKKQm4wMthSK9J4La4nAiidGozt
{
    "addr": "14KEKbYtKKQm4wMthSK9J4La4nAiidGozt",
    "execAccount": [
        {
            "execer": "coins",
            "account": {
                "balance": "100000000.0000",
                "frozen": "0.0000"
            }
        }
    ]
}
```

#### 3.1.2 account create: Create A New Account
cli account create -l "custom address label"

```bash
[lyn@localhost build]$ ./Chain33-cli account create -l test
{
    "acc": {
        "balance": "0.0000",
        "frozen": "0.0000",
        "addr": "1RackwdGHK5CzdP8oytmRvdb5EGQP3YUX"
    },
    "label": "test"
}
```

#### 3.1.3 account dump_key: Export Wallet Address Private Key 
cli account dump_key -a "account address to export"

```bash
[lyn@localhost build]$ ./Chain33-cli account dump_key -a 1RackwdGHK5CzdP8oytmRvdb5EGQP3YUX
{
    "replystr": "0x1a8ba8d001fe0a11b02622297ab599f7a1c1116e272ad759d602c7ba708c55d4"
}
```

#### 3.1.4 account import_key: Import Wallet Address Private Key 
cli account import_key -k "external private key" -l "address label"

```bash
[lyn@localhost build]$ ./Chain33-cli account import_key -k "0xa830cd3b4b4b236153c9b67bc161076f0e43eb002fec71e283c0ee0d1f644623" -l test
{
    "acc": {
        "balance": "0.0000",
        "frozen": "0.0000",
        "addr": "183BMp5Qcjx52e5yGERGs97DPCioChW7gj"
    },
    "label": "test"
}
```

#### 3.1.5 account list: Get Account List
cli account list

```bash
[lyn@localhost build]$ ./Chain33-cli account list
{
    "wallets": [
        {
            "acc": {
                "balance": "0.0000",
                "frozen": "0.0000",
                "addr": "16mMKG3h8yGJxUji6pUQGQWDd29jHA6e2Q"
            },
            "label": "node award"
        },
        {
            "acc": {
                "balance": "0.0000",
                "frozen": "0.0000",
                "addr": "183BMp5Qcjx52e5yGERGs97DPCioChW7gj"
            },
            "label": "test"
        }
    ]
}
```

#### 3.1.6 account set_label: Set Account Address Label Name
cli account set_label -a "account address" -l "address table signature"

```bash
[lyn@localhost build]$ ./Chain33-cli account set_label -a 183BMp5Qcjx52e5yGERGs97DPCioChW7gj -l test1
{
    "acc": {
        "balance": "0.0000",
        "frozen": "0.0000",
        "addr": "183BMp5Qcjx52e5yGERGs97DPCioChW7gj"
    },
    "label": "test1"
}
```

### 3.2 block
Get block header or body info

```bash
Usage:
  Chain33-cli block [command]

Available Commands:
  get           Get blocks between [start, end]
  hash          Get hash of block at height
  headers       Get block headers between [start, end]
  last_header   View last block header
  last_sequence View last block sequence
  query_hashs   Query block by hashs
  sequences     Get block sequences between [start, end]
  view          View block info by block hash
```

#### 3.2.1 block get: Get Block Details for the Specified Block Height Interval
cli block get -s "initial query height" -e "end query height" -d "whether to display details"(optional)

```bash
Usage:
  Chain33-cli block get [flags]

Flags:
  -d, --detail string   whether print block detail info (0/f/false for No; 1/t/true for Yes) (default "f")
  -e, --end int         block end height
  -h, --help            help for get
  -s, --start int       block start height
```
Example:
```bash
[lyn@localhost build]$ ./Chain33-cli block get -s 5765 -e 5765
{
    "items": [
        {
            "block": {
                "version": 0,
                "parenthash": "0x5153191bb51dacb01311f6ef15726fed82f84b756603fbf0d49a473562e45672",
                "txhash": "0x22849a81d554b4f914d7d65c1080d8cc98e5d1de0fd2be4f0db34b439c6a0173",
                "statehash": "0x0352bdf0ddb0d51d3e68aa75d402a880c4d877683c2a6393971ca80462af8efd",
                "height": 5765,
                "blocktime": 1541135879,
                "txs": [
                    {
                        "execer": "norm",
                        "payload": {
                            "rawlog": "0x28010a7c0a1445565641784b61484d797a7175586e494856424f1264774f4a7457625a4846464b5a6e67766a756b6d665179784558526c4f56536b75626659446c736a6951434166695a44424e65506150657841644b42667a5559514548684f6349594b5a576f48447a68726156795a6f73786b44424844734c504458656765"
                        },
                        "rawpayload": "0x28010a7c0a1445565641784b61484d797a7175586e494856424f1264774f4a7457625a4846464b5a6e67766a756b6d665179784558526c4f56536b75626659446c736a6951434166695a44424e65506150657841644b42667a5559514548684f6349594b5a576f48447a68726156795a6f73786b44424844734c504458656765",
                        "signature": {
                            "ty": 1,
                            "pubkey": "0x03fe25b1a4261c4b98ad1b81307c7b20b776be6c503b95afb5d73ca9d42daecd7a",
                            "signature": "0x3044022078d751b8e1d0daeb0aa0eb264ce7b54e1320c7017953a397f38d8cb6c920b93902200267edab907706fa2cbb4bb8606e8677135ee7be5fb820c66ae0004056c2cca8"
                        },
                        "fee": "0.0100",
                        "expire": 0,
                        "nonce": 6935173039743788574,
                        "to": "1CnmrBJcpTiY6TphmuAiz7HoYSsGwgYgho",
                        "from": "1FbZaK5HJRwDaN2sQ5oRoUwi7fHJA1QJT1"
                    }
                ]
            },
            "receipts": null
        }
    ]
}
```

#### 3.2.2 block hash: Get Block Hash for the Specified Height of the Block

cli block hash -t {block height}

```bash
Usage:
  Chain33-cli block hash [flags]

Flags:
  -t, --height int   block height
  -h, --help         help for hash
```

Example:
```bash
[lyn@localhost build]$ ./Chain33-cli block hash -t 10
{
    "hash": "0x09055102ecb36033adde0fc9c0d523500c1d81693e7ad12181cfc2497b407da9"
}
```

#### 3.2.3 block headers：Get the Block Header Information Within the Specified Block Height Interval
cli block headers -s initial query height -e end query height

```bash
Usage:
  Chain33-cli block headers [flags]

Flags:
  -d, --detail string   whether print header detail info (0/f/false for No; 1/t/true for Yes) (default "f")
  -e, --end int         block end height
  -h, --help            help for headers
  -s, --start int       block start height
```

Example:

```bash
[lyn@localhost build]$ ./Chain33-cli block headers -s 5765 -e 5765
{
    "items": [
        {
            "version": 0,
            "parentHash": "0x5153191bb51dacb01311f6ef15726fed82f84b756603fbf0d49a473562e45672",
            "txHash": "0x22849a81d554b4f914d7d65c1080d8cc98e5d1de0fd2be4f0db34b439c6a0173",
            "stateHash": "0x0352bdf0ddb0d51d3e68aa75d402a880c4d877683c2a6393971ca80462af8efd",
            "height": 5765,
            "blockTime": 1541135879,
            "txCount": 1,
            "hash": "0xeab471cf4957253ac991bc56744ef7ae9a6b249236e97db2c5c4d998d3e787f2",
            "difficulty": 0
        }
    ]
}
```

※ The cli command has an optional parameter entry for -d, but it has no effect. Can be omitted.

#### 3.2.4 block last_header: Get the Latest Block Header Information of the Current Synchronized Block in this Wallet
cli block last_header

```bash
[lyn@localhost build]$ ./Chain33-cli block last_header
{
    "version": 0,
    "parentHash": "0xb6bedeb8b7bcd52348f162bed80bf26420df3e886a13ff9aaf7eb2b733cf392d",
    "txHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
    "stateHash": "0x0352bdf0ddb0d51d3e68aa75d402a880c4d877683c2a6393971ca80462af8efd",
    "height": 5772,
    "blockTime": 1541136720,
    "txCount": 0,
    "hash": "0x08bcf1957beb722ca874d46f7f7e35b4dea032ac4c0bd519c2eee214e1661284",
    "difficulty": 0
}
```

#### 3.2.5 block last_sequence: Get the Latest Sequential Number that the Wallet is Currently Synchronized with
cli block last_sequence

```bash
[lyn@localhost build]$ ./Chain33-cli block last_sequence
33
```

※ The configuration item whether the sequence is open in the configuration file, which should be off by default and returns 0.

#### 3.2.6 block query_hashs: Get Block Details by Block Hash
cli block query_hashs "hash 1" "hash 2"

```bash
[lyn@localhost build]$ ./Chain33-cli block query_hashs -s 0x08bcf1957beb722ca874d46f7f7e35b4dea032ac4c0bd519c2eee214e1661284
{
    "items": [
        {
            "block": {
                "parentHash": "tr7euLe81SNI8WK+2AvyZCDfPohqE/+ar36ytzPPOS0=",
                "txHash": "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=",
                "stateHash": "A1K98N2w1R0+aKp11AKogMTYd2g8KmOTlxyoBGKvjv0=",
                "height": 5772,
                "blockTime": 1541136720
            },
            "prevStatusHash": "A1K98N2w1R0+aKp11AKogMTYd2g8KmOTlxyoBGKvjv0="
        }
    ]
}
```

#### 3.2.7 block sequences: Query the Corresponding Block Hash According to the Sequential Number (only used for parallel chain correlation)
cli block sequences -s "initial query height" -e "end query height"

```bash
[lyn@localhost build]$ ./Chain33-cli block sequences -s 0 -e 1
{
    "blkseqInfos": [
        {
            "hash": "0x67c58d6ba9175313f0468ae4e0ddec946549af7748037c2fdd5d54298afd20b6",
            "type": 1
        }
    ]
}
```

#### 3.2.8 block view: Query the Block Header Information for the Specified Block Based on the Block Hash
cli block view -s block hash

```bash
[lyn@localhost build]$ ./Chain33-cli block view -s 0xeab471cf4957253ac991bc56744ef7ae9a6b249236e97db2c5c4d998d3e787f2
{
    "head": {
        "version": 0,
        "parentHash": "0x5153191bb51dacb01311f6ef15726fed82f84b756603fbf0d49a473562e45672",
        "txHash": "0x22849a81d554b4f914d7d65c1080d8cc98e5d1de0fd2be4f0db34b439c6a0173",
        "stateHash": "0x0352bdf0ddb0d51d3e68aa75d402a880c4d877683c2a6393971ca80462af8efd",
        "height": 5765,
        "blockTime": 1541135879,
        "txCount": 1,
        "hash": "0xeab471cf4957253ac991bc56744ef7ae9a6b249236e97db2c5c4d998d3e787f2",
        "difficulty": 0
    },
    "txCount": 1,
    "txHashes": [
        "0x22849a81d554b4f914d7d65c1080d8cc98e5d1de0fd2be4f0db34b439c6a0173"
    ]
}
```

### 3.3 bty
Construct BTY transactions

```bash
Usage:
  Chain33-cli bty [command]

Available Commands:
  priv2priv   Create a privacy to privacy transaction
  priv2pub    Create a privacy to public transaction
  pub2priv    Create a public to privacy transaction
  send_exec   Create a send to executor transaction
  transfer    Create a transfer transaction
  txgroup     Create a transaction group
  withdraw    Create a withdraw transaction
```

#### 3.3.1 send_exec Construct Transaction Transfer to Specified Actuator at Specified Address
cli bty send_exec -a "sending limit" -e "destination actuator" -n "transaction remarks"  

```bash
[lyn@localhost build]$ ./Chain33-cli bty send_exec -a 1000 -e coins
0a05636f696e731212180a2a0e1080d0dbc3f4022205636f696e7320a08d0630e892958d98bbb6fa7b3a22314761485970576d71414a7371527772706f4e6342385676674b7453776a63487174
```

※ Unsigned transaction information is returned. See sign and send in wallet for further information

#### 3.3.2 transfer
cli bty transfer -a "transfer limit" -t "receiver account address" -n "transaction remarks"

```bash
[lyn@localhost build]$ ./Chain33-cli bty transfer -a 5210314 -t "1CRkrCJHHqgQFm59AiHe35T5vJ1o5QpPW3"
0a05636f696e73123018010a2c1080948e9c81bc7622223143526b72434a4848716751466d35394169486533355435764a316f35517050573320a08d06309de3af99a6c087bc7c3a223143526b72434a4848716751466d35394169486533355435764a316f355170505733
```

※ Unsigned transaction information is returned. See sign and send in wallet for further information

#### 3.3.3 withdraw
cli bty withdraw -a "transaction limit" -e "name of the executor that sends the transaction" -n "transaction remarks"

```bash
[lyn@localhost build]$ ./Chain33-cli bty withdraw -a 1000 -e coins
0a05636f696e7312121803220e1080d0dbc3f4022205636f696e7320a08d0630f3eaba82b5b098c56e3a22314761485970576d71414a7371527772706f4e6342385676674b7453776a63487174
```

### 3.4 exec
Executor operation
```bash
Usage:
  Chain33-cli exec [command]

Available Commands:
  addr        Get address of executor
  userdata    Write data to user defined executor
```
#### 3.4.1 addr: Get Actuator Address 
cli exec addr -e "actuator name"
```bash
[lyn@localhost build]$ ./Chain33-cli exec addr  -e coins
1GaHYpWmqAJsqRwrpoNcB8VvgKtSwjcHqt
```
### 3.5 mempool
Mempool management
```bash
Usage:
  Chain33-cli mempool [command]

Available Commands:
  last_txs    Get latest mempool txs
  list        List mempool txs
```
#### 3.5.1 last_txs: Get the Last Ten Transactions in Mempool
cli mempool last_txs
```bash
[lyn@localhost build]$ ./Chain33-cli mempool last_txs
{
    "txs": [
        {
            "execer": "norm",
            "payload": {
                "nput": {
                    "key": "vrgMFUSFeEWNdJBUEWTJ",
                    "value": "0x6c5a706d44566b756251766e69757547494375645341416c564b5967426c504c797158414169456e7577754d6d4b477363726c6369714b43707978414865426579445963484b774274664f65706249464970635351524c744a42544d66554351745a7965"
                },
                "ty": 1
            },
            "rawpayload": "0x28010a7c0a147672674d465553466545574e644a42554557544a12646c5a706d44566b756251766e69757547494375645341416c564b5967426c504c797158414169456e7577754d6d4b477363726c6369714b43707978414865426579445963484b774274664f65706249464970635351524c744a42544d66554351745a7965",
            "signature": {
                "ty": 1,
                "pubkey": "0x027bdcc95bc051df0e047cd76f8488b40fd513e429c1b284ddd990f531e4cf42af",
                "signature": "0x304402202c671aac350f56bd07a3563e3c3bebfbc7ffae2d10ce7c7ea4e14953c7f6770b02203b4fe2185481ba17d089d309150e01e68682c0a5b3d46d3532ad93c1304961ab"
            },
            "fee": "0.0100",
            "expire": 0,
            "nonce": 8872632247761828259,
            "to": "1CnmrBJcpTiY6TphmuAiz7HoYSsGwgYgho",
            "from": "17DjBft6j9VBxJddRxe9eSCiN1Y2NiDe7L"
        }
    ]
}
```
#### 3.5.2 list: Get Transaction List in Mempool
cli mempool list
```bash
[lyn@localhost build]$ ./Chain33-cli mempool list
{
    "txs": [
        {
            "execer": "norm",
            "payload": {
                "nput": {
                    "key": "vrgMFUSFeEWNdJBUEWTJ",
                    "value": "0x6c5a706d44566b756251766e69757547494375645341416c564b5967426c504c797158414169456e7577754d6d4b477363726c6369714b43707978414865426579445963484b774274664f65706249464970635351524c744a42544d66554351745a7965"
                },
                "ty": 1
            },
            "rawpayload": "0x28010a7c0a147672674d465553466545574e644a42554557544a12646c5a706d44566b756251766e69757547494375645341416c564b5967426c504c797158414169456e7577754d6d4b477363726c6369714b43707978414865426579445963484b774274664f65706249464970635351524c744a42544d66554351745a7965",
            "signature": {
                "ty": 1,
                "pubkey": "0x027bdcc95bc051df0e047cd76f8488b40fd513e429c1b284ddd990f531e4cf42af",
                "signature": "0x304402202c671aac350f56bd07a3563e3c3bebfbc7ffae2d10ce7c7ea4e14953c7f6770b02203b4fe2185481ba17d089d309150e01e68682c0a5b3d46d3532ad93c1304961ab"
            },
            "fee": "0.0100",
            "expire": 0,
            "nonce": 8872632247761828259,
            "to": "1CnmrBJcpTiY6TphmuAiz7HoYSsGwgYgho",
            "from": "17DjBft6j9VBxJddRxe9eSCiN1Y2NiDe7L"
        }
    ]
}
```
### 3.6 net
Net operation
```bash
Usage:
  Chain33-cli net [command]

Available Commands:
  fault         Get system fault
  info          Get net information
  is_clock_sync Get ntp clock synchronization status
  is_sync       Get blockchain synchronization status
  peer_info     Get remote peer nodes
  time          Get time status
```
#### 3.6.1 fault: Check the Number of Major Failures on this Node
cli net fault
```bash
[lyn@localhost build]$ ./Chain33-cli net fault
0
```
#### 3.6.2 info：Query the Network Information of this Node
cli net info
```bash
[lyn@localhost build]$ ./Chain33-cli net info
{
    "externalAddr": "192.168.0.147:13802",
    "localAddr": "192.168.0.147:13802",
    "service": true,
    "outbounds": 0,
    "inbounds": 0
}
```
#### 3.6.3 is_clock_sync: Check if This Node Time is Synchronized
cli net is\_clock_syn
```bash
[lyn@localhost build]$ ./Chain33-cli net is_clock_sync
true
```
#### 3.6.4 is_sync: Check if This Node Time is Synchronized
cli net is_sync
```bash
[lyn@localhost build]$ ./Chain33-cli net  is_sync
true
```
#### 3.6.5 peer_info: Check if This Node Time is Synchronized
cli net peer_info
```bash
[lyn@localhost build]$ ./Chain33-cli net peer_info
{
    "peers": [
        {
            "addr": "192.168.0.147",
            "port": 13802,
            "name": "02e466e00b8db4e67de85d7c667dabeda92faea9fd06f72c29b2c851eb106fefa4",
            "mempoolSize": 0,
            "self": true,
            "header": {
                "version": 0,
                "parentHash": "0x5be67d5026e2bc4aede0feda9ce7cea214b7dc89eff481f1f2c4d33e6a7a3c0a",
                "txHash": "0x0a382a097d9b7e2d0971832e1b7d49f41059cd6340a5c241f7a4c91bbeaf896f",
                "stateHash": "0x98f10651192e2df48a0b48200c9024896e1351a342403d27227ee0f37025f15b",
                "height": 5,
                "blockTime": 1541393636,
                "txCount": 100,
                "hash": "0xab67feeb56baf68eef300ef1f01a2fbe026623e3846729277d74de008e149e58",
                "difficulty": 0
            }
        }
    ]
}
```

#### 3.6.6 time: Get Local Time and NTP Time
cli net time
```bash
[lyn@localhost build]$ ./Chain33-cli net time
{
    "ntpTime": "2018-11-05 14:20:08",
    "localTime": "2018-11-05 12:55:08",
    "diff": -5100
}
```
### 3.7 seed
Seed management
```bash
Usage:
  Chain33-cli seed [command]

Available Commands:
  generate    Generate seed
  get         Get seed by password
  save        Save seed and encrypt with passwd
```
#### 3.7.1 generate: Generate Seed
cli seed generate -l "seed language type 0:'English' 1:' simplified Chinese '"
```bash
[lyn@localhost build]$ ./Chain33-cli seed generate -l 0
{
    "seed": "melt inflict dose foam tuna whip fruit boil scrub rude puzzle length ask cruise embody"
}
```
#### 3.7.2 get: Get the Seed of this Wallet
cli seed get -p "get the password of seed"
```bash
[lyn@localhost build]$ ./Chain33-cli seed get -p fzm
{
    "seed": "melt inflict dose foam tuna whip fruit boil scrub rude puzzle length ask cruise embody"
}
```
#### 3.7.3 save: Save the Seed in this Wallet
cli seed save -s "space-delimited seed(15 characters or words)" -p "password used in seed encryption"
```bash
[lyn@localhost build]$ ./Chain33-cli seed save -s "melt inflict dose foam tuna whip fruit boil scrub rude puzzle length ask cruise embody" -p fzm
{
    "isOK": true,
    "msg": ""
}
```
### 3.8 send
cli send bty transfer -a "transaction limit" -n "note" -t "receiver address" -k "private key/sender address"
```bash
[lyn@localhost build]$ ./Chain33-cli send bty transfer -a "1000" -n "transfer tx" -t "1LBKc8mA7s57sVoij6AhL7CG6pS3TFkqBu" -k "14KEKbYtKKQm4wMthSK9J4La4nAiidGozt"
0x037513739705f899d92add16b3bbcc077076d81e20074b61ca7b391875514480
```
### 3.9 stat
Coin statistic
```bash
Usage:
  Chain33-cli stat [command]

Available Commands:
  miner            Get miner statistic
  ticket_info      Get ticket info by ticket_id
  ticket_info_list Get ticket info list by ticket_id
  ticket_stat      Get ticket statistics by addr
  total_coins      Get total amount of a token (default: bty of current height)
```

### 3.10 tx
Transaction management
```bash
Usage:
Chain33-cli tx [command]

Available Commands:
addr_overview View transactions of address
decode        Decode a hex format transaction
get_hex       Get transaction hex by hash
query         Query transaction by hash
query_addr    Query transaction by account address
query_hash    Get transactions by hashes
```
#### 3.10.1 addr_overview: Query Transactions of the Specified Address Under the Coins Contract
cli tx addr_overview -a "account address"
```bash
[lyn@localhost build]$ ./Chain33-cli tx addr_overview  -a 1EcE1nzwRzhrUUVy9k2xDMH5kw9bymcJPc
{
    "receiver": "1000.0000",
    "balance": "100.9960",
    "txCount": 5
}
```
#### 3.10.2 decode: Decode Transaction String
cli tx decode -d "transaction information needs to be decoded"
```bash
[lyn@localhost build]$ ./Chain33-cli tx decode -d 0a05636f696e7312121803220e1080d0dbc3f4022205636f696e7320a08d0630eaceade1e389c1a5293a22314761485970576d71414a7371527772706f4e6342385676674b7453776a63487174
{
    "execer": "coins",
    "payload": {
        "withdraw": {
            "cointoken": "",
            "amount": "100000000000",
            "note": "",
            "execName": "coins",
            "to": ""
        },
        "ty": 3
    },
    "rawpayload": "0x1803220e1080d0dbc3f4022205636f696e73",
    "signature": {
        "ty": 0,
        "pubkey": "",
        "signature": ""
    },
    "fee": "0.0010",
    "expire": 0,
    "nonce": 2975476712871782250,
    "to": "1GaHYpWmqAJsqRwrpoNcB8VvgKtSwjcHqt",
    "from": "1HT7xU2Ngenf7D4yocz2SAcnNLW7rK8d4E"
}
```
#### 3.10.3 get_hex: Get Hexadecimal String Based on Transaction
cli tx get_hex -s "transaction hash"
```bash
[lyn@localhost build]$ ./Chain33-cli tx get_hex -s 0x57fbde79b74a0c3286ca5947c05a5b95efd14f1411669bedabae1c68390237a3
0a05636f696e73122f18010a2b1080b081daaf14222231456345316e7a77527a687255555679396b3278444d48356b773962796d634a50631a6e0801122102504fa1c28caaf1d5a20fefb87c50a49724ff401043420cb3ba271997eb5a43871a47304502210081d32f66581903960f5fedc79ad742f43a4198209b766e1d5e6668288c3a9bc9022062bb2aa67c5db22aff68cc179fd7af7aad92b7f8cfd634857ff9b77c9c97d86320a08d062887e789df05309bd0b0d793f4cfca6f3a2231456345316e7a77527a687255555679396b3278444d48356b773962796d634a5063
```
#### 3.10.4 query: Get Transaction Details By Transaction Hash
cli tx query -s "transaction hash"
```bash
[lyn@localhost build]$ ./Chain33-cli  tx query -s 0x57fbde79b74a0c3286ca5947c05a5b95efd14f1411669bedabae1c68390237a3
{
    "tx": {
        "execer": "coins",
        "payload": {
            "transfer": {
                "cointoken": "",
                "amount": "700000000000",
                "note": "",
                "to": "1EcE1nzwRzhrUUVy9k2xDMH5kw9bymcJPc"
            },
            "ty": 1
        },
        "rawpayload": "0x18010a2b1080b081daaf14222231456345316e7a77527a687255555679396b3278444d48356b773962796d634a5063",
        "signature": {
            "ty": 1,
            "pubkey": "0x02504fa1c28caaf1d5a20fefb87c50a49724ff401043420cb3ba271997eb5a4387",
            "signature": "0x304502210081d32f66581903960f5fedc79ad742f43a4198209b766e1d5e6668288c3a9bc9022062bb2aa67c5db22aff68cc179fd7af7aad92b7f8cfd634857ff9b77c9c97d863"
        },
        "fee": "0.0010",
        "expire": 1541567367,
        "nonce": 8040402671450728475,
        "to": "1EcE1nzwRzhrUUVy9k2xDMH5kw9bymcJPc",
        "from": "14KEKbYtKKQm4wMthSK9J4La4nAiidGozt"
    },
    "receipt": {
        "ty": 2,
        "tyName": "ExecOk",
        "logs": [
            {
                "ty": 2,
                "tyName": "LogFee",
                "log": {
                    "prev": {
                        "currency": 0,
                        "balance": "9999699999700000",
                        "frozen": "0",
                        "addr": "14KEKbYtKKQm4wMthSK9J4La4nAiidGozt"
                    },
                    "current": {
                        "currency": 0,
                        "balance": "9999699999600000",
                        "frozen": "0",
                        "addr": "14KEKbYtKKQm4wMthSK9J4La4nAiidGozt"
                    }
                },
                "rawLog": "0x0a2d10a0e8deb2c9d5e111222231344b454b6259744b4b516d34774d7468534b394a344c61346e41696964476f7a74122d1080dbd8b2c9d5e111222231344b454b6259744b4b516d34774d7468534b394a344c61346e41696964476f7a74"
            },
            {
                "ty": 3,
                "tyName": "LogTransfer",
                "log": {
                    "prev": {
                        "currency": 0,
                        "balance": "9999699999600000",
                        "frozen": "0",
                        "addr": "14KEKbYtKKQm4wMthSK9J4La4nAiidGozt"
                    },
                    "current": {
                        "currency": 0,
                        "balance": "9998999999600000",
                        "frozen": "0",
                        "addr": "14KEKbYtKKQm4wMthSK9J4La4nAiidGozt"
                    }
                },
                "rawLog": "0x0a2d1080dbd8b2c9d5e111222231344b454b6259744b4b516d34774d7468534b394a344c61346e41696964476f7a74122d1080abd7d899c1e111222231344b454b6259744b4b516d34774d7468534b394a344c61346e41696964476f7a74"
            },
            {
                "ty": 3,
                "tyName": "LogTransfer",
                "log": {
                    "prev": {
                        "currency": 0,
                        "balance": "300000000000",
                        "frozen": "0",
                        "addr": "1EcE1nzwRzhrUUVy9k2xDMH5kw9bymcJPc"
                    },
                    "current": {
                        "currency": 0,
                        "balance": "1000000000000",
                        "frozen": "0",
                        "addr": "1EcE1nzwRzhrUUVy9k2xDMH5kw9bymcJPc"
                    }
                },
                "rawLog": "0x0a2b1080f092cbdd08222231456345316e7a77527a687255555679396b3278444d48356b773962796d634a5063122b1080a094a58d1d222231456345316e7a77527a687255555679396b3278444d48356b773962796d634a5063"
            }
        ]
    },
    "height": 38,
    "index": 0,
    "blocktime": 1541567247,
    "amount": "7000.0000",
    "fromaddr": "14KEKbYtKKQm4wMthSK9J4La4nAiidGozt",
    "actionname": "transfer"
}
```

#### 3.10.5 query_addr: Get Transaction List from the Account Address
cli tx query_addr -a "account address" -t "block height" -c "maximum number of returns" -d "query method" -f "transaction method" 
```bash
[lyn@localhost build]$  ./Chain33-cli  tx query_addr -a 1EcE1nzwRzhrUUVy9k2xDMH5kw9bymcJPc -t 36 -c 1 -d 0 -f 0
{
    "txInfos": [
        {
            "hash": "0x79811df8d4ea2fabc1a14e57e48014d71a95dcca34b336e44318920445886862",
            "height": 35,
            "index": 0,
            "assets": [
                {
                    "exec": "coins",
                    "symbol": "BTY"
                }
            ]
        }
    ]
}
```
#### 3.10.6 query_hash: Get Transaction Details by Transaction Hash (group)
cli tx query_hash -s "transaction hash" "transaction hash" "transaction hash" ...

### 3.11 version
Version info
```bash
[lyn@localhost build]$ ./Chain33-cli version
5.3.0-04cad269
```

### 3.12 wallet
Wallet management
```bash
Usage:
  Chain33-cli wallet [command]

Available Commands:
  auto_mine   Set auto mine on/off
  list_txs    List transactions in wallet
  lock        Lock wallet
  merge       Merge accounts' balance into address
  nobalance   Create nobalance transaction
  send        Send a transaction
  set_fee     Set transaction fee
  set_pwd     Set password
  sign        Sign transaction
  status      Get wallet status
  unlock      Unlock wallet
```
#### 3.12.1 auto_mine: Get Transaction List of this Wallet
cli wallet auto_mine -f "whether to start automatic mining (0:off 1:on)"

```bash
[lyn@localhost build]$ ./Chain33-cli  wallet auto_mine -f 0
{
    "isOK": true,
    "msg": ""
}
```

#### 3.12.2 list_txs: Get the Transaction List of this Wallet
cli wallet list_txs -c "transaction amount" -d "query method" -f "initial trading address of the query"

#### 3.12.3 lock: Lock the Wallet
cli wallet lock
```bash
[lyn@localhost build]$ ./Chain33-cli wallet lock
{
    "isOK": true,
    "msg": ""
}
```
#### 3.12.4 merge: Wallet Address Balance Merge
cli wallet merge -t "target account address in the wallet"
```bash
[lyn@localhost build]$ ./Chain33-cli wallet merge -t 1669FvjdPUAqaNLz8yBpXGnfDcqFL7zozG
{
    "hashes": [
        "0x5664ed144c6d202d6085eb1348e5d6e4c2f3e3d9745806af1e5189b1798a9800"
    ]
}
```
#### 3.12.5 nobalance: Construct Transaction Group Without Commission for Transactions Do Not Involve Transfer Amounts
cli wallet nobalance -d "unsigned transaction data" -k "private key signature"
```bash
[lyn@localhost build]$ ./Chain33-cli wallet nobalance -d "0a14757365722e702e67756f64756e2e7469636b6574" -k 0x2660c263b11dbdc1c78e8183230ceec1d0204b00f9cfc220c68b9df3aedc116c
0a046e6f6e6512126e6f2d6665652d7472616e73616374696f6e1a6e08011221036874ba6f252d49c6b90e586ef8fadcaa8b70a7300de3c8ef0cd91dc26eb7d72d1a4730450221009ff944a8118258088f3521a7dadd139d43cf981b76479e2b83f10ee6f9a44aba022054068759504c3112f8fffeea3a0c64edbe2b56831d5525d07fb56c50ed4ce6c520d00f30c6eed8caf287a0e94c3a2231447a5464544c61354a50704c644e4e50325072563161364a4374554c413747735440024ac0020a81020a046e6f6e6512126e6f2d6665652d7472616e73616374696f6e1a6e08011221036874ba6f252d49c6b90e586ef8fadcaa8b70a7300de3c8ef0cd91dc26eb7d72d1a4730450221009ff944a8118258088f3521a7dadd139d43cf981b76479e2b83f10ee6f9a44aba022054068759504c3112f8fffeea3a0c64edbe2b56831d5525d07fb56c50ed4ce6c520d00f30c6eed8caf287a0e94c3a2231447a5464544c61354a50704c644e4e50325072563161364a4374554c413747735440024a2064aa77679686ff056fa1403cc71accc34ade6b668a6971d0cbdd3e3d5a727e895220d8e9b0eaa0a3a6c46cebe56ae8cd662457bf4fa32e866c4ceca36c4ea984b5640a3a0a14757365722e702e67756f64756e2e7469636b657440024a2064aa77679686ff056fa1403cc71accc34ade6b668a6971d0cbdd3e3d5a727e895220d8e9b0eaa0a3a6c46cebe56ae8cd662457bf4fa32e866c4ceca36c4ea984b564
```
#### 3.12.6 send: Send Signed Transaction 
cli wallet send -d "signed transaction information" -t "token name sent (default: BTY)"
```bash
[lyn@localhost build]$ ./Chain33-cli wallet send -d 0a13757365722e702e67756f64756e2e746f6b656e1236380422320a03434e59100a1a05313233313222223136363946766a6450554171614e4c7a3879427058476e66446371464c377a6f7a471a6d0801122102504fa1c28caaf1d5a20fefb87c50a49724ff401043420cb3ba271997eb5a43871a463044022067f735e00946957fde90a7a3ba4418c3e3771977f13b2dc510f6172b0cfb97d902202d2a11e7a69aeee8adf42607d1e32e42c6a43b10ca0702f704cd54e151c045fa20a08d0628cae2ffde053085caa48bc7c594be113a223144527535423766505961776179414b524648315857536e354b66415654386d6848
0x66a9cd227a8483a20c66032d7c071f93de4bf23b430adbed4ee6aa91ec349f15 
```
※ Return the transaction hash recorded in the block

#### 3.12.7 set_fee: Set Transaction Commission Fee
cli wallet set_fee -a "transaction fee"
```bash
[lyn@localhost build]$ ./Chain33-cli wallet set_fee -a 100
{
    "isOK": true,
    "msg": ""
}
```
#### 3.12.8 set_pwd: Set Wallet Password
cli wallet set_pwd -o "old password" -n "new password"
```bash
[lyn@localhost build]$ ./Chain33-cli wallet set_pwd -o fzm -n fzm123
{
    "isOK": true,
    "msg": ""
}
```

#### 3.12.9 sign：Sign the Constructed Transaction
cli wallet sign -d "unsigned transaction information" -a signature address/-k signature private key -e timeout (default: 120 seconds)
```bash
[lyn@localhost build]$ ./Chain33-cli wallet sign -d 0a13757365722e702e67756f64756e2e746f6b656e1236380422320a03434e59100a1a05313233313222223136363946766a6450554171614e4c7a3879427058476e66446371464c377a6f7a4720a08d063085caa48bc7c594be113a223144527535423766505961776179414b524648315857536e354b66415654386d6848 -a 14KEKbYtKKQm4wMthSK9J4La4nAiidGozt
0a13757365722e702e67756f64756e2e746f6b656e1236380422320a03434e59100a1a05313233313222223136363946766a6450554171614e4c7a3879427058476e66446371464c377a6f7a471a6d0801122102504fa1c28caaf1d5a20fefb87c50a49724ff401043420cb3ba271997eb5a43871a463044022067f735e00946957fde90a7a3ba4418c3e3771977f13b2dc510f6172b0cfb97d902202d2a11e7a69aeee8adf42607d1e32e42c6a43b10ca0702f704cd54e151c045fa20a08d0628cae2ffde053085caa48bc7c594be113a223144527535423766505961776179414b524648315857536e354b66415654386d6848
```
※ Return encrypted transaction information

#### 3.12.10 status: Get Wallet Status
cli wallet status
```bash
[lyn@localhost build]$ ./Chain33-cli wallet status
{
    "isWalletLock": false,
    "isAutoMining": false,
    "isHasSeed": true,
    "isTicketLock": true
}
```
#### 3.12.11 unlock: Get Wallet Status
cli wallet unlock -p "password" -t "duration" -s "unlock range (default to unlock wallet)"
```bash
[lyn@localhost build]$ ./Chain33-cli wallet unlock -p fzm -t 0
{
    "isOK": true,
    "msg": ""
}
```
---