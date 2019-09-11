// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Provides a SakuraCloud Private Host resource. This can be used to create, update, and delete Private Hosts.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as sakuracloud from "@pulumi/sakuracloud";
 * 
 * // Create a new Private Host
 * const foobarPrivateHost = new sakuracloud.PrivateHost("foobar", {
 *     description: "description",
 *     tags: [
 *         "foo",
 *         "bar",
 *     ],
 * });
 * // Add server on Private Host
 * const foobarServer = new sakuracloud.Server("foobar", {
 *     privateHostId: "",
 *     "sakuracloud_private_host.foobar.id": [{}],
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-sakuracloud/blob/master/website/docs/r/private_host.html.markdown.
 */
export class PrivateHost extends pulumi.CustomResource {
    /**
     * Get an existing PrivateHost resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PrivateHostState, opts?: pulumi.CustomResourceOptions): PrivateHost {
        return new PrivateHost(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'sakuracloud:index/privateHost:PrivateHost';

    /**
     * Returns true if the given object is an instance of PrivateHost.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is PrivateHost {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === PrivateHost.__pulumiType;
    }

    /**
     * The number of cores assigned to the Server.
     */
    public /*out*/ readonly assignedCore!: pulumi.Output<number>;
    /**
     * The size of memory allocated to the Server (unit:`GB`).
     */
    public /*out*/ readonly assignedMemory!: pulumi.Output<number>;
    /**
     * The description of the resource.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The wait time (seconds) to do graceful shutdown the server connected to the resource.
     */
    public readonly gracefulShutdownTimeout!: pulumi.Output<number | undefined>;
    /**
     * The HostName of the resource.
     */
    public /*out*/ readonly hostname!: pulumi.Output<string>;
    /**
     * The ID of the icon.
     */
    public readonly iconId!: pulumi.Output<string | undefined>;
    /**
     * The name of the resource.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The tag list of the resources.
     */
    public readonly tags!: pulumi.Output<string[]>;
    /**
     * The ID of the zone to which the resource belongs.  
     * Valid value is one of the following: ["is1a" / "is1b" / "tk1a"]
     */
    public readonly zone!: pulumi.Output<string>;

    /**
     * Create a PrivateHost resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: PrivateHostArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: PrivateHostArgs | PrivateHostState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as PrivateHostState | undefined;
            inputs["assignedCore"] = state ? state.assignedCore : undefined;
            inputs["assignedMemory"] = state ? state.assignedMemory : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["gracefulShutdownTimeout"] = state ? state.gracefulShutdownTimeout : undefined;
            inputs["hostname"] = state ? state.hostname : undefined;
            inputs["iconId"] = state ? state.iconId : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["zone"] = state ? state.zone : undefined;
        } else {
            const args = argsOrState as PrivateHostArgs | undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["gracefulShutdownTimeout"] = args ? args.gracefulShutdownTimeout : undefined;
            inputs["iconId"] = args ? args.iconId : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["zone"] = args ? args.zone : undefined;
            inputs["assignedCore"] = undefined /*out*/;
            inputs["assignedMemory"] = undefined /*out*/;
            inputs["hostname"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(PrivateHost.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering PrivateHost resources.
 */
export interface PrivateHostState {
    /**
     * The number of cores assigned to the Server.
     */
    readonly assignedCore?: pulumi.Input<number>;
    /**
     * The size of memory allocated to the Server (unit:`GB`).
     */
    readonly assignedMemory?: pulumi.Input<number>;
    /**
     * The description of the resource.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The wait time (seconds) to do graceful shutdown the server connected to the resource.
     */
    readonly gracefulShutdownTimeout?: pulumi.Input<number>;
    /**
     * The HostName of the resource.
     */
    readonly hostname?: pulumi.Input<string>;
    /**
     * The ID of the icon.
     */
    readonly iconId?: pulumi.Input<string>;
    /**
     * The name of the resource.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The tag list of the resources.
     */
    readonly tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The ID of the zone to which the resource belongs.  
     * Valid value is one of the following: ["is1a" / "is1b" / "tk1a"]
     */
    readonly zone?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a PrivateHost resource.
 */
export interface PrivateHostArgs {
    /**
     * The description of the resource.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The wait time (seconds) to do graceful shutdown the server connected to the resource.
     */
    readonly gracefulShutdownTimeout?: pulumi.Input<number>;
    /**
     * The ID of the icon.
     */
    readonly iconId?: pulumi.Input<string>;
    /**
     * The name of the resource.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The tag list of the resources.
     */
    readonly tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The ID of the zone to which the resource belongs.  
     * Valid value is one of the following: ["is1a" / "is1b" / "tk1a"]
     */
    readonly zone?: pulumi.Input<string>;
}