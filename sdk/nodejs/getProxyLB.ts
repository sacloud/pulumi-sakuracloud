// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Use this data source to retrieve information about a SakuraCloud ProxyLB.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as sakuracloud from "@pulumi/sakuracloud";
 * 
 * const foobar = sakuracloud.getProxyLB({
 *     nameSelectors: ["foobar"],
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-sakuracloud/blob/master/website/docs/d/proxylb.html.markdown.
 */
export function getProxyLB(args?: GetProxyLBArgs, opts?: pulumi.InvokeOptions): Promise<GetProxyLBResult> & GetProxyLBResult {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    const promise: Promise<GetProxyLBResult> = pulumi.runtime.invoke("sakuracloud:index/getProxyLB:getProxyLB", {
        "filters": args.filters,
        "nameSelectors": args.nameSelectors,
        "tagSelectors": args.tagSelectors,
    }, opts);

    return pulumi.utils.liftProperties(promise, opts);
}

/**
 * A collection of arguments for invoking getProxyLB.
 */
export interface GetProxyLBArgs {
    /**
     * The map of filter key and value.
     */
    readonly filters?: inputs.GetProxyLBFilter[];
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
 * A collection of values returned by getProxyLB.
 */
export interface GetProxyLBResult {
    /**
     * The external listen ports. It contains some attributes to Bind Ports.
     */
    readonly bindPorts: outputs.GetProxyLBBindPort[];
    /**
     * Certificate used to terminate SSL/TSL. It contains some attributes to Certificate.
     */
    readonly certificates: outputs.GetProxyLBCertificate[];
    /**
     * The description of the resource.
     */
    readonly description: string;
    readonly filters?: outputs.GetProxyLBFilter[];
    readonly fqdn: string;
    /**
     * The health check rules. It contains some attributes to Health Check.
     */
    readonly healthChecks: outputs.GetProxyLBHealthCheck[];
    /**
     * The ID of the icon.
     */
    readonly iconId: string;
    /**
     * Name of the resource.
     */
    readonly name: string;
    readonly nameSelectors?: string[];
    /**
     * The plan of the resource.
     */
    readonly plan: number;
    readonly proxyNetworks: string[];
    /**
     * Real servers. It contains some attributes to Servers.
     */
    readonly servers: outputs.GetProxyLBServer[];
    /**
     * The pair of IPAddress and port number of sorry-server.
     */
    readonly sorryServers: outputs.GetProxyLBSorryServer[];
    /**
     * The flag of enable Sticky-Session.  
     */
    readonly stickySession: boolean;
    readonly tagSelectors?: string[];
    /**
     * The tag list of the resources.
     */
    readonly tags: string[];
    /**
     * Timeout seconds. 
     */
    readonly timeout: number;
    readonly vip: string;
    /**
     * The flag of enable VIP Fail-Over.  
     */
    readonly vipFailover: boolean;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
