// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sakuracloud

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Manages a SakuraCloud Database Read Replica.
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
// 		master, err := sakuracloud.LookupDatabase(ctx, &GetDatabaseArgs{
// 			Filter: GetDatabaseFilter{
// 				Names: []string{
// 					"master-database-name",
// 				},
// 			},
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		_, err = sakuracloud.NewDatabaseReadReplica(ctx, "foobar", &sakuracloud.DatabaseReadReplicaArgs{
// 			MasterId: pulumi.String(master.Id),
// 			NetworkInterface: &DatabaseReadReplicaNetworkInterfaceArgs{
// 				IpAddress: pulumi.String("192.168.11.111"),
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
type DatabaseReadReplica struct {
	pulumi.CustomResourceState

	// The description of the read-replica database. The length of this value must be in the range [`1`-`512`].
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The icon id to attach to the read-replica database.
	IconId pulumi.StringPtrOutput `pulumi:"iconId"`
	// The id of the replication master database. Changing this forces a new resource to be created.
	MasterId pulumi.StringOutput `pulumi:"masterId"`
	// The name of the read-replica database. The length of this value must be in the range [`1`-`64`].
	Name pulumi.StringOutput `pulumi:"name"`
	// An `networkInterface` block as defined below.
	NetworkInterface DatabaseReadReplicaNetworkInterfaceOutput `pulumi:"networkInterface"`
	// Any tags to assign to the read-replica database.
	Tags pulumi.StringArrayOutput `pulumi:"tags"`
	// The name of zone that the read-replica database will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
	Zone pulumi.StringOutput `pulumi:"zone"`
}

// NewDatabaseReadReplica registers a new resource with the given unique name, arguments, and options.
func NewDatabaseReadReplica(ctx *pulumi.Context,
	name string, args *DatabaseReadReplicaArgs, opts ...pulumi.ResourceOption) (*DatabaseReadReplica, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.MasterId == nil {
		return nil, errors.New("invalid value for required argument 'MasterId'")
	}
	if args.NetworkInterface == nil {
		return nil, errors.New("invalid value for required argument 'NetworkInterface'")
	}
	var resource DatabaseReadReplica
	err := ctx.RegisterResource("sakuracloud:index/databaseReadReplica:DatabaseReadReplica", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDatabaseReadReplica gets an existing DatabaseReadReplica resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDatabaseReadReplica(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DatabaseReadReplicaState, opts ...pulumi.ResourceOption) (*DatabaseReadReplica, error) {
	var resource DatabaseReadReplica
	err := ctx.ReadResource("sakuracloud:index/databaseReadReplica:DatabaseReadReplica", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering DatabaseReadReplica resources.
type databaseReadReplicaState struct {
	// The description of the read-replica database. The length of this value must be in the range [`1`-`512`].
	Description *string `pulumi:"description"`
	// The icon id to attach to the read-replica database.
	IconId *string `pulumi:"iconId"`
	// The id of the replication master database. Changing this forces a new resource to be created.
	MasterId *string `pulumi:"masterId"`
	// The name of the read-replica database. The length of this value must be in the range [`1`-`64`].
	Name *string `pulumi:"name"`
	// An `networkInterface` block as defined below.
	NetworkInterface *DatabaseReadReplicaNetworkInterface `pulumi:"networkInterface"`
	// Any tags to assign to the read-replica database.
	Tags []string `pulumi:"tags"`
	// The name of zone that the read-replica database will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
	Zone *string `pulumi:"zone"`
}

type DatabaseReadReplicaState struct {
	// The description of the read-replica database. The length of this value must be in the range [`1`-`512`].
	Description pulumi.StringPtrInput
	// The icon id to attach to the read-replica database.
	IconId pulumi.StringPtrInput
	// The id of the replication master database. Changing this forces a new resource to be created.
	MasterId pulumi.StringPtrInput
	// The name of the read-replica database. The length of this value must be in the range [`1`-`64`].
	Name pulumi.StringPtrInput
	// An `networkInterface` block as defined below.
	NetworkInterface DatabaseReadReplicaNetworkInterfacePtrInput
	// Any tags to assign to the read-replica database.
	Tags pulumi.StringArrayInput
	// The name of zone that the read-replica database will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
	Zone pulumi.StringPtrInput
}

func (DatabaseReadReplicaState) ElementType() reflect.Type {
	return reflect.TypeOf((*databaseReadReplicaState)(nil)).Elem()
}

type databaseReadReplicaArgs struct {
	// The description of the read-replica database. The length of this value must be in the range [`1`-`512`].
	Description *string `pulumi:"description"`
	// The icon id to attach to the read-replica database.
	IconId *string `pulumi:"iconId"`
	// The id of the replication master database. Changing this forces a new resource to be created.
	MasterId string `pulumi:"masterId"`
	// The name of the read-replica database. The length of this value must be in the range [`1`-`64`].
	Name *string `pulumi:"name"`
	// An `networkInterface` block as defined below.
	NetworkInterface DatabaseReadReplicaNetworkInterface `pulumi:"networkInterface"`
	// Any tags to assign to the read-replica database.
	Tags []string `pulumi:"tags"`
	// The name of zone that the read-replica database will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
	Zone *string `pulumi:"zone"`
}

// The set of arguments for constructing a DatabaseReadReplica resource.
type DatabaseReadReplicaArgs struct {
	// The description of the read-replica database. The length of this value must be in the range [`1`-`512`].
	Description pulumi.StringPtrInput
	// The icon id to attach to the read-replica database.
	IconId pulumi.StringPtrInput
	// The id of the replication master database. Changing this forces a new resource to be created.
	MasterId pulumi.StringInput
	// The name of the read-replica database. The length of this value must be in the range [`1`-`64`].
	Name pulumi.StringPtrInput
	// An `networkInterface` block as defined below.
	NetworkInterface DatabaseReadReplicaNetworkInterfaceInput
	// Any tags to assign to the read-replica database.
	Tags pulumi.StringArrayInput
	// The name of zone that the read-replica database will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
	Zone pulumi.StringPtrInput
}

func (DatabaseReadReplicaArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*databaseReadReplicaArgs)(nil)).Elem()
}

type DatabaseReadReplicaInput interface {
	pulumi.Input

	ToDatabaseReadReplicaOutput() DatabaseReadReplicaOutput
	ToDatabaseReadReplicaOutputWithContext(ctx context.Context) DatabaseReadReplicaOutput
}

func (*DatabaseReadReplica) ElementType() reflect.Type {
	return reflect.TypeOf((*DatabaseReadReplica)(nil))
}

func (i *DatabaseReadReplica) ToDatabaseReadReplicaOutput() DatabaseReadReplicaOutput {
	return i.ToDatabaseReadReplicaOutputWithContext(context.Background())
}

func (i *DatabaseReadReplica) ToDatabaseReadReplicaOutputWithContext(ctx context.Context) DatabaseReadReplicaOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DatabaseReadReplicaOutput)
}

func (i *DatabaseReadReplica) ToDatabaseReadReplicaPtrOutput() DatabaseReadReplicaPtrOutput {
	return i.ToDatabaseReadReplicaPtrOutputWithContext(context.Background())
}

func (i *DatabaseReadReplica) ToDatabaseReadReplicaPtrOutputWithContext(ctx context.Context) DatabaseReadReplicaPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DatabaseReadReplicaPtrOutput)
}

