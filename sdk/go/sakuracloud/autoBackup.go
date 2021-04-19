// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sakuracloud

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages a SakuraCloud Auto Backup.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-sakuracloud/sdk/go/sakuracloud"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		foobarDisk, err := sakuracloud.NewDisk(ctx, "foobarDisk", nil)
// 		if err != nil {
// 			return err
// 		}
// 		_, err = sakuracloud.NewAutoBackup(ctx, "foobarAutoBackup", &sakuracloud.AutoBackupArgs{
// 			DiskId: foobarDisk.ID(),
// 			Weekdays: pulumi.StringArray{
// 				pulumi.String("mon"),
// 				pulumi.String("tue"),
// 				pulumi.String("wed"),
// 				pulumi.String("thu"),
// 				pulumi.String("fri"),
// 				pulumi.String("sat"),
// 				pulumi.String("sun"),
// 			},
// 			MaxBackupNum: pulumi.Int(5),
// 			Description:  pulumi.String("description"),
// 			Tags: pulumi.StringArray{
// 				pulumi.String("tag1"),
// 				pulumi.String("tag2"),
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type AutoBackup struct {
	pulumi.CustomResourceState

	// The description of the AutoBackup. The length of this value must be in the range [`1`-`512`].
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The disk id to backed up. Changing this forces a new resource to be created.
	DiskId pulumi.StringOutput `pulumi:"diskId"`
	// The icon id to attach to the AutoBackup.
	IconId pulumi.StringPtrOutput `pulumi:"iconId"`
	// The number backup files to keep. This must be in the range [`1`-`10`]. Default:`1`.
	MaxBackupNum pulumi.IntPtrOutput `pulumi:"maxBackupNum"`
	// The name of the AutoBackup. The length of this value must be in the range [`1`-`64`].
	Name pulumi.StringOutput `pulumi:"name"`
	// Any tags to assign to the AutoBackup.
	Tags pulumi.StringArrayOutput `pulumi:"tags"`
	// A list of weekdays to backed up. The values in the list must be in [`sun`/`mon`/`tue`/`wed`/`thu`/`fri`/`sat`].
	Weekdays pulumi.StringArrayOutput `pulumi:"weekdays"`
	// The name of zone that the AutoBackup will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
	Zone pulumi.StringOutput `pulumi:"zone"`
}

