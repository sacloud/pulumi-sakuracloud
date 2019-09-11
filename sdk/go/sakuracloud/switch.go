// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sakuracloud

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides a SakuraCloud Switch resource. This can be used to create, update, and delete Switches.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-sakuracloud/blob/master/website/docs/r/switch.html.markdown.
type Switch struct {
	s *pulumi.ResourceState
}

// NewSwitch registers a new resource with the given unique name, arguments, and options.
func NewSwitch(ctx *pulumi.Context,
	name string, args *SwitchArgs, opts ...pulumi.ResourceOpt) (*Switch, error) {
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["bridgeId"] = nil
		inputs["description"] = nil
		inputs["gracefulShutdownTimeout"] = nil
		inputs["iconId"] = nil
		inputs["name"] = nil
		inputs["tags"] = nil
		inputs["zone"] = nil
	} else {
		inputs["bridgeId"] = args.BridgeId
		inputs["description"] = args.Description
		inputs["gracefulShutdownTimeout"] = args.GracefulShutdownTimeout
		inputs["iconId"] = args.IconId
		inputs["name"] = args.Name
		inputs["tags"] = args.Tags
		inputs["zone"] = args.Zone
	}
	inputs["serverIds"] = nil
	s, err := ctx.RegisterResource("sakuracloud:index/switch:Switch", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Switch{s: s}, nil
}

// GetSwitch gets an existing Switch resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSwitch(ctx *pulumi.Context,
	name string, id pulumi.ID, state *SwitchState, opts ...pulumi.ResourceOpt) (*Switch, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["bridgeId"] = state.BridgeId
		inputs["description"] = state.Description
		inputs["gracefulShutdownTimeout"] = state.GracefulShutdownTimeout
		inputs["iconId"] = state.IconId
		inputs["name"] = state.Name
		inputs["serverIds"] = state.ServerIds
		inputs["tags"] = state.Tags
		inputs["zone"] = state.Zone
	}
	s, err := ctx.ReadResource("sakuracloud:index/switch:Switch", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Switch{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *Switch) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *Switch) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The ID of the Bridge to connect to the Switch.
func (r *Switch) BridgeId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["bridgeId"])
}

// The description of the resource.
func (r *Switch) Description() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["description"])
}

// The wait time (seconds) to do graceful shutdown the server connected to the resource.
func (r *Switch) GracefulShutdownTimeout() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["gracefulShutdownTimeout"])
}

// The ID of the icon.
func (r *Switch) IconId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["iconId"])
}

// The name of the resource.
func (r *Switch) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// The ID list of the servers connected to the switch.
func (r *Switch) ServerIds() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["serverIds"])
}

// The tag list of the resources.
func (r *Switch) Tags() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["tags"])
}

// The ID of the zone to which the resource belongs.
func (r *Switch) Zone() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["zone"])
}

// Input properties used for looking up and filtering Switch resources.
type SwitchState struct {
	// The ID of the Bridge to connect to the Switch.
	BridgeId interface{}
	// The description of the resource.
	Description interface{}
	// The wait time (seconds) to do graceful shutdown the server connected to the resource.
	GracefulShutdownTimeout interface{}
	// The ID of the icon.
	IconId interface{}
	// The name of the resource.
	Name interface{}
	// The ID list of the servers connected to the switch.
	ServerIds interface{}
	// The tag list of the resources.
	Tags interface{}
	// The ID of the zone to which the resource belongs.
	Zone interface{}
}

// The set of arguments for constructing a Switch resource.
type SwitchArgs struct {
	// The ID of the Bridge to connect to the Switch.
	BridgeId interface{}
	// The description of the resource.
	Description interface{}
	// The wait time (seconds) to do graceful shutdown the server connected to the resource.
	GracefulShutdownTimeout interface{}
	// The ID of the icon.
	IconId interface{}
	// The name of the resource.
	Name interface{}
	// The tag list of the resources.
	Tags interface{}
	// The ID of the zone to which the resource belongs.
	Zone interface{}
}