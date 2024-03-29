// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "./types";
import * as utilities from "./utilities";

/**
 * Get information about an existing Disk.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as sakuracloud from "@pulumi/sakuracloud";
 *
 * const foobar = pulumi.output(sakuracloud.getDisk({
 *     filter: {
 *         names: ["foobar"],
 *     },
 * }));
 * ```
 */
export function getDisk(args?: GetDiskArgs, opts?: pulumi.InvokeOptions): Promise<GetDiskResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("sakuracloud:index/getDisk:getDisk", {
        "filter": args.filter,
        "zone": args.zone,
    }, opts);
}

/**
 * A collection of arguments for invoking getDisk.
 */
export interface GetDiskArgs {
    /**
     * One or more values used for filtering, as defined below.
     */
    filter?: inputs.GetDiskFilter;
    /**
     * The name of zone that the Disk is in (e.g. `is1a`, `tk1a`).
     */
    zone?: string;
}

/**
 * A collection of values returned by getDisk.
 */
export interface GetDiskResult {
    /**
     * The name of the disk connector. This will be one of [`virtio`/`ide`].
     */
    readonly connector: string;
    /**
     * The description of the Disk.
     */
    readonly description: string;
    readonly filter?: outputs.GetDiskFilter;
    /**
     * The icon id attached to the Disk.
     */
    readonly iconId: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * The name of the Disk.
     */
    readonly name: string;
    /**
     * The plan name of the Disk. This will be one of [`ssd`/`hdd`].
     */
    readonly plan: string;
    /**
     * The id of the Server connected to the Disk.
     */
    readonly serverId: string;
    /**
     * The size of Disk in GiB.
     */
    readonly size: number;
    /**
     * The id of the source archive.
     */
    readonly sourceArchiveId: string;
    /**
     * The id of the source disk.
     */
    readonly sourceDiskId: string;
    /**
     * Any tags assigned to the Disk.
     */
    readonly tags: string[];
    readonly zone: string;
}

export function getDiskOutput(args?: GetDiskOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetDiskResult> {
    return pulumi.output(args).apply(a => getDisk(a, opts))
}

/**
 * A collection of arguments for invoking getDisk.
 */
export interface GetDiskOutputArgs {
    /**
     * One or more values used for filtering, as defined below.
     */
    filter?: pulumi.Input<inputs.GetDiskFilterArgs>;
    /**
     * The name of zone that the Disk is in (e.g. `is1a`, `tk1a`).
     */
    zone?: pulumi.Input<string>;
}
