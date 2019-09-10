# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class Disk(pulumi.CustomResource):
    connector: pulumi.Output[str]
    description: pulumi.Output[str]
    """
    The description of the resource.
    """
    distant_froms: pulumi.Output[list]
    """
    The ID list of the Disks isolated from Disk.
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
    plan: pulumi.Output[str]
    """
    The plan of the resource.  
    Valid value is one of the following: [ "ssd" (default) / "hdd"]
    """
    server_id: pulumi.Output[str]
    """
    The ID of the server connected to the disk.
    """
    size: pulumi.Output[float]
    """
    Size of the resource (unit:`GB`).
    """
    source_archive_id: pulumi.Output[str]
    """
    The ID of source Archive.
    """
    source_disk_id: pulumi.Output[str]
    """
    The ID of source Disk.
    """
    tags: pulumi.Output[list]
    """
    The tag list of the resources.
    """
    zone: pulumi.Output[str]
    """
    The ID of the zone to which the resource belongs.
    """
    def __init__(__self__, resource_name, opts=None, connector=None, description=None, distant_froms=None, graceful_shutdown_timeout=None, icon_id=None, name=None, plan=None, size=None, source_archive_id=None, source_disk_id=None, tags=None, zone=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a SakuraCloud Disk resource. This can be used to create, update, and delete Disks.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the resource.
        :param pulumi.Input[list] distant_froms: The ID list of the Disks isolated from Disk.
        :param pulumi.Input[float] graceful_shutdown_timeout: The wait time (seconds) to do graceful shutdown the server connected to the resource.
        :param pulumi.Input[str] icon_id: The ID of the icon.
        :param pulumi.Input[str] name: The name of the resource.
        :param pulumi.Input[str] plan: The plan of the resource.  
               Valid value is one of the following: [ "ssd" (default) / "hdd"]
        :param pulumi.Input[float] size: Size of the resource (unit:`GB`).
        :param pulumi.Input[str] source_archive_id: The ID of source Archive.
        :param pulumi.Input[str] source_disk_id: The ID of source Disk.
        :param pulumi.Input[list] tags: The tag list of the resources.
        :param pulumi.Input[str] zone: The ID of the zone to which the resource belongs.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-sakuracloud/blob/master/website/docs/r/disk.html.markdown.
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

            __props__['connector'] = connector
            __props__['description'] = description
            __props__['distant_froms'] = distant_froms
            __props__['graceful_shutdown_timeout'] = graceful_shutdown_timeout
            __props__['icon_id'] = icon_id
            __props__['name'] = name
            __props__['plan'] = plan
            __props__['size'] = size
            __props__['source_archive_id'] = source_archive_id
            __props__['source_disk_id'] = source_disk_id
            __props__['tags'] = tags
            __props__['zone'] = zone
            __props__['server_id'] = None
        super(Disk, __self__).__init__(
            'sakuracloud:index/disk:Disk',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, connector=None, description=None, distant_froms=None, graceful_shutdown_timeout=None, icon_id=None, name=None, plan=None, server_id=None, size=None, source_archive_id=None, source_disk_id=None, tags=None, zone=None):
        """
        Get an existing Disk resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the resource.
        :param pulumi.Input[list] distant_froms: The ID list of the Disks isolated from Disk.
        :param pulumi.Input[float] graceful_shutdown_timeout: The wait time (seconds) to do graceful shutdown the server connected to the resource.
        :param pulumi.Input[str] icon_id: The ID of the icon.
        :param pulumi.Input[str] name: The name of the resource.
        :param pulumi.Input[str] plan: The plan of the resource.  
               Valid value is one of the following: [ "ssd" (default) / "hdd"]
        :param pulumi.Input[str] server_id: The ID of the server connected to the disk.
        :param pulumi.Input[float] size: Size of the resource (unit:`GB`).
        :param pulumi.Input[str] source_archive_id: The ID of source Archive.
        :param pulumi.Input[str] source_disk_id: The ID of source Disk.
        :param pulumi.Input[list] tags: The tag list of the resources.
        :param pulumi.Input[str] zone: The ID of the zone to which the resource belongs.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-sakuracloud/blob/master/website/docs/r/disk.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["connector"] = connector
        __props__["description"] = description
        __props__["distant_froms"] = distant_froms
        __props__["graceful_shutdown_timeout"] = graceful_shutdown_timeout
        __props__["icon_id"] = icon_id
        __props__["name"] = name
        __props__["plan"] = plan
        __props__["server_id"] = server_id
        __props__["size"] = size
        __props__["source_archive_id"] = source_archive_id
        __props__["source_disk_id"] = source_disk_id
        __props__["tags"] = tags
        __props__["zone"] = zone
        return Disk(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

