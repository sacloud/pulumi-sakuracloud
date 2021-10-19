// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sakuracloud

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Manages a SakuraCloud Bridge.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-sakuracloud/sdk/go/sakuracloud"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		foobar, err := sakuracloud.NewBridge(ctx, "foobar", &sakuracloud.BridgeArgs{
// 			Description: pulumi.String("description"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = sakuracloud.NewSwitch(ctx, "is1a", &sakuracloud.SwitchArgs{
// 			Description: pulumi.String("description"),
// 			BridgeId:    foobar.ID(),
// 			Zone:        pulumi.String("is1a"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = sakuracloud.NewSwitch(ctx, "is1b", &sakuracloud.SwitchArgs{
// 			Description: pulumi.String("description"),
// 			BridgeId:    foobar.ID(),
// 			Zone:        pulumi.String("is1b"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type Bridge struct {
	pulumi.CustomResourceState

	// The description of the Bridge. The length of this value must be in the range [`1`-`512`].
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The name of the Bridge. The length of this value must be in the range [`1`-`64`].
	Name pulumi.StringOutput `pulumi:"name"`
	// The name of zone that the Bridge will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
	Zone pulumi.StringOutput `pulumi:"zone"`
}

// NewBridge registers a new resource with the given unique name, arguments, and options.
func NewBridge(ctx *pulumi.Context,
	name string, args *BridgeArgs, opts ...pulumi.ResourceOption) (*Bridge, error) {
	if args == nil {
		args = &BridgeArgs{}
	}

	var resource Bridge
	err := ctx.RegisterResource("sakuracloud:index/bridge:Bridge", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetBridge gets an existing Bridge resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetBridge(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *BridgeState, opts ...pulumi.ResourceOption) (*Bridge, error) {
	var resource Bridge
	err := ctx.ReadResource("sakuracloud:index/bridge:Bridge", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Bridge resources.
type bridgeState struct {
	// The description of the Bridge. The length of this value must be in the range [`1`-`512`].
	Description *string `pulumi:"description"`
	// The name of the Bridge. The length of this value must be in the range [`1`-`64`].
	Name *string `pulumi:"name"`
	// The name of zone that the Bridge will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
	Zone *string `pulumi:"zone"`
}

type BridgeState struct {
	// The description of the Bridge. The length of this value must be in the range [`1`-`512`].
	Description pulumi.StringPtrInput
	// The name of the Bridge. The length of this value must be in the range [`1`-`64`].
	Name pulumi.StringPtrInput
	// The name of zone that the Bridge will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
	Zone pulumi.StringPtrInput
}

func (BridgeState) ElementType() reflect.Type {
	return reflect.TypeOf((*bridgeState)(nil)).Elem()
}

type bridgeArgs struct {
	// The description of the Bridge. The length of this value must be in the range [`1`-`512`].
	Description *string `pulumi:"description"`
	// The name of the Bridge. The length of this value must be in the range [`1`-`64`].
	Name *string `pulumi:"name"`
	// The name of zone that the Bridge will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
	Zone *string `pulumi:"zone"`
}

// The set of arguments for constructing a Bridge resource.
type BridgeArgs struct {
	// The description of the Bridge. The length of this value must be in the range [`1`-`512`].
	Description pulumi.StringPtrInput
	// The name of the Bridge. The length of this value must be in the range [`1`-`64`].
	Name pulumi.StringPtrInput
	// The name of zone that the Bridge will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
	Zone pulumi.StringPtrInput
}

func (BridgeArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*bridgeArgs)(nil)).Elem()
}

type BridgeInput interface {
	pulumi.Input

	ToBridgeOutput() BridgeOutput
	ToBridgeOutputWithContext(ctx context.Context) BridgeOutput
}

func (*Bridge) ElementType() reflect.Type {
	return reflect.TypeOf((*Bridge)(nil))
}

func (i *Bridge) ToBridgeOutput() BridgeOutput {
	return i.ToBridgeOutputWithContext(context.Background())
}

func (i *Bridge) ToBridgeOutputWithContext(ctx context.Context) BridgeOutput {
	return pulumi.ToOutputWithContext(ctx, i).(BridgeOutput)
}

func (i *Bridge) ToBridgePtrOutput() BridgePtrOutput {
	return i.ToBridgePtrOutputWithContext(context.Background())
}

func (i *Bridge) ToBridgePtrOutputWithContext(ctx context.Context) BridgePtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(BridgePtrOutput)
}

type BridgePtrInput interface {
	pulumi.Input

	ToBridgePtrOutput() BridgePtrOutput
	ToBridgePtrOutputWithContext(ctx context.Context) BridgePtrOutput
}

type bridgePtrType BridgeArgs

func (*bridgePtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**Bridge)(nil))
}

func (i *bridgePtrType) ToBridgePtrOutput() BridgePtrOutput {
	return i.ToBridgePtrOutputWithContext(context.Background())
}

