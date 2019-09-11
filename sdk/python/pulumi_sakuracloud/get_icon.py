# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class GetIconResult:
    """
    A collection of values returned by getIcon.
    """
    def __init__(__self__, body=None, filters=None, name=None, name_selectors=None, tag_selectors=None, tags=None, url=None, id=None):
        if body and not isinstance(body, str):
            raise TypeError("Expected argument 'body' to be a str")
        __self__.body = body
        """
        Base64 encoded icon data (size:`small`).
        """
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        __self__.filters = filters
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
        if url and not isinstance(url, str):
            raise TypeError("Expected argument 'url' to be a str")
        __self__.url = url
        """
        URL to access this resource.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """
class AwaitableGetIconResult(GetIconResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetIconResult(
            body=self.body,
            filters=self.filters,
            name=self.name,
            name_selectors=self.name_selectors,
            tag_selectors=self.tag_selectors,
            tags=self.tags,
            url=self.url,
            id=self.id)

def get_icon(filters=None,name_selectors=None,tag_selectors=None,opts=None):
    """
    Use this data source to retrieve information about a SakuraCloud Icon.
    
    :param list filters: The map of filter key and value.
    :param list name_selectors: The list of names to filtering.
    :param list tag_selectors: The list of tags to filtering.
    
    The **filters** object supports the following:
    
      * `name` (`str`) - The name of the resource.
      * `values` (`list`)

    > This content is derived from https://github.com/terraform-providers/terraform-provider-sakuracloud/blob/master/website/docs/d/icon.html.markdown.
    """
    __args__ = dict()

    __args__['filters'] = filters
    __args__['nameSelectors'] = name_selectors
    __args__['tagSelectors'] = tag_selectors
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('sakuracloud:index/getIcon:getIcon', __args__, opts=opts).value

    return AwaitableGetIconResult(
        body=__ret__.get('body'),
        filters=__ret__.get('filters'),
        name=__ret__.get('name'),
        name_selectors=__ret__.get('nameSelectors'),
        tag_selectors=__ret__.get('tagSelectors'),
        tags=__ret__.get('tags'),
        url=__ret__.get('url'),
        id=__ret__.get('id'))