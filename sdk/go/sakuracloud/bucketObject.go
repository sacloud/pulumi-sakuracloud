// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sakuracloud

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides a SakuraCloud Bucket Object resource. This can be used to create, update, and delete Bucket Objects.
// 
// > **NOTE on Bucket:**  Sakura Cloud does not support bucket creation by API.
// Buckets should be created on the control panel.
// 
// ## Import (not supported)
// 
// Import of Bucket Object is not supported.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-sakuracloud/blob/master/website/docs/r/bucket_object.html.markdown.
type BucketObject struct {
	s *pulumi.ResourceState
}

// NewBucketObject registers a new resource with the given unique name, arguments, and options.
func NewBucketObject(ctx *pulumi.Context,
	name string, args *BucketObjectArgs, opts ...pulumi.ResourceOpt) (*BucketObject, error) {
	if args == nil || args.AccessKey == nil {
		return nil, errors.New("missing required argument 'AccessKey'")
	}
	if args == nil || args.Bucket == nil {
		return nil, errors.New("missing required argument 'Bucket'")
	}
	if args == nil || args.Key == nil {
		return nil, errors.New("missing required argument 'Key'")
	}
	if args == nil || args.SecretKey == nil {
		return nil, errors.New("missing required argument 'SecretKey'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["accessKey"] = nil
		inputs["bucket"] = nil
		inputs["content"] = nil
		inputs["contentType"] = nil
		inputs["etag"] = nil
		inputs["key"] = nil
		inputs["secretKey"] = nil
		inputs["source"] = nil
	} else {
		inputs["accessKey"] = args.AccessKey
		inputs["bucket"] = args.Bucket
		inputs["content"] = args.Content
		inputs["contentType"] = args.ContentType
		inputs["etag"] = args.Etag
		inputs["key"] = args.Key
		inputs["secretKey"] = args.SecretKey
		inputs["source"] = args.Source
	}
	inputs["httpCacheUrl"] = nil
	inputs["httpPathUrl"] = nil
	inputs["httpUrl"] = nil
	inputs["httpsCacheUrl"] = nil
	inputs["httpsPathUrl"] = nil
	inputs["httpsUrl"] = nil
	inputs["lastModified"] = nil
	inputs["size"] = nil
	s, err := ctx.RegisterResource("sakuracloud:index/bucketObject:BucketObject", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &BucketObject{s: s}, nil
}

// GetBucketObject gets an existing BucketObject resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetBucketObject(ctx *pulumi.Context,
	name string, id pulumi.ID, state *BucketObjectState, opts ...pulumi.ResourceOpt) (*BucketObject, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["accessKey"] = state.AccessKey
		inputs["bucket"] = state.Bucket
		inputs["content"] = state.Content
		inputs["contentType"] = state.ContentType
		inputs["etag"] = state.Etag
		inputs["httpCacheUrl"] = state.HttpCacheUrl
		inputs["httpPathUrl"] = state.HttpPathUrl
		inputs["httpUrl"] = state.HttpUrl
		inputs["httpsCacheUrl"] = state.HttpsCacheUrl
		inputs["httpsPathUrl"] = state.HttpsPathUrl
		inputs["httpsUrl"] = state.HttpsUrl
		inputs["key"] = state.Key
		inputs["lastModified"] = state.LastModified
		inputs["secretKey"] = state.SecretKey
		inputs["size"] = state.Size
		inputs["source"] = state.Source
	}
	s, err := ctx.ReadResource("sakuracloud:index/bucketObject:BucketObject", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &BucketObject{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *BucketObject) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *BucketObject) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The access key of bucket. It must be provided, but it can also be sourced from the `SACLOUD_OJS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY_ID` environment variable.
func (r *BucketObject) AccessKey() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["accessKey"])
}

// The name of bucket.
func (r *BucketObject) Bucket() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["bucket"])
}

// String of the value of the bucket object. 
func (r *BucketObject) Content() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["content"])
}

