// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

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

    public readonly backup!: pulumi.Output<outputs.DatabaseBackup | undefined>;
    /**
     * The type of the database. This must be one of [`mariadb`/`postgres`]
     */
    public readonly databaseType!: pulumi.Output<string | undefined>;
    /**
     * The description of the Database. The length of this value must be in the range [`1`-`512`]
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The icon id to attach to the Database
     */
    public readonly iconId!: pulumi.Output<string | undefined>;
    /**
     * The name of the Database. The length of this value must be in the range [`1`-`64`]
     */
    public readonly name!: pulumi.Output<string>;
    public readonly networkInterface!: pulumi.Output<outputs.DatabaseNetworkInterface>;
    /**
     * The password of default user on the database
     */
    public readonly password!: pulumi.Output<string>;
    /**
     * The plan name of the Database. This must be one of [`10g`/`30g`/`90g`/`240g`/`500g`/`1t`]
     */
    public readonly plan!: pulumi.Output<string | undefined>;
    /**
     * The password of user that processing a replication
     */
    public readonly replicaPassword!: pulumi.Output<string | undefined>;
    /**
     * The name of user that processing a replication
     */
    public readonly replicaUser!: pulumi.Output<string | undefined>;
    /**
     * Any tags to assign to the Database
     */
    public readonly tags!: pulumi.Output<string[] | undefined>;
    /**
     * The name of default user on the database. The length of this value must be in the range [`3`-`20`]
     */
    public readonly username!: pulumi.Output<string>;
    /**
     * The name of zone that the Database will be created (e.g. `is1a`, `tk1a`)
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
            inputs["backup"] = state ? state.backup : undefined;
            inputs["databaseType"] = state ? state.databaseType : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["iconId"] = state ? state.iconId : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["networkInterface"] = state ? state.networkInterface : undefined;
            inputs["password"] = state ? state.password : undefined;
            inputs["plan"] = state ? state.plan : undefined;
            inputs["replicaPassword"] = state ? state.replicaPassword : undefined;
            inputs["replicaUser"] = state ? state.replicaUser : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["username"] = state ? state.username : undefined;
            inputs["zone"] = state ? state.zone : undefined;
        } else {
            const args = argsOrState as DatabaseArgs | undefined;
            if (!args || args.networkInterface === undefined) {
                throw new Error("Missing required property 'networkInterface'");
            }
            if (!args || args.password === undefined) {
                throw new Error("Missing required property 'password'");
            }
            if (!args || args.username === undefined) {
                throw new Error("Missing required property 'username'");
            }
            inputs["backup"] = args ? args.backup : undefined;
            inputs["databaseType"] = args ? args.databaseType : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["iconId"] = args ? args.iconId : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["networkInterface"] = args ? args.networkInterface : undefined;
            inputs["password"] = args ? args.password : undefined;
            inputs["plan"] = args ? args.plan : undefined;
            inputs["replicaPassword"] = args ? args.replicaPassword : undefined;
            inputs["replicaUser"] = args ? args.replicaUser : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["username"] = args ? args.username : undefined;
            inputs["zone"] = args ? args.zone : undefined;
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
    readonly backup?: pulumi.Input<inputs.DatabaseBackup>;
    /**
     * The type of the database. This must be one of [`mariadb`/`postgres`]
     */
    readonly databaseType?: pulumi.Input<string>;
    /**
     * The description of the Database. The length of this value must be in the range [`1`-`512`]
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The icon id to attach to the Database
     */
    readonly iconId?: pulumi.Input<string>;
    /**
     * The name of the Database. The length of this value must be in the range [`1`-`64`]
     */
    readonly name?: pulumi.Input<string>;
    readonly networkInterface?: pulumi.Input<inputs.DatabaseNetworkInterface>;
    /**
     * The password of default user on the database
     */
    readonly password?: pulumi.Input<string>;
    /**
     * The plan name of the Database. This must be one of [`10g`/`30g`/`90g`/`240g`/`500g`/`1t`]
     */
    readonly plan?: pulumi.Input<string>;
    /**
     * The password of user that processing a replication
     */
    readonly replicaPassword?: pulumi.Input<string>;
    /**
     * The name of user that processing a replication
     */
    readonly replicaUser?: pulumi.Input<string>;
    /**
     * Any tags to assign to the Database
     */
    readonly tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The name of default user on the database. The length of this value must be in the range [`3`-`20`]
     */
    readonly username?: pulumi.Input<string>;
    /**
     * The name of zone that the Database will be created (e.g. `is1a`, `tk1a`)
     */
    readonly zone?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Database resource.
 */
export interface DatabaseArgs {
    readonly backup?: pulumi.Input<inputs.DatabaseBackup>;
    /**
     * The type of the database. This must be one of [`mariadb`/`postgres`]
     */
    readonly databaseType?: pulumi.Input<string>;
    /**
     * The description of the Database. The length of this value must be in the range [`1`-`512`]
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The icon id to attach to the Database
     */
    readonly iconId?: pulumi.Input<string>;
    /**
     * The name of the Database. The length of this value must be in the range [`1`-`64`]
     */
    readonly name?: pulumi.Input<string>;
    readonly networkInterface: pulumi.Input<inputs.DatabaseNetworkInterface>;
    /**
     * The password of default user on the database
     */
    readonly password: pulumi.Input<string>;
    /**
     * The plan name of the Database. This must be one of [`10g`/`30g`/`90g`/`240g`/`500g`/`1t`]
     */
    readonly plan?: pulumi.Input<string>;
    /**
     * The password of user that processing a replication
     */
    readonly replicaPassword?: pulumi.Input<string>;
    /**
     * The name of user that processing a replication
     */
    readonly replicaUser?: pulumi.Input<string>;
    /**
     * Any tags to assign to the Database
     */
    readonly tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The name of default user on the database. The length of this value must be in the range [`3`-`20`]
     */
    readonly username: pulumi.Input<string>;
    /**
     * The name of zone that the Database will be created (e.g. `is1a`, `tk1a`)
     */
    readonly zone?: pulumi.Input<string>;
}
