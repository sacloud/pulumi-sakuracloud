// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sakuracloud

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Use this data source to retrieve information about a SakuraCloud Disk.
//
// > This content is derived from https://github.com/sacloud/terraform-provider-sakuracloud/blob/master/website/docs/d/disk.html.markdown.
func LookupDisk(ctx *pulumi.Context, args *GetDiskArgs) (*GetDiskResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["filters"] = args.Filters
		inputs["nameSelectors"] = args.NameSelectors
		inputs["tagSelectors"] = args.TagSelectors
		inputs["zone"] = args.Zone
	}
	outputs, err := ctx.Invoke("sakuracloud:index/getDisk:getDisk", inputs)
	if err != nil {
		return nil, err
	}
	return &GetDiskResult{
		Connector: outputs["connector"],
		Description: outputs["description"],
		Filters: outputs["filters"],
		IconId: outputs["iconId"],
		Name: outputs["name"],
		NameSelectors: outputs["nameSelectors"],
		Plan: outputs["plan"],
		ServerId: outputs["serverId"],
		Size: outputs["size"],
		TagSelectors: outputs["tagSelectors"],
		Tags: outputs["tags"],
		Zone: outputs["zone"],
		Id: outputs["id"],
	}, nil
}

// A collection of arguments for invoking getDisk.
type GetDiskArgs struct {
	// The map of filter key and value.
	Filters interface{}
	// The list of names to filtering.
	NameSelectors interface{}
	// The list of tags to filtering.
	TagSelectors interface{}
	// The ID of the zone.
	Zone interface{}
}

// A collection of values returned by getDisk.
type GetDiskResult struct {
	Connector interface{}
	// The description of the resource.
	Description interface{}
	Filters interface{}
	// The ID of the icon of the resource.
	IconId interface{}
	// The name of the resource.
	Name interface{}
	NameSelectors interface{}
	// The plan of the resource (`ssd`/`hdd`).
	Plan interface{}
	// The ID of the server connected to the disk.
	ServerId interface{}
	// Size of the resource (unit:`GB`).
	Size interface{}
	TagSelectors interface{}
	// The tag list of the resources.
	Tags interface{}
	// The ID of the zone to which the resource belongs.
	Zone interface{}
	// id is the provider-assigned unique ID for this managed resource.
	Id interface{}
}
