// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sakuracloud

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Get information about an existing Container Registry.
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
// 		_, err := sakuracloud.LookupContainerRegistry(ctx, &GetContainerRegistryArgs{
// 			Filter: GetContainerRegistryFilter{
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
func LookupContainerRegistry(ctx *pulumi.Context, args *LookupContainerRegistryArgs, opts ...pulumi.InvokeOption) (*LookupContainerRegistryResult, error) {
	var rv LookupContainerRegistryResult
	err := ctx.Invoke("sakuracloud:index/getContainerRegistry:getContainerRegistry", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getContainerRegistry.
type LookupContainerRegistryArgs struct {
	// One or more values used for filtering, as defined below.
	Filter *GetContainerRegistryFilter `pulumi:"filter"`
}

// A collection of values returned by getContainerRegistry.
type LookupContainerRegistryResult struct {
	// The level of access that allow to users. This will be one of [`readwrite`/`readonly`/`none`].
	AccessLevel string `pulumi:"accessLevel"`
	// The description of the ContainerRegistry.
	Description string                      `pulumi:"description"`
	Filter      *GetContainerRegistryFilter `pulumi:"filter"`
	// The FQDN for accessing the container registry. FQDN is built from `subdomainLabel` + `.sakuracr.jp`.
	Fqdn string `pulumi:"fqdn"`
	// The icon id attached to the ContainerRegistry.
	IconId string `pulumi:"iconId"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// The user name used to authenticate remote access.
	Name string `pulumi:"name"`
	// The label at the lowest of the FQDN used when be accessed from users.
	SubdomainLabel string `pulumi:"subdomainLabel"`
	// Any tags assigned to the ContainerRegistry.
	Tags []string `pulumi:"tags"`
	// A list of `user` blocks as defined below.
	Users []GetContainerRegistryUser `pulumi:"users"`
	// The alias for accessing the container registry.
	VirtualDomain string `pulumi:"virtualDomain"`
}

func LookupContainerRegistryOutput(ctx *pulumi.Context, args LookupContainerRegistryOutputArgs, opts ...pulumi.InvokeOption) LookupContainerRegistryResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupContainerRegistryResult, error) {
			args := v.(LookupContainerRegistryArgs)
			r, err := LookupContainerRegistry(ctx, &args, opts...)
			return *r, err
		}).(LookupContainerRegistryResultOutput)
}

// A collection of arguments for invoking getContainerRegistry.
type LookupContainerRegistryOutputArgs struct {
	// One or more values used for filtering, as defined below.
	Filter GetContainerRegistryFilterPtrInput `pulumi:"filter"`
}

func (LookupContainerRegistryOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupContainerRegistryArgs)(nil)).Elem()
}

// A collection of values returned by getContainerRegistry.
type LookupContainerRegistryResultOutput struct{ *pulumi.OutputState }

func (LookupContainerRegistryResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupContainerRegistryResult)(nil)).Elem()
}

func (o LookupContainerRegistryResultOutput) ToLookupContainerRegistryResultOutput() LookupContainerRegistryResultOutput {
	return o
}

func (o LookupContainerRegistryResultOutput) ToLookupContainerRegistryResultOutputWithContext(ctx context.Context) LookupContainerRegistryResultOutput {
	return o
}

// The level of access that allow to users. This will be one of [`readwrite`/`readonly`/`none`].
func (o LookupContainerRegistryResultOutput) AccessLevel() pulumi.StringOutput {
	return o.ApplyT(func(v LookupContainerRegistryResult) string { return v.AccessLevel }).(pulumi.StringOutput)
}

// The description of the ContainerRegistry.
func (o LookupContainerRegistryResultOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v LookupContainerRegistryResult) string { return v.Description }).(pulumi.StringOutput)
}

func (o LookupContainerRegistryResultOutput) Filter() GetContainerRegistryFilterPtrOutput {
	return o.ApplyT(func(v LookupContainerRegistryResult) *GetContainerRegistryFilter { return v.Filter }).(GetContainerRegistryFilterPtrOutput)
}

// The FQDN for accessing the container registry. FQDN is built from `subdomainLabel` + `.sakuracr.jp`.
func (o LookupContainerRegistryResultOutput) Fqdn() pulumi.StringOutput {
	return o.ApplyT(func(v LookupContainerRegistryResult) string { return v.Fqdn }).(pulumi.StringOutput)
}

// The icon id attached to the ContainerRegistry.
func (o LookupContainerRegistryResultOutput) IconId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupContainerRegistryResult) string { return v.IconId }).(pulumi.StringOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o LookupContainerRegistryResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupContainerRegistryResult) string { return v.Id }).(pulumi.StringOutput)
}

// The user name used to authenticate remote access.
func (o LookupContainerRegistryResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupContainerRegistryResult) string { return v.Name }).(pulumi.StringOutput)
}

// The label at the lowest of the FQDN used when be accessed from users.
func (o LookupContainerRegistryResultOutput) SubdomainLabel() pulumi.StringOutput {
	return o.ApplyT(func(v LookupContainerRegistryResult) string { return v.SubdomainLabel }).(pulumi.StringOutput)
}

// Any tags assigned to the ContainerRegistry.
func (o LookupContainerRegistryResultOutput) Tags() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupContainerRegistryResult) []string { return v.Tags }).(pulumi.StringArrayOutput)
}

// A list of `user` blocks as defined below.
func (o LookupContainerRegistryResultOutput) Users() GetContainerRegistryUserArrayOutput {
	return o.ApplyT(func(v LookupContainerRegistryResult) []GetContainerRegistryUser { return v.Users }).(GetContainerRegistryUserArrayOutput)
}

// The alias for accessing the container registry.
func (o LookupContainerRegistryResultOutput) VirtualDomain() pulumi.StringOutput {
	return o.ApplyT(func(v LookupContainerRegistryResult) string { return v.VirtualDomain }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupContainerRegistryResultOutput{})
}
