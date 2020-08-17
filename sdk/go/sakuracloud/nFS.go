// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package sakuracloud

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

type NFS struct {
	pulumi.CustomResourceState

	// The description of the NFS. The length of this value must be in the range [`1`-`512`]
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The icon id to attach to the NFS
	IconId pulumi.StringPtrOutput `pulumi:"iconId"`
	// The name of the NFS. The length of this value must be in the range [`1`-`64`]
	Name             pulumi.StringOutput       `pulumi:"name"`
	NetworkInterface NFSNetworkInterfaceOutput `pulumi:"networkInterface"`
	// The plan name of the NFS. This must be one of [`hdd`/`ssd`]
	Plan pulumi.StringPtrOutput `pulumi:"plan"`
	// The size of NFS in GiB
	Size pulumi.IntPtrOutput `pulumi:"size"`
	// Any tags to assign to the NFS
	Tags pulumi.StringArrayOutput `pulumi:"tags"`
	// The name of zone that the NFS will be created (e.g. `is1a`, `tk1a`)
	Zone pulumi.StringOutput `pulumi:"zone"`
}

// NewNFS registers a new resource with the given unique name, arguments, and options.
func NewNFS(ctx *pulumi.Context,
	name string, args *NFSArgs, opts ...pulumi.ResourceOption) (*NFS, error) {
	if args == nil || args.NetworkInterface == nil {
		return nil, errors.New("missing required argument 'NetworkInterface'")
	}
	if args == nil {
		args = &NFSArgs{}
	}
	var resource NFS
	err := ctx.RegisterResource("sakuracloud:index/nFS:NFS", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetNFS gets an existing NFS resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetNFS(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *NFSState, opts ...pulumi.ResourceOption) (*NFS, error) {
	var resource NFS
	err := ctx.ReadResource("sakuracloud:index/nFS:NFS", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering NFS resources.
type nfsState struct {
	// The description of the NFS. The length of this value must be in the range [`1`-`512`]
	Description *string `pulumi:"description"`
	// The icon id to attach to the NFS
	IconId *string `pulumi:"iconId"`
	// The name of the NFS. The length of this value must be in the range [`1`-`64`]
	Name             *string              `pulumi:"name"`
	NetworkInterface *NFSNetworkInterface `pulumi:"networkInterface"`
	// The plan name of the NFS. This must be one of [`hdd`/`ssd`]
	Plan *string `pulumi:"plan"`
	// The size of NFS in GiB
	Size *int `pulumi:"size"`
	// Any tags to assign to the NFS
	Tags []string `pulumi:"tags"`
	// The name of zone that the NFS will be created (e.g. `is1a`, `tk1a`)
	Zone *string `pulumi:"zone"`
}

type NFSState struct {
	// The description of the NFS. The length of this value must be in the range [`1`-`512`]
	Description pulumi.StringPtrInput
	// The icon id to attach to the NFS
	IconId pulumi.StringPtrInput
	// The name of the NFS. The length of this value must be in the range [`1`-`64`]
	Name             pulumi.StringPtrInput
	NetworkInterface NFSNetworkInterfacePtrInput
	// The plan name of the NFS. This must be one of [`hdd`/`ssd`]
	Plan pulumi.StringPtrInput
	// The size of NFS in GiB
	Size pulumi.IntPtrInput
	// Any tags to assign to the NFS
	Tags pulumi.StringArrayInput
	// The name of zone that the NFS will be created (e.g. `is1a`, `tk1a`)
	Zone pulumi.StringPtrInput
}

func (NFSState) ElementType() reflect.Type {
	return reflect.TypeOf((*nfsState)(nil)).Elem()
}

type nfsArgs struct {
	// The description of the NFS. The length of this value must be in the range [`1`-`512`]
	Description *string `pulumi:"description"`
	// The icon id to attach to the NFS
	IconId *string `pulumi:"iconId"`
	// The name of the NFS. The length of this value must be in the range [`1`-`64`]
	Name             *string             `pulumi:"name"`
	NetworkInterface NFSNetworkInterface `pulumi:"networkInterface"`
	// The plan name of the NFS. This must be one of [`hdd`/`ssd`]
	Plan *string `pulumi:"plan"`
	// The size of NFS in GiB
	Size *int `pulumi:"size"`
	// Any tags to assign to the NFS
	Tags []string `pulumi:"tags"`
	// The name of zone that the NFS will be created (e.g. `is1a`, `tk1a`)
	Zone *string `pulumi:"zone"`
}

// The set of arguments for constructing a NFS resource.
type NFSArgs struct {
	// The description of the NFS. The length of this value must be in the range [`1`-`512`]
	Description pulumi.StringPtrInput
	// The icon id to attach to the NFS
	IconId pulumi.StringPtrInput
	// The name of the NFS. The length of this value must be in the range [`1`-`64`]
	Name             pulumi.StringPtrInput
	NetworkInterface NFSNetworkInterfaceInput
	// The plan name of the NFS. This must be one of [`hdd`/`ssd`]
	Plan pulumi.StringPtrInput
	// The size of NFS in GiB
	Size pulumi.IntPtrInput
	// Any tags to assign to the NFS
	Tags pulumi.StringArrayInput
	// The name of zone that the NFS will be created (e.g. `is1a`, `tk1a`)
	Zone pulumi.StringPtrInput
}

func (NFSArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*nfsArgs)(nil)).Elem()
}
