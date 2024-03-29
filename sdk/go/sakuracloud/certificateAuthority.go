// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sakuracloud

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Manages a SakuraCloud sakuracloud_certificate_authority.
type CertificateAuthority struct {
	pulumi.CustomResourceState

	// The body of the CA's certificate in PEM format.
	Certificate pulumi.StringOutput `pulumi:"certificate"`
	// One or more `client` blocks as defined below.
	Clients CertificateAuthorityClientArrayOutput `pulumi:"clients"`
	// The URL of the CRL.
	CrlUrl pulumi.StringOutput `pulumi:"crlUrl"`
	// The description of the Certificate Authority. The length of this value must be in the range [`1`-`512`].
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The icon id to attach to the Certificate Authority.
	IconId pulumi.StringPtrOutput `pulumi:"iconId"`
	// The name of the Certificate Authority. The length of this value must be in the range [`1`-`64`].
	Name pulumi.StringOutput `pulumi:"name"`
	// The date on which the certificate validity period ends, in RFC3339 format.
	NotAfter pulumi.StringOutput `pulumi:"notAfter"`
	// The date on which the certificate validity period begins, in RFC3339 format.
	NotBefore pulumi.StringOutput `pulumi:"notBefore"`
	// The body of the CA's certificate in PEM format.
	SerialNumber pulumi.StringOutput `pulumi:"serialNumber"`
	// One or more `server` blocks as defined below.
	Servers CertificateAuthorityServerArrayOutput `pulumi:"servers"`
	// A `subject` block as defined below. Changing this forces a new resource to be created.
	Subject CertificateAuthoritySubjectOutput `pulumi:"subject"`
	// Any tags to assign to the Certificate Authority.
	Tags pulumi.StringArrayOutput `pulumi:"tags"`
	// The number of hours after initial issuing that the certificate will become invalid. Changing this forces a new resource to be created.
	ValidityPeriodHours pulumi.IntOutput `pulumi:"validityPeriodHours"`
}

