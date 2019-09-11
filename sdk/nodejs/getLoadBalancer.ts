// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Use this data source to retrieve information about a SakuraCloud Load Balancer.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as sakuracloud from "@sacloud/pulumi_sakuracloud";
 * 
 * const foobar = sakuracloud.getLoadBalancer({
 *     nameSelectors: ["foobar"],
 * });
 * ```
 *
 * > This content is derived from https://github.com/sacloud/terraform-provider-sakuracloud/blob/master/website/docs/d/load_balancer.html.markdown.
 */
export function getLoadBalancer(args?: GetLoadBalancerArgs, opts?: pulumi.InvokeOptions): Promise<GetLoadBalancerResult> & GetLoadBalancerResult {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    const promise: Promise<GetLoadBalancerResult> = pulumi.runtime.invoke("sakuracloud:index/getLoadBalancer:getLoadBalancer", {
        "filters": args.filters,
        "nameSelectors": args.nameSelectors,
        "tagSelectors": args.tagSelectors,
        "zone": args.zone,
    }, opts);

    return pulumi.utils.liftProperties(promise, opts);
}

/**
 * A collection of arguments for invoking getLoadBalancer.
 */
export interface GetLoadBalancerArgs {
    /**
     * The map of filter key and value.
     */
    readonly filters?: inputs.GetLoadBalancerFilter[];
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
 * A collection of values returned by getLoadBalancer.
 */
export interface GetLoadBalancerResult {
    /**
     * Default gateway address of the Load Balancer.	 
     */
    readonly defaultRoute: string;
    /**
     * The description of the resource.
     */
    readonly description: string;
    readonly filters?: outputs.GetLoadBalancerFilter[];
    /**
     * The flag of enable/disable high-availability mode.
     */
    readonly highAvailability: boolean;
    /**
     * The ID of the icon of the resource.
     */
    readonly iconId: string;
    /**
     * The primary IP address of the Load Balancer.
     */
    readonly ipaddress1: string;
    /**
     * The secondly IP address of the Load Balancer. Used when high-availability mode enabled.
     */
    readonly ipaddress2: string;
    /**
     * The name of the resource.
     */
    readonly name: string;
    readonly nameSelectors?: string[];
    /**
     * Network mask length.
     */
    readonly nwMaskLen: number;
    /**
     * The name of the resource plan. 
     */
    readonly plan: string;
    /**
     * The ID of the Switch connected to the Load Balancer.
     */
    readonly switchId: string;
    readonly tagSelectors?: string[];
    /**
     * The tag list of the resources.
     */
    readonly tags: string[];
    /**
     * VRID used when high-availability mode enabled.
     */
    readonly vrid: number;
    /**
     * The ID of the zone to which the resource belongs.
     */
    readonly zone: string;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
