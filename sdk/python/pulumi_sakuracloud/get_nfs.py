# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class GetNFSResult:
    """
    A collection of values returned by getNFS.
    """
    def __init__(__self__, description=None, filter=None, icon_id=None, id=None, name=None, network_interfaces=None, plan=None, size=None, tags=None, zone=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        __self__.description = description
        if filter and not isinstance(filter, dict):
            raise TypeError("Expected argument 'filter' to be a dict")
        __self__.filter = filter
        if icon_id and not isinstance(icon_id, str):
            raise TypeError("Expected argument 'icon_id' to be a str")
        __self__.icon_id = icon_id
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        if network_interfaces and not isinstance(network_interfaces, list):
            raise TypeError("Expected argument 'network_interfaces' to be a list")
        __self__.network_interfaces = network_interfaces
        if plan and not isinstance(plan, str):
            raise TypeError("Expected argument 'plan' to be a str")
        __self__.plan = plan
        if size and not isinstance(size, float):
            raise TypeError("Expected argument 'size' to be a float")
        __self__.size = size
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        __self__.tags = tags
        if zone and not isinstance(zone, str):
            raise TypeError("Expected argument 'zone' to be a str")
        __self__.zone = zone
class AwaitableGetNFSResult(GetNFSResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNFSResult(
            description=self.description,
            filter=self.filter,
            icon_id=self.icon_id,
            id=self.id,
            name=self.name,
            network_interfaces=self.network_interfaces,
            plan=self.plan,
            size=self.size,
            tags=self.tags,
            zone=self.zone)

def get_nfs(filter=None,zone=None,opts=None):
    """
    Use this data source to access information about an existing resource.


    The **filter** object supports the following:

      * `conditions` (`list`)
        * `name` (`str`)
        * `values` (`list`)

      * `id` (`str`)
      * `names` (`list`)
      * `tags` (`list`)
    """
    __args__ = dict()


    __args__['filter'] = filter
    __args__['zone'] = zone
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('sakuracloud:index/getNFS:getNFS', __args__, opts=opts).value

    return AwaitableGetNFSResult(
        description=__ret__.get('description'),
        filter=__ret__.get('filter'),
        icon_id=__ret__.get('iconId'),
        id=__ret__.get('id'),
        name=__ret__.get('name'),
        network_interfaces=__ret__.get('networkInterfaces'),
        plan=__ret__.get('plan'),
        size=__ret__.get('size'),
        tags=__ret__.get('tags'),
        zone=__ret__.get('zone'))
