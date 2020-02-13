# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class GetLocalRouterResult:
    """
    A collection of values returned by getLocalRouter.
    """
    def __init__(__self__, description=None, filter=None, icon_id=None, id=None, name=None, network_interfaces=None, peers=None, secret_keys=None, static_routes=None, switches=None, tags=None):
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
        if peers and not isinstance(peers, list):
            raise TypeError("Expected argument 'peers' to be a list")
        __self__.peers = peers
        if secret_keys and not isinstance(secret_keys, list):
            raise TypeError("Expected argument 'secret_keys' to be a list")
        __self__.secret_keys = secret_keys
        if static_routes and not isinstance(static_routes, list):
            raise TypeError("Expected argument 'static_routes' to be a list")
        __self__.static_routes = static_routes
        if switches and not isinstance(switches, list):
            raise TypeError("Expected argument 'switches' to be a list")
        __self__.switches = switches
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        __self__.tags = tags
class AwaitableGetLocalRouterResult(GetLocalRouterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLocalRouterResult(
            description=self.description,
            filter=self.filter,
            icon_id=self.icon_id,
            id=self.id,
            name=self.name,
            network_interfaces=self.network_interfaces,
            peers=self.peers,
            secret_keys=self.secret_keys,
            static_routes=self.static_routes,
            switches=self.switches,
            tags=self.tags)

def get_local_router(filter=None,opts=None):
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
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('sakuracloud:index/getLocalRouter:getLocalRouter', __args__, opts=opts).value

    return AwaitableGetLocalRouterResult(
        description=__ret__.get('description'),
        filter=__ret__.get('filter'),
        icon_id=__ret__.get('iconId'),
        id=__ret__.get('id'),
        name=__ret__.get('name'),
        network_interfaces=__ret__.get('networkInterfaces'),
        peers=__ret__.get('peers'),
        secret_keys=__ret__.get('secretKeys'),
        static_routes=__ret__.get('staticRoutes'),
        switches=__ret__.get('switches'),
        tags=__ret__.get('tags'))
