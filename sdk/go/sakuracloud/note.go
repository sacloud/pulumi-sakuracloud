// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sakuracloud

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Manages a SakuraCloud Note.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"io/ioutil"
//
// 	"github.com/pulumi/pulumi-sakuracloud/sdk/go/sakuracloud"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// )
//
// func readFileOrPanic(path string) pulumi.StringPtrInput {
// 	data, err := ioutil.ReadFile(path)
// 	if err != nil {
// 		panic(err.Error())
// 	}
// 	return pulumi.String(string(data))
// }
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := sakuracloud.NewNote(ctx, "foobar", &sakuracloud.NoteArgs{
// 			Content: readFileOrPanic("startup-script.sh"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type Note struct {
	pulumi.CustomResourceState

	// The class of the Note. This must be one of `shell`/`yamlCloudConfig`. Default:`shell`.
	Class pulumi.StringPtrOutput `pulumi:"class"`
	// The content of the Note. This must be specified as a shell script or as a cloud-config.
	Content pulumi.StringOutput `pulumi:"content"`
	// The description of the Note. This will be computed from special tags within body of `content`.
	Description pulumi.StringOutput `pulumi:"description"`
	// The icon id to attach to the Note.
	IconId pulumi.StringPtrOutput `pulumi:"iconId"`
	// The name of the Note. The length of this value must be in the range [`1`-`64`].
	Name pulumi.StringOutput `pulumi:"name"`
	// Any tags to assign to the Note.
	Tags pulumi.StringArrayOutput `pulumi:"tags"`
}

// NewNote registers a new resource with the given unique name, arguments, and options.
func NewNote(ctx *pulumi.Context,
	name string, args *NoteArgs, opts ...pulumi.ResourceOption) (*Note, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Content == nil {
		return nil, errors.New("invalid value for required argument 'Content'")
	}
	var resource Note
	err := ctx.RegisterResource("sakuracloud:index/note:Note", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetNote gets an existing Note resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetNote(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *NoteState, opts ...pulumi.ResourceOption) (*Note, error) {
	var resource Note
	err := ctx.ReadResource("sakuracloud:index/note:Note", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Note resources.
type noteState struct {
	// The class of the Note. This must be one of `shell`/`yamlCloudConfig`. Default:`shell`.
	Class *string `pulumi:"class"`
	// The content of the Note. This must be specified as a shell script or as a cloud-config.
	Content *string `pulumi:"content"`
	// The description of the Note. This will be computed from special tags within body of `content`.
	Description *string `pulumi:"description"`
	// The icon id to attach to the Note.
	IconId *string `pulumi:"iconId"`
	// The name of the Note. The length of this value must be in the range [`1`-`64`].
	Name *string `pulumi:"name"`
	// Any tags to assign to the Note.
	Tags []string `pulumi:"tags"`
}

type NoteState struct {
	// The class of the Note. This must be one of `shell`/`yamlCloudConfig`. Default:`shell`.
	Class pulumi.StringPtrInput
	// The content of the Note. This must be specified as a shell script or as a cloud-config.
	Content pulumi.StringPtrInput
	// The description of the Note. This will be computed from special tags within body of `content`.
	Description pulumi.StringPtrInput
	// The icon id to attach to the Note.
	IconId pulumi.StringPtrInput
	// The name of the Note. The length of this value must be in the range [`1`-`64`].
	Name pulumi.StringPtrInput
	// Any tags to assign to the Note.
	Tags pulumi.StringArrayInput
}

func (NoteState) ElementType() reflect.Type {
	return reflect.TypeOf((*noteState)(nil)).Elem()
}

type noteArgs struct {
	// The class of the Note. This must be one of `shell`/`yamlCloudConfig`. Default:`shell`.
	Class *string `pulumi:"class"`
	// The content of the Note. This must be specified as a shell script or as a cloud-config.
	Content string `pulumi:"content"`
	// The icon id to attach to the Note.
	IconId *string `pulumi:"iconId"`
	// The name of the Note. The length of this value must be in the range [`1`-`64`].
	Name *string `pulumi:"name"`
	// Any tags to assign to the Note.
	Tags []string `pulumi:"tags"`
}

// The set of arguments for constructing a Note resource.
type NoteArgs struct {
	// The class of the Note. This must be one of `shell`/`yamlCloudConfig`. Default:`shell`.
	Class pulumi.StringPtrInput
	// The content of the Note. This must be specified as a shell script or as a cloud-config.
	Content pulumi.StringInput
	// The icon id to attach to the Note.
	IconId pulumi.StringPtrInput
	// The name of the Note. The length of this value must be in the range [`1`-`64`].
	Name pulumi.StringPtrInput
	// Any tags to assign to the Note.
	Tags pulumi.StringArrayInput
}

func (NoteArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*noteArgs)(nil)).Elem()
}

type NoteInput interface {
	pulumi.Input

	ToNoteOutput() NoteOutput
	ToNoteOutputWithContext(ctx context.Context) NoteOutput
}

func (*Note) ElementType() reflect.Type {
	return reflect.TypeOf((*Note)(nil))
}

func (i *Note) ToNoteOutput() NoteOutput {
	return i.ToNoteOutputWithContext(context.Background())
}

func (i *Note) ToNoteOutputWithContext(ctx context.Context) NoteOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NoteOutput)
}

func (i *Note) ToNotePtrOutput() NotePtrOutput {
	return i.ToNotePtrOutputWithContext(context.Background())
}

func (i *Note) ToNotePtrOutputWithContext(ctx context.Context) NotePtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NotePtrOutput)
}

