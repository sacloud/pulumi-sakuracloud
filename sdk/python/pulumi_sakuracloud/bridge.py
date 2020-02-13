# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class Bridge(pulumi.CustomResource):
    description: pulumi.Output[str]
    """
    The description of the Bridge. The length of this value must be in the range [`1`-`512`]
    """
    name: pulumi.Output[str]
    """
    The name of the Bridge. The length of this value must be in the range [`1`-`64`]
    """
    zone: pulumi.Output[str]
    """
    The name of zone that the Bridge will be created (e.g. `is1a`, `tk1a`)
    """
    def __init__(__self__, resource_name, opts=None, description=None, name=None, zone=None, __props__=None, __name__=None, __opts__=None):
        """
        Create a Bridge resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the Bridge. The length of this value must be in the range [`1`-`512`]
        :param pulumi.Input[str] name: The name of the Bridge. The length of this value must be in the range [`1`-`64`]
        :param pulumi.Input[str] zone: The name of zone that the Bridge will be created (e.g. `is1a`, `tk1a`)
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

            __props__['description'] = description
            __props__['name'] = name
            __props__['zone'] = zone
        super(Bridge, __self__).__init__(
            'sakuracloud:index/bridge:Bridge',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, description=None, name=None, zone=None):
        """
        Get an existing Bridge resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the Bridge. The length of this value must be in the range [`1`-`512`]
        :param pulumi.Input[str] name: The name of the Bridge. The length of this value must be in the range [`1`-`64`]
        :param pulumi.Input[str] zone: The name of zone that the Bridge will be created (e.g. `is1a`, `tk1a`)
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["description"] = description
        __props__["name"] = name
        __props__["zone"] = zone
        return Bridge(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

