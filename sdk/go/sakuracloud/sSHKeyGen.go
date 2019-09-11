// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sakuracloud

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides a SakuraCloud SSH Key resource. This can be used to create and delete SSH Keys.
// The private and public keys is generated on the Sakura Cloud platform.
// 
// ## Import (not supported)
// 
// Import of SSH Key Gen is not supported.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-sakuracloud/blob/master/website/docs/r/ssh_key_gen.html.markdown.
type SSHKeyGen struct {
	s *pulumi.ResourceState
}

// NewSSHKeyGen registers a new resource with the given unique name, arguments, and options.
func NewSSHKeyGen(ctx *pulumi.Context,
	name string, args *SSHKeyGenArgs, opts ...pulumi.ResourceOpt) (*SSHKeyGen, error) {
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["description"] = nil
		inputs["name"] = nil
		inputs["passPhrase"] = nil
	} else {
		inputs["description"] = args.Description
		inputs["name"] = args.Name
		inputs["passPhrase"] = args.PassPhrase
	}
	inputs["fingerprint"] = nil
	inputs["privateKey"] = nil
	inputs["publicKey"] = nil
	s, err := ctx.RegisterResource("sakuracloud:index/sSHKeyGen:SSHKeyGen", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &SSHKeyGen{s: s}, nil
}

// GetSSHKeyGen gets an existing SSHKeyGen resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSSHKeyGen(ctx *pulumi.Context,
	name string, id pulumi.ID, state *SSHKeyGenState, opts ...pulumi.ResourceOpt) (*SSHKeyGen, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["description"] = state.Description
		inputs["fingerprint"] = state.Fingerprint
		inputs["name"] = state.Name
		inputs["passPhrase"] = state.PassPhrase
		inputs["privateKey"] = state.PrivateKey
		inputs["publicKey"] = state.PublicKey
	}
	s, err := ctx.ReadResource("sakuracloud:index/sSHKeyGen:SSHKeyGen", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &SSHKeyGen{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *SSHKeyGen) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *SSHKeyGen) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The description of the resource.
func (r *SSHKeyGen) Description() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["description"])
}

func (r *SSHKeyGen) Fingerprint() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["fingerprint"])
}

// The name of the resource.
func (r *SSHKeyGen) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// The path phrase of keys. 
func (r *SSHKeyGen) PassPhrase() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["passPhrase"])
}

// The body of the generated private key. 
func (r *SSHKeyGen) PrivateKey() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["privateKey"])
}

// The body of the generated public key. 
func (r *SSHKeyGen) PublicKey() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["publicKey"])
}

// Input properties used for looking up and filtering SSHKeyGen resources.
type SSHKeyGenState struct {
	// The description of the resource.
	Description interface{}
	Fingerprint interface{}
	// The name of the resource.
	Name interface{}
	// The path phrase of keys. 
	PassPhrase interface{}
	// The body of the generated private key. 
	PrivateKey interface{}
	// The body of the generated public key. 
	PublicKey interface{}
}

// The set of arguments for constructing a SSHKeyGen resource.
type SSHKeyGenArgs struct {
	// The description of the resource.
	Description interface{}
	// The name of the resource.
	Name interface{}
	// The path phrase of keys. 
	PassPhrase interface{}
}