type DatabaseReadReplicaPtrInput interface {
	pulumi.Input

	ToDatabaseReadReplicaPtrOutput() DatabaseReadReplicaPtrOutput
	ToDatabaseReadReplicaPtrOutputWithContext(ctx context.Context) DatabaseReadReplicaPtrOutput
}

type databaseReadReplicaPtrType DatabaseReadReplicaArgs

func (*databaseReadReplicaPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**DatabaseReadReplica)(nil))
}

func (i *databaseReadReplicaPtrType) ToDatabaseReadReplicaPtrOutput() DatabaseReadReplicaPtrOutput {
	return i.ToDatabaseReadReplicaPtrOutputWithContext(context.Background())
}

func (i *databaseReadReplicaPtrType) ToDatabaseReadReplicaPtrOutputWithContext(ctx context.Context) DatabaseReadReplicaPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DatabaseReadReplicaPtrOutput)
}

// DatabaseReadReplicaArrayInput is an input type that accepts DatabaseReadReplicaArray and DatabaseReadReplicaArrayOutput values.
// You can construct a concrete instance of `DatabaseReadReplicaArrayInput` via:
//
//          DatabaseReadReplicaArray{ DatabaseReadReplicaArgs{...} }
type DatabaseReadReplicaArrayInput interface {
	pulumi.Input

	ToDatabaseReadReplicaArrayOutput() DatabaseReadReplicaArrayOutput
	ToDatabaseReadReplicaArrayOutputWithContext(context.Context) DatabaseReadReplicaArrayOutput
}

type DatabaseReadReplicaArray []DatabaseReadReplicaInput

func (DatabaseReadReplicaArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*DatabaseReadReplica)(nil)).Elem()
}

func (i DatabaseReadReplicaArray) ToDatabaseReadReplicaArrayOutput() DatabaseReadReplicaArrayOutput {
	return i.ToDatabaseReadReplicaArrayOutputWithContext(context.Background())
}

func (i DatabaseReadReplicaArray) ToDatabaseReadReplicaArrayOutputWithContext(ctx context.Context) DatabaseReadReplicaArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DatabaseReadReplicaArrayOutput)
}

// DatabaseReadReplicaMapInput is an input type that accepts DatabaseReadReplicaMap and DatabaseReadReplicaMapOutput values.
// You can construct a concrete instance of `DatabaseReadReplicaMapInput` via:
//
//          DatabaseReadReplicaMap{ "key": DatabaseReadReplicaArgs{...} }
type DatabaseReadReplicaMapInput interface {
	pulumi.Input

	ToDatabaseReadReplicaMapOutput() DatabaseReadReplicaMapOutput
	ToDatabaseReadReplicaMapOutputWithContext(context.Context) DatabaseReadReplicaMapOutput
}

