// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Provides a SakuraCloud SSH Key resource. This can be used to create and delete SSH Keys.
 * The private and public keys is generated on the Sakura Cloud platform.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as sakuracloud from "@pulumi/sakuracloud";
 * 
 * // Create a new SSH Key
 * const foobar = new sakuracloud.SSHKeyGen("foobar", {
 *     description: "description",
 *     passPhrase: "<your-pass-phrase>",
 * });
 * ```
 * 
 * ## Import (not supported)
 * 
 * Import of SSH Key Gen is not supported.
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-sakuracloud/blob/master/website/docs/r/ssh_key_gen.html.markdown.
 */
export class SSHKeyGen extends pulumi.CustomResource {
    /**
     * Get an existing SSHKeyGen resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SSHKeyGenState, opts?: pulumi.CustomResourceOptions): SSHKeyGen {
        return new SSHKeyGen(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'sakuracloud:index/sSHKeyGen:SSHKeyGen';

    /**
     * Returns true if the given object is an instance of SSHKeyGen.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is SSHKeyGen {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === SSHKeyGen.__pulumiType;
    }

    /**
     * The description of the resource.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    public /*out*/ readonly fingerprint!: pulumi.Output<string>;
    /**
     * The name of the resource.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The path phrase of keys. 
     */
    public readonly passPhrase!: pulumi.Output<string | undefined>;
    /**
     * The body of the generated private key. 
     */
    public /*out*/ readonly privateKey!: pulumi.Output<string>;
    /**
     * The body of the generated public key. 
     */
    public /*out*/ readonly publicKey!: pulumi.Output<string>;

    /**
     * Create a SSHKeyGen resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: SSHKeyGenArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: SSHKeyGenArgs | SSHKeyGenState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as SSHKeyGenState | undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["fingerprint"] = state ? state.fingerprint : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["passPhrase"] = state ? state.passPhrase : undefined;
            inputs["privateKey"] = state ? state.privateKey : undefined;
            inputs["publicKey"] = state ? state.publicKey : undefined;
        } else {
            const args = argsOrState as SSHKeyGenArgs | undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["passPhrase"] = args ? args.passPhrase : undefined;
            inputs["fingerprint"] = undefined /*out*/;
            inputs["privateKey"] = undefined /*out*/;
            inputs["publicKey"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(SSHKeyGen.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering SSHKeyGen resources.
 */
export interface SSHKeyGenState {
    /**
     * The description of the resource.
     */
    readonly description?: pulumi.Input<string>;
    readonly fingerprint?: pulumi.Input<string>;
    /**
     * The name of the resource.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The path phrase of keys. 
     */
    readonly passPhrase?: pulumi.Input<string>;
    /**
     * The body of the generated private key. 
     */
    readonly privateKey?: pulumi.Input<string>;
    /**
     * The body of the generated public key. 
     */
    readonly publicKey?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a SSHKeyGen resource.
 */
export interface SSHKeyGenArgs {
    /**
     * The description of the resource.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The name of the resource.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The path phrase of keys. 
     */
    readonly passPhrase?: pulumi.Input<string>;
}
