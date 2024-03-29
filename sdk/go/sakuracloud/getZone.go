// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sakuracloud

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Get information about an existing Zone.
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
// 		_, err := sakuracloud.GetZone(ctx, nil, nil)
// 		if err != nil {
// 			return err
// 		}
// 		opt0 := "is1a"
// 		_, err = sakuracloud.GetZone(ctx, &GetZoneArgs{
// 			Name: &opt0,
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
func GetZone(ctx *pulumi.Context, args *GetZoneArgs, opts ...pulumi.InvokeOption) (*GetZoneResult, error) {
	var rv GetZoneResult
	err := ctx.Invoke("sakuracloud:index/getZone:getZone", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getZone.
type GetZoneArgs struct {
	// The name of the zone (e.g. `is1a`,`tk1a`).
	Name *string `pulumi:"name"`
}

// A collection of values returned by getZone.
type GetZoneResult struct {
	// The description of the zone.
	Description string `pulumi:"description"`
	// A list of IP address of DNS server in the zone.
	DnsServers []string `pulumi:"dnsServers"`
	// The provider-assigned unique ID for this managed resource.
	Id   string `pulumi:"id"`
	Name string `pulumi:"name"`
	// The id of the region that the zone belongs.
	RegionId string `pulumi:"regionId"`
	// The name of the region that the zone belongs.
	RegionName string `pulumi:"regionName"`
	// The id of the zone.
	ZoneId string `pulumi:"zoneId"`
}

func GetZoneOutput(ctx *pulumi.Context, args GetZoneOutputArgs, opts ...pulumi.InvokeOption) GetZoneResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetZoneResult, error) {
			args := v.(GetZoneArgs)
			r, err := GetZone(ctx, &args, opts...)
			return *r, err
		}).(GetZoneResultOutput)
}

// A collection of arguments for invoking getZone.
type GetZoneOutputArgs struct {
	// The name of the zone (e.g. `is1a`,`tk1a`).
	Name pulumi.StringPtrInput `pulumi:"name"`
}

func (GetZoneOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetZoneArgs)(nil)).Elem()
}

// A collection of values returned by getZone.
type GetZoneResultOutput struct{ *pulumi.OutputState }

func (GetZoneResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetZoneResult)(nil)).Elem()
}

func (o GetZoneResultOutput) ToGetZoneResultOutput() GetZoneResultOutput {
	return o
}

func (o GetZoneResultOutput) ToGetZoneResultOutputWithContext(ctx context.Context) GetZoneResultOutput {
	return o
}

// The description of the zone.
func (o GetZoneResultOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v GetZoneResult) string { return v.Description }).(pulumi.StringOutput)
}

// A list of IP address of DNS server in the zone.
func (o GetZoneResultOutput) DnsServers() pulumi.StringArrayOutput {
	return o.ApplyT(func(v GetZoneResult) []string { return v.DnsServers }).(pulumi.StringArrayOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o GetZoneResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetZoneResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o GetZoneResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v GetZoneResult) string { return v.Name }).(pulumi.StringOutput)
}

// The id of the region that the zone belongs.
func (o GetZoneResultOutput) RegionId() pulumi.StringOutput {
	return o.ApplyT(func(v GetZoneResult) string { return v.RegionId }).(pulumi.StringOutput)
}

// The name of the region that the zone belongs.
func (o GetZoneResultOutput) RegionName() pulumi.StringOutput {
	return o.ApplyT(func(v GetZoneResult) string { return v.RegionName }).(pulumi.StringOutput)
}

// The id of the zone.
func (o GetZoneResultOutput) ZoneId() pulumi.StringOutput {
	return o.ApplyT(func(v GetZoneResult) string { return v.ZoneId }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(GetZoneResultOutput{})
}
