// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

export function getServer(args?: GetServerArgs, opts?: pulumi.InvokeOptions): Promise<GetServerResult> & GetServerResult {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    const promise: Promise<GetServerResult> = pulumi.runtime.invoke("sakuracloud:index/getServer:getServer", {
        "filter": args.filter,
        "zone": args.zone,
    }, opts);

    return pulumi.utils.liftProperties(promise, opts);
}

/**
 * A collection of arguments for invoking getServer.
 */
export interface GetServerArgs {
    readonly filter?: inputs.GetServerFilter;
    readonly zone?: string;
}

/**
 * A collection of values returned by getServer.
 */
export interface GetServerResult {
    readonly cdromId: string;
    readonly commitment: string;
    readonly core: number;
    readonly description: string;
    readonly disks: string[];
    readonly dnsServers: string[];
    readonly filter?: outputs.GetServerFilter;
    readonly gateway: string;
    readonly hostname: string;
    readonly iconId: string;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly interfaceDriver: string;
    readonly ipAddress: string;
    readonly memory: number;
    readonly name: string;
    readonly netmask: number;
    readonly networkAddress: string;
    readonly networkInterfaces: outputs.GetServerNetworkInterface[];
    readonly privateHostId: string;
    readonly privateHostName: string;
    readonly tags: string[];
    readonly zone: string;
}
