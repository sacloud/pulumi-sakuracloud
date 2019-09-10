// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Provides a SakuraCloud SSH Key resource. This can be used to create, update, and delete SSH Keys.
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-sakuracloud/blob/master/website/docs/r/ssh_key.html.markdown.
 */
export class SSHKey extends pulumi.CustomResource {
    /**
     * Get an existing SSHKey resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SSHKeyState, opts?: pulumi.CustomResourceOptions): SSHKey {
        return new SSHKey(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'sakuracloud:index/sSHKey:SSHKey';

    /**
     * Returns true if the given object is an instance of SSHKey.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is SSHKey {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === SSHKey.__pulumiType;
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
     * The body of the public key. 
     */
    public readonly publicKey!: pulumi.Output<string>;

    /**
     * Create a SSHKey resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: SSHKeyArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: SSHKeyArgs | SSHKeyState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as SSHKeyState | undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["fingerprint"] = state ? state.fingerprint : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["publicKey"] = state ? state.publicKey : undefined;
        } else {
            const args = argsOrState as SSHKeyArgs | undefined;
            if (!args || args.publicKey === undefined) {
                throw new Error("Missing required property 'publicKey'");
            }
            inputs["description"] = args ? args.description : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["publicKey"] = args ? args.publicKey : undefined;
            inputs["fingerprint"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(SSHKey.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering SSHKey resources.
 */
export interface SSHKeyState {
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
     * The body of the public key. 
     */
    readonly publicKey?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a SSHKey resource.
 */
export interface SSHKeyArgs {
    /**
     * The description of the resource.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The name of the resource.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The body of the public key. 
     */
    readonly publicKey: pulumi.Input<string>;
}