// NewAutoBackup registers a new resource with the given unique name, arguments, and options.
func NewAutoBackup(ctx *pulumi.Context,
	name string, args *AutoBackupArgs, opts ...pulumi.ResourceOption) (*AutoBackup, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DiskId == nil {
		return nil, errors.New("invalid value for required argument 'DiskId'")
	}
	if args.Weekdays == nil {
		return nil, errors.New("invalid value for required argument 'Weekdays'")
	}
	var resource AutoBackup
	err := ctx.RegisterResource("sakuracloud:index/autoBackup:AutoBackup", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetAutoBackup gets an existing AutoBackup resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetAutoBackup(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *AutoBackupState, opts ...pulumi.ResourceOption) (*AutoBackup, error) {
	var resource AutoBackup
	err := ctx.ReadResource("sakuracloud:index/autoBackup:AutoBackup", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering AutoBackup resources.
type autoBackupState struct {
	// The description of the AutoBackup. The length of this value must be in the range [`1`-`512`].
	Description *string `pulumi:"description"`
	// The disk id to backed up. Changing this forces a new resource to be created.
	DiskId *string `pulumi:"diskId"`
	// The icon id to attach to the AutoBackup.
	IconId *string `pulumi:"iconId"`
	// The number backup files to keep. This must be in the range [`1`-`10`]. Default:`1`.
	MaxBackupNum *int `pulumi:"maxBackupNum"`
	// The name of the AutoBackup. The length of this value must be in the range [`1`-`64`].
	Name *string `pulumi:"name"`
	// Any tags to assign to the AutoBackup.
	Tags []string `pulumi:"tags"`
	// A list of weekdays to backed up. The values in the list must be in [`sun`/`mon`/`tue`/`wed`/`thu`/`fri`/`sat`].
	Weekdays []string `pulumi:"weekdays"`
	// The name of zone that the AutoBackup will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
	Zone *string `pulumi:"zone"`
}

type AutoBackupState struct {
	// The description of the AutoBackup. The length of this value must be in the range [`1`-`512`].
	Description pulumi.StringPtrInput
	// The disk id to backed up. Changing this forces a new resource to be created.
	DiskId pulumi.StringPtrInput
	// The icon id to attach to the AutoBackup.
	IconId pulumi.StringPtrInput
	// The number backup files to keep. This must be in the range [`1`-`10`]. Default:`1`.
	MaxBackupNum pulumi.IntPtrInput
	// The name of the AutoBackup. The length of this value must be in the range [`1`-`64`].
	Name pulumi.StringPtrInput
	// Any tags to assign to the AutoBackup.
	Tags pulumi.StringArrayInput
	// A list of weekdays to backed up. The values in the list must be in [`sun`/`mon`/`tue`/`wed`/`thu`/`fri`/`sat`].
	Weekdays pulumi.StringArrayInput
	// The name of zone that the AutoBackup will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
	Zone pulumi.StringPtrInput
}

func (AutoBackupState) ElementType() reflect.Type {
	return reflect.TypeOf((*autoBackupState)(nil)).Elem()
}

type autoBackupArgs struct {
	// The description of the AutoBackup. The length of this value must be in the range [`1`-`512`].
	Description *string `pulumi:"description"`
	// The disk id to backed up. Changing this forces a new resource to be created.
	DiskId string `pulumi:"diskId"`
	// The icon id to attach to the AutoBackup.
	IconId *string `pulumi:"iconId"`
	// The number backup files to keep. This must be in the range [`1`-`10`]. Default:`1`.
	MaxBackupNum *int `pulumi:"maxBackupNum"`
	// The name of the AutoBackup. The length of this value must be in the range [`1`-`64`].
	Name *string `pulumi:"name"`
	// Any tags to assign to the AutoBackup.
	Tags []string `pulumi:"tags"`
	// A list of weekdays to backed up. The values in the list must be in [`sun`/`mon`/`tue`/`wed`/`thu`/`fri`/`sat`].
	Weekdays []string `pulumi:"weekdays"`
	// The name of zone that the AutoBackup will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
	Zone *string `pulumi:"zone"`
}

// The set of arguments for constructing a AutoBackup resource.
type AutoBackupArgs struct {
	// The description of the AutoBackup. The length of this value must be in the range [`1`-`512`].
	Description pulumi.StringPtrInput
	// The disk id to backed up. Changing this forces a new resource to be created.
	DiskId pulumi.StringInput
	// The icon id to attach to the AutoBackup.
	IconId pulumi.StringPtrInput
	// The number backup files to keep. This must be in the range [`1`-`10`]. Default:`1`.
	MaxBackupNum pulumi.IntPtrInput
	// The name of the AutoBackup. The length of this value must be in the range [`1`-`64`].
	Name pulumi.StringPtrInput
	// Any tags to assign to the AutoBackup.
	Tags pulumi.StringArrayInput
	// A list of weekdays to backed up. The values in the list must be in [`sun`/`mon`/`tue`/`wed`/`thu`/`fri`/`sat`].
	Weekdays pulumi.StringArrayInput
	// The name of zone that the AutoBackup will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
	Zone pulumi.StringPtrInput
}

func (AutoBackupArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*autoBackupArgs)(nil)).Elem()
}

type AutoBackupInput interface {
	pulumi.Input

	ToAutoBackupOutput() AutoBackupOutput
	ToAutoBackupOutputWithContext(ctx context.Context) AutoBackupOutput
}

func (*AutoBackup) ElementType() reflect.Type {
	return reflect.TypeOf((*AutoBackup)(nil))
}

func (i *AutoBackup) ToAutoBackupOutput() AutoBackupOutput {
	return i.ToAutoBackupOutputWithContext(context.Background())
}

func (i *AutoBackup) ToAutoBackupOutputWithContext(ctx context.Context) AutoBackupOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AutoBackupOutput)
}

func (i *AutoBackup) ToAutoBackupPtrOutput() AutoBackupPtrOutput {
	return i.ToAutoBackupPtrOutputWithContext(context.Background())
}

func (i *AutoBackup) ToAutoBackupPtrOutputWithContext(ctx context.Context) AutoBackupPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AutoBackupPtrOutput)
}

type AutoBackupPtrInput interface {
	pulumi.Input

	ToAutoBackupPtrOutput() AutoBackupPtrOutput
	ToAutoBackupPtrOutputWithContext(ctx context.Context) AutoBackupPtrOutput
}

type autoBackupPtrType AutoBackupArgs

func (*autoBackupPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**AutoBackup)(nil))
}

func (i *autoBackupPtrType) ToAutoBackupPtrOutput() AutoBackupPtrOutput {
	return i.ToAutoBackupPtrOutputWithContext(context.Background())
}

func (i *autoBackupPtrType) ToAutoBackupPtrOutputWithContext(ctx context.Context) AutoBackupPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AutoBackupPtrOutput)
}

