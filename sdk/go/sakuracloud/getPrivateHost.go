// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sakuracloud

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Use this data source to retrieve information about a SakuraCloud Private Host.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-sakuracloud/blob/master/website/docs/d/private_host.html.markdown.
func LookupPrivateHost(ctx *pulumi.Context, args *GetPrivateHostArgs) (*GetPrivateHostResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["filters"] = args.Filters
		inputs["nameSelectors"] = args.NameSelectors
		inputs["tagSelectors"] = args.TagSelectors
		inputs["zone"] = args.Zone
	}
	outputs, err := ctx.Invoke("sakuracloud:index/getPrivateHost:getPrivateHost", inputs)
	if err != nil {
		return nil, err
	}
	return &GetPrivateHostResult{
		AssignedCore: outputs["assignedCore"],
		AssignedMemory: outputs["assignedMemory"],
		Description: outputs["description"],
		Filters: outputs["filters"],
		Hostname: outputs["hostname"],
		Name: outputs["name"],
		NameSelectors: outputs["nameSelectors"],
		TagSelectors: outputs["tagSelectors"],
		Tags: outputs["tags"],
		Zone: outputs["zone"],
		Id: outputs["id"],
	}, nil
}

// A collection of arguments for invoking getPrivateHost.
type GetPrivateHostArgs struct {
	// The map of filter key and value.
	Filters interface{}
	// The list of names to filtering.
	NameSelectors interface{}
	// The list of tags to filtering.
	TagSelectors interface{}
	// The ID of the zone.
	Zone interface{}
}

// A collection of values returned by getPrivateHost.
type GetPrivateHostResult struct {
	// The number of cores assigned to the Server.
	AssignedCore interface{}
	// The size of memory allocated to the Server (unit:`GB`).
	AssignedMemory interface{}
	// The description of the resource.
	Description interface{}
	Filters interface{}
	// The HostName of the resource.
	Hostname interface{}
	// The name of the resource.
	Name interface{}
	NameSelectors interface{}
	TagSelectors interface{}
	// The tag list of the resources.
	Tags interface{}
	// The ID of the zone to which the resource belongs.
	Zone interface{}
	// id is the provider-assigned unique ID for this managed resource.
	Id interface{}
}
