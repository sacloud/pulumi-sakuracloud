// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package sakuracloud

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

type Database struct {
	pulumi.CustomResourceState

	Backup DatabaseBackupPtrOutput `pulumi:"backup"`
	// The type of the database. This must be one of [`mariadb`/`postgres`]
	DatabaseType pulumi.StringPtrOutput `pulumi:"databaseType"`
	// The description of the Database. The length of this value must be in the range [`1`-`512`]
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The icon id to attach to the Database
	IconId pulumi.StringPtrOutput `pulumi:"iconId"`
	// The name of the Database. The length of this value must be in the range [`1`-`64`]
	Name             pulumi.StringOutput            `pulumi:"name"`
	NetworkInterface DatabaseNetworkInterfaceOutput `pulumi:"networkInterface"`
	// The password of default user on the database
	Password pulumi.StringOutput `pulumi:"password"`
	// The plan name of the Database. This must be one of [`10g`/`30g`/`90g`/`240g`/`500g`/`1t`]
	Plan pulumi.StringPtrOutput `pulumi:"plan"`
	// The password of user that processing a replication
	ReplicaPassword pulumi.StringPtrOutput `pulumi:"replicaPassword"`
	// The name of user that processing a replication
	ReplicaUser pulumi.StringPtrOutput `pulumi:"replicaUser"`
	// Any tags to assign to the Database
	Tags pulumi.StringArrayOutput `pulumi:"tags"`
	// The name of default user on the database. The length of this value must be in the range [`3`-`20`]
	Username pulumi.StringOutput `pulumi:"username"`
	// The name of zone that the Database will be created (e.g. `is1a`, `tk1a`)
	Zone pulumi.StringOutput `pulumi:"zone"`
}