// NewCertificateAuthority registers a new resource with the given unique name, arguments, and options.
func NewCertificateAuthority(ctx *pulumi.Context,
	name string, args *CertificateAuthorityArgs, opts ...pulumi.ResourceOption) (*CertificateAuthority, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Subject == nil {
		return nil, errors.New("invalid value for required argument 'Subject'")
	}
	if args.ValidityPeriodHours == nil {
		return nil, errors.New("invalid value for required argument 'ValidityPeriodHours'")
	}
	var resource CertificateAuthority
	err := ctx.RegisterResource("sakuracloud:index/certificateAuthority:CertificateAuthority", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetCertificateAuthority gets an existing CertificateAuthority resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetCertificateAuthority(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *CertificateAuthorityState, opts ...pulumi.ResourceOption) (*CertificateAuthority, error) {
	var resource CertificateAuthority
	err := ctx.ReadResource("sakuracloud:index/certificateAuthority:CertificateAuthority", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering CertificateAuthority resources.
type certificateAuthorityState struct {
	// The body of the CA's certificate in PEM format.
	Certificate *string `pulumi:"certificate"`
	// One or more `client` blocks as defined below.
	Clients []CertificateAuthorityClient `pulumi:"clients"`
	// The URL of the CRL.
	CrlUrl *string `pulumi:"crlUrl"`
	// The description of the Certificate Authority. The length of this value must be in the range [`1`-`512`].
	Description *string `pulumi:"description"`
	// The icon id to attach to the Certificate Authority.
	IconId *string `pulumi:"iconId"`
	// The name of the Certificate Authority. The length of this value must be in the range [`1`-`64`].
	Name *string `pulumi:"name"`
	// The date on which the certificate validity period ends, in RFC3339 format.
	NotAfter *string `pulumi:"notAfter"`
	// The date on which the certificate validity period begins, in RFC3339 format.
	NotBefore *string `pulumi:"notBefore"`
	// The body of the CA's certificate in PEM format.
	SerialNumber *string `pulumi:"serialNumber"`
	// One or more `server` blocks as defined below.
	Servers []CertificateAuthorityServer `pulumi:"servers"`
	// A `subject` block as defined below. Changing this forces a new resource to be created.
	Subject *CertificateAuthoritySubject `pulumi:"subject"`
	// Any tags to assign to the Certificate Authority.
	Tags []string `pulumi:"tags"`
	// The number of hours after initial issuing that the certificate will become invalid. Changing this forces a new resource to be created.
	ValidityPeriodHours *int `pulumi:"validityPeriodHours"`
}

type CertificateAuthorityState struct {
	// The body of the CA's certificate in PEM format.
	Certificate pulumi.StringPtrInput
	// One or more `client` blocks as defined below.
	Clients CertificateAuthorityClientArrayInput
	// The URL of the CRL.
	CrlUrl pulumi.StringPtrInput
	// The description of the Certificate Authority. The length of this value must be in the range [`1`-`512`].
	Description pulumi.StringPtrInput
	// The icon id to attach to the Certificate Authority.
	IconId pulumi.StringPtrInput
	// The name of the Certificate Authority. The length of this value must be in the range [`1`-`64`].
	Name pulumi.StringPtrInput
	// The date on which the certificate validity period ends, in RFC3339 format.
	NotAfter pulumi.StringPtrInput
	// The date on which the certificate validity period begins, in RFC3339 format.
	NotBefore pulumi.StringPtrInput
	// The body of the CA's certificate in PEM format.
	SerialNumber pulumi.StringPtrInput
	// One or more `server` blocks as defined below.
	Servers CertificateAuthorityServerArrayInput
	// A `subject` block as defined below. Changing this forces a new resource to be created.
	Subject CertificateAuthoritySubjectPtrInput
	// Any tags to assign to the Certificate Authority.
	Tags pulumi.StringArrayInput
	// The number of hours after initial issuing that the certificate will become invalid. Changing this forces a new resource to be created.
	ValidityPeriodHours pulumi.IntPtrInput
}

func (CertificateAuthorityState) ElementType() reflect.Type {
	return reflect.TypeOf((*certificateAuthorityState)(nil)).Elem()
}

type certificateAuthorityArgs struct {
	// One or more `client` blocks as defined below.
	Clients []CertificateAuthorityClient `pulumi:"clients"`
	// The description of the Certificate Authority. The length of this value must be in the range [`1`-`512`].
	Description *string `pulumi:"description"`
	// The icon id to attach to the Certificate Authority.
	IconId *string `pulumi:"iconId"`
	// The name of the Certificate Authority. The length of this value must be in the range [`1`-`64`].
	Name *string `pulumi:"name"`
	// One or more `server` blocks as defined below.
	Servers []CertificateAuthorityServer `pulumi:"servers"`
	// A `subject` block as defined below. Changing this forces a new resource to be created.
	Subject CertificateAuthoritySubject `pulumi:"subject"`
	// Any tags to assign to the Certificate Authority.
	Tags []string `pulumi:"tags"`
	// The number of hours after initial issuing that the certificate will become invalid. Changing this forces a new resource to be created.
	ValidityPeriodHours int `pulumi:"validityPeriodHours"`
}

// The set of arguments for constructing a CertificateAuthority resource.
type CertificateAuthorityArgs struct {
	// One or more `client` blocks as defined below.
	Clients CertificateAuthorityClientArrayInput
	// The description of the Certificate Authority. The length of this value must be in the range [`1`-`512`].
	Description pulumi.StringPtrInput
	// The icon id to attach to the Certificate Authority.
	IconId pulumi.StringPtrInput
	// The name of the Certificate Authority. The length of this value must be in the range [`1`-`64`].
	Name pulumi.StringPtrInput
	// One or more `server` blocks as defined below.
	Servers CertificateAuthorityServerArrayInput
	// A `subject` block as defined below. Changing this forces a new resource to be created.
	Subject CertificateAuthoritySubjectInput
	// Any tags to assign to the Certificate Authority.
	Tags pulumi.StringArrayInput
	// The number of hours after initial issuing that the certificate will become invalid. Changing this forces a new resource to be created.
	ValidityPeriodHours pulumi.IntInput
}

func (CertificateAuthorityArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*certificateAuthorityArgs)(nil)).Elem()
}

type CertificateAuthorityInput interface {
	pulumi.Input

	ToCertificateAuthorityOutput() CertificateAuthorityOutput
	ToCertificateAuthorityOutputWithContext(ctx context.Context) CertificateAuthorityOutput
}

func (*CertificateAuthority) ElementType() reflect.Type {
	return reflect.TypeOf((*CertificateAuthority)(nil))
}

func (i *CertificateAuthority) ToCertificateAuthorityOutput() CertificateAuthorityOutput {
	return i.ToCertificateAuthorityOutputWithContext(context.Background())
}

func (i *CertificateAuthority) ToCertificateAuthorityOutputWithContext(ctx context.Context) CertificateAuthorityOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CertificateAuthorityOutput)
}

