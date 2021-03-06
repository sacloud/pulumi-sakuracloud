// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sakuracloud

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Get information about an existing Local Router.
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
// 		_, err := sakuracloud.LookupLocalRouter(ctx, &sakuracloud.LookupLocalRouterArgs{
// 			Filter: sakuracloud.GetLocalRouterFilter{
// 				Names: []string{
// 					"foobar",
// 				},
// 			},
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
func LookupLocalRouter(ctx *pulumi.Context, args *LookupLocalRouterArgs, opts ...pulumi.InvokeOption) (*LookupLocalRouterResult, error) {
	var rv LookupLocalRouterResult
	err := ctx.Invoke("sakuracloud:index/getLocalRouter:getLocalRouter", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getLocalRouter.
type LookupLocalRouterArgs struct {
	// One or more values used for filtering, as defined below.
	Filter *GetLocalRouterFilter `pulumi:"filter"`
}

// A collection of values returned by getLocalRouter.
type LookupLocalRouterResult struct {
	// The description of the LocalRouter.
	Description string                `pulumi:"description"`
	Filter      *GetLocalRouterFilter `pulumi:"filter"`
	// The icon id attached to the LocalRouter.
	IconId string `pulumi:"iconId"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// The name of the LocalRouter.
	Name string `pulumi:"name"`
	// A list of `networkInterface` blocks as defined below.
	NetworkInterfaces []GetLocalRouterNetworkInterface `pulumi:"networkInterfaces"`
	// A list of `peer` blocks as defined below.
	Peers []GetLocalRouterPeer `pulumi:"peers"`
	// A list of secret key used for peering from other LocalRouters.
	SecretKeys []string `pulumi:"secretKeys"`
	// A list of `staticRoute` blocks as defined below.
	StaticRoutes []GetLocalRouterStaticRoute `pulumi:"staticRoutes"`
	// A list of `switch` blocks as defined below.
	Switches []GetLocalRouterSwitch `pulumi:"switches"`
	// Any tags assigned to the LocalRouter.
	Tags []string `pulumi:"tags"`
}
