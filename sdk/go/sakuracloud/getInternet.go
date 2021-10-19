// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sakuracloud

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Get information about an existing Switch+Router.
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
// 		_, err := sakuracloud.LookupInternet(ctx, &GetInternetArgs{
// 			Filter: GetInternetFilter{
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
func LookupInternet(ctx *pulumi.Context, args *LookupInternetArgs, opts ...pulumi.InvokeOption) (*LookupInternetResult, error) {
	var rv LookupInternetResult
	err := ctx.Invoke("sakuracloud:index/getInternet:getInternet", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getInternet.
type LookupInternetArgs struct {
	// One or more values used for filtering, as defined below.
	Filter *GetInternetFilter `pulumi:"filter"`
	// The name of zone that the Switch+Router is in (e.g. `is1a`, `tk1a`).
	Zone *string `pulumi:"zone"`
}

// A collection of values returned by getInternet.
type LookupInternetResult struct {
	// The bandwidth of the network connected to the Internet in Mbps.
	BandWidth int `pulumi:"bandWidth"`
	// The description of the Switch+Router.
	Description string `pulumi:"description"`
	// The flag to enable IPv6.
	EnableIpv6 bool               `pulumi:"enableIpv6"`
	Filter     *GetInternetFilter `pulumi:"filter"`
	// The IP address of the gateway used by Switch+Router.
	Gateway string `pulumi:"gateway"`
	// The icon id attached to the Switch+Router.
	IconId string `pulumi:"iconId"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// A list of assigned global address to the Switch+Router.
	IpAddresses []string `pulumi:"ipAddresses"`
	// The IPv6 network address assigned to the Switch+Router.
	Ipv6NetworkAddress string `pulumi:"ipv6NetworkAddress"`
	// The network prefix of assigned IPv6 addresses to the Switch+Router.
	Ipv6Prefix string `pulumi:"ipv6Prefix"`
	// The bit length of IPv6 network prefix.
	Ipv6PrefixLen int `pulumi:"ipv6PrefixLen"`
	// Maximum IP address in assigned global addresses to the Switch+Router.
	MaxIpAddress string `pulumi:"maxIpAddress"`
	// Minimum IP address in assigned global addresses to the Switch+Router.
	MinIpAddress string `pulumi:"minIpAddress"`
	// The name of the Switch+Router.
	Name string `pulumi:"name"`
	// The bit length of the subnet assigned to the Switch+Router.
	Netmask int `pulumi:"netmask"`
	// The IPv4 network address assigned to the Switch+Router.
	NetworkAddress string `pulumi:"networkAddress"`
	// A list of the ID of Servers connected to the Switch+Router.
	ServerIds []string `pulumi:"serverIds"`
	// The id of the switch connected from the Switch+Router.
	SwitchId string `pulumi:"switchId"`
	// Any tags assigned to the Switch+Router.
	Tags []string `pulumi:"tags"`
	Zone string   `pulumi:"zone"`
}

func LookupInternetOutput(ctx *pulumi.Context, args LookupInternetOutputArgs, opts ...pulumi.InvokeOption) LookupInternetResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupInternetResult, error) {
			args := v.(LookupInternetArgs)
			r, err := LookupInternet(ctx, &args, opts...)
			return *r, err
		}).(LookupInternetResultOutput)
}

// A collection of arguments for invoking getInternet.
type LookupInternetOutputArgs struct {
	// One or more values used for filtering, as defined below.
	Filter GetInternetFilterPtrInput `pulumi:"filter"`
	// The name of zone that the Switch+Router is in (e.g. `is1a`, `tk1a`).
	Zone pulumi.StringPtrInput `pulumi:"zone"`
}

func (LookupInternetOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupInternetArgs)(nil)).Elem()
}

// A collection of values returned by getInternet.
type LookupInternetResultOutput struct{ *pulumi.OutputState }

func (LookupInternetResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupInternetResult)(nil)).Elem()
}

func (o LookupInternetResultOutput) ToLookupInternetResultOutput() LookupInternetResultOutput {
	return o
}

func (o LookupInternetResultOutput) ToLookupInternetResultOutputWithContext(ctx context.Context) LookupInternetResultOutput {
	return o
}

// The bandwidth of the network connected to the Internet in Mbps.
func (o LookupInternetResultOutput) BandWidth() pulumi.IntOutput {
	return o.ApplyT(func(v LookupInternetResult) int { return v.BandWidth }).(pulumi.IntOutput)
}

// The description of the Switch+Router.
func (o LookupInternetResultOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v LookupInternetResult) string { return v.Description }).(pulumi.StringOutput)
}

// The flag to enable IPv6.
func (o LookupInternetResultOutput) EnableIpv6() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupInternetResult) bool { return v.EnableIpv6 }).(pulumi.BoolOutput)
}

func (o LookupInternetResultOutput) Filter() GetInternetFilterPtrOutput {
	return o.ApplyT(func(v LookupInternetResult) *GetInternetFilter { return v.Filter }).(GetInternetFilterPtrOutput)
}

// The IP address of the gateway used by Switch+Router.
func (o LookupInternetResultOutput) Gateway() pulumi.StringOutput {
	return o.ApplyT(func(v LookupInternetResult) string { return v.Gateway }).(pulumi.StringOutput)
}

// The icon id attached to the Switch+Router.
func (o LookupInternetResultOutput) IconId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupInternetResult) string { return v.IconId }).(pulumi.StringOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o LookupInternetResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupInternetResult) string { return v.Id }).(pulumi.StringOutput)
}

// A list of assigned global address to the Switch+Router.
func (o LookupInternetResultOutput) IpAddresses() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupInternetResult) []string { return v.IpAddresses }).(pulumi.StringArrayOutput)
}

// The IPv6 network address assigned to the Switch+Router.
func (o LookupInternetResultOutput) Ipv6NetworkAddress() pulumi.StringOutput {
	return o.ApplyT(func(v LookupInternetResult) string { return v.Ipv6NetworkAddress }).(pulumi.StringOutput)
}

// The network prefix of assigned IPv6 addresses to the Switch+Router.
func (o LookupInternetResultOutput) Ipv6Prefix() pulumi.StringOutput {
	return o.ApplyT(func(v LookupInternetResult) string { return v.Ipv6Prefix }).(pulumi.StringOutput)
}

// The bit length of IPv6 network prefix.
func (o LookupInternetResultOutput) Ipv6PrefixLen() pulumi.IntOutput {
	return o.ApplyT(func(v LookupInternetResult) int { return v.Ipv6PrefixLen }).(pulumi.IntOutput)
}

// Maximum IP address in assigned global addresses to the Switch+Router.
func (o LookupInternetResultOutput) MaxIpAddress() pulumi.StringOutput {
	return o.ApplyT(func(v LookupInternetResult) string { return v.MaxIpAddress }).(pulumi.StringOutput)
}

// Minimum IP address in assigned global addresses to the Switch+Router.
func (o LookupInternetResultOutput) MinIpAddress() pulumi.StringOutput {
	return o.ApplyT(func(v LookupInternetResult) string { return v.MinIpAddress }).(pulumi.StringOutput)
}

// The name of the Switch+Router.
func (o LookupInternetResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupInternetResult) string { return v.Name }).(pulumi.StringOutput)
}

// The bit length of the subnet assigned to the Switch+Router.
func (o LookupInternetResultOutput) Netmask() pulumi.IntOutput {
	return o.ApplyT(func(v LookupInternetResult) int { return v.Netmask }).(pulumi.IntOutput)
}

// The IPv4 network address assigned to the Switch+Router.
func (o LookupInternetResultOutput) NetworkAddress() pulumi.StringOutput {
	return o.ApplyT(func(v LookupInternetResult) string { return v.NetworkAddress }).(pulumi.StringOutput)
}

// A list of the ID of Servers connected to the Switch+Router.
func (o LookupInternetResultOutput) ServerIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupInternetResult) []string { return v.ServerIds }).(pulumi.StringArrayOutput)
}

// The id of the switch connected from the Switch+Router.
func (o LookupInternetResultOutput) SwitchId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupInternetResult) string { return v.SwitchId }).(pulumi.StringOutput)
}

// Any tags assigned to the Switch+Router.
func (o LookupInternetResultOutput) Tags() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupInternetResult) []string { return v.Tags }).(pulumi.StringArrayOutput)
}

func (o LookupInternetResultOutput) Zone() pulumi.StringOutput {
	return o.ApplyT(func(v LookupInternetResult) string { return v.Zone }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupInternetResultOutput{})
}
