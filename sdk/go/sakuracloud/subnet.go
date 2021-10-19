// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sakuracloud

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Manages a SakuraCloud Subnet.
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
// 		foobarInternet, err := sakuracloud.NewInternet(ctx, "foobarInternet", nil)
// 		if err != nil {
// 			return err
// 		}
// 		_, err = sakuracloud.NewSubnet(ctx, "foobarSubnet", &sakuracloud.SubnetArgs{
// 			InternetId: foobarInternet.ID(),
// 			NextHop:    foobarInternet.MinIpAddress,
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type Subnet struct {
	pulumi.CustomResourceState

	// The id of the switch+router resource that the subnet belongs. Changing this forces a new resource to be created.
	InternetId pulumi.StringOutput `pulumi:"internetId"`
	// A list of assigned global address to the subnet.
	IpAddresses pulumi.StringArrayOutput `pulumi:"ipAddresses"`
	// Maximum IP address in assigned global addresses to the subnet.
	MaxIpAddress pulumi.StringOutput `pulumi:"maxIpAddress"`
	// Minimum IP address in assigned global addresses to the subnet.
	MinIpAddress pulumi.StringOutput `pulumi:"minIpAddress"`
	// The bit length of the subnet to assign to the Subnet. This must be in the range [`26`-`28`]. Changing this forces a new resource to be created. Default:`28`.
	Netmask pulumi.IntPtrOutput `pulumi:"netmask"`
	// The IPv4 network address assigned to the Subnet.
	NetworkAddress pulumi.StringOutput `pulumi:"networkAddress"`
	// The ip address of the next-hop at the subnet.
	NextHop pulumi.StringOutput `pulumi:"nextHop"`
	// The id of the switch connected from the Subnet.
	SwitchId pulumi.StringOutput `pulumi:"switchId"`
	// The name of zone that the Subnet will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
	Zone pulumi.StringOutput `pulumi:"zone"`
}

