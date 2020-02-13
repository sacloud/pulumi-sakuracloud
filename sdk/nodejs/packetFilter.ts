// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

export class PacketFilter extends pulumi.CustomResource {
    /**
     * Get an existing PacketFilter resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PacketFilterState, opts?: pulumi.CustomResourceOptions): PacketFilter {
        return new PacketFilter(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'sakuracloud:index/packetFilter:PacketFilter';

    /**
     * Returns true if the given object is an instance of PacketFilter.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is PacketFilter {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === PacketFilter.__pulumiType;
    }

    /**
     * The description of the packetFilter. The length of this value must be in the range [`1`-`512`]
     */
    public readonly description!: pulumi.Output<string | undefined>;
    public readonly expressions!: pulumi.Output<outputs.PacketFilterExpression[]>;
    /**
     * The name of the packetFilter. The length of this value must be in the range [`1`-`64`]
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The name of zone that the packetFilter will be created (e.g. `is1a`, `tk1a`)
     */
    public readonly zone!: pulumi.Output<string>;

    /**
     * Create a PacketFilter resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: PacketFilterArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: PacketFilterArgs | PacketFilterState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as PacketFilterState | undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["expressions"] = state ? state.expressions : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["zone"] = state ? state.zone : undefined;
        } else {
            const args = argsOrState as PacketFilterArgs | undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["expressions"] = args ? args.expressions : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["zone"] = args ? args.zone : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(PacketFilter.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering PacketFilter resources.
 */
export interface PacketFilterState {
    /**
     * The description of the packetFilter. The length of this value must be in the range [`1`-`512`]
     */
    readonly description?: pulumi.Input<string>;
    readonly expressions?: pulumi.Input<pulumi.Input<inputs.PacketFilterExpression>[]>;
    /**
     * The name of the packetFilter. The length of this value must be in the range [`1`-`64`]
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The name of zone that the packetFilter will be created (e.g. `is1a`, `tk1a`)
     */
    readonly zone?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a PacketFilter resource.
 */
export interface PacketFilterArgs {
    /**
     * The description of the packetFilter. The length of this value must be in the range [`1`-`512`]
     */
    readonly description?: pulumi.Input<string>;
    readonly expressions?: pulumi.Input<pulumi.Input<inputs.PacketFilterExpression>[]>;
    /**
     * The name of the packetFilter. The length of this value must be in the range [`1`-`64`]
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The name of zone that the packetFilter will be created (e.g. `is1a`, `tk1a`)
     */
    readonly zone?: pulumi.Input<string>;
}
