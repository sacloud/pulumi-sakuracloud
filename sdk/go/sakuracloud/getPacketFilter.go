// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package sakuracloud

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

func LookupPacketFilter(ctx *pulumi.Context, args *LookupPacketFilterArgs, opts ...pulumi.InvokeOption) (*LookupPacketFilterResult, error) {
	var rv LookupPacketFilterResult
	err := ctx.Invoke("sakuracloud:index/getPacketFilter:getPacketFilter", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getPacketFilter.
type LookupPacketFilterArgs struct {
	Filter *GetPacketFilterFilter `pulumi:"filter"`
	Zone   *string                `pulumi:"zone"`
}

// A collection of values returned by getPacketFilter.
type LookupPacketFilterResult struct {
	Description string                      `pulumi:"description"`
	Expressions []GetPacketFilterExpression `pulumi:"expressions"`
	Filter      *GetPacketFilterFilter      `pulumi:"filter"`
	// id is the provider-assigned unique ID for this managed resource.
	Id   string `pulumi:"id"`
	Name string `pulumi:"name"`
	Zone string `pulumi:"zone"`
}
