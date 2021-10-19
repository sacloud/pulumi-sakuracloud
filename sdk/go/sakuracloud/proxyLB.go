// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sakuracloud

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Manages a SakuraCloud ProxyLB.
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
// 		foobarServer, err := sakuracloud.NewServer(ctx, "foobarServer", &sakuracloud.ServerArgs{
// 			NetworkInterfaces: ServerNetworkInterfaceArray{
// 				&ServerNetworkInterfaceArgs{
// 					Upstream: pulumi.String("shared"),
// 				},
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = sakuracloud.NewProxyLB(ctx, "foobarProxyLB", &sakuracloud.ProxyLBArgs{
// 			Plan:          pulumi.Int(100),
// 			VipFailover:   pulumi.Bool(true),
// 			StickySession: pulumi.Bool(true),
// 			Gzip:          pulumi.Bool(true),
// 			ProxyProtocol: pulumi.Bool(true),
// 			Timeout:       pulumi.Int(10),
// 			Region:        pulumi.String("is1"),
// 			HealthCheck: &ProxyLBHealthCheckArgs{
// 				Protocol:   pulumi.String("http"),
// 				DelayLoop:  pulumi.Int(10),
// 				HostHeader: pulumi.String("example.com"),
// 				Path:       pulumi.String("/"),
// 			},
// 			SorryServer: &ProxyLBSorryServerArgs{
// 				IpAddress: pulumi.String("192.0.2.1"),
// 				Port:      pulumi.Int(80),
// 			},
// 			Syslog: &ProxyLBSyslogArgs{
// 				Server: pulumi.String("192.0.2.1"),
// 				Port:   pulumi.Int(514),
// 			},
// 			BindPorts: ProxyLBBindPortArray{
// 				&ProxyLBBindPortArgs{
// 					ProxyMode: pulumi.String("http"),
// 					Port:      pulumi.Int(80),
// 					ResponseHeaders: ProxyLBBindPortResponseHeaderArray{
// 						&ProxyLBBindPortResponseHeaderArgs{
// 							Header: pulumi.String("Cache-Control"),
// 							Value:  pulumi.String("public, max-age=10"),
// 						},
// 					},
// 				},
// 			},
// 			Servers: ProxyLBServerArray{
// 				&ProxyLBServerArgs{
// 					IpAddress: foobarServer.IpAddress,
// 					Port:      pulumi.Int(80),
// 					Group:     pulumi.String("group1"),
// 				},
// 			},
// 			Rules: ProxyLBRuleArray{
// 				&ProxyLBRuleArgs{
// 					Action: pulumi.String("forward"),
// 					Host:   pulumi.String("www.example.com"),
// 					Path:   pulumi.String("/"),
// 					Group:  pulumi.String("group1"),
// 				},
// 				&ProxyLBRuleArgs{
// 					Action:             pulumi.String("redirect"),
// 					Host:               pulumi.String("www2.example.com"),
// 					Path:               pulumi.String("/"),
// 					Group:              pulumi.String("group1"),
// 					RedirectLocation:   pulumi.String("https://redirect.example.com"),
// 					RedirectStatusCode: pulumi.String("301"),
// 				},
// 				&ProxyLBRuleArgs{
// 					Action:           pulumi.String("fixed"),
// 					Host:             pulumi.String("www3.example.com"),
// 					Path:             pulumi.String("/"),
// 					Group:            pulumi.String("group1"),
// 					FixedStatusCode:  pulumi.String("200"),
// 					FixedContentType: pulumi.String("text/plain"),
// 					FixedMessageBody: pulumi.String("body"),
// 				},
// 			},
// 			Description: pulumi.String("description"),
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
type ProxyLB struct {
	pulumi.CustomResourceState

	// One or more `bindPort` blocks as defined below.
	BindPorts ProxyLBBindPortArrayOutput `pulumi:"bindPorts"`
	// An `certificate` block as defined below.
	Certificate ProxyLBCertificateOutput `pulumi:"certificate"`
	// The description of the ProxyLB. The length of this value must be in the range [`1`-`512`].
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The FQDN for accessing to the ProxyLB. This is typically used as value of CNAME record.
	Fqdn pulumi.StringOutput `pulumi:"fqdn"`
	// The flag to enable gzip compression.
	Gzip pulumi.BoolPtrOutput `pulumi:"gzip"`
	// A `healthCheck` block as defined below.
	HealthCheck ProxyLBHealthCheckOutput `pulumi:"healthCheck"`
	// The icon id to attach to the ProxyLB.
	IconId pulumi.StringPtrOutput `pulumi:"iconId"`
	// The name of the ProxyLB. The length of this value must be in the range [`1`-`64`].
	Name pulumi.StringOutput `pulumi:"name"`
	// The plan name of the ProxyLB. This must be one of [`100`/`500`/`1000`/`5000`/`10000`/`50000`/`100000`]. Default:`100`.
	Plan pulumi.IntPtrOutput `pulumi:"plan"`
	// A list of CIDR block used by the ProxyLB to access the server.
	ProxyNetworks pulumi.StringArrayOutput `pulumi:"proxyNetworks"`
	// The flag to enable proxy protocol v2.
	ProxyProtocol pulumi.BoolPtrOutput `pulumi:"proxyProtocol"`
	// The name of region that the proxy LB is in. This must be one of [`tk1`/`is1`/`anycast`]. Changing this forces a new resource to be created. Default:`is1`.
	Region pulumi.StringPtrOutput `pulumi:"region"`
	// One or more `rule` blocks as defined below.
	Rules ProxyLBRuleArrayOutput `pulumi:"rules"`
	// One or more `server` blocks as defined below.
	Servers ProxyLBServerArrayOutput `pulumi:"servers"`
	// A `sorryServer` block as defined below.
	SorryServer ProxyLBSorryServerPtrOutput `pulumi:"sorryServer"`
	// The flag to enable sticky session.
	StickySession pulumi.BoolPtrOutput `pulumi:"stickySession"`
	// A `syslog` block as defined below.
	Syslog ProxyLBSyslogOutput `pulumi:"syslog"`
	// Any tags to assign to the ProxyLB.
	Tags pulumi.StringArrayOutput `pulumi:"tags"`
	// The timeout duration in seconds. Default:`10`.
	Timeout pulumi.IntPtrOutput `pulumi:"timeout"`
	// The virtual IP address assigned to the ProxyLB.
	Vip pulumi.StringOutput `pulumi:"vip"`
	// The flag to enable VIP fail-over. Changing this forces a new resource to be created.
	VipFailover pulumi.BoolPtrOutput `pulumi:"vipFailover"`
}

// NewProxyLB registers a new resource with the given unique name, arguments, and options.
func NewProxyLB(ctx *pulumi.Context,
	name string, args *ProxyLBArgs, opts ...pulumi.ResourceOption) (*ProxyLB, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.BindPorts == nil {
		return nil, errors.New("invalid value for required argument 'BindPorts'")
	}
	if args.HealthCheck == nil {
		return nil, errors.New("invalid value for required argument 'HealthCheck'")
	}
	var resource ProxyLB
	err := ctx.RegisterResource("sakuracloud:index/proxyLB:ProxyLB", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetProxyLB gets an existing ProxyLB resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetProxyLB(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ProxyLBState, opts ...pulumi.ResourceOption) (*ProxyLB, error) {
	var resource ProxyLB
	err := ctx.ReadResource("sakuracloud:index/proxyLB:ProxyLB", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ProxyLB resources.
type proxyLBState struct {
	// One or more `bindPort` blocks as defined below.
	BindPorts []ProxyLBBindPort `pulumi:"bindPorts"`
	// An `certificate` block as defined below.
	Certificate *ProxyLBCertificate `pulumi:"certificate"`
	// The description of the ProxyLB. The length of this value must be in the range [`1`-`512`].
	Description *string `pulumi:"description"`
	// The FQDN for accessing to the ProxyLB. This is typically used as value of CNAME record.
	Fqdn *string `pulumi:"fqdn"`
	// The flag to enable gzip compression.
	Gzip *bool `pulumi:"gzip"`
	// A `healthCheck` block as defined below.
	HealthCheck *ProxyLBHealthCheck `pulumi:"healthCheck"`
	// The icon id to attach to the ProxyLB.
	IconId *string `pulumi:"iconId"`
	// The name of the ProxyLB. The length of this value must be in the range [`1`-`64`].
	Name *string `pulumi:"name"`
	// The plan name of the ProxyLB. This must be one of [`100`/`500`/`1000`/`5000`/`10000`/`50000`/`100000`]. Default:`100`.
	Plan *int `pulumi:"plan"`
	// A list of CIDR block used by the ProxyLB to access the server.
	ProxyNetworks []string `pulumi:"proxyNetworks"`
	// The flag to enable proxy protocol v2.
	ProxyProtocol *bool `pulumi:"proxyProtocol"`
	// The name of region that the proxy LB is in. This must be one of [`tk1`/`is1`/`anycast`]. Changing this forces a new resource to be created. Default:`is1`.
	Region *string `pulumi:"region"`
	// One or more `rule` blocks as defined below.
	Rules []ProxyLBRule `pulumi:"rules"`
	// One or more `server` blocks as defined below.
	Servers []ProxyLBServer `pulumi:"servers"`
	// A `sorryServer` block as defined below.
	SorryServer *ProxyLBSorryServer `pulumi:"sorryServer"`
	// The flag to enable sticky session.
	StickySession *bool `pulumi:"stickySession"`
	// A `syslog` block as defined below.
	Syslog *ProxyLBSyslog `pulumi:"syslog"`
	// Any tags to assign to the ProxyLB.
	Tags []string `pulumi:"tags"`
	// The timeout duration in seconds. Default:`10`.
	Timeout *int `pulumi:"timeout"`
	// The virtual IP address assigned to the ProxyLB.
	Vip *string `pulumi:"vip"`
	// The flag to enable VIP fail-over. Changing this forces a new resource to be created.
	VipFailover *bool `pulumi:"vipFailover"`
}

type ProxyLBState struct {
	// One or more `bindPort` blocks as defined below.
	BindPorts ProxyLBBindPortArrayInput
	// An `certificate` block as defined below.
	Certificate ProxyLBCertificatePtrInput
	// The description of the ProxyLB. The length of this value must be in the range [`1`-`512`].
	Description pulumi.StringPtrInput
	// The FQDN for accessing to the ProxyLB. This is typically used as value of CNAME record.
	Fqdn pulumi.StringPtrInput
	// The flag to enable gzip compression.
	Gzip pulumi.BoolPtrInput
	// A `healthCheck` block as defined below.
	HealthCheck ProxyLBHealthCheckPtrInput
	// The icon id to attach to the ProxyLB.
	IconId pulumi.StringPtrInput
	// The name of the ProxyLB. The length of this value must be in the range [`1`-`64`].
	Name pulumi.StringPtrInput
	// The plan name of the ProxyLB. This must be one of [`100`/`500`/`1000`/`5000`/`10000`/`50000`/`100000`]. Default:`100`.
	Plan pulumi.IntPtrInput
	// A list of CIDR block used by the ProxyLB to access the server.
	ProxyNetworks pulumi.StringArrayInput
	// The flag to enable proxy protocol v2.
	ProxyProtocol pulumi.BoolPtrInput
	// The name of region that the proxy LB is in. This must be one of [`tk1`/`is1`/`anycast`]. Changing this forces a new resource to be created. Default:`is1`.
	Region pulumi.StringPtrInput
	// One or more `rule` blocks as defined below.
	Rules ProxyLBRuleArrayInput
	// One or more `server` blocks as defined below.
	Servers ProxyLBServerArrayInput
	// A `sorryServer` block as defined below.
	SorryServer ProxyLBSorryServerPtrInput
	// The flag to enable sticky session.
	StickySession pulumi.BoolPtrInput
	// A `syslog` block as defined below.
	Syslog ProxyLBSyslogPtrInput
	// Any tags to assign to the ProxyLB.
	Tags pulumi.StringArrayInput
	// The timeout duration in seconds. Default:`10`.
	Timeout pulumi.IntPtrInput
	// The virtual IP address assigned to the ProxyLB.
	Vip pulumi.StringPtrInput
	// The flag to enable VIP fail-over. Changing this forces a new resource to be created.
	VipFailover pulumi.BoolPtrInput
}

func (ProxyLBState) ElementType() reflect.Type {
	return reflect.TypeOf((*proxyLBState)(nil)).Elem()
}

type proxyLBArgs struct {
	// One or more `bindPort` blocks as defined below.
	BindPorts []ProxyLBBindPort `pulumi:"bindPorts"`
	// An `certificate` block as defined below.
	Certificate *ProxyLBCertificate `pulumi:"certificate"`
	// The description of the ProxyLB. The length of this value must be in the range [`1`-`512`].
	Description *string `pulumi:"description"`
	// The flag to enable gzip compression.
	Gzip *bool `pulumi:"gzip"`
	// A `healthCheck` block as defined below.
	HealthCheck ProxyLBHealthCheck `pulumi:"healthCheck"`
	// The icon id to attach to the ProxyLB.
	IconId *string `pulumi:"iconId"`
	// The name of the ProxyLB. The length of this value must be in the range [`1`-`64`].
	Name *string `pulumi:"name"`
	// The plan name of the ProxyLB. This must be one of [`100`/`500`/`1000`/`5000`/`10000`/`50000`/`100000`]. Default:`100`.
	Plan *int `pulumi:"plan"`
	// The flag to enable proxy protocol v2.
	ProxyProtocol *bool `pulumi:"proxyProtocol"`
	// The name of region that the proxy LB is in. This must be one of [`tk1`/`is1`/`anycast`]. Changing this forces a new resource to be created. Default:`is1`.
	Region *string `pulumi:"region"`
	// One or more `rule` blocks as defined below.
	Rules []ProxyLBRule `pulumi:"rules"`
	// One or more `server` blocks as defined below.
	Servers []ProxyLBServer `pulumi:"servers"`
	// A `sorryServer` block as defined below.
	SorryServer *ProxyLBSorryServer `pulumi:"sorryServer"`
	// The flag to enable sticky session.
	StickySession *bool `pulumi:"stickySession"`
	// A `syslog` block as defined below.
	Syslog *ProxyLBSyslog `pulumi:"syslog"`
	// Any tags to assign to the ProxyLB.
	Tags []string `pulumi:"tags"`
	// The timeout duration in seconds. Default:`10`.
	Timeout *int `pulumi:"timeout"`
	// The flag to enable VIP fail-over. Changing this forces a new resource to be created.
	VipFailover *bool `pulumi:"vipFailover"`
}

// The set of arguments for constructing a ProxyLB resource.
type ProxyLBArgs struct {
	// One or more `bindPort` blocks as defined below.
	BindPorts ProxyLBBindPortArrayInput
	// An `certificate` block as defined below.
	Certificate ProxyLBCertificatePtrInput
	// The description of the ProxyLB. The length of this value must be in the range [`1`-`512`].
	Description pulumi.StringPtrInput
	// The flag to enable gzip compression.
	Gzip pulumi.BoolPtrInput
	// A `healthCheck` block as defined below.
	HealthCheck ProxyLBHealthCheckInput
	// The icon id to attach to the ProxyLB.
	IconId pulumi.StringPtrInput
	// The name of the ProxyLB. The length of this value must be in the range [`1`-`64`].
	Name pulumi.StringPtrInput
	// The plan name of the ProxyLB. This must be one of [`100`/`500`/`1000`/`5000`/`10000`/`50000`/`100000`]. Default:`100`.
	Plan pulumi.IntPtrInput
	// The flag to enable proxy protocol v2.
	ProxyProtocol pulumi.BoolPtrInput
	// The name of region that the proxy LB is in. This must be one of [`tk1`/`is1`/`anycast`]. Changing this forces a new resource to be created. Default:`is1`.
	Region pulumi.StringPtrInput
	// One or more `rule` blocks as defined below.
	Rules ProxyLBRuleArrayInput
	// One or more `server` blocks as defined below.
	Servers ProxyLBServerArrayInput
	// A `sorryServer` block as defined below.
	SorryServer ProxyLBSorryServerPtrInput
	// The flag to enable sticky session.
	StickySession pulumi.BoolPtrInput
	// A `syslog` block as defined below.
	Syslog ProxyLBSyslogPtrInput
	// Any tags to assign to the ProxyLB.
	Tags pulumi.StringArrayInput
	// The timeout duration in seconds. Default:`10`.
	Timeout pulumi.IntPtrInput
	// The flag to enable VIP fail-over. Changing this forces a new resource to be created.
	VipFailover pulumi.BoolPtrInput
}

func (ProxyLBArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*proxyLBArgs)(nil)).Elem()
}

type ProxyLBInput interface {
	pulumi.Input

	ToProxyLBOutput() ProxyLBOutput
	ToProxyLBOutputWithContext(ctx context.Context) ProxyLBOutput
}

func (*ProxyLB) ElementType() reflect.Type {
	return reflect.TypeOf((*ProxyLB)(nil))
}

func (i *ProxyLB) ToProxyLBOutput() ProxyLBOutput {
	return i.ToProxyLBOutputWithContext(context.Background())
}

func (i *ProxyLB) ToProxyLBOutputWithContext(ctx context.Context) ProxyLBOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ProxyLBOutput)
}

func (i *ProxyLB) ToProxyLBPtrOutput() ProxyLBPtrOutput {
	return i.ToProxyLBPtrOutputWithContext(context.Background())
}

func (i *ProxyLB) ToProxyLBPtrOutputWithContext(ctx context.Context) ProxyLBPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ProxyLBPtrOutput)
}

