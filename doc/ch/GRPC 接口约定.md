## GRPC 接口约定
[TOC]
### 1 使用步骤
> grpc 简介: gRPC是一款语言中立、平台中立、开源的远程过程调用系统，即：gRPC 客户端和服务端可以在多种环境中运行交互，例如用java 写一个服务端，可以用go语言写客户端调用gRPC默认使用protocol buffers。

1. 导入 grpc 的 Proto 包文件，例如: `import "github.com/33cn/chain33/types"`
2. 创建 grpc 连接`conn, err := grpc.Dial(target string, opts ...DialOption)`
3. 调用 pb.go 函数，对 conn 进行封装，NewChain33Client(conn)

### 2 例子
#### 2.1 调用接口
```
 CreateRawTransaction(ctx context.Context, in *pb.CreateTx) (*pb.UnsignTx, error)
```
**参数：**
1. ctx context.Context 类型，默认可以用context.Background(),  其他用法可以参考context 包内容
2. CreateTx 结构体参数展示
```
type CreateTx struct {
	To          string `protobuf:"bytes,1,opt,name=to,proto3" json:"to,omitempty"`
	Amount      int64  `protobuf:"varint,2,opt,name=amount,proto3" json:"amount,omitempty"`
	Fee         int64  `protobuf:"varint,3,opt,name=fee,proto3" json:"fee,omitempty"`
	Note        []byte `protobuf:"bytes,4,opt,name=note,proto3" json:"note,omitempty"`
	IsWithdraw  bool   `protobuf:"varint,5,opt,name=isWithdraw,proto3" json:"isWithdraw,omitempty"`
	IsToken     bool   `protobuf:"varint,6,opt,name=isToken,proto3" json:"isToken,omitempty"`
	TokenSymbol string `protobuf:"bytes,7,opt,name=tokenSymbol,proto3" json:"tokenSymbol,omitempty"`
	ExecName    string `protobuf:"bytes,8,opt,name=execName,proto3" json:"execName,omitempty"`
	Execer      string `protobuf:"bytes,9,opt,name=execer,proto3" json:"execer,omitempty"`
}
```
**参数说明：**

|参数|类型|是否必填|说明|
|----|----|----|----|
|To|string|是|发送到地址；如果是合约的充提则为合约地址，合约地址为execName转换而来，详情查看ConvertExectoAddr接口|
|Amount|int64|是|发送金额，注意基础货币单位为10^8|
|Fee|int64|是|手续费，注意基础货币单位为10^8,默认10^5,即Fee=1e5|
|Note|[]byte|否|备注,此处是字节数组, []byte("it's my tx note")|
|IsToken|bool|否|是否是token类型的转账 （非token转账这个不用填 包括平行链的基础代币转账也不用填）|
|IsWithdraw|bool|是|是否为从合约中提款的交易，普通转账为false|
|TokenSymbol|string|否|token 的 symbol （非token转账这个不用填）|
|ExecName|string|否|目标合约名，如果要构造平行链上的转账或普通转账，此参数置空|
|Execer|string|是|资产的执行器名称，如果是普通转账，此处应填coins，如果是构造平行链的基础代币，此处要填写user.p.xxx.coins token同上|

**返回数据：**
```
type UnsignTx struct {
	Data []byte `protobuf:"bytes,1,opt,name=data,proto3" json:"data,omitempty"`
}
```
**参数说明：**

|参数|类型|说明|
|----|----|----|
|Data|[]byte|待签名的已经构造完毕的交易|

#### 2.2 代码示例
假定 grpc服务地址：localhost:8802
```
package main

import (
	"context"
	"github.com/33cn/chain33/common"
	chan33Ty "github.com/33cn/chain33/types"
	"google.golang.org/grpc"
)

func main() {
	conn, err := grpc.Dial("localhost:8802", grpc.WithInsecure(), grpc.WithBlock(), grpc.FailOnNonTempDialError(true))
	if err != nil {
		panic(err)
	}
	defer conn.Close()
	gclient := chan33Ty.NewChain33Client(conn)
	txData, err := gclient.CreateRawTransaction(context.Background(), &chan33Ty.CreateTx{Amount: 10000000, To: "16htvcBNSEA7fZhAdLJphDwQRQJaHpyHTp", Execer: "coins", ...})
	if err != nil {
		//异常处理逻辑
		panic(err)
	}
	txData...
}
```
