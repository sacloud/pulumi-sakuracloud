// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sakuracloud

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
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
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := sakuracloud.LookupLocalRouter(ctx, &GetLocalRouterArgs{
// 			Filter: GetLocalRouterFilter{
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

func LookupLocalRouterOutput(ctx *pulumi.Context, args LookupLocalRouterOutputArgs, opts ...pulumi.InvokeOption) LookupLocalRouterResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupLocalRouterResult, error) {
			args := v.(LookupLocalRouterArgs)
			r, err := LookupLocalRouter(ctx, &args, opts...)
			return *r, err
		}).(LookupLocalRouterResultOutput)
}

// A collection of arguments for invoking getLocalRouter.
type LookupLocalRouterOutputArgs struct {
	// One or more values used for filtering, as defined below.
	Filter GetLocalRouterFilterPtrInput `pulumi:"filter"`
}

func (LookupLocalRouterOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupLocalRouterArgs)(nil)).Elem()
}

// A collection of values returned by getLocalRouter.
type LookupLocalRouterResultOutput struct{ *pulumi.OutputState }

func (LookupLocalRouterResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupLocalRouterResult)(nil)).Elem()
}

func (o LookupLocalRouterResultOutput) ToLookupLocalRouterResultOutput() LookupLocalRouterResultOutput {
	return o
}

func (o LookupLocalRouterResultOutput) ToLookupLocalRouterResultOutputWithContext(ctx context.Context) LookupLocalRouterResultOutput {
	return o
}

// The description of the LocalRouter.
func (o LookupLocalRouterResultOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v LookupLocalRouterResult) string { return v.Description }).(pulumi.StringOutput)
}

func (o LookupLocalRouterResultOutput) Filter() GetLocalRouterFilterPtrOutput {
	return o.ApplyT(func(v LookupLocalRouterResult) *GetLocalRouterFilter { return v.Filter }).(GetLocalRouterFilterPtrOutput)
}

// The icon id attached to the LocalRouter.
func (o LookupLocalRouterResultOutput) IconId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupLocalRouterResult) string { return v.IconId }).(pulumi.StringOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o LookupLocalRouterResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupLocalRouterResult) string { return v.Id }).(pulumi.StringOutput)
}

// The name of the LocalRouter.
func (o LookupLocalRouterResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupLocalRouterResult) string { return v.Name }).(pulumi.StringOutput)
}

// A list of `networkInterface` blocks as defined below.
func (o LookupLocalRouterResultOutput) NetworkInterfaces() GetLocalRouterNetworkInterfaceArrayOutput {
	return o.ApplyT(func(v LookupLocalRouterResult) []GetLocalRouterNetworkInterface { return v.NetworkInterfaces }).(GetLocalRouterNetworkInterfaceArrayOutput)
}

// A list of `peer` blocks as defined below.
func (o LookupLocalRouterResultOutput) Peers() GetLocalRouterPeerArrayOutput {
	return o.ApplyT(func(v LookupLocalRouterResult) []GetLocalRouterPeer { return v.Peers }).(GetLocalRouterPeerArrayOutput)
}

// A list of secret key used for peering from other LocalRouters.
func (o LookupLocalRouterResultOutput) SecretKeys() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupLocalRouterResult) []string { return v.SecretKeys }).(pulumi.StringArrayOutput)
}

// A list of `staticRoute` blocks as defined below.
func (o LookupLocalRouterResultOutput) StaticRoutes() GetLocalRouterStaticRouteArrayOutput {
	return o.ApplyT(func(v LookupLocalRouterResult) []GetLocalRouterStaticRoute { return v.StaticRoutes }).(GetLocalRouterStaticRouteArrayOutput)
}

// A list of `switch` blocks as defined below.
func (o LookupLocalRouterResultOutput) Switches() GetLocalRouterSwitchArrayOutput {
	return o.ApplyT(func(v LookupLocalRouterResult) []GetLocalRouterSwitch { return v.Switches }).(GetLocalRouterSwitchArrayOutput)
}

// Any tags assigned to the LocalRouter.
func (o LookupLocalRouterResultOutput) Tags() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupLocalRouterResult) []string { return v.Tags }).(pulumi.StringArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupLocalRouterResultOutput{})
}
