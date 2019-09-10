// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Provides a SakuraCloud Internet resource. This can be used to create, update, and delete Internet.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as sakuracloud from "@pulumi/sakuracloud";
 * 
 * // Create a new Internet
 * const foobar = new sakuracloud.Internet("foobar", {
 *     bandWidth: 100,
 *     description: "description",
 *     enableIpv6: true,
 *     nwMaskKen: 28,
 *     tags: [
 *         "foo",
 *         "bar",
 *     ],
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-sakuracloud/blob/master/website/docs/r/internet.html.markdown.
 */
export class Internet extends pulumi.CustomResource {
    /**
     * Get an existing Internet resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: InternetState, opts?: pulumi.CustomResourceOptions): Internet {
        return new Internet(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'sakuracloud:index/internet:Internet';

    /**
     * Returns true if the given object is an instance of Internet.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Internet {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Internet.__pulumiType;
    }

    /**
     * Bandwidth of outbound traffic (unit:`Mbps`).  
     * Valid value is one of the following: [ 100 (default) / 250 / 500 / 1000 / 1500 / 2000 / 2500 / 3000 / 5000 ]
     */
    public readonly bandWidth!: pulumi.Output<number | undefined>;
    /**
     * The description of the resource.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The ipv6 enabled flag.
     */
    public readonly enableIpv6!: pulumi.Output<boolean>;
    /**
     * The network gateway address of the switch.
     */
    public /*out*/ readonly gateway!: pulumi.Output<string>;
    /**
     * The wait time (seconds) to do graceful shutdown the server connected to the resource.
     */
    public readonly gracefulShutdownTimeout!: pulumi.Output<number | undefined>;
    /**
     * The ID of the icon.
     */
    public readonly iconId!: pulumi.Output<string | undefined>;
    /**
     * Global IP address list.
     */
    public /*out*/ readonly ipaddresses!: pulumi.Output<string[]>;
    /**
     * The ipv6 network address.
     */
    public /*out*/ readonly ipv6NwAddress!: pulumi.Output<string>;
    /**
     * Address prefix of ipv6 network.
     */
    public /*out*/ readonly ipv6Prefix!: pulumi.Output<string>;
    /**
     * Address prefix length of ipv6 network.
     */
    public /*out*/ readonly ipv6PrefixLen!: pulumi.Output<number>;
    /**
     * Max global IP address.
     */
    public /*out*/ readonly maxIpaddress!: pulumi.Output<string>;
    /**
     * Min global IP address.
     */
    public /*out*/ readonly minIpaddress!: pulumi.Output<string>;
    /**
     * The name of the resource.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The network address.
     */
    public /*out*/ readonly nwAddress!: pulumi.Output<string>;
    /**
     * Network mask length.  
     * Valid value is one of the following: [ 28 (default) / 27 / 26 ]
     */
    public readonly nwMaskLen!: pulumi.Output<number | undefined>;
    /**
     * The ID list of the servers connected to the switch.
     */
    public /*out*/ readonly serverIds!: pulumi.Output<string[]>;
    /**
     * The ID of the switch.
     */
    public /*out*/ readonly switchId!: pulumi.Output<string>;
    /**
     * The tag list of the resources.
     */
    public readonly tags!: pulumi.Output<string[]>;
    /**
     * The ID of the zone to which the resource belongs.
     */
    public readonly zone!: pulumi.Output<string>;

    /**
     * Create a Internet resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: InternetArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: InternetArgs | InternetState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as InternetState | undefined;
            inputs["bandWidth"] = state ? state.bandWidth : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["enableIpv6"] = state ? state.enableIpv6 : undefined;
            inputs["gateway"] = state ? state.gateway : undefined;
            inputs["gracefulShutdownTimeout"] = state ? state.gracefulShutdownTimeout : undefined;
            inputs["iconId"] = state ? state.iconId : undefined;
            inputs["ipaddresses"] = state ? state.ipaddresses : undefined;
            inputs["ipv6NwAddress"] = state ? state.ipv6NwAddress : undefined;
            inputs["ipv6Prefix"] = state ? state.ipv6Prefix : undefined;
            inputs["ipv6PrefixLen"] = state ? state.ipv6PrefixLen : undefined;
            inputs["maxIpaddress"] = state ? state.maxIpaddress : undefined;
            inputs["minIpaddress"] = state ? state.minIpaddress : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["nwAddress"] = state ? state.nwAddress : undefined;
            inputs["nwMaskLen"] = state ? state.nwMaskLen : undefined;
            inputs["serverIds"] = state ? state.serverIds : undefined;
            inputs["switchId"] = state ? state.switchId : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["zone"] = state ? state.zone : undefined;
        } else {
            const args = argsOrState as InternetArgs | undefined;
            inputs["bandWidth"] = args ? args.bandWidth : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["enableIpv6"] = args ? args.enableIpv6 : undefined;
            inputs["gracefulShutdownTimeout"] = args ? args.gracefulShutdownTimeout : undefined;
            inputs["iconId"] = args ? args.iconId : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["nwMaskLen"] = args ? args.nwMaskLen : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["zone"] = args ? args.zone : undefined;
            inputs["gateway"] = undefined /*out*/;
            inputs["ipaddresses"] = undefined /*out*/;
            inputs["ipv6NwAddress"] = undefined /*out*/;
            inputs["ipv6Prefix"] = undefined /*out*/;
            inputs["ipv6PrefixLen"] = undefined /*out*/;
            inputs["maxIpaddress"] = undefined /*out*/;
            inputs["minIpaddress"] = undefined /*out*/;
            inputs["nwAddress"] = undefined /*out*/;
            inputs["serverIds"] = undefined /*out*/;
            inputs["switchId"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Internet.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Internet resources.
 */
export interface InternetState {
    /**
     * Bandwidth of outbound traffic (unit:`Mbps`).  
     * Valid value is one of the following: [ 100 (default) / 250 / 500 / 1000 / 1500 / 2000 / 2500 / 3000 / 5000 ]
     */
    readonly bandWidth?: pulumi.Input<number>;
    /**
     * The description of the resource.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The ipv6 enabled flag.
     */
    readonly enableIpv6?: pulumi.Input<boolean>;
    /**
     * The network gateway address of the switch.
     */
    readonly gateway?: pulumi.Input<string>;
    /**
     * The wait time (seconds) to do graceful shutdown the server connected to the resource.
     */
    readonly gracefulShutdownTimeout?: pulumi.Input<number>;
    /**
     * The ID of the icon.
     */
    readonly iconId?: pulumi.Input<string>;
    /**
     * Global IP address list.
     */
    readonly ipaddresses?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The ipv6 network address.
     */
    readonly ipv6NwAddress?: pulumi.Input<string>;
    /**
     * Address prefix of ipv6 network.
     */
    readonly ipv6Prefix?: pulumi.Input<string>;
    /**
     * Address prefix length of ipv6 network.
     */
    readonly ipv6PrefixLen?: pulumi.Input<number>;
    /**
     * Max global IP address.
     */
    readonly maxIpaddress?: pulumi.Input<string>;
    /**
     * Min global IP address.
     */
    readonly minIpaddress?: pulumi.Input<string>;
    /**
     * The name of the resource.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The network address.
     */
    readonly nwAddress?: pulumi.Input<string>;
    /**
     * Network mask length.  
     * Valid value is one of the following: [ 28 (default) / 27 / 26 ]
     */
    readonly nwMaskLen?: pulumi.Input<number>;
    /**
     * The ID list of the servers connected to the switch.
     */
    readonly serverIds?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The ID of the switch.
     */
    readonly switchId?: pulumi.Input<string>;
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
 * The set of arguments for constructing a Internet resource.
 */
export interface InternetArgs {
    /**
     * Bandwidth of outbound traffic (unit:`Mbps`).  
     * Valid value is one of the following: [ 100 (default) / 250 / 500 / 1000 / 1500 / 2000 / 2500 / 3000 / 5000 ]
     */
    readonly bandWidth?: pulumi.Input<number>;
    /**
     * The description of the resource.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The ipv6 enabled flag.
     */
    readonly enableIpv6?: pulumi.Input<boolean>;
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
     * Network mask length.  
     * Valid value is one of the following: [ 28 (default) / 27 / 26 ]
     */
    readonly nwMaskLen?: pulumi.Input<number>;
    /**
     * The tag list of the resources.
     */
    readonly tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The ID of the zone to which the resource belongs.
     */
    readonly zone?: pulumi.Input<string>;
}
