// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Use this data source to retrieve information about a SakuraCloud GSLB.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as sakuracloud from "@pulumi/sakuracloud";
 * 
 * const foobar = sakuracloud.getGSLB({
 *     nameSelectors: ["foobar"],
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-sakuracloud/blob/master/website/docs/d/gslb.html.markdown.
 */
export function getGSLB(args?: GetGSLBArgs, opts?: pulumi.InvokeOptions): Promise<GetGSLBResult> & GetGSLBResult {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    const promise: Promise<GetGSLBResult> = pulumi.runtime.invoke("sakuracloud:index/getGSLB:getGSLB", {
        "filters": args.filters,
        "nameSelectors": args.nameSelectors,
        "tagSelectors": args.tagSelectors,
    }, opts);

    return pulumi.utils.liftProperties(promise, opts);
}

/**
 * A collection of arguments for invoking getGSLB.
 */
export interface GetGSLBArgs {
    /**
     * The map of filter key and value.
     */
    readonly filters?: inputs.GetGSLBFilter[];
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
 * A collection of values returned by getGSLB.
 */
export interface GetGSLBResult {
    /**
     * The description of the resource.
     */
    readonly description: string;
    readonly filters?: outputs.GetGSLBFilter[];
    /**
     * FQDN to access this resource.
     */
    readonly fqdn: string;
    /**
     * Health check rules. It contains some attributes to Health Check.
     */
    readonly healthChecks: outputs.GetGSLBHealthCheck[];
    /**
     * The ID of the icon of the resource.
     */
    readonly iconId: string;
    /**
     * Name of the resource.
     */
    readonly name: string;
    readonly nameSelectors?: string[];
    /**
     * The hostname or IP address of sorry server.
     */
    readonly sorryServer: string;
    readonly tagSelectors?: string[];
    /**
     * The tag list of the resources.
     */
    readonly tags: string[];
    /**
     * The flag for enable/disable weighting.
     */
    readonly weighted: boolean;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
