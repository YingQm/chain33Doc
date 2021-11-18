**问题描述：**
在区块中出现了有连续2个执行器类型为ticket的交易，该交易的执行操作都是topen，且其中有一个是执行成功，另一个是执行失败。
参考测试链上高度1057421出现的此问题现象：https://testnet.bityuan.com/blockDetail?height=1057421

**解决方法：**
检查出错交易的输入数据，是否minerAddress和returnAddress配置成了同一个地址，并且通过ticket binder_miner检查该地址是否被设置成了离线挖矿地址，如果是则换一个离线地址，问题可以得到修复。
