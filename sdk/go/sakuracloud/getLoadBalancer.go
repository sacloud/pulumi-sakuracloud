// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sakuracloud

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Get information about an existing Load Balancer.
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
// 		_, err := sakuracloud.LookupLoadBalancer(ctx, &GetLoadBalancerArgs{
// 			Filter: GetLoadBalancerFilter{
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
func LookupLoadBalancer(ctx *pulumi.Context, args *LookupLoadBalancerArgs, opts ...pulumi.InvokeOption) (*LookupLoadBalancerResult, error) {
	var rv LookupLoadBalancerResult
	err := ctx.Invoke("sakuracloud:index/getLoadBalancer:getLoadBalancer", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getLoadBalancer.
type LookupLoadBalancerArgs struct {
	// One or more values used for filtering, as defined below.
	Filter *GetLoadBalancerFilter `pulumi:"filter"`
	// The name of zone that the LoadBalancer is in (e.g. `is1a`, `tk1a`).
	Zone *string `pulumi:"zone"`
}

// A collection of values returned by getLoadBalancer.
type LookupLoadBalancerResult struct {
	// The description of the VIP.
	Description string                 `pulumi:"description"`
	Filter      *GetLoadBalancerFilter `pulumi:"filter"`
	// The icon id attached to the LoadBalancer.
	IconId string `pulumi:"iconId"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// The name of the LoadBalancer.
	Name string `pulumi:"name"`
	// A list of `networkInterface` blocks as defined below.
	NetworkInterfaces []GetLoadBalancerNetworkInterface `pulumi:"networkInterfaces"`
	// The plan name of the LoadBalancer. This will be one of [`standard`/`highspec`].
	Plan string `pulumi:"plan"`
	// Any tags assigned to the LoadBalancer.
	Tags []string `pulumi:"tags"`
	// The virtual IP address.
	Vips []GetLoadBalancerVip `pulumi:"vips"`
	Zone string               `pulumi:"zone"`
}

func LookupLoadBalancerOutput(ctx *pulumi.Context, args LookupLoadBalancerOutputArgs, opts ...pulumi.InvokeOption) LookupLoadBalancerResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupLoadBalancerResult, error) {
			args := v.(LookupLoadBalancerArgs)
			r, err := LookupLoadBalancer(ctx, &args, opts...)
			return *r, err
		}).(LookupLoadBalancerResultOutput)
}

// A collection of arguments for invoking getLoadBalancer.
type LookupLoadBalancerOutputArgs struct {
	// One or more values used for filtering, as defined below.
	Filter GetLoadBalancerFilterPtrInput `pulumi:"filter"`
	// The name of zone that the LoadBalancer is in (e.g. `is1a`, `tk1a`).
	Zone pulumi.StringPtrInput `pulumi:"zone"`
}

func (LookupLoadBalancerOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupLoadBalancerArgs)(nil)).Elem()
}

// A collection of values returned by getLoadBalancer.
type LookupLoadBalancerResultOutput struct{ *pulumi.OutputState }

func (LookupLoadBalancerResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupLoadBalancerResult)(nil)).Elem()
}

func (o LookupLoadBalancerResultOutput) ToLookupLoadBalancerResultOutput() LookupLoadBalancerResultOutput {
	return o
}

func (o LookupLoadBalancerResultOutput) ToLookupLoadBalancerResultOutputWithContext(ctx context.Context) LookupLoadBalancerResultOutput {
	return o
}

// The description of the VIP.
func (o LookupLoadBalancerResultOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v LookupLoadBalancerResult) string { return v.Description }).(pulumi.StringOutput)
}

func (o LookupLoadBalancerResultOutput) Filter() GetLoadBalancerFilterPtrOutput {
	return o.ApplyT(func(v LookupLoadBalancerResult) *GetLoadBalancerFilter { return v.Filter }).(GetLoadBalancerFilterPtrOutput)
}

// The icon id attached to the LoadBalancer.
func (o LookupLoadBalancerResultOutput) IconId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupLoadBalancerResult) string { return v.IconId }).(pulumi.StringOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o LookupLoadBalancerResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupLoadBalancerResult) string { return v.Id }).(pulumi.StringOutput)
}

// The name of the LoadBalancer.
func (o LookupLoadBalancerResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupLoadBalancerResult) string { return v.Name }).(pulumi.StringOutput)
}

// A list of `networkInterface` blocks as defined below.
func (o LookupLoadBalancerResultOutput) NetworkInterfaces() GetLoadBalancerNetworkInterfaceArrayOutput {
	return o.ApplyT(func(v LookupLoadBalancerResult) []GetLoadBalancerNetworkInterface { return v.NetworkInterfaces }).(GetLoadBalancerNetworkInterfaceArrayOutput)
}

// The plan name of the LoadBalancer. This will be one of [`standard`/`highspec`].
func (o LookupLoadBalancerResultOutput) Plan() pulumi.StringOutput {
	return o.ApplyT(func(v LookupLoadBalancerResult) string { return v.Plan }).(pulumi.StringOutput)
}

// Any tags assigned to the LoadBalancer.
func (o LookupLoadBalancerResultOutput) Tags() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupLoadBalancerResult) []string { return v.Tags }).(pulumi.StringArrayOutput)
}

// The virtual IP address.
func (o LookupLoadBalancerResultOutput) Vips() GetLoadBalancerVipArrayOutput {
	return o.ApplyT(func(v LookupLoadBalancerResult) []GetLoadBalancerVip { return v.Vips }).(GetLoadBalancerVipArrayOutput)
}

func (o LookupLoadBalancerResultOutput) Zone() pulumi.StringOutput {
	return o.ApplyT(func(v LookupLoadBalancerResult) string { return v.Zone }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupLoadBalancerResultOutput{})
}
