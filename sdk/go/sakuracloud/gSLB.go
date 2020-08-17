// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package sakuracloud

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

type GSLB struct {
	pulumi.CustomResourceState

	// The description of the GSLB. The length of this value must be in the range [`1`-`512`]
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The FQDN for accessing to the GSLB. This is typically used as value of CNAME record
	Fqdn        pulumi.StringOutput   `pulumi:"fqdn"`
	HealthCheck GSLBHealthCheckOutput `pulumi:"healthCheck"`
	// The icon id to attach to the GSLB
	IconId pulumi.StringPtrOutput `pulumi:"iconId"`
	// The name of the GSLB. The length of this value must be in the range [`1`-`64`]
	Name    pulumi.StringOutput   `pulumi:"name"`
	Servers GSLBServerArrayOutput `pulumi:"servers"`
	// The IP address of the SorryServer. This will be used when all servers are down
	SorryServer pulumi.StringPtrOutput `pulumi:"sorryServer"`
	// Any tags to assign to the GSLB
	Tags pulumi.StringArrayOutput `pulumi:"tags"`
	// The flag to enable weighted load-balancing
	Weighted pulumi.BoolPtrOutput `pulumi:"weighted"`
}

// NewGSLB registers a new resource with the given unique name, arguments, and options.
func NewGSLB(ctx *pulumi.Context,
	name string, args *GSLBArgs, opts ...pulumi.ResourceOption) (*GSLB, error) {
	if args == nil || args.HealthCheck == nil {
		return nil, errors.New("missing required argument 'HealthCheck'")
	}
	if args == nil {
		args = &GSLBArgs{}
	}
	var resource GSLB
	err := ctx.RegisterResource("sakuracloud:index/gSLB:GSLB", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetGSLB gets an existing GSLB resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetGSLB(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *GSLBState, opts ...pulumi.ResourceOption) (*GSLB, error) {
	var resource GSLB
	err := ctx.ReadResource("sakuracloud:index/gSLB:GSLB", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering GSLB resources.
type gslbState struct {
	// The description of the GSLB. The length of this value must be in the range [`1`-`512`]
	Description *string `pulumi:"description"`
	// The FQDN for accessing to the GSLB. This is typically used as value of CNAME record
	Fqdn        *string          `pulumi:"fqdn"`
	HealthCheck *GSLBHealthCheck `pulumi:"healthCheck"`
	// The icon id to attach to the GSLB
	IconId *string `pulumi:"iconId"`
	// The name of the GSLB. The length of this value must be in the range [`1`-`64`]
	Name    *string      `pulumi:"name"`
	Servers []GSLBServer `pulumi:"servers"`
	// The IP address of the SorryServer. This will be used when all servers are down
	SorryServer *string `pulumi:"sorryServer"`
	// Any tags to assign to the GSLB
	Tags []string `pulumi:"tags"`
	// The flag to enable weighted load-balancing
	Weighted *bool `pulumi:"weighted"`
}

type GSLBState struct {
	// The description of the GSLB. The length of this value must be in the range [`1`-`512`]
	Description pulumi.StringPtrInput
	// The FQDN for accessing to the GSLB. This is typically used as value of CNAME record
	Fqdn        pulumi.StringPtrInput
	HealthCheck GSLBHealthCheckPtrInput
	// The icon id to attach to the GSLB
	IconId pulumi.StringPtrInput
	// The name of the GSLB. The length of this value must be in the range [`1`-`64`]
	Name    pulumi.StringPtrInput
	Servers GSLBServerArrayInput
	// The IP address of the SorryServer. This will be used when all servers are down
	SorryServer pulumi.StringPtrInput
	// Any tags to assign to the GSLB
	Tags pulumi.StringArrayInput
	// The flag to enable weighted load-balancing
	Weighted pulumi.BoolPtrInput
}

func (GSLBState) ElementType() reflect.Type {
	return reflect.TypeOf((*gslbState)(nil)).Elem()
}

type gslbArgs struct {
	// The description of the GSLB. The length of this value must be in the range [`1`-`512`]
	Description *string         `pulumi:"description"`
	HealthCheck GSLBHealthCheck `pulumi:"healthCheck"`
	// The icon id to attach to the GSLB
	IconId *string `pulumi:"iconId"`
	// The name of the GSLB. The length of this value must be in the range [`1`-`64`]
	Name    *string      `pulumi:"name"`
	Servers []GSLBServer `pulumi:"servers"`
	// The IP address of the SorryServer. This will be used when all servers are down
	SorryServer *string `pulumi:"sorryServer"`
	// Any tags to assign to the GSLB
	Tags []string `pulumi:"tags"`
	// The flag to enable weighted load-balancing
	Weighted *bool `pulumi:"weighted"`
}

// The set of arguments for constructing a GSLB resource.
type GSLBArgs struct {
	// The description of the GSLB. The length of this value must be in the range [`1`-`512`]
	Description pulumi.StringPtrInput
	HealthCheck GSLBHealthCheckInput
	// The icon id to attach to the GSLB
	IconId pulumi.StringPtrInput
	// The name of the GSLB. The length of this value must be in the range [`1`-`64`]
	Name    pulumi.StringPtrInput
	Servers GSLBServerArrayInput
	// The IP address of the SorryServer. This will be used when all servers are down
	SorryServer pulumi.StringPtrInput
	// Any tags to assign to the GSLB
	Tags pulumi.StringArrayInput
	// The flag to enable weighted load-balancing
	Weighted pulumi.BoolPtrInput
}

func (GSLBArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*gslbArgs)(nil)).Elem()
}
