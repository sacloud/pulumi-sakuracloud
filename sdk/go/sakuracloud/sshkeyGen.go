// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sakuracloud

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Manages a SakuraCloud SSH Key Gen.
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
// 		_, err := sakuracloud.NewSSHKeyGen(ctx, "foobar", &sakuracloud.SSHKeyGenArgs{
// 			Description: pulumi.String("description"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type SSHKeyGen struct {
	pulumi.CustomResourceState

	// The description of the SSHKey. The length of this value must be in the range [`1`-`512`]. Changing this forces a new resource to be created.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The fingerprint of the public key.
	Fingerprint pulumi.StringOutput `pulumi:"fingerprint"`
	// The name of the SSHKey. The length of this value must be in the range [`1`-`64`]. Changing this forces a new resource to be created.
	Name pulumi.StringOutput `pulumi:"name"`
	// The pass phrase of the private key. The length of this value must be in the range [`8`-`64`]. Changing this forces a new resource to be created.
	PassPhrase pulumi.StringPtrOutput `pulumi:"passPhrase"`
	// The body of the private key.
	PrivateKey pulumi.StringOutput `pulumi:"privateKey"`
	// The body of the public key.
	PublicKey pulumi.StringOutput `pulumi:"publicKey"`
}

// NewSSHKeyGen registers a new resource with the given unique name, arguments, and options.
func NewSSHKeyGen(ctx *pulumi.Context,
	name string, args *SSHKeyGenArgs, opts ...pulumi.ResourceOption) (*SSHKeyGen, error) {
	if args == nil {
		args = &SSHKeyGenArgs{}
	}

	var resource SSHKeyGen
	err := ctx.RegisterResource("sakuracloud:index/sSHKeyGen:SSHKeyGen", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSSHKeyGen gets an existing SSHKeyGen resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSSHKeyGen(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SSHKeyGenState, opts ...pulumi.ResourceOption) (*SSHKeyGen, error) {
	var resource SSHKeyGen
	err := ctx.ReadResource("sakuracloud:index/sSHKeyGen:SSHKeyGen", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering SSHKeyGen resources.
type sshkeyGenState struct {
	// The description of the SSHKey. The length of this value must be in the range [`1`-`512`]. Changing this forces a new resource to be created.
	Description *string `pulumi:"description"`
	// The fingerprint of the public key.
	Fingerprint *string `pulumi:"fingerprint"`
	// The name of the SSHKey. The length of this value must be in the range [`1`-`64`]. Changing this forces a new resource to be created.
	Name *string `pulumi:"name"`
	// The pass phrase of the private key. The length of this value must be in the range [`8`-`64`]. Changing this forces a new resource to be created.
	PassPhrase *string `pulumi:"passPhrase"`
	// The body of the private key.
	PrivateKey *string `pulumi:"privateKey"`
	// The body of the public key.
	PublicKey *string `pulumi:"publicKey"`
}

type SSHKeyGenState struct {
	// The description of the SSHKey. The length of this value must be in the range [`1`-`512`]. Changing this forces a new resource to be created.
	Description pulumi.StringPtrInput
	// The fingerprint of the public key.
	Fingerprint pulumi.StringPtrInput
	// The name of the SSHKey. The length of this value must be in the range [`1`-`64`]. Changing this forces a new resource to be created.
	Name pulumi.StringPtrInput
	// The pass phrase of the private key. The length of this value must be in the range [`8`-`64`]. Changing this forces a new resource to be created.
	PassPhrase pulumi.StringPtrInput
	// The body of the private key.
	PrivateKey pulumi.StringPtrInput
	// The body of the public key.
	PublicKey pulumi.StringPtrInput
}

func (SSHKeyGenState) ElementType() reflect.Type {
	return reflect.TypeOf((*sshkeyGenState)(nil)).Elem()
}

type sshkeyGenArgs struct {
	// The description of the SSHKey. The length of this value must be in the range [`1`-`512`]. Changing this forces a new resource to be created.
	Description *string `pulumi:"description"`
	// The name of the SSHKey. The length of this value must be in the range [`1`-`64`]. Changing this forces a new resource to be created.
	Name *string `pulumi:"name"`
	// The pass phrase of the private key. The length of this value must be in the range [`8`-`64`]. Changing this forces a new resource to be created.
	PassPhrase *string `pulumi:"passPhrase"`
}

// The set of arguments for constructing a SSHKeyGen resource.
type SSHKeyGenArgs struct {
	// The description of the SSHKey. The length of this value must be in the range [`1`-`512`]. Changing this forces a new resource to be created.
	Description pulumi.StringPtrInput
	// The name of the SSHKey. The length of this value must be in the range [`1`-`64`]. Changing this forces a new resource to be created.
	Name pulumi.StringPtrInput
	// The pass phrase of the private key. The length of this value must be in the range [`8`-`64`]. Changing this forces a new resource to be created.
	PassPhrase pulumi.StringPtrInput
}

func (SSHKeyGenArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*sshkeyGenArgs)(nil)).Elem()
}

type SSHKeyGenInput interface {
	pulumi.Input

	ToSSHKeyGenOutput() SSHKeyGenOutput
	ToSSHKeyGenOutputWithContext(ctx context.Context) SSHKeyGenOutput
}

func (*SSHKeyGen) ElementType() reflect.Type {
	return reflect.TypeOf((*SSHKeyGen)(nil))
}

func (i *SSHKeyGen) ToSSHKeyGenOutput() SSHKeyGenOutput {
	return i.ToSSHKeyGenOutputWithContext(context.Background())
}

func (i *SSHKeyGen) ToSSHKeyGenOutputWithContext(ctx context.Context) SSHKeyGenOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SSHKeyGenOutput)
}

