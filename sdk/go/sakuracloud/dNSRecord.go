// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package sakuracloud

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

type DNSRecord struct {
	pulumi.CustomResourceState

	// The id of the DNS resource
	DnsId pulumi.StringOutput `pulumi:"dnsId"`
	// The name of the DNS Record resource
	Name pulumi.StringOutput `pulumi:"name"`
	// The number of port. This must be in the range [`1`-`65535`]
	Port pulumi.IntPtrOutput `pulumi:"port"`
	// The priority of target DNS Record. This must be in the range [`0`-`65535`]
	Priority pulumi.IntPtrOutput `pulumi:"priority"`
	// The number of the TTL
	Ttl pulumi.IntPtrOutput `pulumi:"ttl"`
	// The type of DNS Record. This must be one of [`A`/`AAAA`/`ALIAS`/`CNAME`/`NS`/`MX`/`TXT`/`SRV`/`CAA`/`PTR`]
	Type pulumi.StringOutput `pulumi:"type"`
	// The value of the DNS Record
	Value pulumi.StringOutput `pulumi:"value"`
	// The weight of target DNS Record. This must be in the range [`0`-`65535`]
	Weight pulumi.IntPtrOutput `pulumi:"weight"`
}

// NewDNSRecord registers a new resource with the given unique name, arguments, and options.
func NewDNSRecord(ctx *pulumi.Context,
	name string, args *DNSRecordArgs, opts ...pulumi.ResourceOption) (*DNSRecord, error) {
	if args == nil || args.DnsId == nil {
		return nil, errors.New("missing required argument 'DnsId'")
	}
	if args == nil || args.Type == nil {
		return nil, errors.New("missing required argument 'Type'")
	}
	if args == nil || args.Value == nil {
		return nil, errors.New("missing required argument 'Value'")
	}
	if args == nil {
		args = &DNSRecordArgs{}
	}
	var resource DNSRecord
	err := ctx.RegisterResource("sakuracloud:index/dNSRecord:DNSRecord", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDNSRecord gets an existing DNSRecord resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDNSRecord(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DNSRecordState, opts ...pulumi.ResourceOption) (*DNSRecord, error) {
	var resource DNSRecord
	err := ctx.ReadResource("sakuracloud:index/dNSRecord:DNSRecord", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering DNSRecord resources.
type dnsrecordState struct {
	// The id of the DNS resource
	DnsId *string `pulumi:"dnsId"`
	// The name of the DNS Record resource
	Name *string `pulumi:"name"`
	// The number of port. This must be in the range [`1`-`65535`]
	Port *int `pulumi:"port"`
	// The priority of target DNS Record. This must be in the range [`0`-`65535`]
	Priority *int `pulumi:"priority"`
	// The number of the TTL
	Ttl *int `pulumi:"ttl"`
	// The type of DNS Record. This must be one of [`A`/`AAAA`/`ALIAS`/`CNAME`/`NS`/`MX`/`TXT`/`SRV`/`CAA`/`PTR`]
	Type *string `pulumi:"type"`
	// The value of the DNS Record
	Value *string `pulumi:"value"`
	// The weight of target DNS Record. This must be in the range [`0`-`65535`]
	Weight *int `pulumi:"weight"`
}

type DNSRecordState struct {
	// The id of the DNS resource
	DnsId pulumi.StringPtrInput
	// The name of the DNS Record resource
	Name pulumi.StringPtrInput
	// The number of port. This must be in the range [`1`-`65535`]
	Port pulumi.IntPtrInput
	// The priority of target DNS Record. This must be in the range [`0`-`65535`]
	Priority pulumi.IntPtrInput
	// The number of the TTL
	Ttl pulumi.IntPtrInput
	// The type of DNS Record. This must be one of [`A`/`AAAA`/`ALIAS`/`CNAME`/`NS`/`MX`/`TXT`/`SRV`/`CAA`/`PTR`]
	Type pulumi.StringPtrInput
	// The value of the DNS Record
	Value pulumi.StringPtrInput
	// The weight of target DNS Record. This must be in the range [`0`-`65535`]
	Weight pulumi.IntPtrInput
}

func (DNSRecordState) ElementType() reflect.Type {
	return reflect.TypeOf((*dnsrecordState)(nil)).Elem()
}

type dnsrecordArgs struct {
	// The id of the DNS resource
	DnsId string `pulumi:"dnsId"`
	// The name of the DNS Record resource
	Name *string `pulumi:"name"`
	// The number of port. This must be in the range [`1`-`65535`]
	Port *int `pulumi:"port"`
	// The priority of target DNS Record. This must be in the range [`0`-`65535`]
	Priority *int `pulumi:"priority"`
	// The number of the TTL
	Ttl *int `pulumi:"ttl"`
	// The type of DNS Record. This must be one of [`A`/`AAAA`/`ALIAS`/`CNAME`/`NS`/`MX`/`TXT`/`SRV`/`CAA`/`PTR`]
	Type string `pulumi:"type"`
	// The value of the DNS Record
	Value string `pulumi:"value"`
	// The weight of target DNS Record. This must be in the range [`0`-`65535`]
	Weight *int `pulumi:"weight"`
}

// The set of arguments for constructing a DNSRecord resource.
type DNSRecordArgs struct {
	// The id of the DNS resource
	DnsId pulumi.StringInput
	// The name of the DNS Record resource
	Name pulumi.StringPtrInput
	// The number of port. This must be in the range [`1`-`65535`]
	Port pulumi.IntPtrInput
	// The priority of target DNS Record. This must be in the range [`0`-`65535`]
	Priority pulumi.IntPtrInput
	// The number of the TTL
	Ttl pulumi.IntPtrInput
	// The type of DNS Record. This must be one of [`A`/`AAAA`/`ALIAS`/`CNAME`/`NS`/`MX`/`TXT`/`SRV`/`CAA`/`PTR`]
	Type pulumi.StringInput
	// The value of the DNS Record
	Value pulumi.StringInput
	// The weight of target DNS Record. This must be in the range [`0`-`65535`]
	Weight pulumi.IntPtrInput
}

func (DNSRecordArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*dnsrecordArgs)(nil)).Elem()
}

