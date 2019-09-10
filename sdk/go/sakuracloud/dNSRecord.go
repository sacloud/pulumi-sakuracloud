// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sakuracloud

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides a SakuraCloud DNS Record resource. This can be used to create and delete DNS Records.
// 
// ## Import (not supported)
// 
// Import of DNS Record is not supported.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-sakuracloud/blob/master/website/docs/r/dns_record.html.markdown.
type DNSRecord struct {
	s *pulumi.ResourceState
}

// NewDNSRecord registers a new resource with the given unique name, arguments, and options.
func NewDNSRecord(ctx *pulumi.Context,
	name string, args *DNSRecordArgs, opts ...pulumi.ResourceOpt) (*DNSRecord, error) {
	if args == nil || args.DnsId == nil {
		return nil, errors.New("missing required argument 'DnsId'")
	}
	if args == nil || args.Type == nil {
		return nil, errors.New("missing required argument 'Type'")
	}
	if args == nil || args.Value == nil {
		return nil, errors.New("missing required argument 'Value'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["dnsId"] = nil
		inputs["name"] = nil
		inputs["port"] = nil
		inputs["priority"] = nil
		inputs["ttl"] = nil
		inputs["type"] = nil
		inputs["value"] = nil
		inputs["weight"] = nil
	} else {
		inputs["dnsId"] = args.DnsId
		inputs["name"] = args.Name
		inputs["port"] = args.Port
		inputs["priority"] = args.Priority
		inputs["ttl"] = args.Ttl
		inputs["type"] = args.Type
		inputs["value"] = args.Value
		inputs["weight"] = args.Weight
	}
	s, err := ctx.RegisterResource("sakuracloud:index/dNSRecord:DNSRecord", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &DNSRecord{s: s}, nil
}

// GetDNSRecord gets an existing DNSRecord resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDNSRecord(ctx *pulumi.Context,
	name string, id pulumi.ID, state *DNSRecordState, opts ...pulumi.ResourceOpt) (*DNSRecord, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["dnsId"] = state.DnsId
		inputs["name"] = state.Name
		inputs["port"] = state.Port
		inputs["priority"] = state.Priority
		inputs["ttl"] = state.Ttl
		inputs["type"] = state.Type
		inputs["value"] = state.Value
		inputs["weight"] = state.Weight
	}
	s, err := ctx.ReadResource("sakuracloud:index/dNSRecord:DNSRecord", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &DNSRecord{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *DNSRecord) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *DNSRecord) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The ID of DNS zones to which the Record belongs.
func (r *DNSRecord) DnsId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["dnsId"])
}

// The hostname of target Record. If "@" is specified, it indicates own zone.
func (r *DNSRecord) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// The port number used when `type` is `SRV`. 
func (r *DNSRecord) Port() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["port"])
}

// The priority used when `type` is `MX` or `SRV`.
func (r *DNSRecord) Priority() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["priority"])
}

// The ttl value of the Record (unit:`second`). 
func (r *DNSRecord) Ttl() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["ttl"])
}

// The Record type.  
// Valid value is one of the following: [ "A" / "AAAA" / "CNAME" / "NS" / "MX" / "TXT" / "SRV" / "CAA"]
func (r *DNSRecord) Type() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["type"])
}

// The value of the Record. 
func (r *DNSRecord) Value() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["value"])
}

// The weight used when `type` is `SRV`.
func (r *DNSRecord) Weight() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["weight"])
}

// Input properties used for looking up and filtering DNSRecord resources.
type DNSRecordState struct {
	// The ID of DNS zones to which the Record belongs.
	DnsId interface{}
	// The hostname of target Record. If "@" is specified, it indicates own zone.
	Name interface{}
	// The port number used when `type` is `SRV`. 
	Port interface{}
	// The priority used when `type` is `MX` or `SRV`.
	Priority interface{}
	// The ttl value of the Record (unit:`second`). 
	Ttl interface{}
	// The Record type.  
	// Valid value is one of the following: [ "A" / "AAAA" / "CNAME" / "NS" / "MX" / "TXT" / "SRV" / "CAA"]
	Type interface{}
	// The value of the Record. 
	Value interface{}
	// The weight used when `type` is `SRV`.
	Weight interface{}
}

// The set of arguments for constructing a DNSRecord resource.
type DNSRecordArgs struct {
	// The ID of DNS zones to which the Record belongs.
	DnsId interface{}
	// The hostname of target Record. If "@" is specified, it indicates own zone.
	Name interface{}
	// The port number used when `type` is `SRV`. 
	Port interface{}
	// The priority used when `type` is `MX` or `SRV`.
	Priority interface{}
	// The ttl value of the Record (unit:`second`). 
	Ttl interface{}
	// The Record type.  
	// Valid value is one of the following: [ "A" / "AAAA" / "CNAME" / "NS" / "MX" / "TXT" / "SRV" / "CAA"]
	Type interface{}
	// The value of the Record. 
	Value interface{}
	// The weight used when `type` is `SRV`.
	Weight interface{}
}
