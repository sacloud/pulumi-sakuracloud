# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class Icon(pulumi.CustomResource):
    base64content: pulumi.Output[str]
    """
    The base64 encoded body of source content.
    """
    body: pulumi.Output[str]
    """
    Base64 encoded icon data (size:`small`).
    """
    name: pulumi.Output[str]
    """
    The name of the resource.
    """
    source: pulumi.Output[str]
    """
    The path of source content file.
    """
    tags: pulumi.Output[list]
    """
    The tag list of the resources.
    """
    url: pulumi.Output[str]
    """
    URL to access this resource.
    """
    def __init__(__self__, resource_name, opts=None, base64content=None, name=None, source=None, tags=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a SakuraCloud Icon resource. This can be used to create, update, and delete Icons.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] base64content: The base64 encoded body of source content.
        :param pulumi.Input[str] name: The name of the resource.
        :param pulumi.Input[str] source: The path of source content file.
        :param pulumi.Input[list] tags: The tag list of the resources.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-sakuracloud/blob/master/website/docs/r/icon.html.markdown.
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

            __props__['base64content'] = base64content
            __props__['name'] = name
            __props__['source'] = source
            __props__['tags'] = tags
            __props__['body'] = None
            __props__['url'] = None
        super(Icon, __self__).__init__(
            'sakuracloud:index/icon:Icon',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, base64content=None, body=None, name=None, source=None, tags=None, url=None):
        """
        Get an existing Icon resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] base64content: The base64 encoded body of source content.
        :param pulumi.Input[str] body: Base64 encoded icon data (size:`small`).
        :param pulumi.Input[str] name: The name of the resource.
        :param pulumi.Input[str] source: The path of source content file.
        :param pulumi.Input[list] tags: The tag list of the resources.
        :param pulumi.Input[str] url: URL to access this resource.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-sakuracloud/blob/master/website/docs/r/icon.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["base64content"] = base64content
        __props__["body"] = body
        __props__["name"] = name
        __props__["source"] = source
        __props__["tags"] = tags
        __props__["url"] = url
        return Icon(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

