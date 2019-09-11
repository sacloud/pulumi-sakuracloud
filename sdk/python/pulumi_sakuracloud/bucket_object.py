# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class BucketObject(pulumi.CustomResource):
    access_key: pulumi.Output[str]
    """
    The access key of bucket. It must be provided, but it can also be sourced from the `SACLOUD_OJS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY_ID` environment variable.
    """
    bucket: pulumi.Output[str]
    """
    The name of bucket.
    """
    content: pulumi.Output[str]
    """
    String of the value of the bucket object. 
    """
    content_type: pulumi.Output[str]
    """
    Content-Type header value of the bucket object.
    """
    etag: pulumi.Output[str]
    """
    ETag of the resource.
    """
    http_cache_url: pulumi.Output[str]
    """
    URL for accessing the object via HTTP (type:`cache`).
    """
    http_path_url: pulumi.Output[str]
    """
    URL for accessing the object via HTTP (type:`path`).
    """
    http_url: pulumi.Output[str]
    """
    URL for accessing the object via HTTP (type:`subdomain`).
    """
    https_cache_url: pulumi.Output[str]
    """
    URL for accessing the object via HTTPS (type:`cache`)..
    """
    https_path_url: pulumi.Output[str]
    https_url: pulumi.Output[str]
    """
    URL for accessing the object via HTTPS (type:`subdomain`).
    """
    key: pulumi.Output[str]
    """
    The key of the bucket object.
    """
    last_modified: pulumi.Output[str]
    """
    Update date of the resource.
    """
    secret_key: pulumi.Output[str]
    """
    The secret key of bucket. It must be provided, but it can also be sourced from the `SACLOUD_OJS_SECRET_ACCESS_KEY` or `AWS_SECRET_ACCESS_KEY` environment variable.
    """
    size: pulumi.Output[float]
    """
    Size of the resource (unit:`byte`).
    """
    source: pulumi.Output[str]
    """
    Source file path of value of the bucket object.
    """
    def __init__(__self__, resource_name, opts=None, access_key=None, bucket=None, content=None, content_type=None, etag=None, key=None, secret_key=None, source=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a SakuraCloud Bucket Object resource. This can be used to create, update, and delete Bucket Objects.
        
        > **NOTE on Bucket:**  Sakura Cloud does not support bucket creation by API.
        Buckets should be created on the control panel.
        
        ## Import (not supported)
        
        Import of Bucket Object is not supported.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_key: The access key of bucket. It must be provided, but it can also be sourced from the `SACLOUD_OJS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY_ID` environment variable.
        :param pulumi.Input[str] bucket: The name of bucket.
        :param pulumi.Input[str] content: String of the value of the bucket object. 
        :param pulumi.Input[str] content_type: Content-Type header value of the bucket object.
        :param pulumi.Input[str] etag: ETag of the resource.
        :param pulumi.Input[str] key: The key of the bucket object.
        :param pulumi.Input[str] secret_key: The secret key of bucket. It must be provided, but it can also be sourced from the `SACLOUD_OJS_SECRET_ACCESS_KEY` or `AWS_SECRET_ACCESS_KEY` environment variable.
        :param pulumi.Input[str] source: Source file path of value of the bucket object.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-sakuracloud/blob/master/website/docs/r/bucket_object.html.markdown.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            if access_key is None:
                raise TypeError("Missing required property 'access_key'")
            __props__['access_key'] = access_key
            if bucket is None:
                raise TypeError("Missing required property 'bucket'")
            __props__['bucket'] = bucket
            __props__['content'] = content
            __props__['content_type'] = content_type
            __props__['etag'] = etag
            if key is None:
                raise TypeError("Missing required property 'key'")
            __props__['key'] = key
            if secret_key is None:
                raise TypeError("Missing required property 'secret_key'")
            __props__['secret_key'] = secret_key
            __props__['source'] = source
            __props__['http_cache_url'] = None
            __props__['http_path_url'] = None
            __props__['http_url'] = None
            __props__['https_cache_url'] = None
            __props__['https_path_url'] = None
            __props__['https_url'] = None
            __props__['last_modified'] = None
            __props__['size'] = None
        super(BucketObject, __self__).__init__(
            'sakuracloud:index/bucketObject:BucketObject',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, access_key=None, bucket=None, content=None, content_type=None, etag=None, http_cache_url=None, http_path_url=None, http_url=None, https_cache_url=None, https_path_url=None, https_url=None, key=None, last_modified=None, secret_key=None, size=None, source=None):
        """
        Get an existing BucketObject resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_key: The access key of bucket. It must be provided, but it can also be sourced from the `SACLOUD_OJS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY_ID` environment variable.
        :param pulumi.Input[str] bucket: The name of bucket.
        :param pulumi.Input[str] content: String of the value of the bucket object. 
        :param pulumi.Input[str] content_type: Content-Type header value of the bucket object.
        :param pulumi.Input[str] etag: ETag of the resource.
        :param pulumi.Input[str] http_cache_url: URL for accessing the object via HTTP (type:`cache`).
        :param pulumi.Input[str] http_path_url: URL for accessing the object via HTTP (type:`path`).
        :param pulumi.Input[str] http_url: URL for accessing the object via HTTP (type:`subdomain`).
        :param pulumi.Input[str] https_cache_url: URL for accessing the object via HTTPS (type:`cache`)..
        :param pulumi.Input[str] https_url: URL for accessing the object via HTTPS (type:`subdomain`).
        :param pulumi.Input[str] key: The key of the bucket object.
        :param pulumi.Input[str] last_modified: Update date of the resource.
        :param pulumi.Input[str] secret_key: The secret key of bucket. It must be provided, but it can also be sourced from the `SACLOUD_OJS_SECRET_ACCESS_KEY` or `AWS_SECRET_ACCESS_KEY` environment variable.
        :param pulumi.Input[float] size: Size of the resource (unit:`byte`).
        :param pulumi.Input[str] source: Source file path of value of the bucket object.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-sakuracloud/blob/master/website/docs/r/bucket_object.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["access_key"] = access_key
        __props__["bucket"] = bucket
        __props__["content"] = content
        __props__["content_type"] = content_type
        __props__["etag"] = etag
        __props__["http_cache_url"] = http_cache_url
        __props__["http_path_url"] = http_path_url
        __props__["http_url"] = http_url
        __props__["https_cache_url"] = https_cache_url
        __props__["https_path_url"] = https_path_url
        __props__["https_url"] = https_url
        __props__["key"] = key
        __props__["last_modified"] = last_modified
        __props__["secret_key"] = secret_key
        __props__["size"] = size
        __props__["source"] = source
        return BucketObject(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
