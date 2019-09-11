// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sakuracloud

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Use this data source to retrieve information about a SakuraCloud DNS.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-sakuracloud/blob/master/website/docs/d/dns.html.markdown.
func LookupDNS(ctx *pulumi.Context, args *GetDNSArgs) (*GetDNSResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["filters"] = args.Filters
		inputs["nameSelectors"] = args.NameSelectors
		inputs["tagSelectors"] = args.TagSelectors
	}
	outputs, err := ctx.Invoke("sakuracloud:index/getDNS:getDNS", inputs)
	if err != nil {
		return nil, err
	}
	return &GetDNSResult{
		Description: outputs["description"],
		DnsServers: outputs["dnsServers"],
		Filters: outputs["filters"],
		IconId: outputs["iconId"],
		NameSelectors: outputs["nameSelectors"],
		Records: outputs["records"],
		TagSelectors: outputs["tagSelectors"],
		Tags: outputs["tags"],
		Zone: outputs["zone"],
		Id: outputs["id"],
	}, nil
}

// A collection of arguments for invoking getDNS.
type GetDNSArgs struct {
	// The map of filter key and value.
	Filters interface{}
	// The list of names to filtering.
	NameSelectors interface{}
	// The list of tags to filtering.
	TagSelectors interface{}
}

// A collection of values returned by getDNS.
type GetDNSResult struct {
	// The description of the resource.
	Description interface{}
	// List of host names of DNS servers.
	DnsServers interface{}
	Filters interface{}
	// The ID of the icon of the resource.
	IconId interface{}
	NameSelectors interface{}
	Records interface{}
	TagSelectors interface{}
	// The tag list of the resources.
	Tags interface{}
	// The name of the zone.
	Zone interface{}
	// id is the provider-assigned unique ID for this managed resource.
	Id interface{}
}