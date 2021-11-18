Chain33的配置文件为模块化配置，默认没有配置solo共识的参数，所以直接启动会报错，需要在配置文件中增加如下solo相关的配置参数：

```ini
[consensus.sub.solo]
genesisBlockTime=1514533394
genesis="1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs"
```