// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "./types";
import * as utilities from "./utilities";

/**
 * Get information about an existing Bucket Object.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as sakuracloud from "@pulumi/sakuracloud";
 *
 * const foobar = pulumi.output(sakuracloud.getBucketObject({
 *     bucket: "foobar",
 *     key: "key.txt",
 * }, { async: true }));
 * ```
 */
export function getBucketObject(args: GetBucketObjectArgs, opts?: pulumi.InvokeOptions): Promise<GetBucketObjectResult> {
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("sakuracloud:index/getBucketObject:getBucketObject", {
        "accessKey": args.accessKey,
        "bucket": args.bucket,
        "key": args.key,
        "secretKey": args.secretKey,
    }, opts);
}

/**
 * A collection of arguments for invoking getBucketObject.
 */
export interface GetBucketObjectArgs {
    /**
     * The access key for using SakuraCloud Object Storage API.
     */
    readonly accessKey: string;
    /**
     * The name of bucket.
     */
    readonly bucket: string;
    /**
     * The name of the BucketObject.
     */
    readonly key: string;
    /**
     * The secret key for using SakuraCloud Object Storage API.
     */
    readonly secretKey: string;
}

/**
 * A collection of values returned by getBucketObject.
 */
export interface GetBucketObjectResult {
    readonly accessKey: string;
    /**
     * The body of the BucketObject.
     */
    readonly body: string;
    readonly bucket: string;
    /**
     * The content type of the BucketObject.
     */
    readonly contentType: string;
    /**
     * The etag of the BucketObject.
     */
    readonly etag: string;
    /**
     * The URL for cached access to the BucketObject via HTTP.
     */
    readonly httpCacheUrl: string;
    /**
     * The URL with path-format for accessing the BucketObject via HTTP.
     */
    readonly httpPathUrl: string;
    /**
     * The URL for accessing the BucketObject via HTTP.
     */
    readonly httpUrl: string;
    /**
     * The URL for cached access to the BucketObject via HTTPS.
     */
    readonly httpsCacheUrl: string;
    /**
     * The URL with path-format for accessing the BucketObject via HTTPS.
     */
    readonly httpsPathUrl: string;
    /**
     * The URL for accessing the BucketObject via HTTPS.
     */
    readonly httpsUrl: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly key: string;
    /**
     * The time when the BucketObject last modified.
     */
    readonly lastModified: string;
    readonly secretKey: string;
    /**
     * The size of the BucketObject in bytes.
     */
    readonly size: number;
}
