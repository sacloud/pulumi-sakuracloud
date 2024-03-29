// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sakuracloud

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Manages a SakuraCloud DNS.
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
// 		_, err := sakuracloud.NewDNS(ctx, "foobar", &sakuracloud.DNSArgs{
// 			Description: pulumi.String("description"),
// 			Records: DNSRecordArray{
// 				&DNSRecordArgs{
// 					Name:  pulumi.String("www"),
// 					Type:  pulumi.String("A"),
// 					Value: pulumi.String("192.168.11.1"),
// 				},
// 				&DNSRecordArgs{
// 					Name:  pulumi.String("www"),
// 					Type:  pulumi.String("A"),
// 					Value: pulumi.String("192.168.11.2"),
// 				},
// 			},
// 			Tags: pulumi.StringArray{
// 				pulumi.String("tag1"),
// 				pulumi.String("tag2"),
// 			},
// 			Zone: pulumi.String("example.com"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type DNS struct {
	pulumi.CustomResourceState

	// The description of the DNS. The length of this value must be in the range [`1`-`512`].
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// A list of IP address of DNS server that manage this zone.
	DnsServers pulumi.StringArrayOutput `pulumi:"dnsServers"`
	// The icon id to attach to the DNS.
	IconId pulumi.StringPtrOutput `pulumi:"iconId"`
	// One or more `record` blocks as defined below.
	Records DNSRecordTypeArrayOutput `pulumi:"records"`
	// Any tags to assign to the DNS.
	Tags pulumi.StringArrayOutput `pulumi:"tags"`
	// The target zone. (e.g. `example.com`). Changing this forces a new resource to be created.
	Zone pulumi.StringOutput `pulumi:"zone"`
}

// NewDNS registers a new resource with the given unique name, arguments, and options.
func NewDNS(ctx *pulumi.Context,
	name string, args *DNSArgs, opts ...pulumi.ResourceOption) (*DNS, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Zone == nil {
		return nil, errors.New("invalid value for required argument 'Zone'")
	}
	var resource DNS
	err := ctx.RegisterResource("sakuracloud:index/dNS:DNS", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDNS gets an existing DNS resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDNS(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DNSState, opts ...pulumi.ResourceOption) (*DNS, error) {
	var resource DNS
	err := ctx.ReadResource("sakuracloud:index/dNS:DNS", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering DNS resources.
type dnsState struct {
	// The description of the DNS. The length of this value must be in the range [`1`-`512`].
	Description *string `pulumi:"description"`
	// A list of IP address of DNS server that manage this zone.
	DnsServers []string `pulumi:"dnsServers"`
	// The icon id to attach to the DNS.
	IconId *string `pulumi:"iconId"`
	// One or more `record` blocks as defined below.
	Records []DNSRecordType `pulumi:"records"`
	// Any tags to assign to the DNS.
	Tags []string `pulumi:"tags"`
	// The target zone. (e.g. `example.com`). Changing this forces a new resource to be created.
	Zone *string `pulumi:"zone"`
}

type DNSState struct {
	// The description of the DNS. The length of this value must be in the range [`1`-`512`].
	Description pulumi.StringPtrInput
	// A list of IP address of DNS server that manage this zone.
	DnsServers pulumi.StringArrayInput
	// The icon id to attach to the DNS.
	IconId pulumi.StringPtrInput
	// One or more `record` blocks as defined below.
	Records DNSRecordTypeArrayInput
	// Any tags to assign to the DNS.
	Tags pulumi.StringArrayInput
	// The target zone. (e.g. `example.com`). Changing this forces a new resource to be created.
	Zone pulumi.StringPtrInput
}

func (DNSState) ElementType() reflect.Type {
	return reflect.TypeOf((*dnsState)(nil)).Elem()
}

type dnsArgs struct {
	// The description of the DNS. The length of this value must be in the range [`1`-`512`].
	Description *string `pulumi:"description"`
	// The icon id to attach to the DNS.
	IconId *string `pulumi:"iconId"`
	// One or more `record` blocks as defined below.
	Records []DNSRecordType `pulumi:"records"`
	// Any tags to assign to the DNS.
	Tags []string `pulumi:"tags"`
	// The target zone. (e.g. `example.com`). Changing this forces a new resource to be created.
	Zone string `pulumi:"zone"`
}

// The set of arguments for constructing a DNS resource.
type DNSArgs struct {
	// The description of the DNS. The length of this value must be in the range [`1`-`512`].
	Description pulumi.StringPtrInput
	// The icon id to attach to the DNS.
	IconId pulumi.StringPtrInput
	// One or more `record` blocks as defined below.
	Records DNSRecordTypeArrayInput
	// Any tags to assign to the DNS.
	Tags pulumi.StringArrayInput
	// The target zone. (e.g. `example.com`). Changing this forces a new resource to be created.
	Zone pulumi.StringInput
}

func (DNSArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*dnsArgs)(nil)).Elem()
}

type DNSInput interface {
	pulumi.Input

	ToDNSOutput() DNSOutput
	ToDNSOutputWithContext(ctx context.Context) DNSOutput
}

func (*DNS) ElementType() reflect.Type {
	return reflect.TypeOf((*DNS)(nil))
}

func (i *DNS) ToDNSOutput() DNSOutput {
	return i.ToDNSOutputWithContext(context.Background())
}

func (i *DNS) ToDNSOutputWithContext(ctx context.Context) DNSOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DNSOutput)
}