type ProxyLBPtrInput interface {
	pulumi.Input

	ToProxyLBPtrOutput() ProxyLBPtrOutput
	ToProxyLBPtrOutputWithContext(ctx context.Context) ProxyLBPtrOutput
}

type proxyLBPtrType ProxyLBArgs

func (*proxyLBPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**ProxyLB)(nil))
}

func (i *proxyLBPtrType) ToProxyLBPtrOutput() ProxyLBPtrOutput {
	return i.ToProxyLBPtrOutputWithContext(context.Background())
}

func (i *proxyLBPtrType) ToProxyLBPtrOutputWithContext(ctx context.Context) ProxyLBPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ProxyLBPtrOutput)
}

// ProxyLBArrayInput is an input type that accepts ProxyLBArray and ProxyLBArrayOutput values.
// You can construct a concrete instance of `ProxyLBArrayInput` via:
//
//          ProxyLBArray{ ProxyLBArgs{...} }
type ProxyLBArrayInput interface {
	pulumi.Input

	ToProxyLBArrayOutput() ProxyLBArrayOutput
	ToProxyLBArrayOutputWithContext(context.Context) ProxyLBArrayOutput
}

type ProxyLBArray []ProxyLBInput

func (ProxyLBArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*ProxyLB)(nil)).Elem()
}

