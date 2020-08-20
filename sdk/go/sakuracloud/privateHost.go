// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package sakuracloud

import (
	"reflect"

	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

type PrivateHost struct {
	pulumi.CustomResourceState

	// The total number of CPUs assigned to servers on the private host
	AssignedCore pulumi.IntOutput `pulumi:"assignedCore"`
	// The total size of memory assigned to servers on the private host
	AssignedMemory pulumi.IntOutput `pulumi:"assignedMemory"`
	// The class of the PrivateHost. This will be one of [`dynamic`/`ms_windows`]
	Class pulumi.StringPtrOutput `pulumi:"class"`
	// The description of the PrivateHost. The length of this value must be in the range [`1`-`512`]
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The hostname of the private host
	Hostname pulumi.StringOutput `pulumi:"hostname"`
	// The icon id to attach to the PrivateHost
	IconId pulumi.StringPtrOutput `pulumi:"iconId"`
	// The name of the PrivateHost. The length of this value must be in the range [`1`-`64`]
	Name pulumi.StringOutput `pulumi:"name"`
	// Any tags to assign to the PrivateHost
	Tags pulumi.StringArrayOutput `pulumi:"tags"`
	// The name of zone that the PrivateHost will be created (e.g. `is1a`, `tk1a`)
	Zone pulumi.StringOutput `pulumi:"zone"`
}

// NewPrivateHost registers a new resource with the given unique name, arguments, and options.
func NewPrivateHost(ctx *pulumi.Context,
	name string, args *PrivateHostArgs, opts ...pulumi.ResourceOption) (*PrivateHost, error) {
	if args == nil {
		args = &PrivateHostArgs{}
	}
	var resource PrivateHost
	err := ctx.RegisterResource("sakuracloud:index/privateHost:PrivateHost", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetPrivateHost gets an existing PrivateHost resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetPrivateHost(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *PrivateHostState, opts ...pulumi.ResourceOption) (*PrivateHost, error) {
	var resource PrivateHost
	err := ctx.ReadResource("sakuracloud:index/privateHost:PrivateHost", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering PrivateHost resources.
type privateHostState struct {
	// The total number of CPUs assigned to servers on the private host
	AssignedCore *int `pulumi:"assignedCore"`
	// The total size of memory assigned to servers on the private host
	AssignedMemory *int `pulumi:"assignedMemory"`
	// The class of the PrivateHost. This will be one of [`dynamic`/`ms_windows`]
	Class *string `pulumi:"class"`
	// The description of the PrivateHost. The length of this value must be in the range [`1`-`512`]
	Description *string `pulumi:"description"`
	// The hostname of the private host
	Hostname *string `pulumi:"hostname"`
	// The icon id to attach to the PrivateHost
	IconId *string `pulumi:"iconId"`
	// The name of the PrivateHost. The length of this value must be in the range [`1`-`64`]
	Name *string `pulumi:"name"`
	// Any tags to assign to the PrivateHost
	Tags []string `pulumi:"tags"`
	// The name of zone that the PrivateHost will be created (e.g. `is1a`, `tk1a`)
	Zone *string `pulumi:"zone"`
}

type PrivateHostState struct {
	// The total number of CPUs assigned to servers on the private host
	AssignedCore pulumi.IntPtrInput
	// The total size of memory assigned to servers on the private host
	AssignedMemory pulumi.IntPtrInput
	// The class of the PrivateHost. This will be one of [`dynamic`/`ms_windows`]
	Class pulumi.StringPtrInput
	// The description of the PrivateHost. The length of this value must be in the range [`1`-`512`]
	Description pulumi.StringPtrInput
	// The hostname of the private host
	Hostname pulumi.StringPtrInput
	// The icon id to attach to the PrivateHost
	IconId pulumi.StringPtrInput
	// The name of the PrivateHost. The length of this value must be in the range [`1`-`64`]
	Name pulumi.StringPtrInput
	// Any tags to assign to the PrivateHost
	Tags pulumi.StringArrayInput
	// The name of zone that the PrivateHost will be created (e.g. `is1a`, `tk1a`)
	Zone pulumi.StringPtrInput
}

func (PrivateHostState) ElementType() reflect.Type {
	return reflect.TypeOf((*privateHostState)(nil)).Elem()
}

type privateHostArgs struct {
	// The class of the PrivateHost. This will be one of [`dynamic`/`ms_windows`]
	Class *string `pulumi:"class"`
	// The description of the PrivateHost. The length of this value must be in the range [`1`-`512`]
	Description *string `pulumi:"description"`
	// The icon id to attach to the PrivateHost
	IconId *string `pulumi:"iconId"`
	// The name of the PrivateHost. The length of this value must be in the range [`1`-`64`]
	Name *string `pulumi:"name"`
	// Any tags to assign to the PrivateHost
	Tags []string `pulumi:"tags"`
	// The name of zone that the PrivateHost will be created (e.g. `is1a`, `tk1a`)
	Zone *string `pulumi:"zone"`
}

// The set of arguments for constructing a PrivateHost resource.
type PrivateHostArgs struct {
	// The class of the PrivateHost. This will be one of [`dynamic`/`ms_windows`]
	Class pulumi.StringPtrInput
	// The description of the PrivateHost. The length of this value must be in the range [`1`-`512`]
	Description pulumi.StringPtrInput
	// The icon id to attach to the PrivateHost
	IconId pulumi.StringPtrInput
	// The name of the PrivateHost. The length of this value must be in the range [`1`-`64`]
	Name pulumi.StringPtrInput
	// Any tags to assign to the PrivateHost
	Tags pulumi.StringArrayInput
	// The name of zone that the PrivateHost will be created (e.g. `is1a`, `tk1a`)
	Zone pulumi.StringPtrInput
}

func (PrivateHostArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*privateHostArgs)(nil)).Elem()
}
