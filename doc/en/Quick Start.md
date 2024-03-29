## 1 Quick Start
[TOC]
## 1.1 Download Chain33 Program
```bash
	# Linux version download address
	wget https://github.com/33cn/plugin/releases/download/v6.1.0/Chain33_6.1.0_linux.tar.gz
    tar -zxvf Chain33_6.1.0_linux.tar.gz
	
	# Windows version download address
	https://github.com/33cn/plugin/releases/download/v6.1.0/Chain33_6.1.0_Windows.zip
```

## 1.2 Start Chain33 Main Program 
> Use the following command to start the main program Chain33, Chain33.toml is the system configuration file.which in the sample is configured in the common way for the local single node solo. The sample is configured with the local single node solo consensus mode.
```bash
    nohup ./Chain33 -f Chain33.toml >>log.out 2>&1 &
```
## 1.3 Create Wallets and Accounts
>   In the Chain33 directory, follow these steps to initialize the account, which consist of the following:
- Create the wallet and save the wallet password as "test"
- Import the creation address private key in the wallet
- Create an account address under the wallet labeled "test"

```bash
# Generate random number seed, it is suggested that you can manually generate and save it, and then you can use this seed to restore the wallet
./Chain33-cli seed generate -l 0

# Save the seed and set the wallet password to tech, note: the password can be customized and should be kept in mind that it will be used later to unlock the wallet.
./Chain33-cli seed save -p tech -s "seed generated in the previous step"

# Use the password we just set to unlock the wallet (the wallet will be locked by default when newly created)
./Chain33-cli wallet unlock -p tech

# Import the private key of creation address of solo consensus that we configured (there is some money in this address, which will be used in later transfer operations).
Import the private key of creation address of solo consensus that we configured (there is some money in this address, which will be used in later transfer operations).
./Chain33-cli account import_key -k 3990969DF92A5914F7B71EEB9A4E58D6E255F32BF042FEA5318FC8B3D50EE6E8 -l genesis

# Create a new account labeled "test"
./Chain33-cli account create -l test

# Check the current wallet account list (if nothing goes wrong, genesis should have a lot of money under it)
./Chain33-cli account list
```

> The last command should execute as follows:
> Node award is the air-drop address automatically generated by the system, and test is the address we just created. The two addresses generated locally by the developers will definitely be different from those in the example.Genesis will have a default balance of 100 million;

```bash
test@localhost:~/Chain33 $ ./Chain33-cli account list
{
    "wallets": [
        {
            "acc": {
                "balance": "0.0000",
                "frozen": "0.0000",
                "addr": "1Mb1rzJpj48oeEp8Fk9PESsExuUxK2wfxw"
            },
            "label": "node award"
        },
        {
            "acc": {
                "balance": "0.0000",
                "frozen": "0.0000",
                "addr": "1Kkq2neiAWSGkk3djkJ9SPoG2tdGzfwDpa"
            },
            "label": "test"
        },
        {
            "acc": {
                "balance": "100000000.0000",
                "frozen": "0.0000",
                "addr": "1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs"
            },
            "label": "genesis"
        }
    ]
}
```

## 1.4 Use the Chain33 Command Line
**Chain33-cli is the command-line interface for Chain33, which provides packaging for almost all the external capabilities of the Chain33 program. Here is a simple demonstration of the most basic transfer transactions and trading results of the query operation**
 
### 1.4.1 Check Wallet Status
>   Use the following command to query the current status of the wallet
>   IsWalletLock represents the current lock state of the wallet. When the wallet is unlocked, no operation can be performed and you need to use ./Chain33-cli unlock -p test to unlock the wallet

```bash
    test@localhost:~/Chain33$ ./Chain33-cli wallet status
    {
        "isWalletLock": false,
        "isAutoMining": true,
        "isHasSeed": true,
        "isTicketLock": true
    }
 ```
 
### 1.4.2 Send Transfer Transaction
>Construct a transfer transaction. Here's an example of 1000 BTY transfers from genesis to test:

```bash
test@localhost:~/Chain33 $ ./Chain33-cli send bty transfer -a 1000 -t 1Kkq2neiAWSGkk3djkJ9SPoG2tdGzfwDpa -n "test for transfer bty" -k 1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs
0x5b49636ec48c597363e692b0090dd7c5190129400d3777e3ee4093bb565a621b
```
This command returns a hexadecimal string that is the hash of the transaction which can be used to query the execution result of the transaction

### 1.4.3 Query Transaction Result
> Use the following command to query the result of the trade by the trade hash output above ,

```bash
test@localhost:~/Chain33 $ ./Chain33-cli tx query -s 0x5b49636ec48c597363e692b0090dd7c5190129400d3777e3ee4093bb565a621b
```

The output of this example is as follows (simplified for easy viewing) :
```json
{
    "tx": {
        "execer": "coins",
        "payload": {
            "transfer": {
                "cointoken": "",
                "amount": "100000000000",
                "note": "test for transfer bty",
                "to": "1Kkq2neiAWSGkk3djkJ9SPoG2tdGzfwDpa"
            },
            "ty": 1
        },
        ......
        "fee": "0.0010",
        ......
        "to": "1Kkq2neiAWSGkk3djkJ9SPoG2tdGzfwDpa",
        "from": "1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs"
    },
    "receipt": {
        "ty": 2,
        "tyName": "ExecOk",
        "logs": [
           ......
        ]
    },
    "height": 1,
    "index": 0,
    "blocktime": 1542596665,
    "amount": "1000.0000",
    "fromaddr": "1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs",
    "actionname": "transfer"
}
```
From the output above you can see exactly what we did and what the results were, and a lot of other information that we'll come back to later.

Use the following command to see if the balance of the test account has changed:
```bash
test@localhost:~/Chain33 $ ./Chain33-cli account balance -a 1Kkq2neiAWSGkk3djkJ9SPoG2tdGzfwDpa
```
The output results are as follows:
```json
{
    "addr": "1Kkq2neiAWSGkk3djkJ9SPoG2tdGzfwDpa",
    "execAccount": [
        {
            "execer": "coins",
            "account": {
                "balance": "1000.0000",
                "frozen": "0.0000"
            }
        }
    ]
}
```
As you can see, the balance of the test account went from 0 to 1000; you can also try to see if your genesis account is 1000 less.

Now that the basic Chain33 environment is set up and you have experienced the transfer operation on the blockchain, the next step is to learn more about Chain33.
