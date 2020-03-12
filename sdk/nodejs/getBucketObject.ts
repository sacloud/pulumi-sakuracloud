// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

export function getBucketObject(args: GetBucketObjectArgs, opts?: pulumi.InvokeOptions): Promise<GetBucketObjectResult> & GetBucketObjectResult {
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    const promise: Promise<GetBucketObjectResult> = pulumi.runtime.invoke("sakuracloud:index/getBucketObject:getBucketObject", {
        "accessKey": args.accessKey,
        "bucket": args.bucket,
        "key": args.key,
        "secretKey": args.secretKey,
    }, opts);

    return pulumi.utils.liftProperties(promise, opts);
}

/**
 * A collection of arguments for invoking getBucketObject.
 */
export interface GetBucketObjectArgs {
    readonly accessKey: string;
    readonly bucket: string;
    readonly key: string;
    readonly secretKey: string;
}

/**
 * A collection of values returned by getBucketObject.
 */
export interface GetBucketObjectResult {
    readonly accessKey: string;
    readonly body: string;
    readonly bucket: string;
    readonly contentType: string;
    readonly etag: string;
    readonly httpCacheUrl: string;
    readonly httpPathUrl: string;
    readonly httpUrl: string;
    readonly httpsCacheUrl: string;
    readonly httpsPathUrl: string;
    readonly httpsUrl: string;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly key: string;
    readonly lastModified: string;
    readonly secretKey: string;
    readonly size: number;
}
