// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sakuracloud

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Use this data source to retrieve information about a SakuraCloud NFS.
//
// > This content is derived from https://github.com/sacloud/terraform-provider-sakuracloud/blob/master/website/docs/d/nfs.html.markdown.
func LookupNFS(ctx *pulumi.Context, args *GetNFSArgs) (*GetNFSResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["filters"] = args.Filters
		inputs["nameSelectors"] = args.NameSelectors
		inputs["tagSelectors"] = args.TagSelectors
		inputs["zone"] = args.Zone
	}
	outputs, err := ctx.Invoke("sakuracloud:index/getNFS:getNFS", inputs)
	if err != nil {
		return nil, err
	}
	return &GetNFSResult{
		DefaultRoute: outputs["defaultRoute"],
		Description: outputs["description"],
		Filters: outputs["filters"],
		IconId: outputs["iconId"],
		Ipaddress: outputs["ipaddress"],
		Name: outputs["name"],
		NameSelectors: outputs["nameSelectors"],
		NwMaskLen: outputs["nwMaskLen"],
		Plan: outputs["plan"],
		Size: outputs["size"],
		SwitchId: outputs["switchId"],
		TagSelectors: outputs["tagSelectors"],
		Tags: outputs["tags"],
		Zone: outputs["zone"],
		Id: outputs["id"],
	}, nil
}

// A collection of arguments for invoking getNFS.
type GetNFSArgs struct {
	// The map of filter key and value.
	Filters interface{}
	// The list of names to filtering.
	NameSelectors interface{}
	// The list of tags to filtering.
	TagSelectors interface{}
	// The ID of the zone.
	Zone interface{}
}

// A collection of values returned by getNFS.
type GetNFSResult struct {
	// Default gateway address of the NFS.	 
	DefaultRoute interface{}
	// The description of the resource.
	Description interface{}
	Filters interface{}
	// The ID of the icon of the resource.
	IconId interface{}
	// The IP address of the NFS.
	Ipaddress interface{}
	// The name of the resource.
	Name interface{}
	NameSelectors interface{}
	// Network mask length.
	NwMaskLen interface{}
	// The name of the resource plan.
	Plan interface{}
	// The size of the NFS.
	Size interface{}
	// The ID of the Switch connected to the NFS.
	SwitchId interface{}
	TagSelectors interface{}
	// The tag list of the resources.
	Tags interface{}
	// The ID of the zone to which the resource belongs.
	Zone interface{}
	// id is the provider-assigned unique ID for this managed resource.
	Id interface{}
}
