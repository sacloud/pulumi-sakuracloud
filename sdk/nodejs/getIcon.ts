// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Use this data source to retrieve information about a SakuraCloud Icon.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as sakuracloud from "@sacloud/pulumi_sakuracloud";
 * 
 * const foobar = sakuracloud.getIcon({
 *     nameSelectors: ["foobar"],
 * });
 * ```
 *
 * > This content is derived from https://github.com/sacloud/terraform-provider-sakuracloud/blob/master/website/docs/d/icon.html.markdown.
 */
export function getIcon(args?: GetIconArgs, opts?: pulumi.InvokeOptions): Promise<GetIconResult> & GetIconResult {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    const promise: Promise<GetIconResult> = pulumi.runtime.invoke("sakuracloud:index/getIcon:getIcon", {
        "filters": args.filters,
        "nameSelectors": args.nameSelectors,
        "tagSelectors": args.tagSelectors,
    }, opts);

    return pulumi.utils.liftProperties(promise, opts);
}

/**
 * A collection of arguments for invoking getIcon.
 */
export interface GetIconArgs {
    /**
     * The map of filter key and value.
     */
    readonly filters?: inputs.GetIconFilter[];
    /**
     * The list of names to filtering.
     */
    readonly nameSelectors?: string[];
    /**
     * The list of tags to filtering.
     */
    readonly tagSelectors?: string[];
}

/**
 * A collection of values returned by getIcon.
 */
export interface GetIconResult {
    /**
     * Base64 encoded icon data (size:`small`).
     */
    readonly body: string;
    readonly filters?: outputs.GetIconFilter[];
    /**
     * The name of the resource.
     */
    readonly name: string;
    readonly nameSelectors?: string[];
    readonly tagSelectors?: string[];
    /**
     * The tag list of the resources.
     */
    readonly tags: string[];
    /**
     * URL to access this resource.
     */
    readonly url: string;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