func (i ProxyLBArray) ToProxyLBArrayOutput() ProxyLBArrayOutput {
	return i.ToProxyLBArrayOutputWithContext(context.Background())
}

func (i ProxyLBArray) ToProxyLBArrayOutputWithContext(ctx context.Context) ProxyLBArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ProxyLBArrayOutput)
}

// ProxyLBMapInput is an input type that accepts ProxyLBMap and ProxyLBMapOutput values.
// You can construct a concrete instance of `ProxyLBMapInput` via:
//
//          ProxyLBMap{ "key": ProxyLBArgs{...} }
type ProxyLBMapInput interface {
	pulumi.Input

	ToProxyLBMapOutput() ProxyLBMapOutput
	ToProxyLBMapOutputWithContext(context.Context) ProxyLBMapOutput
}

type ProxyLBMap map[string]ProxyLBInput

func (ProxyLBMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*ProxyLB)(nil)).Elem()
}

func (i ProxyLBMap) ToProxyLBMapOutput() ProxyLBMapOutput {
	return i.ToProxyLBMapOutputWithContext(context.Background())
}

func (i ProxyLBMap) ToProxyLBMapOutputWithContext(ctx context.Context) ProxyLBMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ProxyLBMapOutput)
}

type ProxyLBOutput struct{ *pulumi.OutputState }