// Content-Type header value of the bucket object.
func (r *BucketObject) ContentType() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["contentType"])
}

// ETag of the resource.
func (r *BucketObject) Etag() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["etag"])
}

// URL for accessing the object via HTTP (type:`cache`).
func (r *BucketObject) HttpCacheUrl() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["httpCacheUrl"])
}

// URL for accessing the object via HTTP (type:`path`).
func (r *BucketObject) HttpPathUrl() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["httpPathUrl"])
}

// URL for accessing the object via HTTP (type:`subdomain`).
func (r *BucketObject) HttpUrl() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["httpUrl"])
}

// URL for accessing the object via HTTPS (type:`cache`)..
func (r *BucketObject) HttpsCacheUrl() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["httpsCacheUrl"])
}

func (r *BucketObject) HttpsPathUrl() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["httpsPathUrl"])
}

// URL for accessing the object via HTTPS (type:`subdomain`).
func (r *BucketObject) HttpsUrl() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["httpsUrl"])
}

// The key of the bucket object.
func (r *BucketObject) Key() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["key"])
}

// Update date of the resource.
func (r *BucketObject) LastModified() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["lastModified"])
}

// The secret key of bucket. It must be provided, but it can also be sourced from the `SACLOUD_OJS_SECRET_ACCESS_KEY` or `AWS_SECRET_ACCESS_KEY` environment variable.
func (r *BucketObject) SecretKey() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["secretKey"])
}

// Size of the resource (unit:`byte`).
func (r *BucketObject) Size() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["size"])
}

// Source file path of value of the bucket object.
func (r *BucketObject) Source() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["source"])
}

// Input properties used for looking up and filtering BucketObject resources.
type BucketObjectState struct {
	// The access key of bucket. It must be provided, but it can also be sourced from the `SACLOUD_OJS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY_ID` environment variable.
	AccessKey interface{}
	// The name of bucket.
	Bucket interface{}
	// String of the value of the bucket object. 
	Content interface{}
	// Content-Type header value of the bucket object.
	ContentType interface{}
	// ETag of the resource.
	Etag interface{}
	// URL for accessing the object via HTTP (type:`cache`).
	HttpCacheUrl interface{}
	// URL for accessing the object via HTTP (type:`path`).
	HttpPathUrl interface{}
	// URL for accessing the object via HTTP (type:`subdomain`).
	HttpUrl interface{}
	// URL for accessing the object via HTTPS (type:`cache`)..
	HttpsCacheUrl interface{}
	HttpsPathUrl interface{}
	// URL for accessing the object via HTTPS (type:`subdomain`).
	HttpsUrl interface{}
	// The key of the bucket object.
	Key interface{}
	// Update date of the resource.
	LastModified interface{}
	// The secret key of bucket. It must be provided, but it can also be sourced from the `SACLOUD_OJS_SECRET_ACCESS_KEY` or `AWS_SECRET_ACCESS_KEY` environment variable.
	SecretKey interface{}
	// Size of the resource (unit:`byte`).
	Size interface{}
	// Source file path of value of the bucket object.
	Source interface{}
}

// The set of arguments for constructing a BucketObject resource.
type BucketObjectArgs struct {
	// The access key of bucket. It must be provided, but it can also be sourced from the `SACLOUD_OJS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY_ID` environment variable.
	AccessKey interface{}
	// The name of bucket.
	Bucket interface{}
	// String of the value of the bucket object. 
	Content interface{}
	// Content-Type header value of the bucket object.
	ContentType interface{}
	// ETag of the resource.
	Etag interface{}
	// The key of the bucket object.
	Key interface{}
	// The secret key of bucket. It must be provided, but it can also be sourced from the `SACLOUD_OJS_SECRET_ACCESS_KEY` or `AWS_SECRET_ACCESS_KEY` environment variable.
	SecretKey interface{}
	// Source file path of value of the bucket object.
	Source interface{}
}