type DatabaseReadReplicaMap map[string]DatabaseReadReplicaInput

func (DatabaseReadReplicaMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*DatabaseReadReplica)(nil)).Elem()
}

func (i DatabaseReadReplicaMap) ToDatabaseReadReplicaMapOutput() DatabaseReadReplicaMapOutput {
	return i.ToDatabaseReadReplicaMapOutputWithContext(context.Background())
}

func (i DatabaseReadReplicaMap) ToDatabaseReadReplicaMapOutputWithContext(ctx context.Context) DatabaseReadReplicaMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DatabaseReadReplicaMapOutput)
}

type DatabaseReadReplicaOutput struct{ *pulumi.OutputState }

func (DatabaseReadReplicaOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*DatabaseReadReplica)(nil))
}

func (o DatabaseReadReplicaOutput) ToDatabaseReadReplicaOutput() DatabaseReadReplicaOutput {
	return o
}

func (o DatabaseReadReplicaOutput) ToDatabaseReadReplicaOutputWithContext(ctx context.Context) DatabaseReadReplicaOutput {
	return o
}

func (o DatabaseReadReplicaOutput) ToDatabaseReadReplicaPtrOutput() DatabaseReadReplicaPtrOutput {
	return o.ToDatabaseReadReplicaPtrOutputWithContext(context.Background())
}

func (o DatabaseReadReplicaOutput) ToDatabaseReadReplicaPtrOutputWithContext(ctx context.Context) DatabaseReadReplicaPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v DatabaseReadReplica) *DatabaseReadReplica {
		return &v
	}).(DatabaseReadReplicaPtrOutput)
}

type DatabaseReadReplicaPtrOutput struct{ *pulumi.OutputState }

func (DatabaseReadReplicaPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**DatabaseReadReplica)(nil))
}

func (o DatabaseReadReplicaPtrOutput) ToDatabaseReadReplicaPtrOutput() DatabaseReadReplicaPtrOutput {
	return o
}

func (o DatabaseReadReplicaPtrOutput) ToDatabaseReadReplicaPtrOutputWithContext(ctx context.Context) DatabaseReadReplicaPtrOutput {
	return o
}

func (o DatabaseReadReplicaPtrOutput) Elem() DatabaseReadReplicaOutput {
	return o.ApplyT(func(v *DatabaseReadReplica) DatabaseReadReplica {
		if v != nil {
			return *v
		}
		var ret DatabaseReadReplica
		return ret
	}).(DatabaseReadReplicaOutput)
}

type DatabaseReadReplicaArrayOutput struct{ *pulumi.OutputState }

func (DatabaseReadReplicaArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]DatabaseReadReplica)(nil))
}

func (o DatabaseReadReplicaArrayOutput) ToDatabaseReadReplicaArrayOutput() DatabaseReadReplicaArrayOutput {
	return o
}

func (o DatabaseReadReplicaArrayOutput) ToDatabaseReadReplicaArrayOutputWithContext(ctx context.Context) DatabaseReadReplicaArrayOutput {
	return o
}

func (o DatabaseReadReplicaArrayOutput) Index(i pulumi.IntInput) DatabaseReadReplicaOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) DatabaseReadReplica {
		return vs[0].([]DatabaseReadReplica)[vs[1].(int)]
	}).(DatabaseReadReplicaOutput)
}

type DatabaseReadReplicaMapOutput struct{ *pulumi.OutputState }

func (DatabaseReadReplicaMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]DatabaseReadReplica)(nil))
}

func (o DatabaseReadReplicaMapOutput) ToDatabaseReadReplicaMapOutput() DatabaseReadReplicaMapOutput {
	return o
}

func (o DatabaseReadReplicaMapOutput) ToDatabaseReadReplicaMapOutputWithContext(ctx context.Context) DatabaseReadReplicaMapOutput {
	return o
}

func (o DatabaseReadReplicaMapOutput) MapIndex(k pulumi.StringInput) DatabaseReadReplicaOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) DatabaseReadReplica {
		return vs[0].(map[string]DatabaseReadReplica)[vs[1].(string)]
	}).(DatabaseReadReplicaOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*DatabaseReadReplicaInput)(nil)).Elem(), &DatabaseReadReplica{})
	pulumi.RegisterInputType(reflect.TypeOf((*DatabaseReadReplicaPtrInput)(nil)).Elem(), &DatabaseReadReplica{})
	pulumi.RegisterInputType(reflect.TypeOf((*DatabaseReadReplicaArrayInput)(nil)).Elem(), DatabaseReadReplicaArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*DatabaseReadReplicaMapInput)(nil)).Elem(), DatabaseReadReplicaMap{})
	pulumi.RegisterOutputType(DatabaseReadReplicaOutput{})
	pulumi.RegisterOutputType(DatabaseReadReplicaPtrOutput{})
	pulumi.RegisterOutputType(DatabaseReadReplicaArrayOutput{})
	pulumi.RegisterOutputType(DatabaseReadReplicaMapOutput{})
}