type NotePtrInput interface {
	pulumi.Input

	ToNotePtrOutput() NotePtrOutput
	ToNotePtrOutputWithContext(ctx context.Context) NotePtrOutput
}

type notePtrType NoteArgs

func (*notePtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**Note)(nil))
}

func (i *notePtrType) ToNotePtrOutput() NotePtrOutput {
	return i.ToNotePtrOutputWithContext(context.Background())
}

func (i *notePtrType) ToNotePtrOutputWithContext(ctx context.Context) NotePtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NotePtrOutput)
}

// NoteArrayInput is an input type that accepts NoteArray and NoteArrayOutput values.
// You can construct a concrete instance of `NoteArrayInput` via:
//
//          NoteArray{ NoteArgs{...} }
type NoteArrayInput interface {
	pulumi.Input

	ToNoteArrayOutput() NoteArrayOutput
	ToNoteArrayOutputWithContext(context.Context) NoteArrayOutput
}

type NoteArray []NoteInput

func (NoteArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Note)(nil)).Elem()
}

func (i NoteArray) ToNoteArrayOutput() NoteArrayOutput {
	return i.ToNoteArrayOutputWithContext(context.Background())
}

func (i NoteArray) ToNoteArrayOutputWithContext(ctx context.Context) NoteArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NoteArrayOutput)
}

// NoteMapInput is an input type that accepts NoteMap and NoteMapOutput values.
// You can construct a concrete instance of `NoteMapInput` via:
//
//          NoteMap{ "key": NoteArgs{...} }
type NoteMapInput interface {
	pulumi.Input

	ToNoteMapOutput() NoteMapOutput
	ToNoteMapOutputWithContext(context.Context) NoteMapOutput
}

type NoteMap map[string]NoteInput

func (NoteMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Note)(nil)).Elem()
}

func (i NoteMap) ToNoteMapOutput() NoteMapOutput {
	return i.ToNoteMapOutputWithContext(context.Background())
}

func (i NoteMap) ToNoteMapOutputWithContext(ctx context.Context) NoteMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NoteMapOutput)
}

type NoteOutput struct{ *pulumi.OutputState }

func (NoteOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Note)(nil))
}

func (o NoteOutput) ToNoteOutput() NoteOutput {
	return o
}

func (o NoteOutput) ToNoteOutputWithContext(ctx context.Context) NoteOutput {
	return o
}

func (o NoteOutput) ToNotePtrOutput() NotePtrOutput {
	return o.ToNotePtrOutputWithContext(context.Background())
}

func (o NoteOutput) ToNotePtrOutputWithContext(ctx context.Context) NotePtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v Note) *Note {
		return &v
	}).(NotePtrOutput)
}

type NotePtrOutput struct{ *pulumi.OutputState }

func (NotePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Note)(nil))
}

func (o NotePtrOutput) ToNotePtrOutput() NotePtrOutput {
	return o
}

func (o NotePtrOutput) ToNotePtrOutputWithContext(ctx context.Context) NotePtrOutput {
	return o
}

func (o NotePtrOutput) Elem() NoteOutput {
	return o.ApplyT(func(v *Note) Note {
		if v != nil {
			return *v
		}
		var ret Note
		return ret
	}).(NoteOutput)
}

type NoteArrayOutput struct{ *pulumi.OutputState }

func (NoteArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]Note)(nil))
}

func (o NoteArrayOutput) ToNoteArrayOutput() NoteArrayOutput {
	return o
}

func (o NoteArrayOutput) ToNoteArrayOutputWithContext(ctx context.Context) NoteArrayOutput {
	return o
}

func (o NoteArrayOutput) Index(i pulumi.IntInput) NoteOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) Note {
		return vs[0].([]Note)[vs[1].(int)]
	}).(NoteOutput)
}

type NoteMapOutput struct{ *pulumi.OutputState }

func (NoteMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]Note)(nil))
}

func (o NoteMapOutput) ToNoteMapOutput() NoteMapOutput {
	return o
}

func (o NoteMapOutput) ToNoteMapOutputWithContext(ctx context.Context) NoteMapOutput {
	return o
}

func (o NoteMapOutput) MapIndex(k pulumi.StringInput) NoteOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) Note {
		return vs[0].(map[string]Note)[vs[1].(string)]
	}).(NoteOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*NoteInput)(nil)).Elem(), &Note{})
	pulumi.RegisterInputType(reflect.TypeOf((*NotePtrInput)(nil)).Elem(), &Note{})
	pulumi.RegisterInputType(reflect.TypeOf((*NoteArrayInput)(nil)).Elem(), NoteArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*NoteMapInput)(nil)).Elem(), NoteMap{})
	pulumi.RegisterOutputType(NoteOutput{})
	pulumi.RegisterOutputType(NotePtrOutput{})
	pulumi.RegisterOutputType(NoteArrayOutput{})
	pulumi.RegisterOutputType(NoteMapOutput{})
}
