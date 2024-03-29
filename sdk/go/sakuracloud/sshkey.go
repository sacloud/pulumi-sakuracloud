// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sakuracloud

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Manages a SakuraCloud SSH Key.
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
// 		_, err := sakuracloud.NewSSHKey(ctx, "foobar", &sakuracloud.SSHKeyArgs{
// 			PublicKey: readFileOrPanic("~/.ssh/id_rsa.pub"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type SSHKey struct {
	pulumi.CustomResourceState

	// The description of the SSHKey. The length of this value must be in the range [`1`-`512`].
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The fingerprint of the public key.
	Fingerprint pulumi.StringOutput `pulumi:"fingerprint"`
	// The name of the SSHKey. The length of this value must be in the range [`1`-`64`].
	Name pulumi.StringOutput `pulumi:"name"`
	// The body of the public key. Changing this forces a new resource to be created.
	PublicKey pulumi.StringOutput `pulumi:"publicKey"`
}

// NewSSHKey registers a new resource with the given unique name, arguments, and options.
func NewSSHKey(ctx *pulumi.Context,
	name string, args *SSHKeyArgs, opts ...pulumi.ResourceOption) (*SSHKey, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.PublicKey == nil {
		return nil, errors.New("invalid value for required argument 'PublicKey'")
	}
	var resource SSHKey
	err := ctx.RegisterResource("sakuracloud:index/sSHKey:SSHKey", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSSHKey gets an existing SSHKey resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSSHKey(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SSHKeyState, opts ...pulumi.ResourceOption) (*SSHKey, error) {
	var resource SSHKey
	err := ctx.ReadResource("sakuracloud:index/sSHKey:SSHKey", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering SSHKey resources.
type sshkeyState struct {
	// The description of the SSHKey. The length of this value must be in the range [`1`-`512`].
	Description *string `pulumi:"description"`
	// The fingerprint of the public key.
	Fingerprint *string `pulumi:"fingerprint"`
	// The name of the SSHKey. The length of this value must be in the range [`1`-`64`].
	Name *string `pulumi:"name"`
	// The body of the public key. Changing this forces a new resource to be created.
	PublicKey *string `pulumi:"publicKey"`
}

type SSHKeyState struct {
	// The description of the SSHKey. The length of this value must be in the range [`1`-`512`].
	Description pulumi.StringPtrInput
	// The fingerprint of the public key.
	Fingerprint pulumi.StringPtrInput
	// The name of the SSHKey. The length of this value must be in the range [`1`-`64`].
	Name pulumi.StringPtrInput
	// The body of the public key. Changing this forces a new resource to be created.
	PublicKey pulumi.StringPtrInput
}

func (SSHKeyState) ElementType() reflect.Type {
	return reflect.TypeOf((*sshkeyState)(nil)).Elem()
}

type sshkeyArgs struct {
	// The description of the SSHKey. The length of this value must be in the range [`1`-`512`].
	Description *string `pulumi:"description"`
	// The name of the SSHKey. The length of this value must be in the range [`1`-`64`].
	Name *string `pulumi:"name"`
	// The body of the public key. Changing this forces a new resource to be created.
	PublicKey string `pulumi:"publicKey"`
}

// The set of arguments for constructing a SSHKey resource.
type SSHKeyArgs struct {
	// The description of the SSHKey. The length of this value must be in the range [`1`-`512`].
	Description pulumi.StringPtrInput
	// The name of the SSHKey. The length of this value must be in the range [`1`-`64`].
	Name pulumi.StringPtrInput
	// The body of the public key. Changing this forces a new resource to be created.
	PublicKey pulumi.StringInput
}

func (SSHKeyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*sshkeyArgs)(nil)).Elem()
}

type SSHKeyInput interface {
	pulumi.Input

	ToSSHKeyOutput() SSHKeyOutput
	ToSSHKeyOutputWithContext(ctx context.Context) SSHKeyOutput
}

func (*SSHKey) ElementType() reflect.Type {
	return reflect.TypeOf((*SSHKey)(nil))
}

func (i *SSHKey) ToSSHKeyOutput() SSHKeyOutput {
	return i.ToSSHKeyOutputWithContext(context.Background())
}

func (i *SSHKey) ToSSHKeyOutputWithContext(ctx context.Context) SSHKeyOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SSHKeyOutput)
}

func (i *SSHKey) ToSSHKeyPtrOutput() SSHKeyPtrOutput {
	return i.ToSSHKeyPtrOutputWithContext(context.Background())
}

func (i *SSHKey) ToSSHKeyPtrOutputWithContext(ctx context.Context) SSHKeyPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SSHKeyPtrOutput)
}

type SSHKeyPtrInput interface {
	pulumi.Input

	ToSSHKeyPtrOutput() SSHKeyPtrOutput
	ToSSHKeyPtrOutputWithContext(ctx context.Context) SSHKeyPtrOutput
}

type sshkeyPtrType SSHKeyArgs

func (*sshkeyPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**SSHKey)(nil))
}

func (i *sshkeyPtrType) ToSSHKeyPtrOutput() SSHKeyPtrOutput {
	return i.ToSSHKeyPtrOutputWithContext(context.Background())
}

func (i *sshkeyPtrType) ToSSHKeyPtrOutputWithContext(ctx context.Context) SSHKeyPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SSHKeyPtrOutput)
}