func (i *CertificateAuthority) ToCertificateAuthorityPtrOutput() CertificateAuthorityPtrOutput {
	return i.ToCertificateAuthorityPtrOutputWithContext(context.Background())
}

func (i *CertificateAuthority) ToCertificateAuthorityPtrOutputWithContext(ctx context.Context) CertificateAuthorityPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CertificateAuthorityPtrOutput)
}

type CertificateAuthorityPtrInput interface {
	pulumi.Input

	ToCertificateAuthorityPtrOutput() CertificateAuthorityPtrOutput
	ToCertificateAuthorityPtrOutputWithContext(ctx context.Context) CertificateAuthorityPtrOutput
}

type certificateAuthorityPtrType CertificateAuthorityArgs

func (*certificateAuthorityPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**CertificateAuthority)(nil))
}

func (i *certificateAuthorityPtrType) ToCertificateAuthorityPtrOutput() CertificateAuthorityPtrOutput {
	return i.ToCertificateAuthorityPtrOutputWithContext(context.Background())
}

func (i *certificateAuthorityPtrType) ToCertificateAuthorityPtrOutputWithContext(ctx context.Context) CertificateAuthorityPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CertificateAuthorityPtrOutput)
}

// CertificateAuthorityArrayInput is an input type that accepts CertificateAuthorityArray and CertificateAuthorityArrayOutput values.
// You can construct a concrete instance of `CertificateAuthorityArrayInput` via:
//
//          CertificateAuthorityArray{ CertificateAuthorityArgs{...} }
type CertificateAuthorityArrayInput interface {
	pulumi.Input

	ToCertificateAuthorityArrayOutput() CertificateAuthorityArrayOutput
	ToCertificateAuthorityArrayOutputWithContext(context.Context) CertificateAuthorityArrayOutput
}

type CertificateAuthorityArray []CertificateAuthorityInput

func (CertificateAuthorityArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*CertificateAuthority)(nil)).Elem()
}

func (i CertificateAuthorityArray) ToCertificateAuthorityArrayOutput() CertificateAuthorityArrayOutput {
	return i.ToCertificateAuthorityArrayOutputWithContext(context.Background())
}

func (i CertificateAuthorityArray) ToCertificateAuthorityArrayOutputWithContext(ctx context.Context) CertificateAuthorityArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CertificateAuthorityArrayOutput)
}

// CertificateAuthorityMapInput is an input type that accepts CertificateAuthorityMap and CertificateAuthorityMapOutput values.
// You can construct a concrete instance of `CertificateAuthorityMapInput` via:
//
//          CertificateAuthorityMap{ "key": CertificateAuthorityArgs{...} }
type CertificateAuthorityMapInput interface {
	pulumi.Input

	ToCertificateAuthorityMapOutput() CertificateAuthorityMapOutput
	ToCertificateAuthorityMapOutputWithContext(context.Context) CertificateAuthorityMapOutput
}

type CertificateAuthorityMap map[string]CertificateAuthorityInput

func (CertificateAuthorityMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*CertificateAuthority)(nil)).Elem()
}

func (i CertificateAuthorityMap) ToCertificateAuthorityMapOutput() CertificateAuthorityMapOutput {
	return i.ToCertificateAuthorityMapOutputWithContext(context.Background())
}

