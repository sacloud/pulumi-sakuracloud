# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class GetDNSResult:
    """
    A collection of values returned by getDNS.
    """
    def __init__(__self__, description=None, dns_servers=None, filters=None, icon_id=None, name_selectors=None, records=None, tag_selectors=None, tags=None, zone=None, id=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        __self__.description = description
        """
        The description of the resource.
        """
        if dns_servers and not isinstance(dns_servers, list):
            raise TypeError("Expected argument 'dns_servers' to be a list")
        __self__.dns_servers = dns_servers
        """
        List of host names of DNS servers.
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
        if name_selectors and not isinstance(name_selectors, list):
            raise TypeError("Expected argument 'name_selectors' to be a list")
        __self__.name_selectors = name_selectors
        if records and not isinstance(records, list):
            raise TypeError("Expected argument 'records' to be a list")
        __self__.records = records
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
        The name of the zone.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """
class AwaitableGetDNSResult(GetDNSResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDNSResult(
            description=self.description,
            dns_servers=self.dns_servers,
            filters=self.filters,
            icon_id=self.icon_id,
            name_selectors=self.name_selectors,
            records=self.records,
            tag_selectors=self.tag_selectors,
            tags=self.tags,
            zone=self.zone,
            id=self.id)

def get_dns(filters=None,name_selectors=None,tag_selectors=None,opts=None):
    """
    Use this data source to retrieve information about a SakuraCloud DNS.
    
    :param list filters: The map of filter key and value.
    :param list name_selectors: The list of names to filtering.
    :param list tag_selectors: The list of tags to filtering.
    
    The **filters** object supports the following:
    
      * `name` (`str`)
      * `values` (`list`)

    > This content is derived from https://github.com/terraform-providers/terraform-provider-sakuracloud/blob/master/website/docs/d/dns.html.markdown.
    """
    __args__ = dict()

    __args__['filters'] = filters
    __args__['nameSelectors'] = name_selectors
    __args__['tagSelectors'] = tag_selectors
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('sakuracloud:index/getDNS:getDNS', __args__, opts=opts).value

    return AwaitableGetDNSResult(
        description=__ret__.get('description'),
        dns_servers=__ret__.get('dnsServers'),
        filters=__ret__.get('filters'),
        icon_id=__ret__.get('iconId'),
        name_selectors=__ret__.get('nameSelectors'),
        records=__ret__.get('records'),
        tag_selectors=__ret__.get('tagSelectors'),
        tags=__ret__.get('tags'),
        zone=__ret__.get('zone'),
        id=__ret__.get('id'))
