// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sakuracloud

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides a SakuraCloud Database resource. This can be used to create, update, and delete Databases.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-sakuracloud/blob/master/website/docs/r/database.html.markdown.
type Database struct {
	s *pulumi.ResourceState
}

// NewDatabase registers a new resource with the given unique name, arguments, and options.
func NewDatabase(ctx *pulumi.Context,
	name string, args *DatabaseArgs, opts ...pulumi.ResourceOpt) (*Database, error) {
	if args == nil || args.DefaultRoute == nil {
		return nil, errors.New("missing required argument 'DefaultRoute'")
	}
	if args == nil || args.Ipaddress1 == nil {
		return nil, errors.New("missing required argument 'Ipaddress1'")
	}
	if args == nil || args.NwMaskLen == nil {
		return nil, errors.New("missing required argument 'NwMaskLen'")
	}
	if args == nil || args.SwitchId == nil {
		return nil, errors.New("missing required argument 'SwitchId'")
	}
	if args == nil || args.UserName == nil {
		return nil, errors.New("missing required argument 'UserName'")
	}
	if args == nil || args.UserPassword == nil {
		return nil, errors.New("missing required argument 'UserPassword'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["allowNetworks"] = nil
		inputs["backupTime"] = nil
		inputs["backupWeekdays"] = nil
		inputs["databaseType"] = nil
		inputs["defaultRoute"] = nil
		inputs["description"] = nil
		inputs["gracefulShutdownTimeout"] = nil
		inputs["iconId"] = nil
		inputs["ipaddress1"] = nil
		inputs["name"] = nil
		inputs["nwMaskLen"] = nil
		inputs["plan"] = nil
		inputs["port"] = nil
		inputs["replicaPassword"] = nil
		inputs["switchId"] = nil
		inputs["tags"] = nil
		inputs["userName"] = nil
		inputs["userPassword"] = nil
		inputs["zone"] = nil
	} else {
		inputs["allowNetworks"] = args.AllowNetworks
		inputs["backupTime"] = args.BackupTime
		inputs["backupWeekdays"] = args.BackupWeekdays
		inputs["databaseType"] = args.DatabaseType
		inputs["defaultRoute"] = args.DefaultRoute
		inputs["description"] = args.Description
		inputs["gracefulShutdownTimeout"] = args.GracefulShutdownTimeout
		inputs["iconId"] = args.IconId
		inputs["ipaddress1"] = args.Ipaddress1
		inputs["name"] = args.Name
		inputs["nwMaskLen"] = args.NwMaskLen
		inputs["plan"] = args.Plan
		inputs["port"] = args.Port
		inputs["replicaPassword"] = args.ReplicaPassword
		inputs["switchId"] = args.SwitchId
		inputs["tags"] = args.Tags
		inputs["userName"] = args.UserName
		inputs["userPassword"] = args.UserPassword
		inputs["zone"] = args.Zone
	}
	inputs["replicaUser"] = nil
	s, err := ctx.RegisterResource("sakuracloud:index/database:Database", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Database{s: s}, nil
}

// GetDatabase gets an existing Database resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDatabase(ctx *pulumi.Context,
	name string, id pulumi.ID, state *DatabaseState, opts ...pulumi.ResourceOpt) (*Database, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["allowNetworks"] = state.AllowNetworks
		inputs["backupTime"] = state.BackupTime
		inputs["backupWeekdays"] = state.BackupWeekdays
		inputs["databaseType"] = state.DatabaseType
		inputs["defaultRoute"] = state.DefaultRoute
		inputs["description"] = state.Description
		inputs["gracefulShutdownTimeout"] = state.GracefulShutdownTimeout
		inputs["iconId"] = state.IconId
		inputs["ipaddress1"] = state.Ipaddress1
		inputs["name"] = state.Name
		inputs["nwMaskLen"] = state.NwMaskLen
		inputs["plan"] = state.Plan
		inputs["port"] = state.Port
		inputs["replicaPassword"] = state.ReplicaPassword
		inputs["replicaUser"] = state.ReplicaUser
		inputs["switchId"] = state.SwitchId
		inputs["tags"] = state.Tags
		inputs["userName"] = state.UserName
		inputs["userPassword"] = state.UserPassword
		inputs["zone"] = state.Zone
	}
	s, err := ctx.ReadResource("sakuracloud:index/database:Database", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Database{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *Database) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *Database) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The network address list that allowed connections to the database.
func (r *Database) AllowNetworks() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["allowNetworks"])
}

// The time to perform backup (format:`HH:mm`).
func (r *Database) BackupTime() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["backupTime"])
}

// Day of the week to get backup.  
// Valid values are the following: ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
func (r *Database) BackupWeekdays() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["backupWeekdays"])
}

