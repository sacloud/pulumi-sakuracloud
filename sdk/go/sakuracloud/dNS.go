// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sakuracloud

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides a SakuraCloud DNS zones resource. This can be used to create, update, and delete DNS zones.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-sakuracloud/blob/master/website/docs/r/dns.html.markdown.
type DNS struct {
	s *pulumi.ResourceState
}

// NewDNS registers a new resource with the given unique name, arguments, and options.
func NewDNS(ctx *pulumi.Context,
	name string, args *DNSArgs, opts ...pulumi.ResourceOpt) (*DNS, error) {
	if args == nil || args.Zone == nil {
		return nil, errors.New("missing required argument 'Zone'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["description"] = nil
		inputs["iconId"] = nil
		inputs["records"] = nil
		inputs["tags"] = nil
		inputs["zone"] = nil
	} else {
		inputs["description"] = args.Description
		inputs["iconId"] = args.IconId
		inputs["records"] = args.Records
		inputs["tags"] = args.Tags
		inputs["zone"] = args.Zone
	}
	inputs["dnsServers"] = nil
	s, err := ctx.RegisterResource("sakuracloud:index/dNS:DNS", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &DNS{s: s}, nil
}

// GetDNS gets an existing DNS resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDNS(ctx *pulumi.Context,
	name string, id pulumi.ID, state *DNSState, opts ...pulumi.ResourceOpt) (*DNS, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["description"] = state.Description
		inputs["dnsServers"] = state.DnsServers
		inputs["iconId"] = state.IconId
		inputs["records"] = state.Records
		inputs["tags"] = state.Tags
		inputs["zone"] = state.Zone
	}
	s, err := ctx.ReadResource("sakuracloud:index/dNS:DNS", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &DNS{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *DNS) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *DNS) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The description of the resource.
func (r *DNS) Description() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["description"])
}

// List of host names of DNS servers.
func (r *DNS) DnsServers() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["dnsServers"])
}

// The ID of the icon.
func (r *DNS) IconId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["iconId"])
}

// Records. It contains some attributes to Records.
func (r *DNS) Records() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["records"])
}

// The tag list of the resources.
func (r *DNS) Tags() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["tags"])
}

// The name of the zone.
func (r *DNS) Zone() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["zone"])
}

// Input properties used for looking up and filtering DNS resources.
type DNSState struct {
	// The description of the resource.
	Description interface{}
	// List of host names of DNS servers.
	DnsServers interface{}
	// The ID of the icon.
	IconId interface{}
	// Records. It contains some attributes to Records.
	Records interface{}
	// The tag list of the resources.
	Tags interface{}
	// The name of the zone.
	Zone interface{}
}

// The set of arguments for constructing a DNS resource.
type DNSArgs struct {
	// The description of the resource.
	Description interface{}
	// The ID of the icon.
	IconId interface{}
	// Records. It contains some attributes to Records.
	Records interface{}
	// The tag list of the resources.
	Tags interface{}
	// The name of the zone.
	Zone interface{}
}