func (ProxyLBOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ProxyLB)(nil))
}

func (o ProxyLBOutput) ToProxyLBOutput() ProxyLBOutput {
	return o
}

func (o ProxyLBOutput) ToProxyLBOutputWithContext(ctx context.Context) ProxyLBOutput {
	return o
}

func (o ProxyLBOutput) ToProxyLBPtrOutput() ProxyLBPtrOutput {
	return o.ToProxyLBPtrOutputWithContext(context.Background())
}

func (o ProxyLBOutput) ToProxyLBPtrOutputWithContext(ctx context.Context) ProxyLBPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v ProxyLB) *ProxyLB {
		return &v
	}).(ProxyLBPtrOutput)
}

type ProxyLBPtrOutput struct{ *pulumi.OutputState }

func (ProxyLBPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ProxyLB)(nil))
}

func (o ProxyLBPtrOutput) ToProxyLBPtrOutput() ProxyLBPtrOutput {
	return o
}

func (o ProxyLBPtrOutput) ToProxyLBPtrOutputWithContext(ctx context.Context) ProxyLBPtrOutput {
	return o
}

func (o ProxyLBPtrOutput) Elem() ProxyLBOutput {
	return o.ApplyT(func(v *ProxyLB) ProxyLB {
		if v != nil {
			return *v
		}
		var ret ProxyLB
		return ret
	}).(ProxyLBOutput)
}

