// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Use this data source to retrieve information about a SakuraCloud Simple Monitor.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as sakuracloud from "@pulumi/sakuracloud";
 * 
 * const foobar = sakuracloud.getSimpleMonitor({
 *     nameSelectors: ["foobar"],
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-sakuracloud/blob/master/website/docs/d/simple_monitor.html.markdown.
 */
export function getSimpleMonitor(args?: GetSimpleMonitorArgs, opts?: pulumi.InvokeOptions): Promise<GetSimpleMonitorResult> & GetSimpleMonitorResult {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    const promise: Promise<GetSimpleMonitorResult> = pulumi.runtime.invoke("sakuracloud:index/getSimpleMonitor:getSimpleMonitor", {
        "filters": args.filters,
        "nameSelectors": args.nameSelectors,
        "tagSelectors": args.tagSelectors,
    }, opts);

    return pulumi.utils.liftProperties(promise, opts);
}

/**
 * A collection of arguments for invoking getSimpleMonitor.
 */
export interface GetSimpleMonitorArgs {
    /**
     * The map of filter key and value.
     */
    readonly filters?: inputs.GetSimpleMonitorFilter[];
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
 * A collection of values returned by getSimpleMonitor.
 */
export interface GetSimpleMonitorResult {
    /**
     * The description of the resource.
     */
    readonly description: string;
    /**
     * The flag of enable/disable monitoring.
     */
    readonly enabled: boolean;
    readonly filters?: outputs.GetSimpleMonitorFilter[];
    /**
     * Health check rules. It contains some attributes to Health Check.
     */
    readonly healthChecks: outputs.GetSimpleMonitorHealthCheck[];
    /**
     * The ID of the icon of the resource.
     */
    readonly iconId: string;
    readonly nameSelectors?: string[];
    /**
     * The flag of enable/disable notification by E-mail.
     */
    readonly notifyEmailEnabled: boolean;
    /**
     * The flag of enable/disable HTML format for E-mail.
     */
    readonly notifyEmailHtml: boolean;
    /**
     * The flag of enable/disable notification by slack.
     */
    readonly notifySlackEnabled: boolean;
    /**
     * The webhook URL of destination of slack notification.
     */
    readonly notifySlackWebhook: string;
    readonly tagSelectors?: string[];
    /**
     * The tag list of the resources.
     */
    readonly tags: string[];
    /**
     * The HostName or IP address of monitoring target.
     */
    readonly target: string;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
