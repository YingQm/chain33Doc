# Parallel Chain Environment Construction

[TOC]

## Official Version（Only Linux-like environments are supported）
### 1 Fetch Files
```bash 
wget https://bty.oss-ap-southeast-1.aliyuncs.com/chain33/paraChain.tar.gz
```

### 2 Uncompress
```bash
tar zxvf paraChain.tar.gz
```

### 3 Configuration File Modification

Value ParaRemoteGrpcClient as："101.37.227.226:8802,39.97.20.242:8802,47.107.15.126:8802,jiedian2.33.cn"


The modifications are shown below：
![paraRemoteGrpcClient](https://public.33.cn/web/storage/upload/20190718/4b0828fecc5b4604c1cab783468269e6.png "paraRemoteGrpcClient")


Start Chain33 process
```bash
cd paraChain && ./chain33 -f chain33.para.toml
```

Since the official bin file only supports linux-like environments, so [native compiled](#native compiled) binary file is needed in the Windows environment.

## Native Compilation
### 1 Switch Path

```bash
cd ${GoPath}/src/github.com/33cn
```

>GoPath is the environment variable after the Go compiler is installed. If Go is not installed, refer to [Go environmental installation](https://chain.33.cn/document/81#1.1%20Go%20%E7%8E%AF%E5%A2%83%E5%AE%89%E8%A3%85)

>If any subdirectories other than GoPath do not exist, please create them manually.

### 2 Get the Latest Chain33 Code Branch to Compile
```bash
git clone git@github.com:33cn/plugin.git
```
#### 2.1 Compiling in Linux
```bash
cd plugin && make
```
#### 2.2 Compiling in Windows
Use the following instructions in Command Prompt:

```bash
cd plugin && build.bat
```

Use the following instructions in Powershell：

```bash
(cd .\plugin) -or (.\build.bat)
```

