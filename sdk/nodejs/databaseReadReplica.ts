// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "./types";
import * as utilities from "./utilities";

/**
 * Manages a SakuraCloud Database Read Replica.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as sakuracloud from "@pulumi/sakuracloud";
 *
 * const master = sakuracloud.getDatabase({
 *     filter: {
 *         names: ["master-database-name"],
 *     },
 * });
 * const foobar = new sakuracloud.DatabaseReadReplica("foobar", {
 *     masterId: master.then(master => master.id),
 *     networkInterface: {
 *         ipAddress: "192.168.11.111",
 *     },
 *     description: "description",
 *     tags: [
 *         "tag1",
 *         "tag2",
 *     ],
 * });
 * ```
 */
export class DatabaseReadReplica extends pulumi.CustomResource {
    /**
     * Get an existing DatabaseReadReplica resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DatabaseReadReplicaState, opts?: pulumi.CustomResourceOptions): DatabaseReadReplica {
        return new DatabaseReadReplica(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'sakuracloud:index/databaseReadReplica:DatabaseReadReplica';

    /**
     * Returns true if the given object is an instance of DatabaseReadReplica.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is DatabaseReadReplica {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === DatabaseReadReplica.__pulumiType;
    }

    /**
     * The description of the read-replica database. The length of this value must be in the range [`1`-`512`].
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The icon id to attach to the read-replica database.
     */
    public readonly iconId!: pulumi.Output<string | undefined>;
    /**
     * The id of the replication master database. Changing this forces a new resource to be created.
     */
    public readonly masterId!: pulumi.Output<string>;
    /**
     * The name of the read-replica database. The length of this value must be in the range [`1`-`64`].
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * An `networkInterface` block as defined below.
     */
    public readonly networkInterface!: pulumi.Output<outputs.DatabaseReadReplicaNetworkInterface>;
    /**
     * Any tags to assign to the read-replica database.
     */
    public readonly tags!: pulumi.Output<string[] | undefined>;
    /**
     * The name of zone that the read-replica database will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
     */
    public readonly zone!: pulumi.Output<string>;

    /**
     * Create a DatabaseReadReplica resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: DatabaseReadReplicaArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: DatabaseReadReplicaArgs | DatabaseReadReplicaState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as DatabaseReadReplicaState | undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["iconId"] = state ? state.iconId : undefined;
            inputs["masterId"] = state ? state.masterId : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["networkInterface"] = state ? state.networkInterface : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["zone"] = state ? state.zone : undefined;
        } else {
            const args = argsOrState as DatabaseReadReplicaArgs | undefined;
            if ((!args || args.masterId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'masterId'");
            }
            if ((!args || args.networkInterface === undefined) && !opts.urn) {
                throw new Error("Missing required property 'networkInterface'");
            }
            inputs["description"] = args ? args.description : undefined;
            inputs["iconId"] = args ? args.iconId : undefined;
            inputs["masterId"] = args ? args.masterId : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["networkInterface"] = args ? args.networkInterface : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["zone"] = args ? args.zone : undefined;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(DatabaseReadReplica.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering DatabaseReadReplica resources.
 */
export interface DatabaseReadReplicaState {
    /**
     * The description of the read-replica database. The length of this value must be in the range [`1`-`512`].
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The icon id to attach to the read-replica database.
     */
    readonly iconId?: pulumi.Input<string>;
    /**
     * The id of the replication master database. Changing this forces a new resource to be created.
     */
    readonly masterId?: pulumi.Input<string>;
    /**
     * The name of the read-replica database. The length of this value must be in the range [`1`-`64`].
     */
    readonly name?: pulumi.Input<string>;
    /**
     * An `networkInterface` block as defined below.
     */
    readonly networkInterface?: pulumi.Input<inputs.DatabaseReadReplicaNetworkInterface>;
    /**
     * Any tags to assign to the read-replica database.
     */
    readonly tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The name of zone that the read-replica database will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
     */
    readonly zone?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a DatabaseReadReplica resource.
 */
export interface DatabaseReadReplicaArgs {
    /**
     * The description of the read-replica database. The length of this value must be in the range [`1`-`512`].
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The icon id to attach to the read-replica database.
     */
    readonly iconId?: pulumi.Input<string>;
    /**
     * The id of the replication master database. Changing this forces a new resource to be created.
     */
    readonly masterId: pulumi.Input<string>;
    /**
     * The name of the read-replica database. The length of this value must be in the range [`1`-`64`].
     */
    readonly name?: pulumi.Input<string>;
    /**
     * An `networkInterface` block as defined below.
     */
    readonly networkInterface: pulumi.Input<inputs.DatabaseReadReplicaNetworkInterface>;
    /**
     * Any tags to assign to the read-replica database.
     */
    readonly tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The name of zone that the read-replica database will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
     */
    readonly zone?: pulumi.Input<string>;
}
