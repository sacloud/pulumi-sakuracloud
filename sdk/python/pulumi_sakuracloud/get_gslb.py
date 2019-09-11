# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class GetGSLBResult:
    """
    A collection of values returned by getGSLB.
    """
    def __init__(__self__, description=None, filters=None, fqdn=None, health_checks=None, icon_id=None, name=None, name_selectors=None, sorry_server=None, tag_selectors=None, tags=None, weighted=None, id=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        __self__.description = description
        """
        The description of the resource.
        """
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        __self__.filters = filters
        if fqdn and not isinstance(fqdn, str):
            raise TypeError("Expected argument 'fqdn' to be a str")
        __self__.fqdn = fqdn
        """
        FQDN to access this resource.
        """
        if health_checks and not isinstance(health_checks, list):
            raise TypeError("Expected argument 'health_checks' to be a list")
        __self__.health_checks = health_checks
        """
        Health check rules. It contains some attributes to Health Check.
        """
        if icon_id and not isinstance(icon_id, str):
            raise TypeError("Expected argument 'icon_id' to be a str")
        __self__.icon_id = icon_id
        """
        The ID of the icon of the resource.
        """
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        """
        Name of the resource.
        """
        if name_selectors and not isinstance(name_selectors, list):
            raise TypeError("Expected argument 'name_selectors' to be a list")
        __self__.name_selectors = name_selectors
        if sorry_server and not isinstance(sorry_server, str):
            raise TypeError("Expected argument 'sorry_server' to be a str")
        __self__.sorry_server = sorry_server
        """
        The hostname or IP address of sorry server.
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
        if weighted and not isinstance(weighted, bool):
            raise TypeError("Expected argument 'weighted' to be a bool")
        __self__.weighted = weighted
        """
        The flag for enable/disable weighting.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """
class AwaitableGetGSLBResult(GetGSLBResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGSLBResult(
            description=self.description,
            filters=self.filters,
            fqdn=self.fqdn,
            health_checks=self.health_checks,
            icon_id=self.icon_id,
            name=self.name,
            name_selectors=self.name_selectors,
            sorry_server=self.sorry_server,
            tag_selectors=self.tag_selectors,
            tags=self.tags,
            weighted=self.weighted,
            id=self.id)

def get_gslb(filters=None,name_selectors=None,tag_selectors=None,opts=None):
    """
    Use this data source to retrieve information about a SakuraCloud GSLB.
    
    :param list filters: The map of filter key and value.
    :param list name_selectors: The list of names to filtering.
    :param list tag_selectors: The list of tags to filtering.
    
    The **filters** object supports the following:
    
      * `name` (`str`) - Name of the resource.
      * `values` (`list`)

    > This content is derived from https://github.com/sacloud/terraform-provider-sakuracloud/blob/master/website/docs/d/gslb.html.markdown.
    """
    __args__ = dict()

    __args__['filters'] = filters
    __args__['nameSelectors'] = name_selectors
    __args__['tagSelectors'] = tag_selectors
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('sakuracloud:index/getGSLB:getGSLB', __args__, opts=opts).value

    return AwaitableGetGSLBResult(
        description=__ret__.get('description'),
        filters=__ret__.get('filters'),
        fqdn=__ret__.get('fqdn'),
        health_checks=__ret__.get('healthChecks'),
        icon_id=__ret__.get('iconId'),
        name=__ret__.get('name'),
        name_selectors=__ret__.get('nameSelectors'),
        sorry_server=__ret__.get('sorryServer'),
        tag_selectors=__ret__.get('tagSelectors'),
        tags=__ret__.get('tags'),
        weighted=__ret__.get('weighted'),
        id=__ret__.get('id'))
