// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Use this data source to retrieve information about a SakuraCloud Disk.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as sakuracloud from "@pulumi/sakuracloud";
 * 
 * const foobar = sakuracloud.getDisk({
 *     nameSelectors: ["foobar"],
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-sakuracloud/blob/master/website/docs/d/disk.html.markdown.
 */
export function getDisk(args?: GetDiskArgs, opts?: pulumi.InvokeOptions): Promise<GetDiskResult> & GetDiskResult {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    const promise: Promise<GetDiskResult> = pulumi.runtime.invoke("sakuracloud:index/getDisk:getDisk", {
        "filters": args.filters,
        "nameSelectors": args.nameSelectors,
        "tagSelectors": args.tagSelectors,
        "zone": args.zone,
    }, opts);

    return pulumi.utils.liftProperties(promise, opts);
}

/**
 * A collection of arguments for invoking getDisk.
 */
export interface GetDiskArgs {
    /**
     * The map of filter key and value.
     */
    readonly filters?: inputs.GetDiskFilter[];
    /**
     * The list of names to filtering.
     */
    readonly nameSelectors?: string[];
    /**
     * The list of tags to filtering.
     */
    readonly tagSelectors?: string[];
    /**
     * The ID of the zone.
     */
    readonly zone?: string;
}

/**
 * A collection of values returned by getDisk.
 */
export interface GetDiskResult {
    readonly connector: string;
    /**
     * The description of the resource.
     */
    readonly description: string;
    readonly filters?: outputs.GetDiskFilter[];
    /**
     * The ID of the icon of the resource.
     */
    readonly iconId: string;
    /**
     * The name of the resource.
     */
    readonly name: string;
    readonly nameSelectors?: string[];
    /**
     * The plan of the resource (`ssd`/`hdd`).
     */
    readonly plan: string;
    /**
     * The ID of the server connected to the disk.
     */
    readonly serverId: string;
    /**
     * Size of the resource (unit:`GB`).
     */
    readonly size: number;
    readonly tagSelectors?: string[];
    /**
     * The tag list of the resources.
     */
    readonly tags: string[];
    /**
     * The ID of the zone to which the resource belongs.
     */
    readonly zone: string;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
