# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class Switch(pulumi.CustomResource):
    bridge_id: pulumi.Output[str]
    """
    The ID of the Bridge to connect to the Switch.
    """
    description: pulumi.Output[str]
    """
    The description of the resource.
    """
    graceful_shutdown_timeout: pulumi.Output[float]
    """
    The wait time (seconds) to do graceful shutdown the server connected to the resource.
    """
    icon_id: pulumi.Output[str]
    """
    The ID of the icon.
    """
    name: pulumi.Output[str]
    """
    The name of the resource.
    """
    server_ids: pulumi.Output[list]
    """
    The ID list of the servers connected to the switch.
    """
    tags: pulumi.Output[list]
    """
    The tag list of the resources.
    """
    zone: pulumi.Output[str]
    """
    The ID of the zone to which the resource belongs.
    """
    def __init__(__self__, resource_name, opts=None, bridge_id=None, description=None, graceful_shutdown_timeout=None, icon_id=None, name=None, tags=None, zone=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a SakuraCloud Switch resource. This can be used to create, update, and delete Switches.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bridge_id: The ID of the Bridge to connect to the Switch.
        :param pulumi.Input[str] description: The description of the resource.
        :param pulumi.Input[float] graceful_shutdown_timeout: The wait time (seconds) to do graceful shutdown the server connected to the resource.
        :param pulumi.Input[str] icon_id: The ID of the icon.
        :param pulumi.Input[str] name: The name of the resource.
        :param pulumi.Input[list] tags: The tag list of the resources.
        :param pulumi.Input[str] zone: The ID of the zone to which the resource belongs.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-sakuracloud/blob/master/website/docs/r/switch.html.markdown.
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

            __props__['bridge_id'] = bridge_id
            __props__['description'] = description
            __props__['graceful_shutdown_timeout'] = graceful_shutdown_timeout
            __props__['icon_id'] = icon_id
            __props__['name'] = name
            __props__['tags'] = tags
            __props__['zone'] = zone
            __props__['server_ids'] = None
        super(Switch, __self__).__init__(
            'sakuracloud:index/switch:Switch',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, bridge_id=None, description=None, graceful_shutdown_timeout=None, icon_id=None, name=None, server_ids=None, tags=None, zone=None):
        """
        Get an existing Switch resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bridge_id: The ID of the Bridge to connect to the Switch.
        :param pulumi.Input[str] description: The description of the resource.
        :param pulumi.Input[float] graceful_shutdown_timeout: The wait time (seconds) to do graceful shutdown the server connected to the resource.
        :param pulumi.Input[str] icon_id: The ID of the icon.
        :param pulumi.Input[str] name: The name of the resource.
        :param pulumi.Input[list] server_ids: The ID list of the servers connected to the switch.
        :param pulumi.Input[list] tags: The tag list of the resources.
        :param pulumi.Input[str] zone: The ID of the zone to which the resource belongs.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-sakuracloud/blob/master/website/docs/r/switch.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["bridge_id"] = bridge_id
        __props__["description"] = description
        __props__["graceful_shutdown_timeout"] = graceful_shutdown_timeout
        __props__["icon_id"] = icon_id
        __props__["name"] = name
        __props__["server_ids"] = server_ids
        __props__["tags"] = tags
        __props__["zone"] = zone
        return Switch(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

