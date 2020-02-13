# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class GetContainerRegistryResult:
    """
    A collection of values returned by getContainerRegistry.
    """
    def __init__(__self__, access_level=None, description=None, filter=None, fqdn=None, icon_id=None, id=None, name=None, subdomain_label=None, tags=None):
        if access_level and not isinstance(access_level, str):
            raise TypeError("Expected argument 'access_level' to be a str")
        __self__.access_level = access_level
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        __self__.description = description
        if filter and not isinstance(filter, dict):
            raise TypeError("Expected argument 'filter' to be a dict")
        __self__.filter = filter
        if fqdn and not isinstance(fqdn, str):
            raise TypeError("Expected argument 'fqdn' to be a str")
        __self__.fqdn = fqdn
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
        if subdomain_label and not isinstance(subdomain_label, str):
            raise TypeError("Expected argument 'subdomain_label' to be a str")
        __self__.subdomain_label = subdomain_label
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        __self__.tags = tags
class AwaitableGetContainerRegistryResult(GetContainerRegistryResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetContainerRegistryResult(
            access_level=self.access_level,
            description=self.description,
            filter=self.filter,
            fqdn=self.fqdn,
            icon_id=self.icon_id,
            id=self.id,
            name=self.name,
            subdomain_label=self.subdomain_label,
            tags=self.tags)

def get_container_registry(filter=None,opts=None):
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
    __ret__ = pulumi.runtime.invoke('sakuracloud:index/getContainerRegistry:getContainerRegistry', __args__, opts=opts).value

    return AwaitableGetContainerRegistryResult(
        access_level=__ret__.get('accessLevel'),
        description=__ret__.get('description'),
        filter=__ret__.get('filter'),
        fqdn=__ret__.get('fqdn'),
        icon_id=__ret__.get('iconId'),
        id=__ret__.get('id'),
        name=__ret__.get('name'),
        subdomain_label=__ret__.get('subdomainLabel'),
        tags=__ret__.get('tags'))
