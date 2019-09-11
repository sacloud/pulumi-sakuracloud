// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Use this data source to retrieve information about a SakuraCloud Internet (Switch+Router).
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as sakuracloud from "@sacloud/pulumi_sakuracloud";
 * 
 * const foobar = sakuracloud.getInternet({
 *     nameSelectors: ["foobar"],
 * });
 * ```
 *
 * > This content is derived from https://github.com/sacloud/terraform-provider-sakuracloud/blob/master/website/docs/d/internet.html.markdown.
 */
export function getInternet(args?: GetInternetArgs, opts?: pulumi.InvokeOptions): Promise<GetInternetResult> & GetInternetResult {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    const promise: Promise<GetInternetResult> = pulumi.runtime.invoke("sakuracloud:index/getInternet:getInternet", {
        "filters": args.filters,
        "nameSelectors": args.nameSelectors,
        "tagSelectors": args.tagSelectors,
        "zone": args.zone,
    }, opts);

    return pulumi.utils.liftProperties(promise, opts);
}

/**
 * A collection of arguments for invoking getInternet.
 */
export interface GetInternetArgs {
    /**
     * The map of filter key and value.
     */
    readonly filters?: inputs.GetInternetFilter[];
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
 * A collection of values returned by getInternet.
 */
export interface GetInternetResult {
    /**
     * Bandwidth of outbound traffic.
     */
    readonly bandWidth: number;
    /**
     * The description of the resource.
     */
    readonly description: string;
    /**
     * The ipv6 enabled flag.
     */
    readonly enableIpv6: boolean;
    readonly filters?: outputs.GetInternetFilter[];
    /**
     * The network gateway address of the switch.
     */
    readonly gateway: string;
    /**
     * The ID of the icon of the resource.
     */
    readonly iconId: string;
    /**
     * Global IP address list.
     */
    readonly ipaddresses: string[];
    /**
     * The ipv6 network address.
     */
    readonly ipv6NwAddress: string;
    /**
     * Address prefix of ipv6 network.
     */
    readonly ipv6Prefix: string;
    /**
     * Address prefix length of ipv6 network.
     */
    readonly ipv6PrefixLen: number;
    /**
     * Max global IP address.
     */
    readonly maxIpaddress: string;
    /**
     * Min global IP address.
     */
    readonly minIpaddress: string;
    /**
     * The name of the resource.
     */
    readonly name: string;
    readonly nameSelectors?: string[];
    /**
     * The network address.
     */
    readonly nwAddress: string;
    /**
     * Network mask length.
     */
    readonly nwMaskLen: number;
    /**
     * The ID list of the servers connected to the switch.
     */
    readonly serverIds: string[];
    /**
     * The ID of the switch.
     */
    readonly switchId: string;
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
