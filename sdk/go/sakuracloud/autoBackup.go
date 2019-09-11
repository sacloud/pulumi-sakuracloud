// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sakuracloud

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides a SakuraCloud Auto Backup resource. This can be used to create, update, and delete Auto Backups.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-sakuracloud/blob/master/website/docs/r/auto_backup.html.markdown.
type AutoBackup struct {
	s *pulumi.ResourceState
}

// NewAutoBackup registers a new resource with the given unique name, arguments, and options.
func NewAutoBackup(ctx *pulumi.Context,
	name string, args *AutoBackupArgs, opts ...pulumi.ResourceOpt) (*AutoBackup, error) {
	if args == nil || args.DiskId == nil {
		return nil, errors.New("missing required argument 'DiskId'")
	}
	if args == nil || args.Weekdays == nil {
		return nil, errors.New("missing required argument 'Weekdays'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["description"] = nil
		inputs["diskId"] = nil
		inputs["iconId"] = nil
		inputs["maxBackupNum"] = nil
		inputs["name"] = nil
		inputs["tags"] = nil
		inputs["weekdays"] = nil
		inputs["zone"] = nil
	} else {
		inputs["description"] = args.Description
		inputs["diskId"] = args.DiskId
		inputs["iconId"] = args.IconId
		inputs["maxBackupNum"] = args.MaxBackupNum
		inputs["name"] = args.Name
		inputs["tags"] = args.Tags
		inputs["weekdays"] = args.Weekdays
		inputs["zone"] = args.Zone
	}
	s, err := ctx.RegisterResource("sakuracloud:index/autoBackup:AutoBackup", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &AutoBackup{s: s}, nil
}

// GetAutoBackup gets an existing AutoBackup resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetAutoBackup(ctx *pulumi.Context,
	name string, id pulumi.ID, state *AutoBackupState, opts ...pulumi.ResourceOpt) (*AutoBackup, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["description"] = state.Description
		inputs["diskId"] = state.DiskId
		inputs["iconId"] = state.IconId
		inputs["maxBackupNum"] = state.MaxBackupNum
		inputs["name"] = state.Name
		inputs["tags"] = state.Tags
		inputs["weekdays"] = state.Weekdays
		inputs["zone"] = state.Zone
	}
	s, err := ctx.ReadResource("sakuracloud:index/autoBackup:AutoBackup", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &AutoBackup{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *AutoBackup) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *AutoBackup) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The description of the resource.
func (r *AutoBackup) Description() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["description"])
}

// The ID of the target disk. 
func (r *AutoBackup) DiskId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["diskId"])
}

// The ID of the icon.
func (r *AutoBackup) IconId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["iconId"])
}

// Max number of backups to keep.
func (r *AutoBackup) MaxBackupNum() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["maxBackupNum"])
}

// The name of the resource.
func (r *AutoBackup) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// The tag list of the resources.
func (r *AutoBackup) Tags() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["tags"])
}

// Day of the week to get backup.  
// Valid values are the following: ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
func (r *AutoBackup) Weekdays() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["weekdays"])
}

// The ID of the zone to which the resource belongs.  
// Valid value is one of the following: ["is1b" / "tk1a" / "is1a"]
func (r *AutoBackup) Zone() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["zone"])
}

// Input properties used for looking up and filtering AutoBackup resources.
type AutoBackupState struct {
	// The description of the resource.
	Description interface{}
	// The ID of the target disk. 
	DiskId interface{}
	// The ID of the icon.
	IconId interface{}
	// Max number of backups to keep.
	MaxBackupNum interface{}
	// The name of the resource.
	Name interface{}
	// The tag list of the resources.
	Tags interface{}
	// Day of the week to get backup.  
	// Valid values are the following: ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
	Weekdays interface{}
	// The ID of the zone to which the resource belongs.  
	// Valid value is one of the following: ["is1b" / "tk1a" / "is1a"]
	Zone interface{}
}

// The set of arguments for constructing a AutoBackup resource.
type AutoBackupArgs struct {
	// The description of the resource.
	Description interface{}
	// The ID of the target disk. 
	DiskId interface{}
	// The ID of the icon.
	IconId interface{}
	// Max number of backups to keep.
	MaxBackupNum interface{}
	// The name of the resource.
	Name interface{}
	// The tag list of the resources.
	Tags interface{}
	// Day of the week to get backup.  
	// Valid values are the following: ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
	Weekdays interface{}
	// The ID of the zone to which the resource belongs.  
	// Valid value is one of the following: ["is1b" / "tk1a" / "is1a"]
	Zone interface{}
}