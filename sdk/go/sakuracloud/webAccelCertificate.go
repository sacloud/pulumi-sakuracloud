// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sakuracloud

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages a SakuraCloud sakuracloud_webaccel_certificate.
type WebAccelCertificate struct {
	pulumi.CustomResourceState

	// .
	CertificateChain pulumi.StringOutput `pulumi:"certificateChain"`
	// .
	DnsNames pulumi.StringArrayOutput `pulumi:"dnsNames"`
	// .
	IssuerCommonName pulumi.StringOutput `pulumi:"issuerCommonName"`
	// .
	NotAfter pulumi.StringOutput `pulumi:"notAfter"`
	// .
	NotBefore pulumi.StringOutput `pulumi:"notBefore"`
	// .
	PrivateKey pulumi.StringOutput `pulumi:"privateKey"`
	// .
	SerialNumber pulumi.StringOutput `pulumi:"serialNumber"`
	// .
	Sha256Fingerprint pulumi.StringOutput `pulumi:"sha256Fingerprint"`
	// .
	SiteId pulumi.StringOutput `pulumi:"siteId"`
	// .
	SubjectCommonName pulumi.StringOutput `pulumi:"subjectCommonName"`
}

// NewWebAccelCertificate registers a new resource with the given unique name, arguments, and options.
func NewWebAccelCertificate(ctx *pulumi.Context,
	name string, args *WebAccelCertificateArgs, opts ...pulumi.ResourceOption) (*WebAccelCertificate, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.CertificateChain == nil {
		return nil, errors.New("invalid value for required argument 'CertificateChain'")
	}
	if args.PrivateKey == nil {
		return nil, errors.New("invalid value for required argument 'PrivateKey'")
	}
	if args.SiteId == nil {
		return nil, errors.New("invalid value for required argument 'SiteId'")
	}
	var resource WebAccelCertificate
	err := ctx.RegisterResource("sakuracloud:index/webAccelCertificate:WebAccelCertificate", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetWebAccelCertificate gets an existing WebAccelCertificate resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetWebAccelCertificate(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *WebAccelCertificateState, opts ...pulumi.ResourceOption) (*WebAccelCertificate, error) {
	var resource WebAccelCertificate
	err := ctx.ReadResource("sakuracloud:index/webAccelCertificate:WebAccelCertificate", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering WebAccelCertificate resources.
type webAccelCertificateState struct {
	// .
	CertificateChain *string `pulumi:"certificateChain"`
	// .
	DnsNames []string `pulumi:"dnsNames"`
	// .
	IssuerCommonName *string `pulumi:"issuerCommonName"`
	// .
	NotAfter *string `pulumi:"notAfter"`
	// .
	NotBefore *string `pulumi:"notBefore"`
	// .
	PrivateKey *string `pulumi:"privateKey"`
	// .
	SerialNumber *string `pulumi:"serialNumber"`
	// .
	Sha256Fingerprint *string `pulumi:"sha256Fingerprint"`
	// .
	SiteId *string `pulumi:"siteId"`
	// .
	SubjectCommonName *string `pulumi:"subjectCommonName"`
}

type WebAccelCertificateState struct {
	// .
	CertificateChain pulumi.StringPtrInput
	// .
	DnsNames pulumi.StringArrayInput
	// .
	IssuerCommonName pulumi.StringPtrInput
	// .
	NotAfter pulumi.StringPtrInput
	// .
	NotBefore pulumi.StringPtrInput
	// .
	PrivateKey pulumi.StringPtrInput
	// .
	SerialNumber pulumi.StringPtrInput
	// .
	Sha256Fingerprint pulumi.StringPtrInput
	// .
	SiteId pulumi.StringPtrInput
	// .
	SubjectCommonName pulumi.StringPtrInput
}

func (WebAccelCertificateState) ElementType() reflect.Type {
	return reflect.TypeOf((*webAccelCertificateState)(nil)).Elem()
}

type webAccelCertificateArgs struct {
	// .
	CertificateChain string `pulumi:"certificateChain"`
	// .
	PrivateKey string `pulumi:"privateKey"`
	// .
	SiteId string `pulumi:"siteId"`
}

// The set of arguments for constructing a WebAccelCertificate resource.
type WebAccelCertificateArgs struct {
	// .
	CertificateChain pulumi.StringInput
	// .
	PrivateKey pulumi.StringInput
	// .
	SiteId pulumi.StringInput
}

func (WebAccelCertificateArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*webAccelCertificateArgs)(nil)).Elem()
}

type WebAccelCertificateInput interface {
	pulumi.Input

	ToWebAccelCertificateOutput() WebAccelCertificateOutput
	ToWebAccelCertificateOutputWithContext(ctx context.Context) WebAccelCertificateOutput
}

func (*WebAccelCertificate) ElementType() reflect.Type {
	return reflect.TypeOf((*WebAccelCertificate)(nil))
}

func (i *WebAccelCertificate) ToWebAccelCertificateOutput() WebAccelCertificateOutput {
	return i.ToWebAccelCertificateOutputWithContext(context.Background())
}

func (i *WebAccelCertificate) ToWebAccelCertificateOutputWithContext(ctx context.Context) WebAccelCertificateOutput {
	return pulumi.ToOutputWithContext(ctx, i).(WebAccelCertificateOutput)
}

func (i *WebAccelCertificate) ToWebAccelCertificatePtrOutput() WebAccelCertificatePtrOutput {
	return i.ToWebAccelCertificatePtrOutputWithContext(context.Background())
}

func (i *WebAccelCertificate) ToWebAccelCertificatePtrOutputWithContext(ctx context.Context) WebAccelCertificatePtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(WebAccelCertificatePtrOutput)
}

type WebAccelCertificatePtrInput interface {
	pulumi.Input

	ToWebAccelCertificatePtrOutput() WebAccelCertificatePtrOutput
	ToWebAccelCertificatePtrOutputWithContext(ctx context.Context) WebAccelCertificatePtrOutput
}

type webAccelCertificatePtrType WebAccelCertificateArgs

func (*webAccelCertificatePtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**WebAccelCertificate)(nil))
}