func (i CertificateAuthorityMap) ToCertificateAuthorityMapOutputWithContext(ctx context.Context) CertificateAuthorityMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CertificateAuthorityMapOutput)
}

type CertificateAuthorityOutput struct{ *pulumi.OutputState }

func (CertificateAuthorityOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*CertificateAuthority)(nil))
}

func (o CertificateAuthorityOutput) ToCertificateAuthorityOutput() CertificateAuthorityOutput {
	return o
}

func (o CertificateAuthorityOutput) ToCertificateAuthorityOutputWithContext(ctx context.Context) CertificateAuthorityOutput {
	return o
}

func (o CertificateAuthorityOutput) ToCertificateAuthorityPtrOutput() CertificateAuthorityPtrOutput {
	return o.ToCertificateAuthorityPtrOutputWithContext(context.Background())
}

func (o CertificateAuthorityOutput) ToCertificateAuthorityPtrOutputWithContext(ctx context.Context) CertificateAuthorityPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v CertificateAuthority) *CertificateAuthority {
		return &v
	}).(CertificateAuthorityPtrOutput)
}

type CertificateAuthorityPtrOutput struct{ *pulumi.OutputState }

func (CertificateAuthorityPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**CertificateAuthority)(nil))
}

func (o CertificateAuthorityPtrOutput) ToCertificateAuthorityPtrOutput() CertificateAuthorityPtrOutput {
	return o
}

func (o CertificateAuthorityPtrOutput) ToCertificateAuthorityPtrOutputWithContext(ctx context.Context) CertificateAuthorityPtrOutput {
	return o
}

func (o CertificateAuthorityPtrOutput) Elem() CertificateAuthorityOutput {
	return o.ApplyT(func(v *CertificateAuthority) CertificateAuthority {
		if v != nil {
			return *v
		}
		var ret CertificateAuthority
		return ret
	}).(CertificateAuthorityOutput)
}

type CertificateAuthorityArrayOutput struct{ *pulumi.OutputState }

func (CertificateAuthorityArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]CertificateAuthority)(nil))
}

func (o CertificateAuthorityArrayOutput) ToCertificateAuthorityArrayOutput() CertificateAuthorityArrayOutput {
	return o
}

func (o CertificateAuthorityArrayOutput) ToCertificateAuthorityArrayOutputWithContext(ctx context.Context) CertificateAuthorityArrayOutput {
	return o
}

func (o CertificateAuthorityArrayOutput) Index(i pulumi.IntInput) CertificateAuthorityOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) CertificateAuthority {
		return vs[0].([]CertificateAuthority)[vs[1].(int)]
	}).(CertificateAuthorityOutput)
}

type CertificateAuthorityMapOutput struct{ *pulumi.OutputState }

func (CertificateAuthorityMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]CertificateAuthority)(nil))
}

func (o CertificateAuthorityMapOutput) ToCertificateAuthorityMapOutput() CertificateAuthorityMapOutput {
	return o
}

func (o CertificateAuthorityMapOutput) ToCertificateAuthorityMapOutputWithContext(ctx context.Context) CertificateAuthorityMapOutput {
	return o
}

func (o CertificateAuthorityMapOutput) MapIndex(k pulumi.StringInput) CertificateAuthorityOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) CertificateAuthority {
		return vs[0].(map[string]CertificateAuthority)[vs[1].(string)]
	}).(CertificateAuthorityOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*CertificateAuthorityInput)(nil)).Elem(), &CertificateAuthority{})
	pulumi.RegisterInputType(reflect.TypeOf((*CertificateAuthorityPtrInput)(nil)).Elem(), &CertificateAuthority{})
	pulumi.RegisterInputType(reflect.TypeOf((*CertificateAuthorityArrayInput)(nil)).Elem(), CertificateAuthorityArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*CertificateAuthorityMapInput)(nil)).Elem(), CertificateAuthorityMap{})
	pulumi.RegisterOutputType(CertificateAuthorityOutput{})
	pulumi.RegisterOutputType(CertificateAuthorityPtrOutput{})
	pulumi.RegisterOutputType(CertificateAuthorityArrayOutput{})
	pulumi.RegisterOutputType(CertificateAuthorityMapOutput{})
}
