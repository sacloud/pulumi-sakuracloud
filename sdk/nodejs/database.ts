// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Provides a SakuraCloud Database resource. This can be used to create, update, and delete Databases.
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-sakuracloud/blob/master/website/docs/r/database.html.markdown.
 */
export class Database extends pulumi.CustomResource {
    /**
     * Get an existing Database resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DatabaseState, opts?: pulumi.CustomResourceOptions): Database {
        return new Database(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'sakuracloud:index/database:Database';

    /**
     * Returns true if the given object is an instance of Database.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Database {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Database.__pulumiType;
    }

    /**
     * The network address list that allowed connections to the database.
     */
    public readonly allowNetworks!: pulumi.Output<string[] | undefined>;
    /**
     * The time to perform backup (format:`HH:mm`).
     */
    public readonly backupTime!: pulumi.Output<string | undefined>;
    /**
     * Day of the week to get backup.  
     * Valid values are the following: ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
     */
    public readonly backupWeekdays!: pulumi.Output<string[] | undefined>;
    /**
     * The Database type.  
     * Valid value is one of the following: [ "postgresql" (default) / "mariadb"]
     */
    public readonly databaseType!: pulumi.Output<string | undefined>;
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
     * The name of the resource.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The network mask length of the database.
     */
    public readonly nwMaskLen!: pulumi.Output<number>;
    /**
     * The plan (size) of the Database.   
     * Valid value is one of the following: [ "10g" (default) / "30g" / "90g" / "240g" / "500g" / "1t" ]
     */
    public readonly plan!: pulumi.Output<string | undefined>;
    /**
     * The number of the port on which the database is listening (default:`5432`).
     */
    public readonly port!: pulumi.Output<number | undefined>;
    public readonly replicaPassword!: pulumi.Output<string | undefined>;
    public /*out*/ readonly replicaUser!: pulumi.Output<string>;
    /**
     * The ID of the switch connected to the database.
     */
    public readonly switchId!: pulumi.Output<string>;
    /**
     * The tag list of the resources.
     */
    public readonly tags!: pulumi.Output<string[]>;
    /**
     * The username to access database.
     */
    public readonly userName!: pulumi.Output<string>;
    /**
     * The password to access database.
     */
    public readonly userPassword!: pulumi.Output<string>;
    /**
     * The ID of the zone to which the resource belongs.
     */
    public readonly zone!: pulumi.Output<string>;

