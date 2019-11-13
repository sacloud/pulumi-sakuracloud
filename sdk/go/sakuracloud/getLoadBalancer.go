// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sakuracloud

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Use this data source to retrieve information about a SakuraCloud Load Balancer.
//
// > This content is derived from https://github.com/sacloud/terraform-provider-sakuracloud/blob/master/website/docs/d/load_balancer.html.markdown.
func LookupLoadBalancer(ctx *pulumi.Context, args *GetLoadBalancerArgs) (*GetLoadBalancerResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["filters"] = args.Filters
		inputs["nameSelectors"] = args.NameSelectors
		inputs["tagSelectors"] = args.TagSelectors
		inputs["zone"] = args.Zone
	}
	outputs, err := ctx.Invoke("sakuracloud:index/getLoadBalancer:getLoadBalancer", inputs)
	if err != nil {
		return nil, err
	}
	return &GetLoadBalancerResult{
		DefaultRoute: outputs["defaultRoute"],
		Description: outputs["description"],
		Filters: outputs["filters"],
		HighAvailability: outputs["highAvailability"],
		IconId: outputs["iconId"],
		Ipaddress1: outputs["ipaddress1"],
		Ipaddress2: outputs["ipaddress2"],
		Name: outputs["name"],
		NameSelectors: outputs["nameSelectors"],
		NwMaskLen: outputs["nwMaskLen"],
		Plan: outputs["plan"],
		SwitchId: outputs["switchId"],
		TagSelectors: outputs["tagSelectors"],
		Tags: outputs["tags"],
		Vrid: outputs["vrid"],
		Zone: outputs["zone"],
		Id: outputs["id"],
	}, nil
}

// A collection of arguments for invoking getLoadBalancer.
type GetLoadBalancerArgs struct {
	// The map of filter key and value.
	Filters interface{}
	// The list of names to filtering.
	NameSelectors interface{}
	// The list of tags to filtering.
	TagSelectors interface{}
	// The ID of the zone.
	Zone interface{}
}

// A collection of values returned by getLoadBalancer.
type GetLoadBalancerResult struct {
	// Default gateway address of the Load Balancer.	 
	DefaultRoute interface{}
	// The description of the resource.
	Description interface{}
	Filters interface{}
	// The flag of enable/disable high-availability mode.
	HighAvailability interface{}
	// The ID of the icon of the resource.
	IconId interface{}
	// The primary IP address of the Load Balancer.
	Ipaddress1 interface{}
	// The secondly IP address of the Load Balancer. Used when high-availability mode enabled.
	Ipaddress2 interface{}
	// The name of the resource.
	Name interface{}
	NameSelectors interface{}
	// Network mask length.
	NwMaskLen interface{}
	// The name of the resource plan. 
	Plan interface{}
	// The ID of the Switch connected to the Load Balancer.
	SwitchId interface{}
	TagSelectors interface{}
	// The tag list of the resources.
	Tags interface{}
	// VRID used when high-availability mode enabled.
	Vrid interface{}
	// The ID of the zone to which the resource belongs.
	Zone interface{}
	// id is the provider-assigned unique ID for this managed resource.
	Id interface{}
}
