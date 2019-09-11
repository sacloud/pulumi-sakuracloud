# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class GetPrivateHostResult:
    """
    A collection of values returned by getPrivateHost.
    """
    def __init__(__self__, assigned_core=None, assigned_memory=None, description=None, filters=None, hostname=None, name=None, name_selectors=None, tag_selectors=None, tags=None, zone=None, id=None):
        if assigned_core and not isinstance(assigned_core, float):
            raise TypeError("Expected argument 'assigned_core' to be a float")
        __self__.assigned_core = assigned_core
        """
        The number of cores assigned to the Server.
        """
        if assigned_memory and not isinstance(assigned_memory, float):
            raise TypeError("Expected argument 'assigned_memory' to be a float")
        __self__.assigned_memory = assigned_memory
        """
        The size of memory allocated to the Server (unit:`GB`).
        """
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        __self__.description = description
        """
        The description of the resource.
        """
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        __self__.filters = filters
        if hostname and not isinstance(hostname, str):
            raise TypeError("Expected argument 'hostname' to be a str")
        __self__.hostname = hostname
        """
        The HostName of the resource.
        """
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        """
        The name of the resource.
        """
        if name_selectors and not isinstance(name_selectors, list):
            raise TypeError("Expected argument 'name_selectors' to be a list")
        __self__.name_selectors = name_selectors
        if tag_selectors and not isinstance(tag_selectors, list):
            raise TypeError("Expected argument 'tag_selectors' to be a list")
        __self__.tag_selectors = tag_selectors
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        __self__.tags = tags
        """
        The tag list of the resources.
        """
        if zone and not isinstance(zone, str):
            raise TypeError("Expected argument 'zone' to be a str")
        __self__.zone = zone
        """
        The ID of the zone to which the resource belongs.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """
class AwaitableGetPrivateHostResult(GetPrivateHostResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPrivateHostResult(
            assigned_core=self.assigned_core,
            assigned_memory=self.assigned_memory,
            description=self.description,
            filters=self.filters,
            hostname=self.hostname,
            name=self.name,
            name_selectors=self.name_selectors,
            tag_selectors=self.tag_selectors,
            tags=self.tags,
            zone=self.zone,
            id=self.id)

def get_private_host(filters=None,name_selectors=None,tag_selectors=None,zone=None,opts=None):
    """
    Use this data source to retrieve information about a SakuraCloud Private Host.
    
    :param list filters: The map of filter key and value.
    :param list name_selectors: The list of names to filtering.
    :param list tag_selectors: The list of tags to filtering.
    :param str zone: The ID of the zone.
    
    The **filters** object supports the following:
    
      * `name` (`str`) - The name of the resource.
      * `values` (`list`)

    > This content is derived from https://github.com/terraform-providers/terraform-provider-sakuracloud/blob/master/website/docs/d/private_host.html.markdown.
    """
    __args__ = dict()

    __args__['filters'] = filters
    __args__['nameSelectors'] = name_selectors
    __args__['tagSelectors'] = tag_selectors
    __args__['zone'] = zone
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('sakuracloud:index/getPrivateHost:getPrivateHost', __args__, opts=opts).value

    return AwaitableGetPrivateHostResult(
        assigned_core=__ret__.get('assignedCore'),
        assigned_memory=__ret__.get('assignedMemory'),
        description=__ret__.get('description'),
        filters=__ret__.get('filters'),
        hostname=__ret__.get('hostname'),
        name=__ret__.get('name'),
        name_selectors=__ret__.get('nameSelectors'),
        tag_selectors=__ret__.get('tagSelectors'),
        tags=__ret__.get('tags'),
        zone=__ret__.get('zone'),
        id=__ret__.get('id'))