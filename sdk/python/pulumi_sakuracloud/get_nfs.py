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
    def __init__(__self__, default_route=None, description=None, filters=None, icon_id=None, ipaddress=None, name=None, name_selectors=None, nw_mask_len=None, plan=None, size=None, switch_id=None, tag_selectors=None, tags=None, zone=None, id=None):
        if default_route and not isinstance(default_route, str):
            raise TypeError("Expected argument 'default_route' to be a str")
        __self__.default_route = default_route
        """
        Default gateway address of the NFS.	 
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
        if icon_id and not isinstance(icon_id, str):
            raise TypeError("Expected argument 'icon_id' to be a str")
        __self__.icon_id = icon_id
        """
        The ID of the icon of the resource.
        """
        if ipaddress and not isinstance(ipaddress, str):
            raise TypeError("Expected argument 'ipaddress' to be a str")
        __self__.ipaddress = ipaddress
        """
        The IP address of the NFS.
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
        if nw_mask_len and not isinstance(nw_mask_len, float):
            raise TypeError("Expected argument 'nw_mask_len' to be a float")
        __self__.nw_mask_len = nw_mask_len
        """
        Network mask length.
        """
        if plan and not isinstance(plan, str):
            raise TypeError("Expected argument 'plan' to be a str")
        __self__.plan = plan
        """
        The name of the resource plan.
        """
        if size and not isinstance(size, float):
            raise TypeError("Expected argument 'size' to be a float")
        __self__.size = size
        """
        The size of the NFS.
        """
        if switch_id and not isinstance(switch_id, str):
            raise TypeError("Expected argument 'switch_id' to be a str")
        __self__.switch_id = switch_id
        """
        The ID of the Switch connected to the NFS.
        """
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
class AwaitableGetNFSResult(GetNFSResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNFSResult(
            default_route=self.default_route,
            description=self.description,
            filters=self.filters,
            icon_id=self.icon_id,
            ipaddress=self.ipaddress,
            name=self.name,
            name_selectors=self.name_selectors,
            nw_mask_len=self.nw_mask_len,
            plan=self.plan,
            size=self.size,
            switch_id=self.switch_id,
            tag_selectors=self.tag_selectors,
            tags=self.tags,
            zone=self.zone,
            id=self.id)

def get_nfs(filters=None,name_selectors=None,tag_selectors=None,zone=None,opts=None):
    """
    Use this data source to retrieve information about a SakuraCloud NFS.
    
    :param list filters: The map of filter key and value.
    :param list name_selectors: The list of names to filtering.
    :param list tag_selectors: The list of tags to filtering.
    :param str zone: The ID of the zone.
    
    The **filters** object supports the following:
    
      * `name` (`str`) - The name of the resource.
      * `values` (`list`)

    > This content is derived from https://github.com/terraform-providers/terraform-provider-sakuracloud/blob/master/website/docs/d/nfs.html.markdown.
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
    __ret__ = pulumi.runtime.invoke('sakuracloud:index/getNFS:getNFS', __args__, opts=opts).value

    return AwaitableGetNFSResult(
        default_route=__ret__.get('defaultRoute'),
        description=__ret__.get('description'),
        filters=__ret__.get('filters'),
        icon_id=__ret__.get('iconId'),
        ipaddress=__ret__.get('ipaddress'),
        name=__ret__.get('name'),
        name_selectors=__ret__.get('nameSelectors'),
        nw_mask_len=__ret__.get('nwMaskLen'),
        plan=__ret__.get('plan'),
        size=__ret__.get('size'),
        switch_id=__ret__.get('switchId'),
        tag_selectors=__ret__.get('tagSelectors'),
        tags=__ret__.get('tags'),
        zone=__ret__.get('zone'),
        id=__ret__.get('id'))