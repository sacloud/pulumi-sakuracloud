// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package sakuracloud

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

func LookupDNS(ctx *pulumi.Context, args *LookupDNSArgs, opts ...pulumi.InvokeOption) (*LookupDNSResult, error) {
	var rv LookupDNSResult
	err := ctx.Invoke("sakuracloud:index/getDNS:getDNS", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getDNS.
type LookupDNSArgs struct {
	Filter *GetDNSFilter `pulumi:"filter"`
}


// A collection of values returned by getDNS.
type LookupDNSResult struct {
	Description string `pulumi:"description"`
	DnsServers []string `pulumi:"dnsServers"`
	Filter *GetDNSFilter `pulumi:"filter"`
	IconId string `pulumi:"iconId"`
	// id is the provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	Records []GetDNSRecordType `pulumi:"records"`
	Tags []string `pulumi:"tags"`
	Zone string `pulumi:"zone"`
}

