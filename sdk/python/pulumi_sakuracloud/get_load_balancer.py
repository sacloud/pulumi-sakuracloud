# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class GetLoadBalancerResult:
    """
    A collection of values returned by getLoadBalancer.
    """
    def __init__(__self__, description=None, filter=None, icon_id=None, id=None, name=None, network_interfaces=None, plan=None, tags=None, vips=None, zone=None):
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
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        __self__.tags = tags
        if vips and not isinstance(vips, list):
            raise TypeError("Expected argument 'vips' to be a list")
        __self__.vips = vips
        if zone and not isinstance(zone, str):
            raise TypeError("Expected argument 'zone' to be a str")
        __self__.zone = zone
class AwaitableGetLoadBalancerResult(GetLoadBalancerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLoadBalancerResult(
            description=self.description,
            filter=self.filter,
            icon_id=self.icon_id,
            id=self.id,
            name=self.name,
            network_interfaces=self.network_interfaces,
            plan=self.plan,
            tags=self.tags,
            vips=self.vips,
            zone=self.zone)

def get_load_balancer(filter=None,zone=None,opts=None):
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
    __ret__ = pulumi.runtime.invoke('sakuracloud:index/getLoadBalancer:getLoadBalancer', __args__, opts=opts).value

    return AwaitableGetLoadBalancerResult(
        description=__ret__.get('description'),
        filter=__ret__.get('filter'),
        icon_id=__ret__.get('iconId'),
        id=__ret__.get('id'),
        name=__ret__.get('name'),
        network_interfaces=__ret__.get('networkInterfaces'),
        plan=__ret__.get('plan'),
        tags=__ret__.get('tags'),
        vips=__ret__.get('vips'),
        zone=__ret__.get('zone'))
