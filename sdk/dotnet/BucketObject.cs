// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Sakuracloud
{
    /// <summary>
    /// Manages a SakuraCloud Bucket Object.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.IO;
    /// using Pulumi;
    /// using Sakuracloud = Pulumi.Sakuracloud;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var foobar = new Sakuracloud.BucketObject("foobar", new Sakuracloud.BucketObjectArgs
    ///         {
    ///             Bucket = "foobar",
    ///             Key = "example.txt",
    ///             Content = File.ReadAllText("example.txt"),
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// </summary>
    [SakuracloudResourceType("sakuracloud:index/bucketObject:BucketObject")]
    public partial class BucketObject : Pulumi.CustomResource
    {
        /// <summary>
        /// The access key for using SakuraCloud Object Storage API.
        /// </summary>
        [Output("accessKey")]
        public Output<string> AccessKey { get; private set; } = null!;

        /// <summary>
        /// The name of the bucket. Changing this forces a new resource to be created.
        /// </summary>
        [Output("bucket")]
        public Output<string> Bucket { get; private set; } = null!;

        /// <summary>
        /// The content to upload to as the bucket object. This conflicts with [`source`].
        /// </summary>
        [Output("content")]
        public Output<string?> Content { get; private set; } = null!;

        /// <summary>
        /// The content-type of the bucket object.
        /// </summary>
        [Output("contentType")]
        public Output<string> ContentType { get; private set; } = null!;

        /// <summary>
        /// The etag of the bucket object.
        /// </summary>
        [Output("etag")]
        public Output<string> Etag { get; private set; } = null!;

        /// <summary>
        /// The URL for cached access to the bucket object via HTTP.
        /// </summary>
        [Output("httpCacheUrl")]
        public Output<string> HttpCacheUrl { get; private set; } = null!;

        /// <summary>
        /// The URL with path-format for accessing the bucket object via HTTP.
        /// </summary>
        [Output("httpPathUrl")]
        public Output<string> HttpPathUrl { get; private set; } = null!;

        /// <summary>
        /// The URL for accessing the bucket object via HTTP.
        /// </summary>
        [Output("httpUrl")]
        public Output<string> HttpUrl { get; private set; } = null!;

        /// <summary>
        /// The URL for cached access to the bucket object via HTTPS.
        /// </summary>
        [Output("httpsCacheUrl")]
        public Output<string> HttpsCacheUrl { get; private set; } = null!;

        /// <summary>
        /// The URL with path-format for accessing the bucket object via HTTPS.
        /// </summary>
        [Output("httpsPathUrl")]
        public Output<string> HttpsPathUrl { get; private set; } = null!;

        /// <summary>
        /// The URL for accessing the bucket object via HTTPS.
        /// </summary>
        [Output("httpsUrl")]
        public Output<string> HttpsUrl { get; private set; } = null!;

        /// <summary>
        /// The name of the bucket object. Changing this forces a new resource to be created.
        /// </summary>
        [Output("key")]
        public Output<string> Key { get; private set; } = null!;

        /// <summary>
        /// The time when the bucket object last modified.
        /// </summary>
        [Output("lastModified")]
        public Output<string> LastModified { get; private set; } = null!;

        /// <summary>
        /// The secret key for using SakuraCloud Object Storage API.
        /// </summary>
        [Output("secretKey")]
        public Output<string> SecretKey { get; private set; } = null!;

        /// <summary>
        /// The size of the bucket object in bytes.
        /// </summary>
        [Output("size")]
        public Output<int> Size { get; private set; } = null!;

        /// <summary>
        /// The file path to upload to as the bucket object. This conflicts with [`content`].
        /// </summary>
        [Output("source")]
        public Output<string?> Source { get; private set; } = null!;


        /// <summary>
        /// Create a BucketObject resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public BucketObject(string name, BucketObjectArgs args, CustomResourceOptions? options = null)
            : base("sakuracloud:index/bucketObject:BucketObject", name, args ?? new BucketObjectArgs(), MakeResourceOptions(options, ""))
        {
        }

        private BucketObject(string name, Input<string> id, BucketObjectState? state = null, CustomResourceOptions? options = null)
            : base("sakuracloud:index/bucketObject:BucketObject", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing BucketObject resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static BucketObject Get(string name, Input<string> id, BucketObjectState? state = null, CustomResourceOptions? options = null)
        {
            return new BucketObject(name, id, state, options);
        }
    }

    public sealed class BucketObjectArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The access key for using SakuraCloud Object Storage API.
        /// </summary>
        [Input("accessKey", required: true)]
        public Input<string> AccessKey { get; set; } = null!;

        /// <summary>
        /// The name of the bucket. Changing this forces a new resource to be created.
        /// </summary>
        [Input("bucket", required: true)]
        public Input<string> Bucket { get; set; } = null!;

        /// <summary>
        /// The content to upload to as the bucket object. This conflicts with [`source`].
        /// </summary>
        [Input("content")]
        public Input<string>? Content { get; set; }

        /// <summary>
        /// The content-type of the bucket object.
        /// </summary>
        [Input("contentType")]
        public Input<string>? ContentType { get; set; }

        /// <summary>
        /// The etag of the bucket object.
        /// </summary>
        [Input("etag")]
        public Input<string>? Etag { get; set; }

        /// <summary>
        /// The name of the bucket object. Changing this forces a new resource to be created.
        /// </summary>
        [Input("key", required: true)]
        public Input<string> Key { get; set; } = null!;

        /// <summary>
        /// The secret key for using SakuraCloud Object Storage API.
        /// </summary>
        [Input("secretKey", required: true)]
        public Input<string> SecretKey { get; set; } = null!;

        /// <summary>
        /// The file path to upload to as the bucket object. This conflicts with [`content`].
        /// </summary>
        [Input("source")]
        public Input<string>? Source { get; set; }

        public BucketObjectArgs()
        {
        }
    }

    public sealed class BucketObjectState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The access key for using SakuraCloud Object Storage API.
        /// </summary>
        [Input("accessKey")]
        public Input<string>? AccessKey { get; set; }

        /// <summary>
        /// The name of the bucket. Changing this forces a new resource to be created.
        /// </summary>
        [Input("bucket")]
        public Input<string>? Bucket { get; set; }

        /// <summary>
        /// The content to upload to as the bucket object. This conflicts with [`source`].
        /// </summary>
        [Input("content")]
        public Input<string>? Content { get; set; }

        /// <summary>
        /// The content-type of the bucket object.
        /// </summary>
        [Input("contentType")]
        public Input<string>? ContentType { get; set; }

        /// <summary>
        /// The etag of the bucket object.
        /// </summary>
        [Input("etag")]
        public Input<string>? Etag { get; set; }

        /// <summary>
        /// The URL for cached access to the bucket object via HTTP.
        /// </summary>
        [Input("httpCacheUrl")]
        public Input<string>? HttpCacheUrl { get; set; }

        /// <summary>
        /// The URL with path-format for accessing the bucket object via HTTP.
        /// </summary>
        [Input("httpPathUrl")]
        public Input<string>? HttpPathUrl { get; set; }

        /// <summary>
        /// The URL for accessing the bucket object via HTTP.
        /// </summary>
        [Input("httpUrl")]
        public Input<string>? HttpUrl { get; set; }

        /// <summary>
        /// The URL for cached access to the bucket object via HTTPS.
        /// </summary>
        [Input("httpsCacheUrl")]
        public Input<string>? HttpsCacheUrl { get; set; }

        /// <summary>
        /// The URL with path-format for accessing the bucket object via HTTPS.
        /// </summary>
        [Input("httpsPathUrl")]
        public Input<string>? HttpsPathUrl { get; set; }

        /// <summary>
        /// The URL for accessing the bucket object via HTTPS.
        /// </summary>
        [Input("httpsUrl")]
        public Input<string>? HttpsUrl { get; set; }

        /// <summary>
        /// The name of the bucket object. Changing this forces a new resource to be created.
        /// </summary>
        [Input("key")]
        public Input<string>? Key { get; set; }

        /// <summary>
        /// The time when the bucket object last modified.
        /// </summary>
        [Input("lastModified")]
        public Input<string>? LastModified { get; set; }

        /// <summary>
        /// The secret key for using SakuraCloud Object Storage API.
        /// </summary>
        [Input("secretKey")]
        public Input<string>? SecretKey { get; set; }

        /// <summary>
        /// The size of the bucket object in bytes.
        /// </summary>
        [Input("size")]
        public Input<int>? Size { get; set; }

        /// <summary>
        /// The file path to upload to as the bucket object. This conflicts with [`content`].
        /// </summary>
        [Input("source")]
        public Input<string>? Source { get; set; }

        public BucketObjectState()
        {
        }
    }
}
