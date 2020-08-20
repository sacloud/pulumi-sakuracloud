// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package sakuracloud

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

type DNS struct {
	pulumi.CustomResourceState

	// The description of the DNS. The length of this value must be in the range [`1`-`512`]
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// A list of IP address of DNS server that manage this zone
	DnsServers pulumi.StringArrayOutput `pulumi:"dnsServers"`
	// The icon id to attach to the DNS
	IconId  pulumi.StringPtrOutput   `pulumi:"iconId"`
	Records DNSRecordTypeArrayOutput `pulumi:"records"`
	// Any tags to assign to the DNS
	Tags pulumi.StringArrayOutput `pulumi:"tags"`
	// The target zone. (e.g. `example.com`)
	Zone pulumi.StringOutput `pulumi:"zone"`
}

// NewDNS registers a new resource with the given unique name, arguments, and options.
func NewDNS(ctx *pulumi.Context,
	name string, args *DNSArgs, opts ...pulumi.ResourceOption) (*DNS, error) {
	if args == nil || args.Zone == nil {
		return nil, errors.New("missing required argument 'Zone'")
	}
	if args == nil {
		args = &DNSArgs{}
	}
	var resource DNS
	err := ctx.RegisterResource("sakuracloud:index/dNS:DNS", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDNS gets an existing DNS resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDNS(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DNSState, opts ...pulumi.ResourceOption) (*DNS, error) {
	var resource DNS
	err := ctx.ReadResource("sakuracloud:index/dNS:DNS", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering DNS resources.
type dnsState struct {
	// The description of the DNS. The length of this value must be in the range [`1`-`512`]
	Description *string `pulumi:"description"`
	// A list of IP address of DNS server that manage this zone
	DnsServers []string `pulumi:"dnsServers"`
	// The icon id to attach to the DNS
	IconId  *string         `pulumi:"iconId"`
	Records []DNSRecordType `pulumi:"records"`
	// Any tags to assign to the DNS
	Tags []string `pulumi:"tags"`
	// The target zone. (e.g. `example.com`)
	Zone *string `pulumi:"zone"`
}

type DNSState struct {
	// The description of the DNS. The length of this value must be in the range [`1`-`512`]
	Description pulumi.StringPtrInput
	// A list of IP address of DNS server that manage this zone
	DnsServers pulumi.StringArrayInput
	// The icon id to attach to the DNS
	IconId  pulumi.StringPtrInput
	Records DNSRecordTypeArrayInput
	// Any tags to assign to the DNS
	Tags pulumi.StringArrayInput
	// The target zone. (e.g. `example.com`)
	Zone pulumi.StringPtrInput
}

func (DNSState) ElementType() reflect.Type {
	return reflect.TypeOf((*dnsState)(nil)).Elem()
}

type dnsArgs struct {
	// The description of the DNS. The length of this value must be in the range [`1`-`512`]
	Description *string `pulumi:"description"`
	// The icon id to attach to the DNS
	IconId  *string         `pulumi:"iconId"`
	Records []DNSRecordType `pulumi:"records"`
	// Any tags to assign to the DNS
	Tags []string `pulumi:"tags"`
	// The target zone. (e.g. `example.com`)
	Zone string `pulumi:"zone"`
}

// The set of arguments for constructing a DNS resource.
type DNSArgs struct {
	// The description of the DNS. The length of this value must be in the range [`1`-`512`]
	Description pulumi.StringPtrInput
	// The icon id to attach to the DNS
	IconId  pulumi.StringPtrInput
	Records DNSRecordTypeArrayInput
	// Any tags to assign to the DNS
	Tags pulumi.StringArrayInput
	// The target zone. (e.g. `example.com`)
	Zone pulumi.StringInput
}

func (DNSArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*dnsArgs)(nil)).Elem()
}
