# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class Provider(pulumi.ProviderResource):
    def __init__(__self__, resource_name, opts=None, accept_language=None, api_request_rate_limit=None, api_request_timeout=None, api_root_url=None, retry_interval=None, retry_max=None, secret=None, timeout=None, token=None, trace=None, zone=None, __props__=None, __name__=None, __opts__=None):
        """
        The provider type for the sakuracloud package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-sakuracloud/blob/master/website/docs/index.html.markdown.
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

            __props__['accept_language'] = accept_language
            __props__['api_request_rate_limit'] = pulumi.Output.from_input(api_request_rate_limit).apply(json.dumps) if api_request_rate_limit is not None else None
            __props__['api_request_timeout'] = pulumi.Output.from_input(api_request_timeout).apply(json.dumps) if api_request_timeout is not None else None
            __props__['api_root_url'] = api_root_url
            __props__['retry_interval'] = pulumi.Output.from_input(retry_interval).apply(json.dumps) if retry_interval is not None else None
            __props__['retry_max'] = pulumi.Output.from_input(retry_max).apply(json.dumps) if retry_max is not None else None
            if secret is None:
                secret = (utilities.get_env('SAKURACLOUD_ACCESS_TOKEN_SECRET') or '')
            __props__['secret'] = secret
            __props__['timeout'] = pulumi.Output.from_input(timeout).apply(json.dumps) if timeout is not None else None
            if token is None:
                token = (utilities.get_env('SAKURACLOUD_ACCESS_TOKEN') or '')
            __props__['token'] = token
            __props__['trace'] = pulumi.Output.from_input(trace).apply(json.dumps) if trace is not None else None
            if zone is None:
                zone = (utilities.get_env('SAKURACLOUD_ZONE') or 'is1b')
            __props__['zone'] = zone
        super(Provider, __self__).__init__(
            'sakuracloud',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None):
        """
        Get an existing Provider resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-sakuracloud/blob/master/website/docs/index.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        return Provider(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
