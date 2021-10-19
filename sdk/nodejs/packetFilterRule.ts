// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "./types";
import * as utilities from "./utilities";

/**
 * Manages a SakuraCloud Packet Filter Rules.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as sakuracloud from "@pulumi/sakuracloud";
 *
 * const foobar = new sakuracloud.PacketFilter("foobar", {description: "description"});
 * const rules = new sakuracloud.PacketFilterRule("rules", {
 *     packetFilterId: foobar.id,
 *     expressions: [
 *         {
 *             protocol: "tcp",
 *             destinationPort: "22",
 *         },
 *         {
 *             protocol: "tcp",
 *             destinationPort: "80",
 *         },
 *         {
 *             protocol: "tcp",
 *             destinationPort: "443",
 *         },
 *         {
 *             protocol: "icmp",
 *         },
 *         {
 *             protocol: "fragment",
 *         },
 *         {
 *             protocol: "udp",
 *             sourcePort: "123",
 *         },
 *         {
 *             protocol: "tcp",
 *             destinationPort: "32768-61000",
 *         },
 *         {
 *             protocol: "udp",
 *             destinationPort: "32768-61000",
 *         },
 *         {
 *             protocol: "ip",
 *             allow: false,
 *             description: "Deny ALL",
 *         },
 *     ],
 * });
 * ```
 */
export class PacketFilterRule extends pulumi.CustomResource {
    /**
     * Get an existing PacketFilterRule resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PacketFilterRuleState, opts?: pulumi.CustomResourceOptions): PacketFilterRule {
        return new PacketFilterRule(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'sakuracloud:index/packetFilterRule:PacketFilterRule';

    /**
     * Returns true if the given object is an instance of PacketFilterRule.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is PacketFilterRule {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === PacketFilterRule.__pulumiType;
    }

    /**
     * One or more `expression` blocks as defined below. Changing this forces a new resource to be created.
     */
    public readonly expressions!: pulumi.Output<outputs.PacketFilterRuleExpression[] | undefined>;
    /**
     * The id of the packet filter that set expressions to. Changing this forces a new resource to be created.
     */
    public readonly packetFilterId!: pulumi.Output<string>;
    /**
     * The name of zone that the PacketFilter Rule will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
     */
    public readonly zone!: pulumi.Output<string>;

    /**
     * Create a PacketFilterRule resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: PacketFilterRuleArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: PacketFilterRuleArgs | PacketFilterRuleState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as PacketFilterRuleState | undefined;
            inputs["expressions"] = state ? state.expressions : undefined;
            inputs["packetFilterId"] = state ? state.packetFilterId : undefined;
            inputs["zone"] = state ? state.zone : undefined;
        } else {
            const args = argsOrState as PacketFilterRuleArgs | undefined;
            if ((!args || args.packetFilterId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'packetFilterId'");
            }
            inputs["expressions"] = args ? args.expressions : undefined;
            inputs["packetFilterId"] = args ? args.packetFilterId : undefined;
            inputs["zone"] = args ? args.zone : undefined;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(PacketFilterRule.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering PacketFilterRule resources.
 */
export interface PacketFilterRuleState {
    /**
     * One or more `expression` blocks as defined below. Changing this forces a new resource to be created.
     */
    expressions?: pulumi.Input<pulumi.Input<inputs.PacketFilterRuleExpression>[]>;
    /**
     * The id of the packet filter that set expressions to. Changing this forces a new resource to be created.
     */
    packetFilterId?: pulumi.Input<string>;
    /**
     * The name of zone that the PacketFilter Rule will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
     */
    zone?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a PacketFilterRule resource.
 */
export interface PacketFilterRuleArgs {
    /**
     * One or more `expression` blocks as defined below. Changing this forces a new resource to be created.
     */
    expressions?: pulumi.Input<pulumi.Input<inputs.PacketFilterRuleExpression>[]>;
    /**
     * The id of the packet filter that set expressions to. Changing this forces a new resource to be created.
     */
    packetFilterId: pulumi.Input<string>;
    /**
     * The name of zone that the PacketFilter Rule will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
     */
    zone?: pulumi.Input<string>;
}
