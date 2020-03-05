# Super Node Account Group Management
[TOC]

## 1 Create super node account group

> Super node account group is used to manage the confirmation of super node consensus of parallel chain. Only accounts within the account group can participate in the consensus and get mining rewards

** Three types of operations were provided in the account group creation**
  1. Apply to create a super node account group
  1. Super account approves the application of account group
  1. Abort application of super node account group

**Description**
  1. Applicants for the account group need to deposit a certain quantity of coins in the paracross contract in advance, which will be frozen after the application
  1. The quantity of frozen coins approved by the super account shall be the quantity of admission coins. The quantity of frozen coins of the applicant can not be less than the quantity of the approver. Otherwise, the applicant have to cancel the application and resubmit
  1. Before the application of the account group is approved, the applicant can cancel the application and release the frozen coins


### RPC Interface
 **Description：** The RPC interface can only be used on parallel chains, at the address of parallel chain IP :8901
 * Create transaction for applications to create account group (unsigned)

```
  {
     "method" : "Chain33.CreateTransaction",
     "params" : [
        {
           "execer" : "paracross",
           "actionName" : "NodeGroupConfig",
           "payload" : {
              "op" : "1",
              "addrs" : "1Ka7EPFRqerwerwuswpow7Qs,G6qA4RQbNmbPJCZPjsfspopoowhe3T",
              "coinsFrozen":"500000000"
           }
        }
     ],
     "jsonrpc" : "2.0"
  }
 ```

**Parameter description：**

 |Parameter|Type|Description|
 |----|----|----|
 |method|string|Chain33.CreateTransaction|
 |execer|string|paracross|
 |actionName|string|NodeConfig|
 |op|string|configuration type: join: request to join in|
 |addrs|string|apply for accounts, or multiple accounts|
 |coinsFrozen|string|quantity of frozen coins|

* Approve the applied transaction for creating account group (unsigned)

```
    {
       "method" : "Chain33.CreateTransaction",
       "params" : [
          {
             "execer" : "paracross",
             "actionName" : "NodeGroupConfig",
             "payload" : {
                "op" : "2",
                "id" : "mavl-paracross-title-nodegroupid-user.p.para.-0xf2fsdfsfsdfsdfasadfsdfesiwiwoirwer",
                "coinsFrozen":"500000000"
             }
          }
       ],
       "jsonrpc" : "2.0"
    }
```

**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
   |method|string|Chain33.CreateTransaction|
   |execer|string|paracross|
   |actionName|string|NodeGroupConfig|
   |op|string|configuration type：1：application，2：approval,3:cancel application,4:modification|
   |id|string|must be the same as the id created in application|
   |coinsFrozen|string|the number of coins required for approval|

* Cancel the applied transaction for creating account group (unsigned)

```
   {
      "method" : "Chain33.CreateTransaction",
      "params" : [
         {
            "execer" : "paracross",
            "actionName" : "NodeGroupConfig",
            "payload" : {
               "op" : "3",
               "id" : "mavl-paracross-title-nodegroupid-user.p.para.-0xf2fsdfsfsdfsdfasadfsdfesiwiwoirwer",
            }
         }
      ],
      "jsonrpc" : "2.0"
   }
   ```

**Parameter description：**

  |Parameter|Type|Description|
  |----|----|----|
  |method|string|Chain33.CreateTransaction|
  |execer|string|paracross|
  |actionName|string|NodeGroupConfig|
  |op|string|configuration type：1：application，2：approval,3:cancel application,4:modification|
  |id|string|must be the same as the account created in application|

* Modify the applied transaction for creating account group (unsigned)

```
   {
      "method" : "Chain33.CreateTransaction",
      "params" : [
         {
            "execer" : "paracross",
            "actionName" : "NodeGroupConfig",
            "payload" : {
               "op" : "4",
               "coinFrozen" : "600000000",
            }
         }
      ],
      "jsonrpc" : "2.0"
   }
   ```

**Parameter description：**

  |Parameter|Type|Description|
  |----|----|----|
  |method|string|Chain33.CreateTransaction|
  |execer|string|paracross|
  |actionName|string|NodeGroupConfig|
  |op|string|configuration type：1：application，2：approval,3:cancel application,4:modification|
  |coinFrozen|int64|modified quantity of frozen coins|

* Query the account information of the account group

```
 {
       "method" : "Chain33.GetNodeGroupAddrs",
       "params" : [
          {
             "title" : "user.p.para.",
          }
       ],
       "jsonrpc" : "2.0"
 }
 ```

**Parameter description：**

  |Parameter|Type|Description|
  |----|----|----|
  |method|string|Chain33.GetNodeGroupAddrs|
  |title|string|title name of the parallel chain|