func (i *SSHKeyGen) ToSSHKeyGenPtrOutput() SSHKeyGenPtrOutput {
	return i.ToSSHKeyGenPtrOutputWithContext(context.Background())
}

func (i *SSHKeyGen) ToSSHKeyGenPtrOutputWithContext(ctx context.Context) SSHKeyGenPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SSHKeyGenPtrOutput)
}

type SSHKeyGenPtrInput interface {
	pulumi.Input

	ToSSHKeyGenPtrOutput() SSHKeyGenPtrOutput
	ToSSHKeyGenPtrOutputWithContext(ctx context.Context) SSHKeyGenPtrOutput
}

type sshkeyGenPtrType SSHKeyGenArgs

func (*sshkeyGenPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**SSHKeyGen)(nil))
}

func (i *sshkeyGenPtrType) ToSSHKeyGenPtrOutput() SSHKeyGenPtrOutput {
	return i.ToSSHKeyGenPtrOutputWithContext(context.Background())
}

func (i *sshkeyGenPtrType) ToSSHKeyGenPtrOutputWithContext(ctx context.Context) SSHKeyGenPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SSHKeyGenPtrOutput)
}

// SSHKeyGenArrayInput is an input type that accepts SSHKeyGenArray and SSHKeyGenArrayOutput values.
// You can construct a concrete instance of `SSHKeyGenArrayInput` via:
//
//          SSHKeyGenArray{ SSHKeyGenArgs{...} }
type SSHKeyGenArrayInput interface {
	pulumi.Input

	ToSSHKeyGenArrayOutput() SSHKeyGenArrayOutput
	ToSSHKeyGenArrayOutputWithContext(context.Context) SSHKeyGenArrayOutput
}

type SSHKeyGenArray []SSHKeyGenInput

func (SSHKeyGenArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*SSHKeyGen)(nil)).Elem()
}

func (i SSHKeyGenArray) ToSSHKeyGenArrayOutput() SSHKeyGenArrayOutput {
	return i.ToSSHKeyGenArrayOutputWithContext(context.Background())
}

func (i SSHKeyGenArray) ToSSHKeyGenArrayOutputWithContext(ctx context.Context) SSHKeyGenArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SSHKeyGenArrayOutput)
}

// SSHKeyGenMapInput is an input type that accepts SSHKeyGenMap and SSHKeyGenMapOutput values.
// You can construct a concrete instance of `SSHKeyGenMapInput` via:
//
//          SSHKeyGenMap{ "key": SSHKeyGenArgs{...} }
type SSHKeyGenMapInput interface {
	pulumi.Input

	ToSSHKeyGenMapOutput() SSHKeyGenMapOutput
	ToSSHKeyGenMapOutputWithContext(context.Context) SSHKeyGenMapOutput
}

type SSHKeyGenMap map[string]SSHKeyGenInput