// NewSubnet registers a new resource with the given unique name, arguments, and options.
func NewSubnet(ctx *pulumi.Context,
	name string, args *SubnetArgs, opts ...pulumi.ResourceOption) (*Subnet, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.InternetId == nil {
		return nil, errors.New("invalid value for required argument 'InternetId'")
	}
	if args.NextHop == nil {
		return nil, errors.New("invalid value for required argument 'NextHop'")
	}
	var resource Subnet
	err := ctx.RegisterResource("sakuracloud:index/subnet:Subnet", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSubnet gets an existing Subnet resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSubnet(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SubnetState, opts ...pulumi.ResourceOption) (*Subnet, error) {
	var resource Subnet
	err := ctx.ReadResource("sakuracloud:index/subnet:Subnet", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Subnet resources.
type subnetState struct {
	// The id of the switch+router resource that the subnet belongs. Changing this forces a new resource to be created.
	InternetId *string `pulumi:"internetId"`
	// A list of assigned global address to the subnet.
	IpAddresses []string `pulumi:"ipAddresses"`
	// Maximum IP address in assigned global addresses to the subnet.
	MaxIpAddress *string `pulumi:"maxIpAddress"`
	// Minimum IP address in assigned global addresses to the subnet.
	MinIpAddress *string `pulumi:"minIpAddress"`
	// The bit length of the subnet to assign to the Subnet. This must be in the range [`26`-`28`]. Changing this forces a new resource to be created. Default:`28`.
	Netmask *int `pulumi:"netmask"`
	// The IPv4 network address assigned to the Subnet.
	NetworkAddress *string `pulumi:"networkAddress"`
	// The ip address of the next-hop at the subnet.
	NextHop *string `pulumi:"nextHop"`
	// The id of the switch connected from the Subnet.
	SwitchId *string `pulumi:"switchId"`
	// The name of zone that the Subnet will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
	Zone *string `pulumi:"zone"`
}

type SubnetState struct {
	// The id of the switch+router resource that the subnet belongs. Changing this forces a new resource to be created.
	InternetId pulumi.StringPtrInput
	// A list of assigned global address to the subnet.
	IpAddresses pulumi.StringArrayInput
	// Maximum IP address in assigned global addresses to the subnet.
	MaxIpAddress pulumi.StringPtrInput
	// Minimum IP address in assigned global addresses to the subnet.
	MinIpAddress pulumi.StringPtrInput
	// The bit length of the subnet to assign to the Subnet. This must be in the range [`26`-`28`]. Changing this forces a new resource to be created. Default:`28`.
	Netmask pulumi.IntPtrInput
	// The IPv4 network address assigned to the Subnet.
	NetworkAddress pulumi.StringPtrInput
	// The ip address of the next-hop at the subnet.
	NextHop pulumi.StringPtrInput
	// The id of the switch connected from the Subnet.
	SwitchId pulumi.StringPtrInput
	// The name of zone that the Subnet will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
	Zone pulumi.StringPtrInput
}

func (SubnetState) ElementType() reflect.Type {
	return reflect.TypeOf((*subnetState)(nil)).Elem()
}

type subnetArgs struct {
	// The id of the switch+router resource that the subnet belongs. Changing this forces a new resource to be created.
	InternetId string `pulumi:"internetId"`
	// The bit length of the subnet to assign to the Subnet. This must be in the range [`26`-`28`]. Changing this forces a new resource to be created. Default:`28`.
	Netmask *int `pulumi:"netmask"`
	// The ip address of the next-hop at the subnet.
	NextHop string `pulumi:"nextHop"`
	// The name of zone that the Subnet will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
	Zone *string `pulumi:"zone"`
}

// The set of arguments for constructing a Subnet resource.
type SubnetArgs struct {
	// The id of the switch+router resource that the subnet belongs. Changing this forces a new resource to be created.
	InternetId pulumi.StringInput
	// The bit length of the subnet to assign to the Subnet. This must be in the range [`26`-`28`]. Changing this forces a new resource to be created. Default:`28`.
	Netmask pulumi.IntPtrInput
	// The ip address of the next-hop at the subnet.
	NextHop pulumi.StringInput
	// The name of zone that the Subnet will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
	Zone pulumi.StringPtrInput
}

func (SubnetArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*subnetArgs)(nil)).Elem()
}

type SubnetInput interface {
	pulumi.Input

	ToSubnetOutput() SubnetOutput
	ToSubnetOutputWithContext(ctx context.Context) SubnetOutput
}

func (*Subnet) ElementType() reflect.Type {
	return reflect.TypeOf((*Subnet)(nil))
}

func (i *Subnet) ToSubnetOutput() SubnetOutput {
	return i.ToSubnetOutputWithContext(context.Background())
}

func (i *Subnet) ToSubnetOutputWithContext(ctx context.Context) SubnetOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SubnetOutput)
}

func (i *Subnet) ToSubnetPtrOutput() SubnetPtrOutput {
	return i.ToSubnetPtrOutputWithContext(context.Background())
}

func (i *Subnet) ToSubnetPtrOutputWithContext(ctx context.Context) SubnetPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SubnetPtrOutput)
}

type SubnetPtrInput interface {
	pulumi.Input

	ToSubnetPtrOutput() SubnetPtrOutput
	ToSubnetPtrOutputWithContext(ctx context.Context) SubnetPtrOutput
}

type subnetPtrType SubnetArgs

func (*subnetPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**Subnet)(nil))
}

func (i *subnetPtrType) ToSubnetPtrOutput() SubnetPtrOutput {
	return i.ToSubnetPtrOutputWithContext(context.Background())
}

func (i *subnetPtrType) ToSubnetPtrOutputWithContext(ctx context.Context) SubnetPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SubnetPtrOutput)
}

// SubnetArrayInput is an input type that accepts SubnetArray and SubnetArrayOutput values.
// You can construct a concrete instance of `SubnetArrayInput` via:
//
//          SubnetArray{ SubnetArgs{...} }
type SubnetArrayInput interface {
	pulumi.Input

	ToSubnetArrayOutput() SubnetArrayOutput
	ToSubnetArrayOutputWithContext(context.Context) SubnetArrayOutput
}

type SubnetArray []SubnetInput

func (SubnetArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Subnet)(nil)).Elem()
}

func (i SubnetArray) ToSubnetArrayOutput() SubnetArrayOutput {
	return i.ToSubnetArrayOutputWithContext(context.Background())
}

