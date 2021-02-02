# Go Language DApp Development
[TOC]

## 1 Overall Introduction
We can learn from the  [Introduction](161)  chapter, a DApp consists of three parts: the actuator, the command line, and the RPC interface. This article demonstrates the specific details of the development of these three parts of DApp with an example.

The development of actuator please refer to [Secondary Development](182#4%20Secondary%20Development), which has introduced the detailed development of the executor part of a DApp.

The following contents of this article, on the basis of the development of the executor, add the contents of the command line and RPC interface.

The project directory structure is as follows:

![project directory](https://public.zhaobi.tech/web/storage/upload/20181115/f6f948a6985cd4e828e0c049a58f225b.png "project directory")

In addition to the original executor, the commands and RPC packages have been added, respectively corresponding to specific implementation code.

## 2 RPC Interface Development
About the detailed introduction of RPC module, please refer to [HERE](184),this section introduces secondary development related to this example.

Suppose, in the case of echo, we want to add an RPC interface for the query, support the query of Ping message, pass in a certain message value, and return the number of pings called by this message.

### 2.1 RPC Initialization for DApp
First, the RPC interface of this DApp needs to be initialized:

```go
package rpc

import (
	"context"
	echotypes "github.com/dev/echo/types"
	rpctypes "gitlab.33.cn/chain33/chain33/rpc/types"
	"gitlab.33.cn/chain33/chain33/types"
)

// Overall definition of the RPC interface for external service provision
type Jrpc struct {
	cli *channelClient
}

// Local implementation of the RPC interface
type channelClient struct {
	rpctypes.ChannelClient
}

func Init(name string, s rpctypes.RPCServer) {
	cli := &channelClient{}
	// For simplicity, only Jrpc is registered here, and if GRPC is provided, so is it
	cli.Init(name, s, &Jrpc{cli: cli}, nil)
}
```

The sample code above shows that initialization consists of three parts:
- **RPC external interface definition:：**
    
    Same as the Jrpc structure definition above, the public method defined on this structure, is the open RPC service interface of this DApp

- **RPC interface local implementation：**

    Same as the channelClient structure definition above, It is an auxiliary RPC interface logic implementation, which does not have to exist. If other service interfaces need to be called to the system, it is better to realize through this structure. Because the rpctypes.ChannelClient can communicate directly with other services.

- **RPC interface initialization：**

    Same as the Init method above, register the RPC service interface opened by this DApp with Chain33 system. The first parameter is the executor name of this DApp. The second parameter is the RPC service reference of the system. This initialization method is used by DApp framework for initialization.

### 2.2 Service Interface Development
We need to provide an external Ping query interface, assuming QueryPing, which need to define the Query structure on the Jrpc structure. The input parameters are the same as the Query structure we defined in the executor type. The implementation code is as follows:

```go
// The general Query interface can be used for the Query operation of this contract. The RPC Query interface is encapsulated here just for the purpose of illustrating the implementation
// Receive the client request, invoke the local concrete implementation logic, and return the result
func (c *Jrpc) QueryPing(param *echotypes.Query, result *interface{}) error {
	if param == nil {
		return types.ErrInvalidParam
	}

    // Pass the concrete interface implementation to the local logic
	reply, err := c.cli.QueryPing(context.Background(), param)
	if err != nil {
		return err
	}
	*result = reply
	return nil
}
```
As can be seen from the above code logic, the implementation logic of this method is simple three-step packaging: input check -> call implementation -> result packaging, which is general.

### 2.3 Local Service Interface Logic Implementation

The main logic of RPC service interface is implemented in this part. The code of this example is as follows:
```go
// Local concrete logic implementation 
func (c *channelClient) QueryPing(ctx context.Context, queryParam *echotypes.Query) (types.Message, error) {
	return c.Query(echotypes.EchoX, "GetPing", queryParam)
}
```
As you can see, since we have implemented the generic Query method in the executor development, we can directly call the general Query method of the system through ChannelClient to return the result. In the real world, developers can combine their own reality, add processing logic, or even combine other service interfaces to assemble concrete implementation logic.

At this point, we have added a QueryPing RPC interface to the DApp.

## 3 Command Line Interface Development
For the detailed introduction to command line modules, please refer to [HERE](178), this chapter only introduces the secondary development related to this example.

In general, a command-line interface is just a bunch of call logic that encapsulates an RPC interface, which is essentially a call to an RPC interface, but with some local wrapping that makes it easier to use.

In this case, we wrap the RPC interface QueryPing provided in the previous chapter by the command line.

### 3.1 DApp Command Line Initialization

Generally speaking, a DApp only needs to provide one command line entry, which can contain many sub-commands. The initialization entrance is as follows:

```go
// Main entrance of Command line initialization for this actuator
func EchoCmd() *cobra.Command {
	cmd := &cobra.Command{
		Use:   "echo",
		Short: "echo commandline interface",
		Args:  cobra.MinimumNArgs(1),
	}
	cmd.AddCommand(
        QueryCmd(),  // Query message record
        // If there are other commands, add them here
	)
	return cmd
}
```

As you can see, we've defined an initialization method called EchoCmd which has two parts:

- **Description of this command group:**

    Describes the command name, brief description, and parameter requirements;

- **Sub-Commands contained:**

    Add supporting sub-commands, without amount limit. Each command is encapsulated by one method; this example contains only one query command.

### 3.2 Sub-Command Implementation

Let's move on to how the query command is implemented, starting with the wrapper around the QueryCmd command method as follows:

```go
func QueryCmd() *cobra.Command {
	cmd := &cobra.Command{
		Use:   "query",
		Short: "query message history",
		Run:   queryMesage,
	}
	addPingPangFlags(cmd)
	return cmd
}
```
here are two key pieces of information, addPingPangFlags and the Run parameter queryMesage, as shown below:

#### 3.2.1 addPingPangFlags
The function of this method is to register the supported parameters and the detailed information of the parameters with the command object. You can refer to the implementation code of this example:

```go
func addPingPangFlags(cmd *cobra.Command) {
    // The type parameter, which specifies the message type of the query, is type uint32, and the default value is 1, which is specified by the -t parameter
	cmd.Flags().Uint32P("type", "t", 1, "message type, 1:ping  2:pang")
	cmd.MarkFlagRequired("type")

    // Message parameter, execute message content, string type, default value is null, specified by -m parameter
	cmd.Flags().StringP("message", "m", "", "message content")
    cmd.MarkFlagRequired("message")
    
    // The above two parameters are required
}
```
This query command supports two parameters, specific instructions can be seen in the code comments, this logic is relatively simple.

### 3.2.2 Run Parameter queryMesage
This is the core execution logic of the command, which needs to obtain the parameters passed by the user through the command line, then assemble the parameters, send RPC request, and encapsulate the returned results:

```go
func queryMesage(cmd *cobra.Command, args []string) {
	// This is the default command line parameter that specifies which service address to call
	rpcLaddr, _ := cmd.Flags().GetString("rpc_laddr")
	echoType, _ := cmd.Flags().GetUint32("type")
	msg, _ := cmd.Flags().GetString("message")

	// Create the RPC client and call the QueryPing service interface we implemented
	client, err := jsonclient.NewJSONClient(rpcLaddr)
	if err != nil {
		fmt.Fprintln(os.Stderr, err)
		return
	}

	// Initialize the query parameter structure
	var action = &echotypes.Query{Msg: msg}
	if echoType != 1 {
		fmt.Fprintln(os.Stderr, "not support")
		return
	}

	var result echotypes.QueryResult
	err = client.Call("echo.QueryPing", action, &result)
	if err != nil {
		fmt.Fprintln(os.Stderr, err)
		return
	}

	proto.MarshalText(os.Stdout, &result)
}
```

In fact, the logic of initializing the query parameter structure is not complicated. Before line 13 is fixed processing logic, get parameters and verify, then create RPC client;

After that, RPC request parameters are constructed according to the incoming parameters. This requires different request structures to be defined according to the RPC interface signature, and then call RPC client to send the request. Finally, the structure is packaged for output. Two things to note:

- **Data structure**

    The structure of the request parameters and the return will vary according to the RPC interface called. Be careful to use the correct structure definition, otherwise parsing will fail.

- **Service name:**

    That is, the first parameter of client.call method to locate which service interface to call. It must be filled in correctly. In the case of a generic interface provided by Chain33, format chain33.xxx; in the case of an interface provided by DApp itself, format: executor name.xxx


## 4 Initialize DApp
> plugin.go
> 
> Register this DApp plug-in with the system. The implementation logic is as follows:
> 
> The second development section of the executor has been introduced, but the content is not complete, so here adding the command line and RPC part;

```go
package echo

import (
	"gitlab.33.cn/chain33/chain33/pluginmgr"
	echotypes "github.com/dev/echo/types"
	"github.com/dev/echo/executor"
)

func init() {
	pluginmgr.Register(&pluginmgr.PluginBase{
		Name:     "echo",
		ExecName: echotypes.EchoX,
		Exec:     executor.Init,
		Cmd:      commands.EchoCmd,
		RPC:      rpc.Init,
	})
}

```

## 5 Implementation Effect

### 5.1 Call the RPC Interface Directly
```bash
curl --data-binary '{"jsonrpc":"2.0", "id": 1, "method":"echo.QueryPing","params":[{"msg": "hello"}] }' \
>     -H 'content-type:text/plain;' \
>     http://localhost:8901
```

```json
{"id":1,"result":{"msg":"hello","count":2},"error":null}
```

### 5.2 Called From Command Line
```bash
test@localhost:~/chain33 $ ./chain33-cli echo
echo commandline interface

Usage:
  chain33-cli echo [command]

Available Commands:
  query       query message history

Flags:
  -h, --help   help for echo

Global Flags:
      --paraName string    parachain
      --rpc_laddr string   http url (default "http://localhost:8801")

Use "chain33-cli echo [command] --help" for more information about a command.

test@localhost:~/chain33 $ ./chain33-cli echo query -m hello -t 1
msg: "hello"
count: 2
```