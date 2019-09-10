// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Use this data source to retrieve information about a SakuraCloud Bucket Object.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as sakuracloud from "@pulumi/sakuracloud";
 * 
 * const foobar = sakuracloud.getBucketObject({
 *     bucket: "your-bucket-name",
 *     key: "path/to/your/object",
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-sakuracloud/blob/master/website/docs/d/bucket_object.html.markdown.
 */
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
    /**
     * The access key of bucket. It must be provided, but it can also be sourced from the `SACLOUD_OJS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY_ID` environment variable.
     */
    readonly accessKey: string;
    /**
     * The name of bucket.
     */
    readonly bucket: string;
    /**
     * The key of the bucket object.
     */
    readonly key: string;
    /**
     * The secret key of bucket. It must be provided, but it can also be sourced from the `SACLOUD_OJS_SECRET_ACCESS_KEY` or `AWS_SECRET_ACCESS_KEY` environment variable.
     */
    readonly secretKey: string;
}

/**
 * A collection of values returned by getBucketObject.
 */
export interface GetBucketObjectResult {
    readonly accessKey: string;
    /**
     * String of the value of the bucket object. Set when Content-Type is `"text/*"` or `"application/json"`.
     */
    readonly body: string;
    readonly bucket: string;
    /**
     * Content-Type header value of the bucket object.
     */
    readonly contentType: string;
    /**
     * ETag of the resource.
     */
    readonly etag: string;
    /**
     * URL for accessing the object via HTTP (type:`cache`).
     */
    readonly httpCacheUrl: string;
    /**
     * URL for accessing the object via HTTP (type:`path`).
     */
    readonly httpPathUrl: string;
    /**
     * URL for accessing the object via HTTP (type:`subdomain`).
     */
    readonly httpUrl: string;
    /**
     * URL for accessing the object via HTTPS (type:`cache`)..
     */
    readonly httpsCacheUrl: string;
    readonly httpsPathUrl: string;
    /**
     * URL for accessing the object via HTTPS (type:`subdomain`).
     */
    readonly httpsUrl: string;
    readonly key: string;
    /**
     * Update date of the resource.
     */
    readonly lastModified: string;
    readonly secretKey: string;
    /**
     * Size of the resource (unit:`byte`).
     */
    readonly size: number;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
