// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package sakuracloud

import (
	"reflect"

	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

type Icon struct {
	pulumi.CustomResourceState

	// The base64 encoded content to upload to as the Icon. This conflicts with [`source`]
	Base64content pulumi.StringPtrOutput `pulumi:"base64content"`
	// The name of the Icon. The length of this value must be in the range [`1`-`64`]
	Name pulumi.StringOutput `pulumi:"name"`
	// The file path to upload to as the Icon. This conflicts with [`base64content`]
	Source pulumi.StringPtrOutput `pulumi:"source"`
	// Any tags to assign to the Icon
	Tags pulumi.StringArrayOutput `pulumi:"tags"`
	// The URL for getting the icon's raw data
	Url pulumi.StringOutput `pulumi:"url"`
}

// NewIcon registers a new resource with the given unique name, arguments, and options.
func NewIcon(ctx *pulumi.Context,
	name string, args *IconArgs, opts ...pulumi.ResourceOption) (*Icon, error) {
	if args == nil {
		args = &IconArgs{}
	}
	var resource Icon
	err := ctx.RegisterResource("sakuracloud:index/icon:Icon", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetIcon gets an existing Icon resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetIcon(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *IconState, opts ...pulumi.ResourceOption) (*Icon, error) {
	var resource Icon
	err := ctx.ReadResource("sakuracloud:index/icon:Icon", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Icon resources.
type iconState struct {
	// The base64 encoded content to upload to as the Icon. This conflicts with [`source`]
	Base64content *string `pulumi:"base64content"`
	// The name of the Icon. The length of this value must be in the range [`1`-`64`]
	Name *string `pulumi:"name"`
	// The file path to upload to as the Icon. This conflicts with [`base64content`]
	Source *string `pulumi:"source"`
	// Any tags to assign to the Icon
	Tags []string `pulumi:"tags"`
	// The URL for getting the icon's raw data
	Url *string `pulumi:"url"`
}

type IconState struct {
	// The base64 encoded content to upload to as the Icon. This conflicts with [`source`]
	Base64content pulumi.StringPtrInput
	// The name of the Icon. The length of this value must be in the range [`1`-`64`]
	Name pulumi.StringPtrInput
	// The file path to upload to as the Icon. This conflicts with [`base64content`]
	Source pulumi.StringPtrInput
	// Any tags to assign to the Icon
	Tags pulumi.StringArrayInput
	// The URL for getting the icon's raw data
	Url pulumi.StringPtrInput
}

func (IconState) ElementType() reflect.Type {
	return reflect.TypeOf((*iconState)(nil)).Elem()
}

type iconArgs struct {
	// The base64 encoded content to upload to as the Icon. This conflicts with [`source`]
	Base64content *string `pulumi:"base64content"`
	// The name of the Icon. The length of this value must be in the range [`1`-`64`]
	Name *string `pulumi:"name"`
	// The file path to upload to as the Icon. This conflicts with [`base64content`]
	Source *string `pulumi:"source"`
	// Any tags to assign to the Icon
	Tags []string `pulumi:"tags"`
}

// The set of arguments for constructing a Icon resource.
type IconArgs struct {
	// The base64 encoded content to upload to as the Icon. This conflicts with [`source`]
	Base64content pulumi.StringPtrInput
	// The name of the Icon. The length of this value must be in the range [`1`-`64`]
	Name pulumi.StringPtrInput
	// The file path to upload to as the Icon. This conflicts with [`base64content`]
	Source pulumi.StringPtrInput
	// Any tags to assign to the Icon
	Tags pulumi.StringArrayInput
}

func (IconArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*iconArgs)(nil)).Elem()
}
