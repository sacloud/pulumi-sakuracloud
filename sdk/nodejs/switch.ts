// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Provides a SakuraCloud Switch resource. This can be used to create, update, and delete Switches.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as sakuracloud from "@pulumi/sakuracloud";
 * 
 * // Create a new Switch
 * const foobar = new sakuracloud.Switch("foobar", {
 *     description: "description",
 *     tags: [
 *         "foo",
 *         "bar",
 *     ],
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-sakuracloud/blob/master/website/docs/r/switch.html.markdown.
 */
export class Switch extends pulumi.CustomResource {
    /**
     * Get an existing Switch resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SwitchState, opts?: pulumi.CustomResourceOptions): Switch {
        return new Switch(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'sakuracloud:index/switch:Switch';

    /**
     * Returns true if the given object is an instance of Switch.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Switch {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Switch.__pulumiType;
    }

    /**
     * The ID of the Bridge to connect to the Switch.
     */
    public readonly bridgeId!: pulumi.Output<string | undefined>;
    /**
     * The description of the resource.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The wait time (seconds) to do graceful shutdown the server connected to the resource.
     */
    public readonly gracefulShutdownTimeout!: pulumi.Output<number | undefined>;
    /**
     * The ID of the icon.
     */
    public readonly iconId!: pulumi.Output<string | undefined>;
    /**
     * The name of the resource.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The ID list of the servers connected to the switch.
     */
    public /*out*/ readonly serverIds!: pulumi.Output<string[]>;
    /**
     * The tag list of the resources.
     */
    public readonly tags!: pulumi.Output<string[]>;
    /**
     * The ID of the zone to which the resource belongs.
     */
    public readonly zone!: pulumi.Output<string>;

    /**
     * Create a Switch resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: SwitchArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: SwitchArgs | SwitchState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as SwitchState | undefined;
            inputs["bridgeId"] = state ? state.bridgeId : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["gracefulShutdownTimeout"] = state ? state.gracefulShutdownTimeout : undefined;
            inputs["iconId"] = state ? state.iconId : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["serverIds"] = state ? state.serverIds : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["zone"] = state ? state.zone : undefined;
        } else {
            const args = argsOrState as SwitchArgs | undefined;
            inputs["bridgeId"] = args ? args.bridgeId : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["gracefulShutdownTimeout"] = args ? args.gracefulShutdownTimeout : undefined;
            inputs["iconId"] = args ? args.iconId : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["zone"] = args ? args.zone : undefined;
            inputs["serverIds"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Switch.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Switch resources.
 */
export interface SwitchState {
    /**
     * The ID of the Bridge to connect to the Switch.
     */
    readonly bridgeId?: pulumi.Input<string>;
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
     * The ID list of the servers connected to the switch.
     */
    readonly serverIds?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The tag list of the resources.
     */
    readonly tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The ID of the zone to which the resource belongs.
     */
    readonly zone?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Switch resource.
 */
export interface SwitchArgs {
    /**
     * The ID of the Bridge to connect to the Switch.
     */
    readonly bridgeId?: pulumi.Input<string>;
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
     */
    readonly zone?: pulumi.Input<string>;
}