// NewDatabase registers a new resource with the given unique name, arguments, and options.
func NewDatabase(ctx *pulumi.Context,
	name string, args *DatabaseArgs, opts ...pulumi.ResourceOption) (*Database, error) {
	if args == nil || args.NetworkInterface == nil {
		return nil, errors.New("missing required argument 'NetworkInterface'")
	}
	if args == nil || args.Password == nil {
		return nil, errors.New("missing required argument 'Password'")
	}
	if args == nil || args.Username == nil {
		return nil, errors.New("missing required argument 'Username'")
	}
	if args == nil {
		args = &DatabaseArgs{}
	}
	var resource Database
	err := ctx.RegisterResource("sakuracloud:index/database:Database", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDatabase gets an existing Database resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDatabase(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DatabaseState, opts ...pulumi.ResourceOption) (*Database, error) {
	var resource Database
	err := ctx.ReadResource("sakuracloud:index/database:Database", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Database resources.
type databaseState struct {
	Backup *DatabaseBackup `pulumi:"backup"`
	// The type of the database. This must be one of [`mariadb`/`postgres`]
	DatabaseType *string `pulumi:"databaseType"`
	// The description of the Database. The length of this value must be in the range [`1`-`512`]
	Description *string `pulumi:"description"`
	// The icon id to attach to the Database
	IconId *string `pulumi:"iconId"`
	// The name of the Database. The length of this value must be in the range [`1`-`64`]
	Name             *string                   `pulumi:"name"`
	NetworkInterface *DatabaseNetworkInterface `pulumi:"networkInterface"`
	// The password of default user on the database
	Password *string `pulumi:"password"`
	// The plan name of the Database. This must be one of [`10g`/`30g`/`90g`/`240g`/`500g`/`1t`]
	Plan *string `pulumi:"plan"`
	// The password of user that processing a replication
	ReplicaPassword *string `pulumi:"replicaPassword"`
	// The name of user that processing a replication
	ReplicaUser *string `pulumi:"replicaUser"`
	// Any tags to assign to the Database
	Tags []string `pulumi:"tags"`
	// The name of default user on the database. The length of this value must be in the range [`3`-`20`]
	Username *string `pulumi:"username"`
	// The name of zone that the Database will be created (e.g. `is1a`, `tk1a`)
	Zone *string `pulumi:"zone"`
}

type DatabaseState struct {
	Backup DatabaseBackupPtrInput
	// The type of the database. This must be one of [`mariadb`/`postgres`]
	DatabaseType pulumi.StringPtrInput
	// The description of the Database. The length of this value must be in the range [`1`-`512`]
	Description pulumi.StringPtrInput
	// The icon id to attach to the Database
	IconId pulumi.StringPtrInput
	// The name of the Database. The length of this value must be in the range [`1`-`64`]
	Name             pulumi.StringPtrInput
	NetworkInterface DatabaseNetworkInterfacePtrInput
	// The password of default user on the database
	Password pulumi.StringPtrInput
	// The plan name of the Database. This must be one of [`10g`/`30g`/`90g`/`240g`/`500g`/`1t`]
	Plan pulumi.StringPtrInput
	// The password of user that processing a replication
	ReplicaPassword pulumi.StringPtrInput
	// The name of user that processing a replication
	ReplicaUser pulumi.StringPtrInput
	// Any tags to assign to the Database
	Tags pulumi.StringArrayInput
	// The name of default user on the database. The length of this value must be in the range [`3`-`20`]
	Username pulumi.StringPtrInput
	// The name of zone that the Database will be created (e.g. `is1a`, `tk1a`)
	Zone pulumi.StringPtrInput
}

func (DatabaseState) ElementType() reflect.Type {
	return reflect.TypeOf((*databaseState)(nil)).Elem()
}

type databaseArgs struct {
	Backup *DatabaseBackup `pulumi:"backup"`
	// The type of the database. This must be one of [`mariadb`/`postgres`]
	DatabaseType *string `pulumi:"databaseType"`
	// The description of the Database. The length of this value must be in the range [`1`-`512`]
	Description *string `pulumi:"description"`
	// The icon id to attach to the Database
	IconId *string `pulumi:"iconId"`
	// The name of the Database. The length of this value must be in the range [`1`-`64`]
	Name             *string                  `pulumi:"name"`
	NetworkInterface DatabaseNetworkInterface `pulumi:"networkInterface"`
	// The password of default user on the database
	Password string `pulumi:"password"`
	// The plan name of the Database. This must be one of [`10g`/`30g`/`90g`/`240g`/`500g`/`1t`]
	Plan *string `pulumi:"plan"`
	// The password of user that processing a replication
	ReplicaPassword *string `pulumi:"replicaPassword"`
	// The name of user that processing a replication
	ReplicaUser *string `pulumi:"replicaUser"`
	// Any tags to assign to the Database
	Tags []string `pulumi:"tags"`
	// The name of default user on the database. The length of this value must be in the range [`3`-`20`]
	Username string `pulumi:"username"`
	// The name of zone that the Database will be created (e.g. `is1a`, `tk1a`)
	Zone *string `pulumi:"zone"`
}

// The set of arguments for constructing a Database resource.
type DatabaseArgs struct {
	Backup DatabaseBackupPtrInput
	// The type of the database. This must be one of [`mariadb`/`postgres`]
	DatabaseType pulumi.StringPtrInput
	// The description of the Database. The length of this value must be in the range [`1`-`512`]
	Description pulumi.StringPtrInput
	// The icon id to attach to the Database
	IconId pulumi.StringPtrInput
	// The name of the Database. The length of this value must be in the range [`1`-`64`]
	Name             pulumi.StringPtrInput
	NetworkInterface DatabaseNetworkInterfaceInput
	// The password of default user on the database
	Password pulumi.StringInput
	// The plan name of the Database. This must be one of [`10g`/`30g`/`90g`/`240g`/`500g`/`1t`]
	Plan pulumi.StringPtrInput
	// The password of user that processing a replication
	ReplicaPassword pulumi.StringPtrInput
	// The name of user that processing a replication
	ReplicaUser pulumi.StringPtrInput
	// Any tags to assign to the Database
	Tags pulumi.StringArrayInput
	// The name of default user on the database. The length of this value must be in the range [`3`-`20`]
	Username pulumi.StringInput
	// The name of zone that the Database will be created (e.g. `is1a`, `tk1a`)
	Zone pulumi.StringPtrInput
}

func (DatabaseArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*databaseArgs)(nil)).Elem()
}