func (i SubnetArray) ToSubnetArrayOutputWithContext(ctx context.Context) SubnetArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SubnetArrayOutput)
}

// SubnetMapInput is an input type that accepts SubnetMap and SubnetMapOutput values.
// You can construct a concrete instance of `SubnetMapInput` via:
//
//          SubnetMap{ "key": SubnetArgs{...} }
type SubnetMapInput interface {
	pulumi.Input

	ToSubnetMapOutput() SubnetMapOutput
	ToSubnetMapOutputWithContext(context.Context) SubnetMapOutput
}

type SubnetMap map[string]SubnetInput

func (SubnetMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Subnet)(nil)).Elem()
}

func (i SubnetMap) ToSubnetMapOutput() SubnetMapOutput {
	return i.ToSubnetMapOutputWithContext(context.Background())
}

func (i SubnetMap) ToSubnetMapOutputWithContext(ctx context.Context) SubnetMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SubnetMapOutput)
}

type SubnetOutput struct{ *pulumi.OutputState }

func (SubnetOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Subnet)(nil))
}

func (o SubnetOutput) ToSubnetOutput() SubnetOutput {
	return o
}

func (o SubnetOutput) ToSubnetOutputWithContext(ctx context.Context) SubnetOutput {
	return o
}

func (o SubnetOutput) ToSubnetPtrOutput() SubnetPtrOutput {
	return o.ToSubnetPtrOutputWithContext(context.Background())
}

func (o SubnetOutput) ToSubnetPtrOutputWithContext(ctx context.Context) SubnetPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v Subnet) *Subnet {
		return &v
	}).(SubnetPtrOutput)
}

type SubnetPtrOutput struct{ *pulumi.OutputState }

func (SubnetPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Subnet)(nil))
}

func (o SubnetPtrOutput) ToSubnetPtrOutput() SubnetPtrOutput {
	return o
}

func (o SubnetPtrOutput) ToSubnetPtrOutputWithContext(ctx context.Context) SubnetPtrOutput {
	return o
}

func (o SubnetPtrOutput) Elem() SubnetOutput {
	return o.ApplyT(func(v *Subnet) Subnet {
		if v != nil {
			return *v
		}
		var ret Subnet
		return ret
	}).(SubnetOutput)
}

type SubnetArrayOutput struct{ *pulumi.OutputState }

func (SubnetArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]Subnet)(nil))
}

func (o SubnetArrayOutput) ToSubnetArrayOutput() SubnetArrayOutput {
	return o
}

func (o SubnetArrayOutput) ToSubnetArrayOutputWithContext(ctx context.Context) SubnetArrayOutput {
	return o
}

func (o SubnetArrayOutput) Index(i pulumi.IntInput) SubnetOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) Subnet {
		return vs[0].([]Subnet)[vs[1].(int)]
	}).(SubnetOutput)
}

type SubnetMapOutput struct{ *pulumi.OutputState }

func (SubnetMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]Subnet)(nil))
}

func (o SubnetMapOutput) ToSubnetMapOutput() SubnetMapOutput {
	return o
}

func (o SubnetMapOutput) ToSubnetMapOutputWithContext(ctx context.Context) SubnetMapOutput {
	return o
}

func (o SubnetMapOutput) MapIndex(k pulumi.StringInput) SubnetOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) Subnet {
		return vs[0].(map[string]Subnet)[vs[1].(string)]
	}).(SubnetOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*SubnetInput)(nil)).Elem(), &Subnet{})
	pulumi.RegisterInputType(reflect.TypeOf((*SubnetPtrInput)(nil)).Elem(), &Subnet{})
	pulumi.RegisterInputType(reflect.TypeOf((*SubnetArrayInput)(nil)).Elem(), SubnetArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*SubnetMapInput)(nil)).Elem(), SubnetMap{})
	pulumi.RegisterOutputType(SubnetOutput{})
	pulumi.RegisterOutputType(SubnetPtrOutput{})
	pulumi.RegisterOutputType(SubnetArrayOutput{})
	pulumi.RegisterOutputType(SubnetMapOutput{})
}
