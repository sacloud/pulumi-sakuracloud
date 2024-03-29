// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sakuracloud

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Get information about an existing NFS.
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
// 		_, err := sakuracloud.LookupNFS(ctx, &GetNFSArgs{
// 			Filter: GetNFSFilter{
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
func LookupNFS(ctx *pulumi.Context, args *LookupNFSArgs, opts ...pulumi.InvokeOption) (*LookupNFSResult, error) {
	var rv LookupNFSResult
	err := ctx.Invoke("sakuracloud:index/getNFS:getNFS", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getNFS.
type LookupNFSArgs struct {
	// One or more values used for filtering, as defined below.
	Filter *GetNFSFilter `pulumi:"filter"`
	// The name of zone that the NFS is in (e.g. `is1a`, `tk1a`).
	Zone *string `pulumi:"zone"`
}

// A collection of values returned by getNFS.
type LookupNFSResult struct {
	// The description of the NFS.
	Description string        `pulumi:"description"`
	Filter      *GetNFSFilter `pulumi:"filter"`
	// The icon id attached to the NFS.
	IconId string `pulumi:"iconId"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// The name of the NFS.
	Name string `pulumi:"name"`
	// A list of `networkInterface` blocks as defined below.
	NetworkInterfaces []GetNFSNetworkInterface `pulumi:"networkInterfaces"`
	// The plan name of the NFS. This will be one of [`hdd`/`ssd`].
	Plan string `pulumi:"plan"`
	// The size of NFS in GiB.
	Size int `pulumi:"size"`
	// Any tags assigned to the NFS.
	Tags []string `pulumi:"tags"`
	Zone string   `pulumi:"zone"`
}

func LookupNFSOutput(ctx *pulumi.Context, args LookupNFSOutputArgs, opts ...pulumi.InvokeOption) LookupNFSResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupNFSResult, error) {
			args := v.(LookupNFSArgs)
			r, err := LookupNFS(ctx, &args, opts...)
			return *r, err
		}).(LookupNFSResultOutput)
}

// A collection of arguments for invoking getNFS.
type LookupNFSOutputArgs struct {
	// One or more values used for filtering, as defined below.
	Filter GetNFSFilterPtrInput `pulumi:"filter"`
	// The name of zone that the NFS is in (e.g. `is1a`, `tk1a`).
	Zone pulumi.StringPtrInput `pulumi:"zone"`
}

func (LookupNFSOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupNFSArgs)(nil)).Elem()
}

// A collection of values returned by getNFS.
type LookupNFSResultOutput struct{ *pulumi.OutputState }

func (LookupNFSResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupNFSResult)(nil)).Elem()
}

func (o LookupNFSResultOutput) ToLookupNFSResultOutput() LookupNFSResultOutput {
	return o
}

func (o LookupNFSResultOutput) ToLookupNFSResultOutputWithContext(ctx context.Context) LookupNFSResultOutput {
	return o
}

// The description of the NFS.
func (o LookupNFSResultOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v LookupNFSResult) string { return v.Description }).(pulumi.StringOutput)
}

func (o LookupNFSResultOutput) Filter() GetNFSFilterPtrOutput {
	return o.ApplyT(func(v LookupNFSResult) *GetNFSFilter { return v.Filter }).(GetNFSFilterPtrOutput)
}

// The icon id attached to the NFS.
func (o LookupNFSResultOutput) IconId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupNFSResult) string { return v.IconId }).(pulumi.StringOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o LookupNFSResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupNFSResult) string { return v.Id }).(pulumi.StringOutput)
}

// The name of the NFS.
func (o LookupNFSResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupNFSResult) string { return v.Name }).(pulumi.StringOutput)
}

// A list of `networkInterface` blocks as defined below.
func (o LookupNFSResultOutput) NetworkInterfaces() GetNFSNetworkInterfaceArrayOutput {
	return o.ApplyT(func(v LookupNFSResult) []GetNFSNetworkInterface { return v.NetworkInterfaces }).(GetNFSNetworkInterfaceArrayOutput)
}

// The plan name of the NFS. This will be one of [`hdd`/`ssd`].
func (o LookupNFSResultOutput) Plan() pulumi.StringOutput {
	return o.ApplyT(func(v LookupNFSResult) string { return v.Plan }).(pulumi.StringOutput)
}

// The size of NFS in GiB.
func (o LookupNFSResultOutput) Size() pulumi.IntOutput {
	return o.ApplyT(func(v LookupNFSResult) int { return v.Size }).(pulumi.IntOutput)
}

// Any tags assigned to the NFS.
func (o LookupNFSResultOutput) Tags() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupNFSResult) []string { return v.Tags }).(pulumi.StringArrayOutput)
}

func (o LookupNFSResultOutput) Zone() pulumi.StringOutput {
	return o.ApplyT(func(v LookupNFSResult) string { return v.Zone }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupNFSResultOutput{})
}
