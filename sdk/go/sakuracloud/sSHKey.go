// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sakuracloud

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides a SakuraCloud SSH Key resource. This can be used to create, update, and delete SSH Keys.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-sakuracloud/blob/master/website/docs/r/ssh_key.html.markdown.
type SSHKey struct {
	s *pulumi.ResourceState
}

// NewSSHKey registers a new resource with the given unique name, arguments, and options.
func NewSSHKey(ctx *pulumi.Context,
	name string, args *SSHKeyArgs, opts ...pulumi.ResourceOpt) (*SSHKey, error) {
	if args == nil || args.PublicKey == nil {
		return nil, errors.New("missing required argument 'PublicKey'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["description"] = nil
		inputs["name"] = nil
		inputs["publicKey"] = nil
	} else {
		inputs["description"] = args.Description
		inputs["name"] = args.Name
		inputs["publicKey"] = args.PublicKey
	}
	inputs["fingerprint"] = nil
	s, err := ctx.RegisterResource("sakuracloud:index/sSHKey:SSHKey", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &SSHKey{s: s}, nil
}

// GetSSHKey gets an existing SSHKey resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSSHKey(ctx *pulumi.Context,
	name string, id pulumi.ID, state *SSHKeyState, opts ...pulumi.ResourceOpt) (*SSHKey, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["description"] = state.Description
		inputs["fingerprint"] = state.Fingerprint
		inputs["name"] = state.Name
		inputs["publicKey"] = state.PublicKey
	}
	s, err := ctx.ReadResource("sakuracloud:index/sSHKey:SSHKey", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &SSHKey{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *SSHKey) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *SSHKey) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The description of the resource.
func (r *SSHKey) Description() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["description"])
}

func (r *SSHKey) Fingerprint() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["fingerprint"])
}

// The name of the resource.
func (r *SSHKey) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// The body of the public key. 
func (r *SSHKey) PublicKey() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["publicKey"])
}

// Input properties used for looking up and filtering SSHKey resources.
type SSHKeyState struct {
	// The description of the resource.
	Description interface{}
	Fingerprint interface{}
	// The name of the resource.
	Name interface{}
	// The body of the public key. 
	PublicKey interface{}
}

// The set of arguments for constructing a SSHKey resource.
type SSHKeyArgs struct {
	// The description of the resource.
	Description interface{}
	// The name of the resource.
	Name interface{}
	// The body of the public key. 
	PublicKey interface{}
}