func (i *bridgePtrType) ToBridgePtrOutputWithContext(ctx context.Context) BridgePtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(BridgePtrOutput)
}

// BridgeArrayInput is an input type that accepts BridgeArray and BridgeArrayOutput values.
// You can construct a concrete instance of `BridgeArrayInput` via:
//
//          BridgeArray{ BridgeArgs{...} }
type BridgeArrayInput interface {
	pulumi.Input

	ToBridgeArrayOutput() BridgeArrayOutput
	ToBridgeArrayOutputWithContext(context.Context) BridgeArrayOutput
}

type BridgeArray []BridgeInput

func (BridgeArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Bridge)(nil)).Elem()
}

func (i BridgeArray) ToBridgeArrayOutput() BridgeArrayOutput {
	return i.ToBridgeArrayOutputWithContext(context.Background())
}

func (i BridgeArray) ToBridgeArrayOutputWithContext(ctx context.Context) BridgeArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(BridgeArrayOutput)
}

// BridgeMapInput is an input type that accepts BridgeMap and BridgeMapOutput values.
// You can construct a concrete instance of `BridgeMapInput` via:
//
//          BridgeMap{ "key": BridgeArgs{...} }
type BridgeMapInput interface {
	pulumi.Input

	ToBridgeMapOutput() BridgeMapOutput
	ToBridgeMapOutputWithContext(context.Context) BridgeMapOutput
}

type BridgeMap map[string]BridgeInput

func (BridgeMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Bridge)(nil)).Elem()
}

func (i BridgeMap) ToBridgeMapOutput() BridgeMapOutput {
	return i.ToBridgeMapOutputWithContext(context.Background())
}

func (i BridgeMap) ToBridgeMapOutputWithContext(ctx context.Context) BridgeMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(BridgeMapOutput)
}

type BridgeOutput struct{ *pulumi.OutputState }

func (BridgeOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Bridge)(nil))
}

func (o BridgeOutput) ToBridgeOutput() BridgeOutput {
	return o
}

func (o BridgeOutput) ToBridgeOutputWithContext(ctx context.Context) BridgeOutput {
	return o
}

func (o BridgeOutput) ToBridgePtrOutput() BridgePtrOutput {
	return o.ToBridgePtrOutputWithContext(context.Background())
}

func (o BridgeOutput) ToBridgePtrOutputWithContext(ctx context.Context) BridgePtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v Bridge) *Bridge {
		return &v
	}).(BridgePtrOutput)
}

type BridgePtrOutput struct{ *pulumi.OutputState }

func (BridgePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Bridge)(nil))
}

func (o BridgePtrOutput) ToBridgePtrOutput() BridgePtrOutput {
	return o
}

func (o BridgePtrOutput) ToBridgePtrOutputWithContext(ctx context.Context) BridgePtrOutput {
	return o
}

func (o BridgePtrOutput) Elem() BridgeOutput {
	return o.ApplyT(func(v *Bridge) Bridge {
		if v != nil {
			return *v
		}
		var ret Bridge
		return ret
	}).(BridgeOutput)
}

type BridgeArrayOutput struct{ *pulumi.OutputState }

func (BridgeArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]Bridge)(nil))
}

func (o BridgeArrayOutput) ToBridgeArrayOutput() BridgeArrayOutput {
	return o
}

func (o BridgeArrayOutput) ToBridgeArrayOutputWithContext(ctx context.Context) BridgeArrayOutput {
	return o
}

func (o BridgeArrayOutput) Index(i pulumi.IntInput) BridgeOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) Bridge {
		return vs[0].([]Bridge)[vs[1].(int)]
	}).(BridgeOutput)
}

type BridgeMapOutput struct{ *pulumi.OutputState }

func (BridgeMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]Bridge)(nil))
}

func (o BridgeMapOutput) ToBridgeMapOutput() BridgeMapOutput {
	return o
}

func (o BridgeMapOutput) ToBridgeMapOutputWithContext(ctx context.Context) BridgeMapOutput {
	return o
}

func (o BridgeMapOutput) MapIndex(k pulumi.StringInput) BridgeOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) Bridge {
		return vs[0].(map[string]Bridge)[vs[1].(string)]
	}).(BridgeOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*BridgeInput)(nil)).Elem(), &Bridge{})
	pulumi.RegisterInputType(reflect.TypeOf((*BridgePtrInput)(nil)).Elem(), &Bridge{})
	pulumi.RegisterInputType(reflect.TypeOf((*BridgeArrayInput)(nil)).Elem(), BridgeArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*BridgeMapInput)(nil)).Elem(), BridgeMap{})
	pulumi.RegisterOutputType(BridgeOutput{})
	pulumi.RegisterOutputType(BridgePtrOutput{})
	pulumi.RegisterOutputType(BridgeArrayOutput{})
	pulumi.RegisterOutputType(BridgeMapOutput{})
}