// The Database type.  
// Valid value is one of the following: [ "postgresql" (default) / "mariadb"]
func (r *Database) DatabaseType() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["databaseType"])
}

// The default route IP address of the database.
func (r *Database) DefaultRoute() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["defaultRoute"])
}

// The description of the resource.
func (r *Database) Description() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["description"])
}

// The wait time (seconds) to do graceful shutdown the Database.
func (r *Database) GracefulShutdownTimeout() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["gracefulShutdownTimeout"])
}

// The ID of the icon.
func (r *Database) IconId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["iconId"])
}

// The IP address of the database.
func (r *Database) Ipaddress1() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["ipaddress1"])
}

// The name of the resource.
func (r *Database) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// The network mask length of the database.
func (r *Database) NwMaskLen() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["nwMaskLen"])
}

// The plan (size) of the Database.   
// Valid value is one of the following: [ "10g" (default) / "30g" / "90g" / "240g" / "500g" / "1t" ]
func (r *Database) Plan() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["plan"])
}

// The number of the port on which the database is listening (default:`5432`).
func (r *Database) Port() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["port"])
}

func (r *Database) ReplicaPassword() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["replicaPassword"])
}

func (r *Database) ReplicaUser() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["replicaUser"])
}

// The ID of the switch connected to the database.
func (r *Database) SwitchId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["switchId"])
}

// The tag list of the resources.
func (r *Database) Tags() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["tags"])
}

// The username to access database.
func (r *Database) UserName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["userName"])
}

// The password to access database.
func (r *Database) UserPassword() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["userPassword"])
}

// The ID of the zone to which the resource belongs.
func (r *Database) Zone() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["zone"])
}

// Input properties used for looking up and filtering Database resources.
type DatabaseState struct {
	// The network address list that allowed connections to the database.
	AllowNetworks interface{}
	// The time to perform backup (format:`HH:mm`).
	BackupTime interface{}
	// Day of the week to get backup.  
	// Valid values are the following: ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
	BackupWeekdays interface{}
	// The Database type.  
	// Valid value is one of the following: [ "postgresql" (default) / "mariadb"]
	DatabaseType interface{}
	// The default route IP address of the database.
	DefaultRoute interface{}
	// The description of the resource.
	Description interface{}
	// The wait time (seconds) to do graceful shutdown the Database.
	GracefulShutdownTimeout interface{}
	// The ID of the icon.
	IconId interface{}
	// The IP address of the database.
	Ipaddress1 interface{}
	// The name of the resource.
	Name interface{}
	// The network mask length of the database.
	NwMaskLen interface{}
	// The plan (size) of the Database.   
	// Valid value is one of the following: [ "10g" (default) / "30g" / "90g" / "240g" / "500g" / "1t" ]
	Plan interface{}
	// The number of the port on which the database is listening (default:`5432`).
	Port interface{}
	ReplicaPassword interface{}
	ReplicaUser interface{}
	// The ID of the switch connected to the database.
	SwitchId interface{}
	// The tag list of the resources.
	Tags interface{}
	// The username to access database.
	UserName interface{}
	// The password to access database.
	UserPassword interface{}
	// The ID of the zone to which the resource belongs.
	Zone interface{}
}

// The set of arguments for constructing a Database resource.
type DatabaseArgs struct {
	// The network address list that allowed connections to the database.
	AllowNetworks interface{}
	// The time to perform backup (format:`HH:mm`).
	BackupTime interface{}
	// Day of the week to get backup.  
	// Valid values are the following: ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
	BackupWeekdays interface{}
	// The Database type.  
	// Valid value is one of the following: [ "postgresql" (default) / "mariadb"]
	DatabaseType interface{}
	// The default route IP address of the database.
	DefaultRoute interface{}
	// The description of the resource.
	Description interface{}
	// The wait time (seconds) to do graceful shutdown the Database.
	GracefulShutdownTimeout interface{}
	// The ID of the icon.
	IconId interface{}
	// The IP address of the database.
	Ipaddress1 interface{}
	// The name of the resource.
	Name interface{}
	// The network mask length of the database.
	NwMaskLen interface{}
	// The plan (size) of the Database.   
	// Valid value is one of the following: [ "10g" (default) / "30g" / "90g" / "240g" / "500g" / "1t" ]
	Plan interface{}
	// The number of the port on which the database is listening (default:`5432`).
	Port interface{}
	ReplicaPassword interface{}
	// The ID of the switch connected to the database.
	SwitchId interface{}
	// The tag list of the resources.
	Tags interface{}
	// The username to access database.
	UserName interface{}
	// The password to access database.
	UserPassword interface{}
	// The ID of the zone to which the resource belongs.
	Zone interface{}
}