func (i *DNS) ToDNSPtrOutput() DNSPtrOutput {
	return i.ToDNSPtrOutputWithContext(context.Background())
}

func (i *DNS) ToDNSPtrOutputWithContext(ctx context.Context) DNSPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DNSPtrOutput)
}

type DNSPtrInput interface {
	pulumi.Input

	ToDNSPtrOutput() DNSPtrOutput
	ToDNSPtrOutputWithContext(ctx context.Context) DNSPtrOutput
}

type dnsPtrType DNSArgs

func (*dnsPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**DNS)(nil))
}

func (i *dnsPtrType) ToDNSPtrOutput() DNSPtrOutput {
	return i.ToDNSPtrOutputWithContext(context.Background())
}

func (i *dnsPtrType) ToDNSPtrOutputWithContext(ctx context.Context) DNSPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DNSPtrOutput)
}

// DNSArrayInput is an input type that accepts DNSArray and DNSArrayOutput values.
// You can construct a concrete instance of `DNSArrayInput` via:
//
//          DNSArray{ DNSArgs{...} }
type DNSArrayInput interface {
	pulumi.Input

	ToDNSArrayOutput() DNSArrayOutput
	ToDNSArrayOutputWithContext(context.Context) DNSArrayOutput
}

type DNSArray []DNSInput

func (DNSArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*DNS)(nil)).Elem()
}

func (i DNSArray) ToDNSArrayOutput() DNSArrayOutput {
	return i.ToDNSArrayOutputWithContext(context.Background())
}

func (i DNSArray) ToDNSArrayOutputWithContext(ctx context.Context) DNSArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DNSArrayOutput)
}

// DNSMapInput is an input type that accepts DNSMap and DNSMapOutput values.
// You can construct a concrete instance of `DNSMapInput` via:
//
//          DNSMap{ "key": DNSArgs{...} }
type DNSMapInput interface {
	pulumi.Input

	ToDNSMapOutput() DNSMapOutput
	ToDNSMapOutputWithContext(context.Context) DNSMapOutput
}

type DNSMap map[string]DNSInput

func (DNSMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*DNS)(nil)).Elem()
}

func (i DNSMap) ToDNSMapOutput() DNSMapOutput {
	return i.ToDNSMapOutputWithContext(context.Background())
}

func (i DNSMap) ToDNSMapOutputWithContext(ctx context.Context) DNSMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DNSMapOutput)
}

type DNSOutput struct{ *pulumi.OutputState }

func (DNSOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*DNS)(nil))
}

func (o DNSOutput) ToDNSOutput() DNSOutput {
	return o
}

func (o DNSOutput) ToDNSOutputWithContext(ctx context.Context) DNSOutput {
	return o
}

func (o DNSOutput) ToDNSPtrOutput() DNSPtrOutput {
	return o.ToDNSPtrOutputWithContext(context.Background())
}

func (o DNSOutput) ToDNSPtrOutputWithContext(ctx context.Context) DNSPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v DNS) *DNS {
		return &v
	}).(DNSPtrOutput)
}

type DNSPtrOutput struct{ *pulumi.OutputState }

func (DNSPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**DNS)(nil))
}

func (o DNSPtrOutput) ToDNSPtrOutput() DNSPtrOutput {
	return o
}

func (o DNSPtrOutput) ToDNSPtrOutputWithContext(ctx context.Context) DNSPtrOutput {
	return o
}

func (o DNSPtrOutput) Elem() DNSOutput {
	return o.ApplyT(func(v *DNS) DNS {
		if v != nil {
			return *v
		}
		var ret DNS
		return ret
	}).(DNSOutput)
}

type DNSArrayOutput struct{ *pulumi.OutputState }

func (DNSArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]DNS)(nil))
}

func (o DNSArrayOutput) ToDNSArrayOutput() DNSArrayOutput {
	return o
}

func (o DNSArrayOutput) ToDNSArrayOutputWithContext(ctx context.Context) DNSArrayOutput {
	return o
}

func (o DNSArrayOutput) Index(i pulumi.IntInput) DNSOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) DNS {
		return vs[0].([]DNS)[vs[1].(int)]
	}).(DNSOutput)
}

type DNSMapOutput struct{ *pulumi.OutputState }

func (DNSMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]DNS)(nil))
}

func (o DNSMapOutput) ToDNSMapOutput() DNSMapOutput {
	return o
}

func (o DNSMapOutput) ToDNSMapOutputWithContext(ctx context.Context) DNSMapOutput {
	return o
}

func (o DNSMapOutput) MapIndex(k pulumi.StringInput) DNSOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) DNS {
		return vs[0].(map[string]DNS)[vs[1].(string)]
	}).(DNSOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*DNSInput)(nil)).Elem(), &DNS{})
	pulumi.RegisterInputType(reflect.TypeOf((*DNSPtrInput)(nil)).Elem(), &DNS{})
	pulumi.RegisterInputType(reflect.TypeOf((*DNSArrayInput)(nil)).Elem(), DNSArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*DNSMapInput)(nil)).Elem(), DNSMap{})
	pulumi.RegisterOutputType(DNSOutput{})
	pulumi.RegisterOutputType(DNSPtrOutput{})
	pulumi.RegisterOutputType(DNSArrayOutput{})
	pulumi.RegisterOutputType(DNSMapOutput{})
}
