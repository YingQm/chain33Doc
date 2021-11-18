**Problem description:**
 Two consecutive transactions with actuators of type ticket appeared in block,the execution are both topen，And one of them is a successful execution and the other is a failed execution.
Refer to the problem with height 1057421 on the test chain: https://testnet.bityuan.com/blockDetail?height=1057421

**Solution:**
Check the input data of the error transaction, whether minerAddress and returnAddress connfigured to the same address, and use ticket binder_miner to check if the address is set to an offline mining address.If so, change to another offline address and the problem can be fixed.