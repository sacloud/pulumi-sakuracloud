// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sakuracloud

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Get information about VNC for connecting to an existing Server.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-sakuracloud/sdk/go/sakuracloud"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := sakuracloud.GetServerVNCInfo(ctx, &sakuracloud.GetServerVNCInfoArgs{
// 			ServerId: sakuracloud_server.Foobar.Id,
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
func GetServerVNCInfo(ctx *pulumi.Context, args *GetServerVNCInfoArgs, opts ...pulumi.InvokeOption) (*GetServerVNCInfoResult, error) {
	var rv GetServerVNCInfoResult
	err := ctx.Invoke("sakuracloud:index/getServerVNCInfo:getServerVNCInfo", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getServerVNCInfo.
type GetServerVNCInfoArgs struct {
	// The id of the Server.
	ServerId string `pulumi:"serverId"`
	// The name of zone that the Server is in (e.g. `is1a`, `tk1a`).
	Zone *string `pulumi:"zone"`
}

// A collection of values returned by getServerVNCInfo.
type GetServerVNCInfoResult struct {
	// The host name for connecting by VNC.
	Host string `pulumi:"host"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// The password for connecting by VNC.
	Password string `pulumi:"password"`
	// The port number for connecting by VNC.
	Port     int    `pulumi:"port"`
	ServerId string `pulumi:"serverId"`
	Zone     string `pulumi:"zone"`
}
