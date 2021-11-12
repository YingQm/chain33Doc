# 1 Unfreeze

[TOC]

> The periodical unfreeze contract helps users lock up a certain amount of money and defrost it to the beneficiary according to the specified regulations.
> It is applicable to the situation of employee incentive in the form of installment payment.

**Contracts provide three types of operations**
  1. Contracts provide three types of operations：specify the amount and amount of assets to be paid at the time of creation, as well as the form of periodical unfreeze.
  1. Beneficiary withdrawal: withdrawal of unfrozen assets by the beneficiary.
  1. Termination of the contract by the initiator: the initiator can terminate the performance of the contract.

**Unfreezing currently supports two forms**
  1. Unfreeze fixed amount: unfreeze fixed assets at specified time intervals.
  1. Unfreeze at a fixed percentage of the remaining amount: unfreeze at a fixed percentage of the remaining amount at a specified time interval. At way, the farther back you go, the less you thaw.

---
> Note: when the contract is created, it can be unfrozen once.
  For example, a fixed amount of unfreeze and contract, the total amount is 100, one month unfreeze 10.
  10 can be withdrawn by the beneficiary at creation and again after the first month.
  If the beneficiary does not withdraw the money in time,he/she can withdraw all the coins that were supposed to be unfrozen at one time after a certain period of time.
  That is, the coins is unfroze in the specified form, and the withdrawal time and frequency of the beneficiary will not affect the process of unfreezing.

## 1.1 Create Transaction

### 1.1.1 Command Line

```
Create periodical unfreeze contract
./chain33-cli send   unfreeze  create fix_amount -a 0.01  -e coins -s bty -b  12qyocayNF7Lv6C9qW4avxs2E7U41fKSfv -p 60 -t 2  -k  private-key

Beneficiary's withdrawal
./chain33-cli send  unfreeze   withdraw  --id mavl-unfreeze-1a8c91077df8e2be644f61b59706be8f7745f9b800868a73624956bd551abe41  -k private-key

Termination of contract by initiator
./chain33-cli send  unfreeze   terminate  --id mavl-unfreeze-1a8c91077df8e2be644f61b59706be8f7745f9b800868a73624956bd551abe41  -k private-key

```

### 1.1.2 RPC Interface

 * Create periodical unfreeze contract

```
{
   "method" : "unfreeze.CreateRawUnfreezeCreate",
   "params" : [
      {
         "assetSymbol" : "bty",
         "assetExec" : "coins",
         "means" : "FixAmount",
         "totalCount" : 400000000,
         "beneficiary" : "",
         "startTime" : 10000,
         "fixAmount" : {
            "period" : 10,
            "amount" : 1000000
         }
      }
   ],
   "jsonrpc" : "2.0"
}
```

**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|method|string|unfreeze.CreateRawUnfreezeCreate|
|assetSymbol, assetExec  |string|information on assets that need to be frozen|
|totalCount|int64|The amount of frozen assets, in units of 1e-8, ten to the minus eighth coins|
|beneficiary|string|beneficiary's address|
|startTime|int64|Start unfreezing time, UTC seconds, default is the time when the transaction is packaged|
|means|string|Specify unfreezing algorithm, valid value FixAmount LeftProportion|
| fixAmount | struct |unfreeze fixed assets at specified intervals.|
| fixAmount.period | int64 |At a specified time interval, in seconds.|
| fixAmount.amount | int64 |Unfreeze the specified amount of assets. Unit 1e-8 coins.|
| leftProportion | struct |unfreeze at a fixed percentage of the remaining amount at a specified time interval. At way, the farther back you go, the less you unfreeze.|
| leftProportion.period | int64 |At a specified time interval, in seconds.|
| leftProportion.tenThousandth | int64 |Fixed scale, unit is one in ten thousand.|

*  Beneficiary's withdrawal

```
 {
   "method" : "unfreeze.CreateRawUnfreezeWithdraw",
   "params" : [
      {
         "unfreezeID" : " "
      }
   ]
}

```

**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|method|string|unfreeze.CreateRawUnfreezeWithdraw|
|unfreezeID  |string|The ID of the frozen contract, which can be queried when creating the frozen contract, is as same as hexadecimal with the ID of the transaction that created the frozen contract.|
 

 *Termination of frozen contract