func (i *webAccelCertificatePtrType) ToWebAccelCertificatePtrOutput() WebAccelCertificatePtrOutput {
	return i.ToWebAccelCertificatePtrOutputWithContext(context.Background())
}

func (i *webAccelCertificatePtrType) ToWebAccelCertificatePtrOutputWithContext(ctx context.Context) WebAccelCertificatePtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(WebAccelCertificatePtrOutput)
}

// WebAccelCertificateArrayInput is an input type that accepts WebAccelCertificateArray and WebAccelCertificateArrayOutput values.
// You can construct a concrete instance of `WebAccelCertificateArrayInput` via:
//
//          WebAccelCertificateArray{ WebAccelCertificateArgs{...} }
type WebAccelCertificateArrayInput interface {
	pulumi.Input

	ToWebAccelCertificateArrayOutput() WebAccelCertificateArrayOutput
	ToWebAccelCertificateArrayOutputWithContext(context.Context) WebAccelCertificateArrayOutput
}

type WebAccelCertificateArray []WebAccelCertificateInput

func (WebAccelCertificateArray) ElementType() reflect.Type {
	return reflect.TypeOf(([]*WebAccelCertificate)(nil))
}

func (i WebAccelCertificateArray) ToWebAccelCertificateArrayOutput() WebAccelCertificateArrayOutput {
	return i.ToWebAccelCertificateArrayOutputWithContext(context.Background())
}

func (i WebAccelCertificateArray) ToWebAccelCertificateArrayOutputWithContext(ctx context.Context) WebAccelCertificateArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(WebAccelCertificateArrayOutput)
}

// WebAccelCertificateMapInput is an input type that accepts WebAccelCertificateMap and WebAccelCertificateMapOutput values.
// You can construct a concrete instance of `WebAccelCertificateMapInput` via:
//
//          WebAccelCertificateMap{ "key": WebAccelCertificateArgs{...} }
type WebAccelCertificateMapInput interface {
	pulumi.Input

	ToWebAccelCertificateMapOutput() WebAccelCertificateMapOutput
	ToWebAccelCertificateMapOutputWithContext(context.Context) WebAccelCertificateMapOutput
}

