# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class GetInternetResult:
    """
    A collection of values returned by getInternet.
    """
    def __init__(__self__, band_width=None, description=None, enable_ipv6=None, filters=None, gateway=None, icon_id=None, ipaddresses=None, ipv6_nw_address=None, ipv6_prefix=None, ipv6_prefix_len=None, max_ipaddress=None, min_ipaddress=None, name=None, name_selectors=None, nw_address=None, nw_mask_len=None, server_ids=None, switch_id=None, tag_selectors=None, tags=None, zone=None, id=None):
        if band_width and not isinstance(band_width, float):
            raise TypeError("Expected argument 'band_width' to be a float")
        __self__.band_width = band_width
        """
        Bandwidth of outbound traffic.
        """
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        __self__.description = description
        """
        The description of the resource.
        """
        if enable_ipv6 and not isinstance(enable_ipv6, bool):
            raise TypeError("Expected argument 'enable_ipv6' to be a bool")
        __self__.enable_ipv6 = enable_ipv6
        """
        The ipv6 enabled flag.
        """
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        __self__.filters = filters
        if gateway and not isinstance(gateway, str):
            raise TypeError("Expected argument 'gateway' to be a str")
        __self__.gateway = gateway
        """
        The network gateway address of the switch.
        """
        if icon_id and not isinstance(icon_id, str):
            raise TypeError("Expected argument 'icon_id' to be a str")
        __self__.icon_id = icon_id
        """
        The ID of the icon of the resource.
        """
        if ipaddresses and not isinstance(ipaddresses, list):
            raise TypeError("Expected argument 'ipaddresses' to be a list")
        __self__.ipaddresses = ipaddresses
        """
        Global IP address list.
        """
        if ipv6_nw_address and not isinstance(ipv6_nw_address, str):
            raise TypeError("Expected argument 'ipv6_nw_address' to be a str")
        __self__.ipv6_nw_address = ipv6_nw_address
        """
        The ipv6 network address.
        """
        if ipv6_prefix and not isinstance(ipv6_prefix, str):
            raise TypeError("Expected argument 'ipv6_prefix' to be a str")
        __self__.ipv6_prefix = ipv6_prefix
        """
        Address prefix of ipv6 network.
        """
        if ipv6_prefix_len and not isinstance(ipv6_prefix_len, float):
            raise TypeError("Expected argument 'ipv6_prefix_len' to be a float")
        __self__.ipv6_prefix_len = ipv6_prefix_len
        """
        Address prefix length of ipv6 network.
        """
        if max_ipaddress and not isinstance(max_ipaddress, str):
            raise TypeError("Expected argument 'max_ipaddress' to be a str")
        __self__.max_ipaddress = max_ipaddress
        """
        Max global IP address.
        """
        if min_ipaddress and not isinstance(min_ipaddress, str):
            raise TypeError("Expected argument 'min_ipaddress' to be a str")
        __self__.min_ipaddress = min_ipaddress
        """
        Min global IP address.
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
        if nw_address and not isinstance(nw_address, str):
            raise TypeError("Expected argument 'nw_address' to be a str")
        __self__.nw_address = nw_address
        """
        The network address.
        """
        if nw_mask_len and not isinstance(nw_mask_len, float):
            raise TypeError("Expected argument 'nw_mask_len' to be a float")
        __self__.nw_mask_len = nw_mask_len
        """
        Network mask length.
        """
        if server_ids and not isinstance(server_ids, list):
            raise TypeError("Expected argument 'server_ids' to be a list")
        __self__.server_ids = server_ids
        """
        The ID list of the servers connected to the switch.
        """
        if switch_id and not isinstance(switch_id, str):
            raise TypeError("Expected argument 'switch_id' to be a str")
        __self__.switch_id = switch_id
        """
        The ID of the switch.
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
class AwaitableGetInternetResult(GetInternetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInternetResult(
            band_width=self.band_width,
            description=self.description,
            enable_ipv6=self.enable_ipv6,
            filters=self.filters,
            gateway=self.gateway,
            icon_id=self.icon_id,
            ipaddresses=self.ipaddresses,
            ipv6_nw_address=self.ipv6_nw_address,
            ipv6_prefix=self.ipv6_prefix,
            ipv6_prefix_len=self.ipv6_prefix_len,
            max_ipaddress=self.max_ipaddress,
            min_ipaddress=self.min_ipaddress,
            name=self.name,
            name_selectors=self.name_selectors,
            nw_address=self.nw_address,
            nw_mask_len=self.nw_mask_len,
            server_ids=self.server_ids,
            switch_id=self.switch_id,
            tag_selectors=self.tag_selectors,
            tags=self.tags,
            zone=self.zone,
            id=self.id)

def get_internet(filters=None,name_selectors=None,tag_selectors=None,zone=None,opts=None):
    """
    Use this data source to retrieve information about a SakuraCloud Internet (Switch+Router).
    
    :param list filters: The map of filter key and value.
    :param list name_selectors: The list of names to filtering.
    :param list tag_selectors: The list of tags to filtering.
    :param str zone: The ID of the zone.
    
    The **filters** object supports the following:
    
      * `name` (`str`) - The name of the resource.
      * `values` (`list`)

    > This content is derived from https://github.com/terraform-providers/terraform-provider-sakuracloud/blob/master/website/docs/d/internet.html.markdown.
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
    __ret__ = pulumi.runtime.invoke('sakuracloud:index/getInternet:getInternet', __args__, opts=opts).value

    return AwaitableGetInternetResult(
        band_width=__ret__.get('bandWidth'),
        description=__ret__.get('description'),
        enable_ipv6=__ret__.get('enableIpv6'),
        filters=__ret__.get('filters'),
        gateway=__ret__.get('gateway'),
        icon_id=__ret__.get('iconId'),
        ipaddresses=__ret__.get('ipaddresses'),
        ipv6_nw_address=__ret__.get('ipv6NwAddress'),
        ipv6_prefix=__ret__.get('ipv6Prefix'),
        ipv6_prefix_len=__ret__.get('ipv6PrefixLen'),
        max_ipaddress=__ret__.get('maxIpaddress'),
        min_ipaddress=__ret__.get('minIpaddress'),
        name=__ret__.get('name'),
        name_selectors=__ret__.get('nameSelectors'),
        nw_address=__ret__.get('nwAddress'),
        nw_mask_len=__ret__.get('nwMaskLen'),
        server_ids=__ret__.get('serverIds'),
        switch_id=__ret__.get('switchId'),
        tag_selectors=__ret__.get('tagSelectors'),
        tags=__ret__.get('tags'),
        zone=__ret__.get('zone'),
        id=__ret__.get('id'))
