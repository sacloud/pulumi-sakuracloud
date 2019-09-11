# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class NFS(pulumi.CustomResource):
    default_route: pulumi.Output[str]
    """
    The default route IP address of the NFS Appliance.
    """
    description: pulumi.Output[str]
    """
    The description of the resource.
    """
    graceful_shutdown_timeout: pulumi.Output[float]
    """
    The wait time (seconds) to do graceful shutdown the NFS Appliance.
    """
    icon_id: pulumi.Output[str]
    """
    The ID of the icon.
    """
    ipaddress: pulumi.Output[str]
    """
    The IP address of the NFS Appliance.
    """
    name: pulumi.Output[str]
    """
    The name of the resource.
    """
    nw_mask_len: pulumi.Output[float]
    """
    The network mask length of the NFS Appliance.
    """
    plan: pulumi.Output[str]
    """
    The plan of the NFS Appliance 
    Valid value is one of the following: [ hdd (default) / ssd ]
    """
    size: pulumi.Output[float]
    """
    The size of the NFS Appliance (unit:`GB`).  
    Valid value is one of the following: [ 100 (default) / 500 / 1024 / 2048 / 4096 / 8192(hdd only) / 12288(hdd only) ]
    """
    switch_id: pulumi.Output[str]
    """
    The ID of the switch connected to the NFS Appliance.
    """
    tags: pulumi.Output[list]
    """
    The tag list of the resources.
    """
    zone: pulumi.Output[str]
    """
    The ID of the zone to which the resource belongs.
    """
    def __init__(__self__, resource_name, opts=None, default_route=None, description=None, graceful_shutdown_timeout=None, icon_id=None, ipaddress=None, name=None, nw_mask_len=None, plan=None, size=None, switch_id=None, tags=None, zone=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a SakuraCloud NFS Appliance resource. This can be used to create, update, and delete NFS Appliances.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] default_route: The default route IP address of the NFS Appliance.
        :param pulumi.Input[str] description: The description of the resource.
        :param pulumi.Input[float] graceful_shutdown_timeout: The wait time (seconds) to do graceful shutdown the NFS Appliance.
        :param pulumi.Input[str] icon_id: The ID of the icon.
        :param pulumi.Input[str] ipaddress: The IP address of the NFS Appliance.
        :param pulumi.Input[str] name: The name of the resource.
        :param pulumi.Input[float] nw_mask_len: The network mask length of the NFS Appliance.
        :param pulumi.Input[str] plan: The plan of the NFS Appliance 
               Valid value is one of the following: [ hdd (default) / ssd ]
        :param pulumi.Input[float] size: The size of the NFS Appliance (unit:`GB`).  
               Valid value is one of the following: [ 100 (default) / 500 / 1024 / 2048 / 4096 / 8192(hdd only) / 12288(hdd only) ]
        :param pulumi.Input[str] switch_id: The ID of the switch connected to the NFS Appliance.
        :param pulumi.Input[list] tags: The tag list of the resources.
        :param pulumi.Input[str] zone: The ID of the zone to which the resource belongs.

        > This content is derived from https://github.com/sacloud/terraform-provider-sakuracloud/blob/master/website/docs/r/nfs.html.markdown.
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

            __props__['default_route'] = default_route
            __props__['description'] = description
            __props__['graceful_shutdown_timeout'] = graceful_shutdown_timeout
            __props__['icon_id'] = icon_id
            if ipaddress is None:
                raise TypeError("Missing required property 'ipaddress'")
            __props__['ipaddress'] = ipaddress
            __props__['name'] = name
            if nw_mask_len is None:
                raise TypeError("Missing required property 'nw_mask_len'")
            __props__['nw_mask_len'] = nw_mask_len
            __props__['plan'] = plan
            __props__['size'] = size
            if switch_id is None:
                raise TypeError("Missing required property 'switch_id'")
            __props__['switch_id'] = switch_id
            __props__['tags'] = tags
            __props__['zone'] = zone
        super(NFS, __self__).__init__(
            'sakuracloud:index/nFS:NFS',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, default_route=None, description=None, graceful_shutdown_timeout=None, icon_id=None, ipaddress=None, name=None, nw_mask_len=None, plan=None, size=None, switch_id=None, tags=None, zone=None):
        """
        Get an existing NFS resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] default_route: The default route IP address of the NFS Appliance.
        :param pulumi.Input[str] description: The description of the resource.
        :param pulumi.Input[float] graceful_shutdown_timeout: The wait time (seconds) to do graceful shutdown the NFS Appliance.
        :param pulumi.Input[str] icon_id: The ID of the icon.
        :param pulumi.Input[str] ipaddress: The IP address of the NFS Appliance.
        :param pulumi.Input[str] name: The name of the resource.
        :param pulumi.Input[float] nw_mask_len: The network mask length of the NFS Appliance.
        :param pulumi.Input[str] plan: The plan of the NFS Appliance 
               Valid value is one of the following: [ hdd (default) / ssd ]
        :param pulumi.Input[float] size: The size of the NFS Appliance (unit:`GB`).  
               Valid value is one of the following: [ 100 (default) / 500 / 1024 / 2048 / 4096 / 8192(hdd only) / 12288(hdd only) ]
        :param pulumi.Input[str] switch_id: The ID of the switch connected to the NFS Appliance.
        :param pulumi.Input[list] tags: The tag list of the resources.
        :param pulumi.Input[str] zone: The ID of the zone to which the resource belongs.

        > This content is derived from https://github.com/sacloud/terraform-provider-sakuracloud/blob/master/website/docs/r/nfs.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["default_route"] = default_route
        __props__["description"] = description
        __props__["graceful_shutdown_timeout"] = graceful_shutdown_timeout
        __props__["icon_id"] = icon_id
        __props__["ipaddress"] = ipaddress
        __props__["name"] = name
        __props__["nw_mask_len"] = nw_mask_len
        __props__["plan"] = plan
        __props__["size"] = size
        __props__["switch_id"] = switch_id
        __props__["tags"] = tags
        __props__["zone"] = zone
        return NFS(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

