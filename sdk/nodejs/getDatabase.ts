// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "./types";
import * as utilities from "./utilities";

/**
 * Get information about an existing Database.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as sakuracloud from "@pulumi/sakuracloud";
 *
 * const foobar = pulumi.output(sakuracloud.getDatabase({
 *     filter: {
 *         names: ["foobar"],
 *     },
 * }));
 * ```
 */
export function getDatabase(args?: GetDatabaseArgs, opts?: pulumi.InvokeOptions): Promise<GetDatabaseResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("sakuracloud:index/getDatabase:getDatabase", {
        "filter": args.filter,
        "zone": args.zone,
    }, opts);
}

/**
 * A collection of arguments for invoking getDatabase.
 */
export interface GetDatabaseArgs {
    /**
     * One or more values used for filtering, as defined below.
     */
    filter?: inputs.GetDatabaseFilter;
    /**
     * The name of zone that the Database is in (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
     */
    zone?: string;
}

/**
 * A collection of values returned by getDatabase.
 */
export interface GetDatabaseResult {
    /**
     * A list of `backup` blocks as defined below.
     */
    readonly backups: outputs.GetDatabaseBackup[];
    /**
     * The type of the database. This will be one of [`mariadb`/`postgres`].
     */
    readonly databaseType: string;
    /**
     * The description of the Database.
     */
    readonly description: string;
    readonly filter?: outputs.GetDatabaseFilter;
    /**
     * The icon id attached to the Database.
     */
    readonly iconId: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * The name of the Database.
     */
    readonly name: string;
    /**
     * A list of `networkInterface` blocks as defined below.
     */
    readonly networkInterfaces: outputs.GetDatabaseNetworkInterface[];
    /**
     * The map for setting RDBMS-specific parameters. Valid keys can be found with the `usacloud database list-parameters` command.
     */
    readonly parameters: {[key: string]: string};
    /**
     * The password of default user on the database.
     */
    readonly password: string;
    /**
     * The plan name of the Database. This will be one of [`10g`/`30g`/`90g`/`240g`/`500g`/`1t`].
     */
    readonly plan: string;
    /**
     * The password of user that processing a replication.
     */
    readonly replicaPassword: string;
    /**
     * The name of user that processing a replication.
     */
    readonly replicaUser: string;
    /**
     * Any tags assigned to the Database.
     */
    readonly tags: string[];
    /**
     * The name of default user on the database.
     */
    readonly username: string;
    readonly zone: string;
}

export function getDatabaseOutput(args?: GetDatabaseOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetDatabaseResult> {
    return pulumi.output(args).apply(a => getDatabase(a, opts))
}

/**
 * A collection of arguments for invoking getDatabase.
 */
export interface GetDatabaseOutputArgs {
    /**
     * One or more values used for filtering, as defined below.
     */
    filter?: pulumi.Input<inputs.GetDatabaseFilterArgs>;
    /**
     * The name of zone that the Database is in (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
     */
    zone?: pulumi.Input<string>;
}
