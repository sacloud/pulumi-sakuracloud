// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Get information about VNC for connecting to an existing Server.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as sakuracloud from "@pulumi/sakuracloud";
 *
 * const foobar = sakuracloud.getServerVNCInfo({
 *     serverId: sakuracloud_server.foobar.id,
 * });
 * ```
 */
export function getServerVNCInfo(args: GetServerVNCInfoArgs, opts?: pulumi.InvokeOptions): Promise<GetServerVNCInfoResult> {
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("sakuracloud:index/getServerVNCInfo:getServerVNCInfo", {
        "serverId": args.serverId,
        "zone": args.zone,
    }, opts);
}

/**
 * A collection of arguments for invoking getServerVNCInfo.
 */
export interface GetServerVNCInfoArgs {
    /**
     * The id of the Server.
     */
    serverId: string;
    /**
     * The name of zone that the Server is in (e.g. `is1a`, `tk1a`).
     */
    zone?: string;
}

/**
 * A collection of values returned by getServerVNCInfo.
 */
export interface GetServerVNCInfoResult {
    /**
     * The host name for connecting by VNC.
     */
    readonly host: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * The password for connecting by VNC.
     */
    readonly password: string;
    /**
     * The port number for connecting by VNC.
     */
    readonly port: number;
    readonly serverId: string;
    readonly zone: string;
}

export function getServerVNCInfoOutput(args: GetServerVNCInfoOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetServerVNCInfoResult> {
    return pulumi.output(args).apply(a => getServerVNCInfo(a, opts))
}

/**
 * A collection of arguments for invoking getServerVNCInfo.
 */
export interface GetServerVNCInfoOutputArgs {
    /**
     * The id of the Server.
     */
    serverId: pulumi.Input<string>;
    /**
     * The name of zone that the Server is in (e.g. `is1a`, `tk1a`).
     */
    zone?: pulumi.Input<string>;
}
