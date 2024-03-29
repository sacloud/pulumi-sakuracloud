// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Manages a SakuraCloud Subnet.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as sakuracloud from "@pulumi/sakuracloud";
 *
 * const foobarInternet = new sakuracloud.Internet("foobarInternet", {});
 * const foobarSubnet = new sakuracloud.Subnet("foobarSubnet", {
 *     internetId: foobarInternet.id,
 *     nextHop: foobarInternet.minIpAddress,
 * });
 * ```
 */
export class Subnet extends pulumi.CustomResource {
    /**
     * Get an existing Subnet resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SubnetState, opts?: pulumi.CustomResourceOptions): Subnet {
        return new Subnet(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'sakuracloud:index/subnet:Subnet';

    /**
     * Returns true if the given object is an instance of Subnet.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Subnet {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Subnet.__pulumiType;
    }

    /**
     * The id of the switch+router resource that the subnet belongs. Changing this forces a new resource to be created.
     */
    public readonly internetId!: pulumi.Output<string>;
    /**
     * A list of assigned global address to the subnet.
     */
    public /*out*/ readonly ipAddresses!: pulumi.Output<string[]>;
    /**
     * Maximum IP address in assigned global addresses to the subnet.
     */
    public /*out*/ readonly maxIpAddress!: pulumi.Output<string>;
    /**
     * Minimum IP address in assigned global addresses to the subnet.
     */
    public /*out*/ readonly minIpAddress!: pulumi.Output<string>;
    /**
     * The bit length of the subnet to assign to the Subnet. This must be in the range [`26`-`28`]. Changing this forces a new resource to be created. Default:`28`.
     */
    public readonly netmask!: pulumi.Output<number | undefined>;
    /**
     * The IPv4 network address assigned to the Subnet.
     */
    public /*out*/ readonly networkAddress!: pulumi.Output<string>;
    /**
     * The ip address of the next-hop at the subnet.
     */
    public readonly nextHop!: pulumi.Output<string>;
    /**
     * The id of the switch connected from the Subnet.
     */
    public /*out*/ readonly switchId!: pulumi.Output<string>;
    /**
     * The name of zone that the Subnet will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
     */
    public readonly zone!: pulumi.Output<string>;

    /**
     * Create a Subnet resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: SubnetArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: SubnetArgs | SubnetState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as SubnetState | undefined;
            inputs["internetId"] = state ? state.internetId : undefined;
            inputs["ipAddresses"] = state ? state.ipAddresses : undefined;
            inputs["maxIpAddress"] = state ? state.maxIpAddress : undefined;
            inputs["minIpAddress"] = state ? state.minIpAddress : undefined;
            inputs["netmask"] = state ? state.netmask : undefined;
            inputs["networkAddress"] = state ? state.networkAddress : undefined;
            inputs["nextHop"] = state ? state.nextHop : undefined;
            inputs["switchId"] = state ? state.switchId : undefined;
            inputs["zone"] = state ? state.zone : undefined;
        } else {
            const args = argsOrState as SubnetArgs | undefined;
            if ((!args || args.internetId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'internetId'");
            }
            if ((!args || args.nextHop === undefined) && !opts.urn) {
                throw new Error("Missing required property 'nextHop'");
            }
            inputs["internetId"] = args ? args.internetId : undefined;
            inputs["netmask"] = args ? args.netmask : undefined;
            inputs["nextHop"] = args ? args.nextHop : undefined;
            inputs["zone"] = args ? args.zone : undefined;
            inputs["ipAddresses"] = undefined /*out*/;
            inputs["maxIpAddress"] = undefined /*out*/;
            inputs["minIpAddress"] = undefined /*out*/;
            inputs["networkAddress"] = undefined /*out*/;
            inputs["switchId"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(Subnet.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Subnet resources.
 */
export interface SubnetState {
    /**
     * The id of the switch+router resource that the subnet belongs. Changing this forces a new resource to be created.
     */
    internetId?: pulumi.Input<string>;
    /**
     * A list of assigned global address to the subnet.
     */
    ipAddresses?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Maximum IP address in assigned global addresses to the subnet.
     */
    maxIpAddress?: pulumi.Input<string>;
    /**
     * Minimum IP address in assigned global addresses to the subnet.
     */
    minIpAddress?: pulumi.Input<string>;
    /**
     * The bit length of the subnet to assign to the Subnet. This must be in the range [`26`-`28`]. Changing this forces a new resource to be created. Default:`28`.
     */
    netmask?: pulumi.Input<number>;
    /**
     * The IPv4 network address assigned to the Subnet.
     */
    networkAddress?: pulumi.Input<string>;
    /**
     * The ip address of the next-hop at the subnet.
     */
    nextHop?: pulumi.Input<string>;
    /**
     * The id of the switch connected from the Subnet.
     */
    switchId?: pulumi.Input<string>;
    /**
     * The name of zone that the Subnet will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
     */
    zone?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Subnet resource.
 */
export interface SubnetArgs {
    /**
     * The id of the switch+router resource that the subnet belongs. Changing this forces a new resource to be created.
     */
    internetId: pulumi.Input<string>;
    /**
     * The bit length of the subnet to assign to the Subnet. This must be in the range [`26`-`28`]. Changing this forces a new resource to be created. Default:`28`.
     */
    netmask?: pulumi.Input<number>;
    /**
     * The ip address of the next-hop at the subnet.
     */
    nextHop: pulumi.Input<string>;
    /**
     * The name of zone that the Subnet will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
     */
    zone?: pulumi.Input<string>;
}
