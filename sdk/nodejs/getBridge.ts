// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Use this data source to retrieve information about a SakuraCloud Bridge.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as sakuracloud from "@sacloud/pulumi_sakuracloud";
 * 
 * const foobar = sakuracloud.getBridge({
 *     nameSelectors: ["foobar"],
 * });
 * ```
 *
 * > This content is derived from https://github.com/sacloud/terraform-provider-sakuracloud/blob/master/website/docs/d/bridge.html.markdown.
 */
export function getBridge(args?: GetBridgeArgs, opts?: pulumi.InvokeOptions): Promise<GetBridgeResult> & GetBridgeResult {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    const promise: Promise<GetBridgeResult> = pulumi.runtime.invoke("sakuracloud:index/getBridge:getBridge", {
        "filters": args.filters,
        "nameSelectors": args.nameSelectors,
        "zone": args.zone,
    }, opts);

    return pulumi.utils.liftProperties(promise, opts);
}

/**
 * A collection of arguments for invoking getBridge.
 */
export interface GetBridgeArgs {
    /**
     * The map of filter key and value.
     */
    readonly filters?: inputs.GetBridgeFilter[];
    /**
     * The list of names to filtering.
     */
    readonly nameSelectors?: string[];
    /**
     * The ID of the zone.
     */
    readonly zone?: string;
}

/**
 * A collection of values returned by getBridge.
 */
export interface GetBridgeResult {
    /**
     * The description of the resource.
     */
    readonly description: string;
    readonly filters?: outputs.GetBridgeFilter[];
    /**
     * The name of the resource.
     */
    readonly name: string;
    readonly nameSelectors?: string[];
    /**
     * The ID list of the switches connected to the bridge.
     */
    readonly switchIds: string[];
    /**
     * The ID of the zone to which the resource belongs.
     */
    readonly zone: string;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