```
{
   "params" : [
      {
         "unfreezeID" : ""
      }
   ],
   "method" : "unfreeze.CreateRawUnfreezeTerminate"
}

```

**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|method|string|unfreeze.CreateRawUnfreezeWithdraw|
|unfreezeID  |string|The ID of the frozen contract, which can be queried when creating the frozen contract, is as same as hexadecimal with the ID of the transaction that created the frozen contract.|

 * Response data: Create a transaction interface, needs to be sent at signature
 
```
{
   "id" : 1,
   "result" : "0a14757365722e702e646576746573742e746f6b656e123238091a2e0a0844455645434f494e12223134476b70356b55454d6f37665868487544526e524e36764a784e7053644477315420a08d0630a5cab6e0fc96d0cd503a22314c5173504264486f776a3945767337583545654c6770736a464441547759755162",
   "error" : null
}
```

## 1.2 Query Contract Status 

```
{
   "params" : [
      {
         "funcName" : "GetUnfreeze",
         "payload" : {
            "data" : "mavl-unfreeze-1a8c91077df8e2be644f61b59706be8f7745f9b800868a73624956bd551abe41"
         },
         "execer" : "unfreeze"
      }
   ],
   "id" : 0,
   "method" : "Chain33.Query"
}

```

**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|method|string|Chain33.Query|
|execer|string|actuator, fill with unfreeze here|
|FuncName|string|query method, here is GetUnfreezeWithdraw under unfreeze|
|payload.data|string|actual data, the contract ID here, is prefix the transaction hash that creates the contract "mavl-unfreeze-"|

Response data:

```
{
   "id" : 0,
   "result" : {
      "assetSymbol" : "bty",
      "assetExec" : "coins",
      "startTime" : "1543888918",
      "unfreezeID" : "mavl-unfreeze-1a8c91077df8e2be644f61b59706be8f7745f9b800868a73624956bd551abe41",
      "initiator" : "14KEKbYtKKQm4wMthSK9J4La4nAiidGozt",
      "totalCount" : "200000000",
      "remaining" : "0",
      "means" : "FixAmount",
      "fixAmount" : {
         "period" : "60",
         "amount" : "1000000"
      },
      "beneficiary" : "12qyocayNF7Lv6C9qW4avxs2E7U41fKSfv"
   },
   "error" : null
}
```

**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|assetSymbol |string|asset identification|
|assetExec |string|name of the actuator where the asset resides|
|startTime | string |contract effective time, UTC seconds|
|unfreezeID |string|actual data, the contract ID here, is prefix the transaction hash that creates the contract "mavl-unfreeze-"|
|initiator |string|contract creator|
|beneficiary |string|contract beneficiary|
|totalCount | string|total frozen assets|
|remaining | string |total remaining assets in the contract|
|means | string |contract unfreeze algorithm name|
|fixAmount| struct |algorithm corresponding parameters|

## 1.3 Query the Amount of Coins Available Under the Contract

```
{
   "params" : [
      {
         "funcName" : "GetUnfreezeWithdraw",
         "payload" : {
            "data" : "mavl-unfreeze-1a8c91077df8e2be644f61b59706be8f7745f9b800868a73624956bd551abe41"
         },
         "execer" : "unfreeze"
      }
   ],
   "id" : 0,
   "method" : "Chain33.Query"
}

```

**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|method|string|Chain33.Query|
|execer|string|actuator, fill with unfreeze here|
|FuncName|string|query method, here is GetUnfreezeWithdraw under unfreeze|
|payload.data|string|actual data, the contract ID here, is prefix the transaction hash that creates the contract "mavl-unfreeze-"|

Response data:
```
{
   "id" : 0,
   "error" : null,
   "result" : {
      "availableAmount" : "0",
      "unfreezeID" : "mavl-unfreeze-1a8c91077df8e2be644f61b59706be8f7745f9b800868a73624956bd551abe41"
   }
}

```

**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|unfreezeID |string|actual data, the contract ID here, is prefix the transaction hash that creates the contract "mavl-unfreeze-"|
|availableAmount |string|the amount of assets unfrozen but not yet withdrawn from the contract|
