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
    def __init__(__self__, default_route=None, description=None, filters=None, high_availability=None, icon_id=None, ipaddress1=None, ipaddress2=None, name=None, name_selectors=None, nw_mask_len=None, plan=None, switch_id=None, tag_selectors=None, tags=None, vrid=None, zone=None, id=None):
        if default_route and not isinstance(default_route, str):
            raise TypeError("Expected argument 'default_route' to be a str")
        __self__.default_route = default_route
        """
        Default gateway address of the Load Balancer.	 
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
        if high_availability and not isinstance(high_availability, bool):
            raise TypeError("Expected argument 'high_availability' to be a bool")
        __self__.high_availability = high_availability
        """
        The flag of enable/disable high-availability mode.
        """
        if icon_id and not isinstance(icon_id, str):
            raise TypeError("Expected argument 'icon_id' to be a str")
        __self__.icon_id = icon_id
        """
        The ID of the icon of the resource.
        """
        if ipaddress1 and not isinstance(ipaddress1, str):
            raise TypeError("Expected argument 'ipaddress1' to be a str")
        __self__.ipaddress1 = ipaddress1
        """
        The primary IP address of the Load Balancer.
        """
        if ipaddress2 and not isinstance(ipaddress2, str):
            raise TypeError("Expected argument 'ipaddress2' to be a str")
        __self__.ipaddress2 = ipaddress2
        """
        The secondly IP address of the Load Balancer. Used when high-availability mode enabled.
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
        if switch_id and not isinstance(switch_id, str):
            raise TypeError("Expected argument 'switch_id' to be a str")
        __self__.switch_id = switch_id
        """
        The ID of the Switch connected to the Load Balancer.
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
        if vrid and not isinstance(vrid, float):
            raise TypeError("Expected argument 'vrid' to be a float")
        __self__.vrid = vrid
        """
        VRID used when high-availability mode enabled.
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
class AwaitableGetLoadBalancerResult(GetLoadBalancerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLoadBalancerResult(
            default_route=self.default_route,
            description=self.description,
            filters=self.filters,
            high_availability=self.high_availability,
            icon_id=self.icon_id,
            ipaddress1=self.ipaddress1,
            ipaddress2=self.ipaddress2,
            name=self.name,
            name_selectors=self.name_selectors,
            nw_mask_len=self.nw_mask_len,
            plan=self.plan,
            switch_id=self.switch_id,
            tag_selectors=self.tag_selectors,
            tags=self.tags,
            vrid=self.vrid,
            zone=self.zone,
            id=self.id)

def get_load_balancer(filters=None,name_selectors=None,tag_selectors=None,zone=None,opts=None):
    """
    Use this data source to retrieve information about a SakuraCloud Load Balancer.
    
    :param list filters: The map of filter key and value.
    :param list name_selectors: The list of names to filtering.
    :param list tag_selectors: The list of tags to filtering.
    :param str zone: The ID of the zone.
    
    The **filters** object supports the following:
    
      * `name` (`str`) - The name of the resource.
      * `values` (`list`)

    > This content is derived from https://github.com/terraform-providers/terraform-provider-sakuracloud/blob/master/website/docs/d/load_balancer.html.markdown.
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
    __ret__ = pulumi.runtime.invoke('sakuracloud:index/getLoadBalancer:getLoadBalancer', __args__, opts=opts).value

    return AwaitableGetLoadBalancerResult(
        default_route=__ret__.get('defaultRoute'),
        description=__ret__.get('description'),
        filters=__ret__.get('filters'),
        high_availability=__ret__.get('highAvailability'),
        icon_id=__ret__.get('iconId'),
        ipaddress1=__ret__.get('ipaddress1'),
        ipaddress2=__ret__.get('ipaddress2'),
        name=__ret__.get('name'),
        name_selectors=__ret__.get('nameSelectors'),
        nw_mask_len=__ret__.get('nwMaskLen'),
        plan=__ret__.get('plan'),
        switch_id=__ret__.get('switchId'),
        tag_selectors=__ret__.get('tagSelectors'),
        tags=__ret__.get('tags'),
        vrid=__ret__.get('vrid'),
        zone=__ret__.get('zone'),
        id=__ret__.get('id'))