// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

export class LocalRouter extends pulumi.CustomResource {
    /**
     * Get an existing LocalRouter resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: LocalRouterState, opts?: pulumi.CustomResourceOptions): LocalRouter {
        return new LocalRouter(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'sakuracloud:index/localRouter:LocalRouter';

    /**
     * Returns true if the given object is an instance of LocalRouter.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is LocalRouter {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === LocalRouter.__pulumiType;
    }

    /**
     * The description of the LocalRouter. The length of this value must be in the range [`1`-`512`]
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The icon id to attach to the LocalRouter
     */
    public readonly iconId!: pulumi.Output<string | undefined>;
    /**
     * The name of the LocalRouter. The length of this value must be in the range [`1`-`64`]
     */
    public readonly name!: pulumi.Output<string>;
    public readonly networkInterface!: pulumi.Output<outputs.LocalRouterNetworkInterface>;
    public readonly peers!: pulumi.Output<outputs.LocalRouterPeer[] | undefined>;
    /**
     * A list of secret key used for peering from other LocalRouters
     */
    public /*out*/ readonly secretKeys!: pulumi.Output<string[]>;
    public readonly staticRoutes!: pulumi.Output<outputs.LocalRouterStaticRoute[] | undefined>;
    public readonly switch!: pulumi.Output<outputs.LocalRouterSwitch>;
    /**
     * Any tags to assign to the LocalRouter
     */
    public readonly tags!: pulumi.Output<string[] | undefined>;

    /**
     * Create a LocalRouter resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: LocalRouterArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: LocalRouterArgs | LocalRouterState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as LocalRouterState | undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["iconId"] = state ? state.iconId : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["networkInterface"] = state ? state.networkInterface : undefined;
            inputs["peers"] = state ? state.peers : undefined;
            inputs["secretKeys"] = state ? state.secretKeys : undefined;
            inputs["staticRoutes"] = state ? state.staticRoutes : undefined;
            inputs["switch"] = state ? state.switch : undefined;
            inputs["tags"] = state ? state.tags : undefined;
        } else {
            const args = argsOrState as LocalRouterArgs | undefined;
            if (!args || args.networkInterface === undefined) {
                throw new Error("Missing required property 'networkInterface'");
            }
            if (!args || args.switch === undefined) {
                throw new Error("Missing required property 'switch'");
            }
            inputs["description"] = args ? args.description : undefined;
            inputs["iconId"] = args ? args.iconId : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["networkInterface"] = args ? args.networkInterface : undefined;
            inputs["peers"] = args ? args.peers : undefined;
            inputs["staticRoutes"] = args ? args.staticRoutes : undefined;
            inputs["switch"] = args ? args.switch : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["secretKeys"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(LocalRouter.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering LocalRouter resources.
 */
export interface LocalRouterState {
    /**
     * The description of the LocalRouter. The length of this value must be in the range [`1`-`512`]
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The icon id to attach to the LocalRouter
     */
    readonly iconId?: pulumi.Input<string>;
    /**
     * The name of the LocalRouter. The length of this value must be in the range [`1`-`64`]
     */
    readonly name?: pulumi.Input<string>;
    readonly networkInterface?: pulumi.Input<inputs.LocalRouterNetworkInterface>;
    readonly peers?: pulumi.Input<pulumi.Input<inputs.LocalRouterPeer>[]>;
    /**
     * A list of secret key used for peering from other LocalRouters
     */
    readonly secretKeys?: pulumi.Input<pulumi.Input<string>[]>;
    readonly staticRoutes?: pulumi.Input<pulumi.Input<inputs.LocalRouterStaticRoute>[]>;
    readonly switch?: pulumi.Input<inputs.LocalRouterSwitch>;
    /**
     * Any tags to assign to the LocalRouter
     */
    readonly tags?: pulumi.Input<pulumi.Input<string>[]>;
}

/**
 * The set of arguments for constructing a LocalRouter resource.
 */
export interface LocalRouterArgs {
    /**
     * The description of the LocalRouter. The length of this value must be in the range [`1`-`512`]
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The icon id to attach to the LocalRouter
     */
    readonly iconId?: pulumi.Input<string>;
    /**
     * The name of the LocalRouter. The length of this value must be in the range [`1`-`64`]
     */
    readonly name?: pulumi.Input<string>;
    readonly networkInterface: pulumi.Input<inputs.LocalRouterNetworkInterface>;
    readonly peers?: pulumi.Input<pulumi.Input<inputs.LocalRouterPeer>[]>;
    readonly staticRoutes?: pulumi.Input<pulumi.Input<inputs.LocalRouterStaticRoute>[]>;
    readonly switch: pulumi.Input<inputs.LocalRouterSwitch>;
    /**
     * Any tags to assign to the LocalRouter
     */
    readonly tags?: pulumi.Input<pulumi.Input<string>[]>;
}