**Response data:**
 ```
 {
        "key": "mavl-paracross-nodes-title-user.p.para.",
        "value": "[1KSBd17H7ZK8iT37aJztFB22XGwsPTdwE4 1JRNjdEqp4LJ5fqycUBm9ayCKSeeskgMKR 1NLHPEcbTWWxxU3dGUZBhayjrCHD3psX7k 1MCftFynyvG2F4ED5mdHYgziDxx6vDrScs]"
 }
   ```

* Query the current status of the account group

```
    {
       "method" : "Chain33.GetNodeGroupStatus",
       "params" : [
          {
             "title" : "user.p.para.",
          }
       ],
       "jsonrpc" : "2.0"
    }
    ```

**Parameter description：**

   |Parameter|Type|Description|
   |----|----|----|
   |method|string|Chain33.GetNodeGroupStatus|
   |title|string|title name of the parallel chain|

**Response data:**

 ```
    {
        "status": 2,
        "title": "user.p.para.",
        "applyAddr": "1E5saiXVb9mW8wcWUUZjsHJPZs5GmdzuSY,1KSBd17H7ZK8iT37aJztFB22XGwsPTdwE4,1JRNjdEqp4LJ5fqycUBm9ayCKSeeskgMKR,1NLHPEcbTWWxxU3dGUZBhayjrCHD3psX7k,1MCftFynyvG2F4ED5mdHYgziDxx6vDrScs",
        "coinsFrozen": 500000000,
        "fromAddr": "1Ka7EPFRqs3v9yreXG6qA4RQbNmbPJCZPj",
		"height": 550,
    }
 ```

* Query the application information by status query account group

```
     {
        "method" : "Chain33.ListNodeGroupStatus",
        "params" : [
           {
              "status" : 1,
           }
        ],
        "jsonrpc" : "2.0"
     }
```

**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
|method|string|Chain33.GetNodeGroupAddrs|
|status|int|0: all, 1: application, 2: approval, 3: withdrawal, 4: modification|

## 2 Super node account group management


**Three types of operations were provided in the account group management**
  1. Apply to join the super node account group
  1. Vote on the applied account, results must be approved by more than two-thirds of all accounts
  1. Apply to quit the super node account group
  1. Withdraw the application before it has been voted through
**Description**
  1. Applicants for the account group need to deposit a certain quantity of coins in the paracross contract in advance, which will be frozen after the application, while the quantity cannot be less than frozen currency applied by account group 
  1. Members of the current super account group vote to add new nodes
  1. Current super account group members apply to quit the account group
  1. Both the application and the withdrawal are proposals for one account, which can be voted on or withdrawn

### RPC Interface
 **Description：** The RPC interface can only be used on parallel chains, at the address of parallel chain IP :8901

* Create transaction for applications to create account group (unsigned)

```
 {
    "method" : "Chain33.CreateTransaction",
    "params" : [
       {
          "execer" : "paracross",
          "actionName" : "NodeConfig",
          "payload" : {
             "op" : "1",
             "addr" : "1E5saiXVb9mW8wwypiZjsHJPZs5GmdzuSY",
             "coinsFrozen":"500000000"
          }
       }
    ],
    "jsonrpc" : "2.0"
 }
```

**Parameter description：**

 |Parameter|Type|Description|
 |----|----|----|
 |method|string|Chain33.CreateTransaction|
 |execer|string|paracross|
 |actionName|string|NodeConfig|
 |op|string|configuration type: 1: apply to join, 2: vote, 3: apply to withdraw, 4: cancel|
 |addrs|string|apply account, only one account is allowed|
 |coinsFrozen|string|quantity of frozen currency|

  * Create transaction for applications to create account group (unsigned)

```
  {
     "method" : "Chain33.CreateTransaction",
     "params" : [
        {
           "execer" : "paracross",
           "actionName" : "NodeConfig",
           "payload" : {
              "op" : "2",
              "id" : "mavl-paracross-title-nodeid-user.p.para.-0xf2fsdfsfsdfsdfasadfsdfesiwiwoirwer",
              "value":"1"
           }
        }
     ],
     "jsonrpc" : "2.0"
 }
```

**Parameter description：**

  |Parameter|Type|Description|
  |----|----|----|
  |method|string|Chain33.CreateTransaction|
  |execer|string|paracross|
  |actionName|string|NodeConfig|
  |op|uint32|configuration type：2：vote|
  |id|string|The application ID of the applied account|
  |value|uint32|1：yes,2:no|

  * Generate exit account group transactions (unsigned)

