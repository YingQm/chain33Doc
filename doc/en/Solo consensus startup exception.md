Chain33 configuration files are modular configurations, there is no solo consensus parameter configured by default, so the error will be reported when starting directly, the following solo related configuration parameters need to be added in the configuration file:

```ini
[consensus.sub.solo]
genesisBlockTime=1514533394
genesis="1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs"
```