// AutoBackupArrayInput is an input type that accepts AutoBackupArray and AutoBackupArrayOutput values.
// You can construct a concrete instance of `AutoBackupArrayInput` via:
//
//          AutoBackupArray{ AutoBackupArgs{...} }
type AutoBackupArrayInput interface {
	pulumi.Input

	ToAutoBackupArrayOutput() AutoBackupArrayOutput
	ToAutoBackupArrayOutputWithContext(context.Context) AutoBackupArrayOutput
}

type AutoBackupArray []AutoBackupInput

func (AutoBackupArray) ElementType() reflect.Type {
	return reflect.TypeOf(([]*AutoBackup)(nil))
}

func (i AutoBackupArray) ToAutoBackupArrayOutput() AutoBackupArrayOutput {
	return i.ToAutoBackupArrayOutputWithContext(context.Background())
}

func (i AutoBackupArray) ToAutoBackupArrayOutputWithContext(ctx context.Context) AutoBackupArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AutoBackupArrayOutput)
}

// AutoBackupMapInput is an input type that accepts AutoBackupMap and AutoBackupMapOutput values.
// You can construct a concrete instance of `AutoBackupMapInput` via:
//
//          AutoBackupMap{ "key": AutoBackupArgs{...} }
type AutoBackupMapInput interface {
	pulumi.Input

	ToAutoBackupMapOutput() AutoBackupMapOutput
	ToAutoBackupMapOutputWithContext(context.Context) AutoBackupMapOutput
}

type AutoBackupMap map[string]AutoBackupInput

func (AutoBackupMap) ElementType() reflect.Type {
	return reflect.TypeOf((map[string]*AutoBackup)(nil))
}

func (i AutoBackupMap) ToAutoBackupMapOutput() AutoBackupMapOutput {
	return i.ToAutoBackupMapOutputWithContext(context.Background())
}

func (i AutoBackupMap) ToAutoBackupMapOutputWithContext(ctx context.Context) AutoBackupMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AutoBackupMapOutput)
}

type AutoBackupOutput struct {
	*pulumi.OutputState
}

func (AutoBackupOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*AutoBackup)(nil))
}

func (o AutoBackupOutput) ToAutoBackupOutput() AutoBackupOutput {
	return o
}

func (o AutoBackupOutput) ToAutoBackupOutputWithContext(ctx context.Context) AutoBackupOutput {
	return o
}

func (o AutoBackupOutput) ToAutoBackupPtrOutput() AutoBackupPtrOutput {
	return o.ToAutoBackupPtrOutputWithContext(context.Background())
}

func (o AutoBackupOutput) ToAutoBackupPtrOutputWithContext(ctx context.Context) AutoBackupPtrOutput {
	return o.ApplyT(func(v AutoBackup) *AutoBackup {
		return &v
	}).(AutoBackupPtrOutput)
}

type AutoBackupPtrOutput struct {
	*pulumi.OutputState
}

func (AutoBackupPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**AutoBackup)(nil))
}

func (o AutoBackupPtrOutput) ToAutoBackupPtrOutput() AutoBackupPtrOutput {
	return o
}

func (o AutoBackupPtrOutput) ToAutoBackupPtrOutputWithContext(ctx context.Context) AutoBackupPtrOutput {
	return o
}

type AutoBackupArrayOutput struct{ *pulumi.OutputState }

func (AutoBackupArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]AutoBackup)(nil))
}

func (o AutoBackupArrayOutput) ToAutoBackupArrayOutput() AutoBackupArrayOutput {
	return o
}

func (o AutoBackupArrayOutput) ToAutoBackupArrayOutputWithContext(ctx context.Context) AutoBackupArrayOutput {
	return o
}

func (o AutoBackupArrayOutput) Index(i pulumi.IntInput) AutoBackupOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) AutoBackup {
		return vs[0].([]AutoBackup)[vs[1].(int)]
	}).(AutoBackupOutput)
}

type AutoBackupMapOutput struct{ *pulumi.OutputState }

func (AutoBackupMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]AutoBackup)(nil))
}

func (o AutoBackupMapOutput) ToAutoBackupMapOutput() AutoBackupMapOutput {
	return o
}

func (o AutoBackupMapOutput) ToAutoBackupMapOutputWithContext(ctx context.Context) AutoBackupMapOutput {
	return o
}

func (o AutoBackupMapOutput) MapIndex(k pulumi.StringInput) AutoBackupOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) AutoBackup {
		return vs[0].(map[string]AutoBackup)[vs[1].(string)]
	}).(AutoBackupOutput)
}

func init() {
	pulumi.RegisterOutputType(AutoBackupOutput{})
	pulumi.RegisterOutputType(AutoBackupPtrOutput{})
	pulumi.RegisterOutputType(AutoBackupArrayOutput{})
	pulumi.RegisterOutputType(AutoBackupMapOutput{})
}