type ProxyLBArrayOutput struct{ *pulumi.OutputState }

func (ProxyLBArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]ProxyLB)(nil))
}

func (o ProxyLBArrayOutput) ToProxyLBArrayOutput() ProxyLBArrayOutput {
	return o
}

func (o ProxyLBArrayOutput) ToProxyLBArrayOutputWithContext(ctx context.Context) ProxyLBArrayOutput {
	return o
}

func (o ProxyLBArrayOutput) Index(i pulumi.IntInput) ProxyLBOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) ProxyLB {
		return vs[0].([]ProxyLB)[vs[1].(int)]
	}).(ProxyLBOutput)
}

type ProxyLBMapOutput struct{ *pulumi.OutputState }

func (ProxyLBMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]ProxyLB)(nil))
}

func (o ProxyLBMapOutput) ToProxyLBMapOutput() ProxyLBMapOutput {
	return o
}

func (o ProxyLBMapOutput) ToProxyLBMapOutputWithContext(ctx context.Context) ProxyLBMapOutput {
	return o
}

func (o ProxyLBMapOutput) MapIndex(k pulumi.StringInput) ProxyLBOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) ProxyLB {
		return vs[0].(map[string]ProxyLB)[vs[1].(string)]
	}).(ProxyLBOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ProxyLBInput)(nil)).Elem(), &ProxyLB{})
	pulumi.RegisterInputType(reflect.TypeOf((*ProxyLBPtrInput)(nil)).Elem(), &ProxyLB{})
	pulumi.RegisterInputType(reflect.TypeOf((*ProxyLBArrayInput)(nil)).Elem(), ProxyLBArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*ProxyLBMapInput)(nil)).Elem(), ProxyLBMap{})
	pulumi.RegisterOutputType(ProxyLBOutput{})
	pulumi.RegisterOutputType(ProxyLBPtrOutput{})
	pulumi.RegisterOutputType(ProxyLBArrayOutput{})
	pulumi.RegisterOutputType(ProxyLBMapOutput{})
}
