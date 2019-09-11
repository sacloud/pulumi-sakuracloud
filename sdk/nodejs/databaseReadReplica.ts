// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Provides a SakuraCloud Database(ReadReplica) resource. This can be used to create, update, and delete Databases.
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-sakuracloud/blob/master/website/docs/r/database_read_replica.html.markdown.
 */
export class DatabaseReadReplica extends pulumi.CustomResource {
    /**
     * Get an existing DatabaseReadReplica resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
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
     * The default route IP address of the database.
     */
    public readonly defaultRoute!: pulumi.Output<string>;
    /**
     * The description of the resource.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The wait time (seconds) to do graceful shutdown the Database.
     */
    public readonly gracefulShutdownTimeout!: pulumi.Output<number | undefined>;
    /**
     * The ID of the icon.
     */
    public readonly iconId!: pulumi.Output<string | undefined>;
    /**
     * The IP address of the database.
     */
    public readonly ipaddress1!: pulumi.Output<string>;
    /**
     * The ID of the master Database Appliance.
     */
    public readonly masterId!: pulumi.Output<string>;
    /**
     * The name of the resource.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The network mask length of the database.
     */
    public readonly nwMaskLen!: pulumi.Output<number>;
    /**
     * The ID of the switch connected to the database.
     */
    public readonly switchId!: pulumi.Output<string>;
    /**
     * The tag list of the resources.
     */
    public readonly tags!: pulumi.Output<string[]>;
    /**
     * The ID of the zone to which the resource belongs.
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
        if (opts && opts.id) {
            const state = argsOrState as DatabaseReadReplicaState | undefined;
            inputs["defaultRoute"] = state ? state.defaultRoute : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["gracefulShutdownTimeout"] = state ? state.gracefulShutdownTimeout : undefined;
            inputs["iconId"] = state ? state.iconId : undefined;
            inputs["ipaddress1"] = state ? state.ipaddress1 : undefined;
            inputs["masterId"] = state ? state.masterId : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["nwMaskLen"] = state ? state.nwMaskLen : undefined;
            inputs["switchId"] = state ? state.switchId : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["zone"] = state ? state.zone : undefined;
        } else {
            const args = argsOrState as DatabaseReadReplicaArgs | undefined;
            if (!args || args.ipaddress1 === undefined) {
                throw new Error("Missing required property 'ipaddress1'");
            }
            if (!args || args.masterId === undefined) {
                throw new Error("Missing required property 'masterId'");
            }
            inputs["defaultRoute"] = args ? args.defaultRoute : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["gracefulShutdownTimeout"] = args ? args.gracefulShutdownTimeout : undefined;
            inputs["iconId"] = args ? args.iconId : undefined;
            inputs["ipaddress1"] = args ? args.ipaddress1 : undefined;
            inputs["masterId"] = args ? args.masterId : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["nwMaskLen"] = args ? args.nwMaskLen : undefined;
            inputs["switchId"] = args ? args.switchId : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["zone"] = args ? args.zone : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(DatabaseReadReplica.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering DatabaseReadReplica resources.
 */
export interface DatabaseReadReplicaState {
    /**
     * The default route IP address of the database.
     */
    readonly defaultRoute?: pulumi.Input<string>;
    /**
     * The description of the resource.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The wait time (seconds) to do graceful shutdown the Database.
     */
    readonly gracefulShutdownTimeout?: pulumi.Input<number>;
    /**
     * The ID of the icon.
     */
    readonly iconId?: pulumi.Input<string>;
    /**
     * The IP address of the database.
     */
    readonly ipaddress1?: pulumi.Input<string>;
    /**
     * The ID of the master Database Appliance.
     */
    readonly masterId?: pulumi.Input<string>;
    /**
     * The name of the resource.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The network mask length of the database.
     */
    readonly nwMaskLen?: pulumi.Input<number>;
    /**
     * The ID of the switch connected to the database.
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
 * The set of arguments for constructing a DatabaseReadReplica resource.
 */
export interface DatabaseReadReplicaArgs {
    /**
     * The default route IP address of the database.
     */
    readonly defaultRoute?: pulumi.Input<string>;
    /**
     * The description of the resource.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The wait time (seconds) to do graceful shutdown the Database.
     */
    readonly gracefulShutdownTimeout?: pulumi.Input<number>;
    /**
     * The ID of the icon.
     */
    readonly iconId?: pulumi.Input<string>;
    /**
     * The IP address of the database.
     */
    readonly ipaddress1: pulumi.Input<string>;
    /**
     * The ID of the master Database Appliance.
     */
    readonly masterId: pulumi.Input<string>;
    /**
     * The name of the resource.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The network mask length of the database.
     */
    readonly nwMaskLen?: pulumi.Input<number>;
    /**
     * The ID of the switch connected to the database.
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