    /**
     * Create a Database resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: DatabaseArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: DatabaseArgs | DatabaseState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as DatabaseState | undefined;
            inputs["allowNetworks"] = state ? state.allowNetworks : undefined;
            inputs["backupTime"] = state ? state.backupTime : undefined;
            inputs["backupWeekdays"] = state ? state.backupWeekdays : undefined;
            inputs["databaseType"] = state ? state.databaseType : undefined;
            inputs["defaultRoute"] = state ? state.defaultRoute : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["gracefulShutdownTimeout"] = state ? state.gracefulShutdownTimeout : undefined;
            inputs["iconId"] = state ? state.iconId : undefined;
            inputs["ipaddress1"] = state ? state.ipaddress1 : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["nwMaskLen"] = state ? state.nwMaskLen : undefined;
            inputs["plan"] = state ? state.plan : undefined;
            inputs["port"] = state ? state.port : undefined;
            inputs["replicaPassword"] = state ? state.replicaPassword : undefined;
            inputs["replicaUser"] = state ? state.replicaUser : undefined;
            inputs["switchId"] = state ? state.switchId : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["userName"] = state ? state.userName : undefined;
            inputs["userPassword"] = state ? state.userPassword : undefined;
            inputs["zone"] = state ? state.zone : undefined;
        } else {
            const args = argsOrState as DatabaseArgs | undefined;
            if (!args || args.defaultRoute === undefined) {
                throw new Error("Missing required property 'defaultRoute'");
            }
            if (!args || args.ipaddress1 === undefined) {
                throw new Error("Missing required property 'ipaddress1'");
            }
            if (!args || args.nwMaskLen === undefined) {
                throw new Error("Missing required property 'nwMaskLen'");
            }
            if (!args || args.switchId === undefined) {
                throw new Error("Missing required property 'switchId'");
            }
            if (!args || args.userName === undefined) {
                throw new Error("Missing required property 'userName'");
            }
            if (!args || args.userPassword === undefined) {
                throw new Error("Missing required property 'userPassword'");
            }
            inputs["allowNetworks"] = args ? args.allowNetworks : undefined;
            inputs["backupTime"] = args ? args.backupTime : undefined;
            inputs["backupWeekdays"] = args ? args.backupWeekdays : undefined;
            inputs["databaseType"] = args ? args.databaseType : undefined;
            inputs["defaultRoute"] = args ? args.defaultRoute : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["gracefulShutdownTimeout"] = args ? args.gracefulShutdownTimeout : undefined;
            inputs["iconId"] = args ? args.iconId : undefined;
            inputs["ipaddress1"] = args ? args.ipaddress1 : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["nwMaskLen"] = args ? args.nwMaskLen : undefined;
            inputs["plan"] = args ? args.plan : undefined;
            inputs["port"] = args ? args.port : undefined;
            inputs["replicaPassword"] = args ? args.replicaPassword : undefined;
            inputs["switchId"] = args ? args.switchId : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["userName"] = args ? args.userName : undefined;
            inputs["userPassword"] = args ? args.userPassword : undefined;
            inputs["zone"] = args ? args.zone : undefined;
            inputs["replicaUser"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Database.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Database resources.
 */
export interface DatabaseState {
    /**
     * The network address list that allowed connections to the database.
     */
    readonly allowNetworks?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The time to perform backup (format:`HH:mm`).
     */
    readonly backupTime?: pulumi.Input<string>;
    /**
     * Day of the week to get backup.  
     * Valid values are the following: ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
     */
    readonly backupWeekdays?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The Database type.  
     * Valid value is one of the following: [ "postgresql" (default) / "mariadb"]
     */
    readonly databaseType?: pulumi.Input<string>;
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
     * The name of the resource.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The network mask length of the database.
     */
    readonly nwMaskLen?: pulumi.Input<number>;
    /**
     * The plan (size) of the Database.   
     * Valid value is one of the following: [ "10g" (default) / "30g" / "90g" / "240g" / "500g" / "1t" ]
     */
    readonly plan?: pulumi.Input<string>;
    /**
     * The number of the port on which the database is listening (default:`5432`).
     */
    readonly port?: pulumi.Input<number>;
    readonly replicaPassword?: pulumi.Input<string>;
    readonly replicaUser?: pulumi.Input<string>;
    /**
     * The ID of the switch connected to the database.
     */
    readonly switchId?: pulumi.Input<string>;
    /**
     * The tag list of the resources.
     */
    readonly tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The username to access database.
     */
    readonly userName?: pulumi.Input<string>;
    /**
     * The password to access database.
     */
    readonly userPassword?: pulumi.Input<string>;
    /**
     * The ID of the zone to which the resource belongs.
     */
    readonly zone?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Database resource.
 */
export interface DatabaseArgs {
    /**
     * The network address list that allowed connections to the database.
     */
    readonly allowNetworks?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The time to perform backup (format:`HH:mm`).
     */
    readonly backupTime?: pulumi.Input<string>;
    /**
     * Day of the week to get backup.  
     * Valid values are the following: ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
     */
    readonly backupWeekdays?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The Database type.  
     * Valid value is one of the following: [ "postgresql" (default) / "mariadb"]
     */
    readonly databaseType?: pulumi.Input<string>;
    /**
     * The default route IP address of the database.
     */
    readonly defaultRoute: pulumi.Input<string>;
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
     * The name of the resource.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The network mask length of the database.
     */
    readonly nwMaskLen: pulumi.Input<number>;
    /**
     * The plan (size) of the Database.   
     * Valid value is one of the following: [ "10g" (default) / "30g" / "90g" / "240g" / "500g" / "1t" ]
     */
    readonly plan?: pulumi.Input<string>;
    /**
     * The number of the port on which the database is listening (default:`5432`).
     */
    readonly port?: pulumi.Input<number>;
    readonly replicaPassword?: pulumi.Input<string>;
    /**
     * The ID of the switch connected to the database.
     */
    readonly switchId: pulumi.Input<string>;
    /**
     * The tag list of the resources.
     */
    readonly tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The username to access database.
     */
    readonly userName: pulumi.Input<string>;
    /**
     * The password to access database.
     */
    readonly userPassword: pulumi.Input<string>;
    /**
     * The ID of the zone to which the resource belongs.
     */
    readonly zone?: pulumi.Input<string>;
}