type WebAccelCertificateMap map[string]WebAccelCertificateInput

func (WebAccelCertificateMap) ElementType() reflect.Type {
	return reflect.TypeOf((map[string]*WebAccelCertificate)(nil))
}

func (i WebAccelCertificateMap) ToWebAccelCertificateMapOutput() WebAccelCertificateMapOutput {
	return i.ToWebAccelCertificateMapOutputWithContext(context.Background())
}

func (i WebAccelCertificateMap) ToWebAccelCertificateMapOutputWithContext(ctx context.Context) WebAccelCertificateMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(WebAccelCertificateMapOutput)
}

type WebAccelCertificateOutput struct {
	*pulumi.OutputState
}

func (WebAccelCertificateOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*WebAccelCertificate)(nil))
}

func (o WebAccelCertificateOutput) ToWebAccelCertificateOutput() WebAccelCertificateOutput {
	return o
}

func (o WebAccelCertificateOutput) ToWebAccelCertificateOutputWithContext(ctx context.Context) WebAccelCertificateOutput {
	return o
}

func (o WebAccelCertificateOutput) ToWebAccelCertificatePtrOutput() WebAccelCertificatePtrOutput {
	return o.ToWebAccelCertificatePtrOutputWithContext(context.Background())
}

func (o WebAccelCertificateOutput) ToWebAccelCertificatePtrOutputWithContext(ctx context.Context) WebAccelCertificatePtrOutput {
	return o.ApplyT(func(v WebAccelCertificate) *WebAccelCertificate {
		return &v
	}).(WebAccelCertificatePtrOutput)
}

type WebAccelCertificatePtrOutput struct {
	*pulumi.OutputState
}

func (WebAccelCertificatePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**WebAccelCertificate)(nil))
}

func (o WebAccelCertificatePtrOutput) ToWebAccelCertificatePtrOutput() WebAccelCertificatePtrOutput {
	return o
}

func (o WebAccelCertificatePtrOutput) ToWebAccelCertificatePtrOutputWithContext(ctx context.Context) WebAccelCertificatePtrOutput {
	return o
}

type WebAccelCertificateArrayOutput struct{ *pulumi.OutputState }

func (WebAccelCertificateArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]WebAccelCertificate)(nil))
}

func (o WebAccelCertificateArrayOutput) ToWebAccelCertificateArrayOutput() WebAccelCertificateArrayOutput {
	return o
}

func (o WebAccelCertificateArrayOutput) ToWebAccelCertificateArrayOutputWithContext(ctx context.Context) WebAccelCertificateArrayOutput {
	return o
}

func (o WebAccelCertificateArrayOutput) Index(i pulumi.IntInput) WebAccelCertificateOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) WebAccelCertificate {
		return vs[0].([]WebAccelCertificate)[vs[1].(int)]
	}).(WebAccelCertificateOutput)
}

type WebAccelCertificateMapOutput struct{ *pulumi.OutputState }

func (WebAccelCertificateMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]WebAccelCertificate)(nil))
}

func (o WebAccelCertificateMapOutput) ToWebAccelCertificateMapOutput() WebAccelCertificateMapOutput {
	return o
}

func (o WebAccelCertificateMapOutput) ToWebAccelCertificateMapOutputWithContext(ctx context.Context) WebAccelCertificateMapOutput {
	return o
}

func (o WebAccelCertificateMapOutput) MapIndex(k pulumi.StringInput) WebAccelCertificateOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) WebAccelCertificate {
		return vs[0].(map[string]WebAccelCertificate)[vs[1].(string)]
	}).(WebAccelCertificateOutput)
}

func init() {
	pulumi.RegisterOutputType(WebAccelCertificateOutput{})
	pulumi.RegisterOutputType(WebAccelCertificatePtrOutput{})
	pulumi.RegisterOutputType(WebAccelCertificateArrayOutput{})
	pulumi.RegisterOutputType(WebAccelCertificateMapOutput{})
}