func (SSHKeyGenMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*SSHKeyGen)(nil)).Elem()
}

func (i SSHKeyGenMap) ToSSHKeyGenMapOutput() SSHKeyGenMapOutput {
	return i.ToSSHKeyGenMapOutputWithContext(context.Background())
}

func (i SSHKeyGenMap) ToSSHKeyGenMapOutputWithContext(ctx context.Context) SSHKeyGenMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SSHKeyGenMapOutput)
}

type SSHKeyGenOutput struct{ *pulumi.OutputState }

func (SSHKeyGenOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*SSHKeyGen)(nil))
}

func (o SSHKeyGenOutput) ToSSHKeyGenOutput() SSHKeyGenOutput {
	return o
}

func (o SSHKeyGenOutput) ToSSHKeyGenOutputWithContext(ctx context.Context) SSHKeyGenOutput {
	return o
}

func (o SSHKeyGenOutput) ToSSHKeyGenPtrOutput() SSHKeyGenPtrOutput {
	return o.ToSSHKeyGenPtrOutputWithContext(context.Background())
}

func (o SSHKeyGenOutput) ToSSHKeyGenPtrOutputWithContext(ctx context.Context) SSHKeyGenPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v SSHKeyGen) *SSHKeyGen {
		return &v
	}).(SSHKeyGenPtrOutput)
}

type SSHKeyGenPtrOutput struct{ *pulumi.OutputState }

func (SSHKeyGenPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**SSHKeyGen)(nil))
}

func (o SSHKeyGenPtrOutput) ToSSHKeyGenPtrOutput() SSHKeyGenPtrOutput {
	return o
}

func (o SSHKeyGenPtrOutput) ToSSHKeyGenPtrOutputWithContext(ctx context.Context) SSHKeyGenPtrOutput {
	return o
}

func (o SSHKeyGenPtrOutput) Elem() SSHKeyGenOutput {
	return o.ApplyT(func(v *SSHKeyGen) SSHKeyGen {
		if v != nil {
			return *v
		}
		var ret SSHKeyGen
		return ret
	}).(SSHKeyGenOutput)
}

type SSHKeyGenArrayOutput struct{ *pulumi.OutputState }

func (SSHKeyGenArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]SSHKeyGen)(nil))
}

func (o SSHKeyGenArrayOutput) ToSSHKeyGenArrayOutput() SSHKeyGenArrayOutput {
	return o
}

func (o SSHKeyGenArrayOutput) ToSSHKeyGenArrayOutputWithContext(ctx context.Context) SSHKeyGenArrayOutput {
	return o
}

func (o SSHKeyGenArrayOutput) Index(i pulumi.IntInput) SSHKeyGenOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) SSHKeyGen {
		return vs[0].([]SSHKeyGen)[vs[1].(int)]
	}).(SSHKeyGenOutput)
}

type SSHKeyGenMapOutput struct{ *pulumi.OutputState }

func (SSHKeyGenMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]SSHKeyGen)(nil))
}

func (o SSHKeyGenMapOutput) ToSSHKeyGenMapOutput() SSHKeyGenMapOutput {
	return o
}

func (o SSHKeyGenMapOutput) ToSSHKeyGenMapOutputWithContext(ctx context.Context) SSHKeyGenMapOutput {
	return o
}

func (o SSHKeyGenMapOutput) MapIndex(k pulumi.StringInput) SSHKeyGenOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) SSHKeyGen {
		return vs[0].(map[string]SSHKeyGen)[vs[1].(string)]
	}).(SSHKeyGenOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*SSHKeyGenInput)(nil)).Elem(), &SSHKeyGen{})
	pulumi.RegisterInputType(reflect.TypeOf((*SSHKeyGenPtrInput)(nil)).Elem(), &SSHKeyGen{})
	pulumi.RegisterInputType(reflect.TypeOf((*SSHKeyGenArrayInput)(nil)).Elem(), SSHKeyGenArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*SSHKeyGenMapInput)(nil)).Elem(), SSHKeyGenMap{})
	pulumi.RegisterOutputType(SSHKeyGenOutput{})
	pulumi.RegisterOutputType(SSHKeyGenPtrOutput{})
	pulumi.RegisterOutputType(SSHKeyGenArrayOutput{})
	pulumi.RegisterOutputType(SSHKeyGenMapOutput{})
}
