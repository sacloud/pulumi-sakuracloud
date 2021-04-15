// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sakuracloud

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Get information about an existing GSLB.
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
// 		_, err := sakuracloud.LookupGSLB(ctx, &sakuracloud.LookupGSLBArgs{
// 			Filter: sakuracloud.GetGSLBFilter{
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
func LookupGSLB(ctx *pulumi.Context, args *LookupGSLBArgs, opts ...pulumi.InvokeOption) (*LookupGSLBResult, error) {
	var rv LookupGSLBResult
	err := ctx.Invoke("sakuracloud:index/getGSLB:getGSLB", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getGSLB.
type LookupGSLBArgs struct {
	// One or more values used for filtering, as defined below.
	Filter *GetGSLBFilter `pulumi:"filter"`
}

// A collection of values returned by getGSLB.
type LookupGSLBResult struct {
	// The description of the GSLB.
	Description string         `pulumi:"description"`
	Filter      *GetGSLBFilter `pulumi:"filter"`
	// The FQDN for accessing to the GSLB. This is typically used as value of CNAME record.
	Fqdn string `pulumi:"fqdn"`
	// A list of `healthCheck` blocks as defined below.
	HealthChecks []GetGSLBHealthCheck `pulumi:"healthChecks"`
	// The icon id attached to the GSLB.
	IconId string `pulumi:"iconId"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// The name of the GSLB.
	Name string `pulumi:"name"`
	// A list of `server` blocks as defined below.
	Servers []GetGSLBServer `pulumi:"servers"`
	// The IP address of the SorryServer. This will be used when all servers are down.
	SorryServer string `pulumi:"sorryServer"`
	// Any tags assigned to the GSLB.
	Tags []string `pulumi:"tags"`
	// The flag to enable weighted load-balancing.
	Weighted bool `pulumi:"weighted"`
}