```
  {
     "method" : "Chain33.CreateTransaction",
     "params" : [
        {
           "execer" : "paracross",
           "actionName" : "NodeConfig",
           "payload" : {
              "op" : "3",
              "addr" : "1E5saiXVb9mW8wwypiZjsHJPZs5GmdzuSY",
           }
        }
     ],
     "jsonrpc" : "2.0"
  }
 ```

**Parameter description：**

  |Parameter|Type|Description|
  |----|----|----|
  |method|string|Chain33.CreateTransaction|
  |execer|string|paracross|
  |actionName|string|NodeConfig|
  |op|uint32|configuration type：3：exit account group|
  |addrs|string|apply account for withdrawal, only one account is allowed|

* Query account application information by status

```
     {
        "method" : "Chain33.ListNodeStatus",
        "params" : [
           {
              "title" : "user.p.para.",
              "status" : 4,
           }
        ],
        "jsonrpc" : "2.0"
     }
 ```

**Parameter description：**

|Parameter|Type|Description|
|----|----|----|
    |method|string|Chain33.ListNodeStatus|
    |title|string|title name of the parallel chain|
    |status|int|0: all, 1: apply to join, 2: apply to withdraw, 3: apply to close, 4: apply to cancel|

*Response data：*
```
    {
        "status": 4,
        "title": "user.p.para.",
        "targetAddr": "1E5saiXVb9mW8wcWUUZjsHJPZs5GmdzuSY",
        "coinsFrozen": 500000000,
        "votes": {
            "addrs": [
                "1KSBd17H7ZK8iT37aJztFB22XGwsPTdwE4",
                "1JRNjdEqp4LJ5fqycUBm9ayCKSeeskgMKR",
                "1E5saiXVb9mW8wcWUUZjsHJPZs5GmdzuSY",
                "1NLHPEcbTWWxxU3dGUZBhayjrCHD3psX7k"
            ],
            "votes": [
                "yes",
                "yes",
                "yes",
                "yes"
            ]
        },
        "fromAddr": "1Ka7EPFRqs3v9yreXG6qA4RQbNmbPJCZPj"
    }
    ```


* Query application information by account
* Description：status：10：joined,  11： quited
```
     {
        "method" : "Chain33.GetNodeAddrStatus",
        "params" : [
           {
              "title" : "user.p.para.",
              "addr" : “1E5saiXVb9mW8wcWUUZjsHJPZs5GmdzuSY”,
           }
        ],
        "jsonrpc" : "2.0"
     }
```

**Parameter description：**

   |Parameter|Type|Description|
   |----|----|----|
   |method|string|Chain33.GetNodeAddrStatus|
   |title|string|title name of the parallel chain|
   |addr|string|application account information|

**Response data：**
```
     {
         "addr": "1E5saiXVb9mW8wcWUUZjsHJPZs5GmdzuSY",
         "title": "user.p.para.",
         "proposalId": "mavl-paracross-title-nodeid-user.p.para.-0xf2fsdfsfsdfsdfasadfsdfesiwiwoirwer",
		 "quitId": "mavl-paracross-title-nodeid-user.p.para.-0xf2fsdfsfsdfsdfasadfsdfesiwiwoirwer",
         "status": 11,
     }
```

* Query information by application ID
* Description：status：1: apply to join, 2: apply to withdraw, 3: apply to close, 4: apply to cancel
```
     {
        "method" : "Chain33.GetNodeAddrStatus",
        "params" : [
           {
              "title" : "user.p.para.",
              "id" : “mavl-paracross-title-nodeid-user.p.para.-0xf2fsdfsfsdfsdfasadfsdfesiwiwoirwer”,
           }
        ],
        "jsonrpc" : "2.0"
     }
```

**Parameter description：**

   |Parameter|Type|Description|
   |----|----|----|
   |method|string|Chain33.GetNodeAddrStatus|
   |title|string|title name of the parallel chain|
   |id|string|application ID|

**Response data：**
```
     {
         "status": 4,
         "title": "user.p.para.",
         "applyAddr": "1E5saiXVb9mW8wcWUUZjsHJPZs5GmdzuSY",
         "coinsFrozen": 500000000,
         "votes": {
             "addrs": [
                 "1KSBd17H7ZK8iT37aJztFB22XGwsPTdwE4",
                 "1JRNjdEqp4LJ5fqycUBm9ayCKSeeskgMKR",
                 "1E5saiXVb9mW8wcWUUZjsHJPZs5GmdzuSY",
                 "1NLHPEcbTWWxxU3dGUZBhayjrCHD3psX7k"
             ],
             "votes": [
                 "yes",
                 "yes",
                 "yes",
                 "yes"
             ]
         },
         "fromAddr": "1Ka7EPFRqs3v9yreXG6qA4RQbNmbPJCZPj", 
		 "height": 100
     }
```
