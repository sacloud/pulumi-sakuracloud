// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package sakuracloud

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

type IPv4Ptr struct {
	pulumi.CustomResourceState

	// The value of the PTR record. This must be FQDN
	Hostname pulumi.StringOutput `pulumi:"hostname"`
	// The IP address to which the PTR record is set
	IpAddress pulumi.StringOutput `pulumi:"ipAddress"`
	// The wait interval(in seconds) for retrying API call used when SakuraCloud API returns any errors
	RetryInterval pulumi.IntPtrOutput `pulumi:"retryInterval"`
	// The maximum number of API call retries used when SakuraCloud API returns any errors
	RetryMax pulumi.IntPtrOutput `pulumi:"retryMax"`
	// The name of zone that the IPv4 PTR will be created (e.g. `is1a`, `tk1a`)
	Zone pulumi.StringOutput `pulumi:"zone"`
}

// NewIPv4Ptr registers a new resource with the given unique name, arguments, and options.
func NewIPv4Ptr(ctx *pulumi.Context,
	name string, args *IPv4PtrArgs, opts ...pulumi.ResourceOption) (*IPv4Ptr, error) {
	if args == nil || args.Hostname == nil {
		return nil, errors.New("missing required argument 'Hostname'")
	}
	if args == nil || args.IpAddress == nil {
		return nil, errors.New("missing required argument 'IpAddress'")
	}
	if args == nil {
		args = &IPv4PtrArgs{}
	}
	var resource IPv4Ptr
	err := ctx.RegisterResource("sakuracloud:index/iPv4Ptr:IPv4Ptr", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetIPv4Ptr gets an existing IPv4Ptr resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetIPv4Ptr(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *IPv4PtrState, opts ...pulumi.ResourceOption) (*IPv4Ptr, error) {
	var resource IPv4Ptr
	err := ctx.ReadResource("sakuracloud:index/iPv4Ptr:IPv4Ptr", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering IPv4Ptr resources.
type ipv4PtrState struct {
	// The value of the PTR record. This must be FQDN
	Hostname *string `pulumi:"hostname"`
	// The IP address to which the PTR record is set
	IpAddress *string `pulumi:"ipAddress"`
	// The wait interval(in seconds) for retrying API call used when SakuraCloud API returns any errors
	RetryInterval *int `pulumi:"retryInterval"`
	// The maximum number of API call retries used when SakuraCloud API returns any errors
	RetryMax *int `pulumi:"retryMax"`
	// The name of zone that the IPv4 PTR will be created (e.g. `is1a`, `tk1a`)
	Zone *string `pulumi:"zone"`
}

type IPv4PtrState struct {
	// The value of the PTR record. This must be FQDN
	Hostname pulumi.StringPtrInput
	// The IP address to which the PTR record is set
	IpAddress pulumi.StringPtrInput
	// The wait interval(in seconds) for retrying API call used when SakuraCloud API returns any errors
	RetryInterval pulumi.IntPtrInput
	// The maximum number of API call retries used when SakuraCloud API returns any errors
	RetryMax pulumi.IntPtrInput
	// The name of zone that the IPv4 PTR will be created (e.g. `is1a`, `tk1a`)
	Zone pulumi.StringPtrInput
}

func (IPv4PtrState) ElementType() reflect.Type {
	return reflect.TypeOf((*ipv4PtrState)(nil)).Elem()
}

type ipv4PtrArgs struct {
	// The value of the PTR record. This must be FQDN
	Hostname string `pulumi:"hostname"`
	// The IP address to which the PTR record is set
	IpAddress string `pulumi:"ipAddress"`
	// The wait interval(in seconds) for retrying API call used when SakuraCloud API returns any errors
	RetryInterval *int `pulumi:"retryInterval"`
	// The maximum number of API call retries used when SakuraCloud API returns any errors
	RetryMax *int `pulumi:"retryMax"`
	// The name of zone that the IPv4 PTR will be created (e.g. `is1a`, `tk1a`)
	Zone *string `pulumi:"zone"`
}

// The set of arguments for constructing a IPv4Ptr resource.
type IPv4PtrArgs struct {
	// The value of the PTR record. This must be FQDN
	Hostname pulumi.StringInput
	// The IP address to which the PTR record is set
	IpAddress pulumi.StringInput
	// The wait interval(in seconds) for retrying API call used when SakuraCloud API returns any errors
	RetryInterval pulumi.IntPtrInput
	// The maximum number of API call retries used when SakuraCloud API returns any errors
	RetryMax pulumi.IntPtrInput
	// The name of zone that the IPv4 PTR will be created (e.g. `is1a`, `tk1a`)
	Zone pulumi.StringPtrInput
}

func (IPv4PtrArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ipv4PtrArgs)(nil)).Elem()
}

