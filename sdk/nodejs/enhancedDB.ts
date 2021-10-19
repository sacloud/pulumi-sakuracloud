// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Manages a SakuraCloud sakuracloud_enhanced_db.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as sakuracloud from "@pulumi/sakuracloud";
 *
 * const foobar = new sakuracloud.EnhancedDB("foobar", {
 *     databaseName: "example",
 *     description: "...",
 *     password: "your-password",
 *     tags: [
 *         "...",
 *         "...",
 *     ],
 * });
 * ```
 */
export class EnhancedDB extends pulumi.CustomResource {
    /**
     * Get an existing EnhancedDB resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: EnhancedDBState, opts?: pulumi.CustomResourceOptions): EnhancedDB {
        return new EnhancedDB(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'sakuracloud:index/enhancedDB:EnhancedDB';

    /**
     * Returns true if the given object is an instance of EnhancedDB.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is EnhancedDB {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === EnhancedDB.__pulumiType;
    }

    /**
     * The name of database. Changing this forces a new resource to be created.
     */
    public readonly databaseName!: pulumi.Output<string>;
    /**
     * The type of database.
     */
    public /*out*/ readonly databaseType!: pulumi.Output<string>;
    /**
     * The description of the Enhanced Database. The length of this value must be in the range [`1`-`512`].
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The name of database host. This will be built from `databaseName` + `tidb-is1.db.sakurausercontent.com`.
     */
    public /*out*/ readonly hostname!: pulumi.Output<string>;
    /**
     * The icon id to attach to the Enhanced Database.
     */
    public readonly iconId!: pulumi.Output<string | undefined>;
    /**
     * The value of max connections setting.
     */
    public /*out*/ readonly maxConnections!: pulumi.Output<number>;
    /**
     * The name of the Enhanced Database. The length of this value must be in the range [`1`-`64`].
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The password of database.
     */
    public readonly password!: pulumi.Output<string>;
    /**
     * The region name.
     */
    public /*out*/ readonly region!: pulumi.Output<string>;
    /**
     * Any tags to assign to the Enhanced Database.
     */
    public readonly tags!: pulumi.Output<string[] | undefined>;

    /**
     * Create a EnhancedDB resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: EnhancedDBArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: EnhancedDBArgs | EnhancedDBState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as EnhancedDBState | undefined;
            inputs["databaseName"] = state ? state.databaseName : undefined;
            inputs["databaseType"] = state ? state.databaseType : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["hostname"] = state ? state.hostname : undefined;
            inputs["iconId"] = state ? state.iconId : undefined;
            inputs["maxConnections"] = state ? state.maxConnections : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["password"] = state ? state.password : undefined;
            inputs["region"] = state ? state.region : undefined;
            inputs["tags"] = state ? state.tags : undefined;
        } else {
            const args = argsOrState as EnhancedDBArgs | undefined;
            if ((!args || args.databaseName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'databaseName'");
            }
            if ((!args || args.password === undefined) && !opts.urn) {
                throw new Error("Missing required property 'password'");
            }
            inputs["databaseName"] = args ? args.databaseName : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["iconId"] = args ? args.iconId : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["password"] = args ? args.password : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["databaseType"] = undefined /*out*/;
            inputs["hostname"] = undefined /*out*/;
            inputs["maxConnections"] = undefined /*out*/;
            inputs["region"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(EnhancedDB.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering EnhancedDB resources.
 */
export interface EnhancedDBState {
    /**
     * The name of database. Changing this forces a new resource to be created.
     */
    readonly databaseName?: pulumi.Input<string>;
    /**
     * The type of database.
     */
    readonly databaseType?: pulumi.Input<string>;
    /**
     * The description of the Enhanced Database. The length of this value must be in the range [`1`-`512`].
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The name of database host. This will be built from `databaseName` + `tidb-is1.db.sakurausercontent.com`.
     */
    readonly hostname?: pulumi.Input<string>;
    /**
     * The icon id to attach to the Enhanced Database.
     */
    readonly iconId?: pulumi.Input<string>;
    /**
     * The value of max connections setting.
     */
    readonly maxConnections?: pulumi.Input<number>;
    /**
     * The name of the Enhanced Database. The length of this value must be in the range [`1`-`64`].
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The password of database.
     */
    readonly password?: pulumi.Input<string>;
    /**
     * The region name.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * Any tags to assign to the Enhanced Database.
     */
    readonly tags?: pulumi.Input<pulumi.Input<string>[]>;
}

/**
 * The set of arguments for constructing a EnhancedDB resource.
 */
export interface EnhancedDBArgs {
    /**
     * The name of database. Changing this forces a new resource to be created.
     */
    readonly databaseName: pulumi.Input<string>;
    /**
     * The description of the Enhanced Database. The length of this value must be in the range [`1`-`512`].
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The icon id to attach to the Enhanced Database.
     */
    readonly iconId?: pulumi.Input<string>;
    /**
     * The name of the Enhanced Database. The length of this value must be in the range [`1`-`64`].
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The password of database.
     */
    readonly password: pulumi.Input<string>;
    /**
     * Any tags to assign to the Enhanced Database.
     */
    readonly tags?: pulumi.Input<pulumi.Input<string>[]>;
}