// SSHKeyArrayInput is an input type that accepts SSHKeyArray and SSHKeyArrayOutput values.
// You can construct a concrete instance of `SSHKeyArrayInput` via:
//
//          SSHKeyArray{ SSHKeyArgs{...} }
type SSHKeyArrayInput interface {
	pulumi.Input

	ToSSHKeyArrayOutput() SSHKeyArrayOutput
	ToSSHKeyArrayOutputWithContext(context.Context) SSHKeyArrayOutput
}

type SSHKeyArray []SSHKeyInput

func (SSHKeyArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*SSHKey)(nil)).Elem()
}

func (i SSHKeyArray) ToSSHKeyArrayOutput() SSHKeyArrayOutput {
	return i.ToSSHKeyArrayOutputWithContext(context.Background())
}

func (i SSHKeyArray) ToSSHKeyArrayOutputWithContext(ctx context.Context) SSHKeyArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SSHKeyArrayOutput)
}

// SSHKeyMapInput is an input type that accepts SSHKeyMap and SSHKeyMapOutput values.
// You can construct a concrete instance of `SSHKeyMapInput` via:
//
//          SSHKeyMap{ "key": SSHKeyArgs{...} }
type SSHKeyMapInput interface {
	pulumi.Input

	ToSSHKeyMapOutput() SSHKeyMapOutput
	ToSSHKeyMapOutputWithContext(context.Context) SSHKeyMapOutput
}

type SSHKeyMap map[string]SSHKeyInput

func (SSHKeyMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*SSHKey)(nil)).Elem()
}

func (i SSHKeyMap) ToSSHKeyMapOutput() SSHKeyMapOutput {
	return i.ToSSHKeyMapOutputWithContext(context.Background())
}

func (i SSHKeyMap) ToSSHKeyMapOutputWithContext(ctx context.Context) SSHKeyMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SSHKeyMapOutput)
}

type SSHKeyOutput struct{ *pulumi.OutputState }

func (SSHKeyOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*SSHKey)(nil))
}

func (o SSHKeyOutput) ToSSHKeyOutput() SSHKeyOutput {
	return o
}

func (o SSHKeyOutput) ToSSHKeyOutputWithContext(ctx context.Context) SSHKeyOutput {
	return o
}

func (o SSHKeyOutput) ToSSHKeyPtrOutput() SSHKeyPtrOutput {
	return o.ToSSHKeyPtrOutputWithContext(context.Background())
}

func (o SSHKeyOutput) ToSSHKeyPtrOutputWithContext(ctx context.Context) SSHKeyPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v SSHKey) *SSHKey {
		return &v
	}).(SSHKeyPtrOutput)
}

type SSHKeyPtrOutput struct{ *pulumi.OutputState }

func (SSHKeyPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**SSHKey)(nil))
}

func (o SSHKeyPtrOutput) ToSSHKeyPtrOutput() SSHKeyPtrOutput {
	return o
}

func (o SSHKeyPtrOutput) ToSSHKeyPtrOutputWithContext(ctx context.Context) SSHKeyPtrOutput {
	return o
}

func (o SSHKeyPtrOutput) Elem() SSHKeyOutput {
	return o.ApplyT(func(v *SSHKey) SSHKey {
		if v != nil {
			return *v
		}
		var ret SSHKey
		return ret
	}).(SSHKeyOutput)
}

type SSHKeyArrayOutput struct{ *pulumi.OutputState }

func (SSHKeyArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]SSHKey)(nil))
}

func (o SSHKeyArrayOutput) ToSSHKeyArrayOutput() SSHKeyArrayOutput {
	return o
}

func (o SSHKeyArrayOutput) ToSSHKeyArrayOutputWithContext(ctx context.Context) SSHKeyArrayOutput {
	return o
}

func (o SSHKeyArrayOutput) Index(i pulumi.IntInput) SSHKeyOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) SSHKey {
		return vs[0].([]SSHKey)[vs[1].(int)]
	}).(SSHKeyOutput)
}

type SSHKeyMapOutput struct{ *pulumi.OutputState }

func (SSHKeyMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]SSHKey)(nil))
}

func (o SSHKeyMapOutput) ToSSHKeyMapOutput() SSHKeyMapOutput {
	return o
}

func (o SSHKeyMapOutput) ToSSHKeyMapOutputWithContext(ctx context.Context) SSHKeyMapOutput {
	return o
}

func (o SSHKeyMapOutput) MapIndex(k pulumi.StringInput) SSHKeyOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) SSHKey {
		return vs[0].(map[string]SSHKey)[vs[1].(string)]
	}).(SSHKeyOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*SSHKeyInput)(nil)).Elem(), &SSHKey{})
	pulumi.RegisterInputType(reflect.TypeOf((*SSHKeyPtrInput)(nil)).Elem(), &SSHKey{})
	pulumi.RegisterInputType(reflect.TypeOf((*SSHKeyArrayInput)(nil)).Elem(), SSHKeyArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*SSHKeyMapInput)(nil)).Elem(), SSHKeyMap{})
	pulumi.RegisterOutputType(SSHKeyOutput{})
	pulumi.RegisterOutputType(SSHKeyPtrOutput{})
	pulumi.RegisterOutputType(SSHKeyArrayOutput{})
	pulumi.RegisterOutputType(SSHKeyMapOutput{})
}
