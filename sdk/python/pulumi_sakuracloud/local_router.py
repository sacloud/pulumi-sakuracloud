# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class LocalRouter(pulumi.CustomResource):
    description: pulumi.Output[str]
    """
    The description of the LocalRouter. The length of this value must be in the range [`1`-`512`]
    """
    icon_id: pulumi.Output[str]
    """
    The icon id to attach to the LocalRouter
    """
    name: pulumi.Output[str]
    """
    The name of the LocalRouter. The length of this value must be in the range [`1`-`64`]
    """
    network_interface: pulumi.Output[dict]
    peers: pulumi.Output[list]
    secret_keys: pulumi.Output[list]
    """
    A list of secret key used for peering from other LocalRouters
    """
    static_routes: pulumi.Output[list]
    switch: pulumi.Output[dict]
    tags: pulumi.Output[list]
    """
    Any tags to assign to the LocalRouter
    """
    def __init__(__self__, resource_name, opts=None, description=None, icon_id=None, name=None, network_interface=None, peers=None, static_routes=None, switch=None, tags=None, __props__=None, __name__=None, __opts__=None):
        """
        Create a LocalRouter resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the LocalRouter. The length of this value must be in the range [`1`-`512`]
        :param pulumi.Input[str] icon_id: The icon id to attach to the LocalRouter
        :param pulumi.Input[str] name: The name of the LocalRouter. The length of this value must be in the range [`1`-`64`]
        :param pulumi.Input[list] tags: Any tags to assign to the LocalRouter

        The **network_interface** object supports the following:

          * `ip_addresses` (`pulumi.Input[list]`)
          * `netmask` (`pulumi.Input[float]`)
          * `vip` (`pulumi.Input[str]`)
          * `vrid` (`pulumi.Input[float]`)

        The **peers** object supports the following:

          * `description` (`pulumi.Input[str]`)
          * `enabled` (`pulumi.Input[bool]`)
          * `peerId` (`pulumi.Input[str]`)
          * `secret_key` (`pulumi.Input[str]`)

        The **static_routes** object supports the following:

          * `next_hop` (`pulumi.Input[str]`)
          * `prefix` (`pulumi.Input[str]`)

        The **switch** object supports the following:

          * `category` (`pulumi.Input[str]`)
          * `code` (`pulumi.Input[str]`)
          * `zoneId` (`pulumi.Input[str]`)
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
            __props__['icon_id'] = icon_id
            __props__['name'] = name
            if network_interface is None:
                raise TypeError("Missing required property 'network_interface'")
            __props__['network_interface'] = network_interface
            __props__['peers'] = peers
            __props__['static_routes'] = static_routes
            if switch is None:
                raise TypeError("Missing required property 'switch'")
            __props__['switch'] = switch
            __props__['tags'] = tags
            __props__['secret_keys'] = None
        super(LocalRouter, __self__).__init__(
            'sakuracloud:index/localRouter:LocalRouter',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, description=None, icon_id=None, name=None, network_interface=None, peers=None, secret_keys=None, static_routes=None, switch=None, tags=None):
        """
        Get an existing LocalRouter resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the LocalRouter. The length of this value must be in the range [`1`-`512`]
        :param pulumi.Input[str] icon_id: The icon id to attach to the LocalRouter
        :param pulumi.Input[str] name: The name of the LocalRouter. The length of this value must be in the range [`1`-`64`]
        :param pulumi.Input[list] secret_keys: A list of secret key used for peering from other LocalRouters
        :param pulumi.Input[list] tags: Any tags to assign to the LocalRouter

        The **network_interface** object supports the following:

          * `ip_addresses` (`pulumi.Input[list]`)
          * `netmask` (`pulumi.Input[float]`)
          * `vip` (`pulumi.Input[str]`)
          * `vrid` (`pulumi.Input[float]`)

        The **peers** object supports the following:

          * `description` (`pulumi.Input[str]`)
          * `enabled` (`pulumi.Input[bool]`)
          * `peerId` (`pulumi.Input[str]`)
          * `secret_key` (`pulumi.Input[str]`)

        The **static_routes** object supports the following:

          * `next_hop` (`pulumi.Input[str]`)
          * `prefix` (`pulumi.Input[str]`)

        The **switch** object supports the following:

          * `category` (`pulumi.Input[str]`)
          * `code` (`pulumi.Input[str]`)
          * `zoneId` (`pulumi.Input[str]`)
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["description"] = description
        __props__["icon_id"] = icon_id
        __props__["name"] = name
        __props__["network_interface"] = network_interface
        __props__["peers"] = peers
        __props__["secret_keys"] = secret_keys
        __props__["static_routes"] = static_routes
        __props__["switch"] = switch
        __props__["tags"] = tags
        return LocalRouter(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
