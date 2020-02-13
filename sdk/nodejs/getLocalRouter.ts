// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

export function getLocalRouter(args?: GetLocalRouterArgs, opts?: pulumi.InvokeOptions): Promise<GetLocalRouterResult> & GetLocalRouterResult {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    const promise: Promise<GetLocalRouterResult> = pulumi.runtime.invoke("sakuracloud:index/getLocalRouter:getLocalRouter", {
        "filter": args.filter,
    }, opts);

    return pulumi.utils.liftProperties(promise, opts);
}

/**
 * A collection of arguments for invoking getLocalRouter.
 */
export interface GetLocalRouterArgs {
    readonly filter?: inputs.GetLocalRouterFilter;
}

/**
 * A collection of values returned by getLocalRouter.
 */
export interface GetLocalRouterResult {
    readonly description: string;
    readonly filter?: outputs.GetLocalRouterFilter;
    readonly iconId: string;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly name: string;
    readonly networkInterfaces: outputs.GetLocalRouterNetworkInterface[];
    readonly peers: outputs.GetLocalRouterPeer[];
    readonly secretKeys: string[];
    readonly staticRoutes: outputs.GetLocalRouterStaticRoute[];
    readonly switches: outputs.GetLocalRouterSwitch[];
    readonly tags: string[];
}
