// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sakuracloud

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
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
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := sakuracloud.LookupContainerRegistry(ctx, &sakuracloud.LookupContainerRegistryArgs{
// 			Filter: sakuracloud.GetContainerRegistryFilter{
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
