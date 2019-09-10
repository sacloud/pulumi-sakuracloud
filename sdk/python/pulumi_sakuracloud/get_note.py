# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class GetNoteResult:
    """
    A collection of values returned by getNote.
    """
    def __init__(__self__, class_=None, content=None, description=None, filters=None, icon_id=None, name=None, name_selectors=None, tag_selectors=None, tags=None, id=None):
        if class_ and not isinstance(class_, str):
            raise TypeError("Expected argument 'class_' to be a str")
        __self__.class_ = class_
        """
        The name of the note class.
        """
        if content and not isinstance(content, str):
            raise TypeError("Expected argument 'content' to be a str")
        __self__.content = content
        """
        The body of the note. 
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
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """
class AwaitableGetNoteResult(GetNoteResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNoteResult(
            class_=self.class_,
            content=self.content,
            description=self.description,
            filters=self.filters,
            icon_id=self.icon_id,
            name=self.name,
            name_selectors=self.name_selectors,
            tag_selectors=self.tag_selectors,
            tags=self.tags,
            id=self.id)

def get_note(filters=None,name_selectors=None,tag_selectors=None,opts=None):
    """
    Use this data source to retrieve information about a SakuraCloud Note.
    
    :param list filters: The map of filter key and value.
    :param list name_selectors: The list of names to filtering.
    :param list tag_selectors: The list of tags to filtering.
    
    The **filters** object supports the following:
    
      * `name` (`str`) - The name of the resource.
      * `values` (`list`)

    > This content is derived from https://github.com/terraform-providers/terraform-provider-sakuracloud/blob/master/website/docs/d/note.html.markdown.
    """
    __args__ = dict()

    __args__['filters'] = filters
    __args__['nameSelectors'] = name_selectors
    __args__['tagSelectors'] = tag_selectors
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('sakuracloud:index/getNote:getNote', __args__, opts=opts).value

    return AwaitableGetNoteResult(
        class_=__ret__.get('class'),
        content=__ret__.get('content'),
        description=__ret__.get('description'),
        filters=__ret__.get('filters'),
        icon_id=__ret__.get('iconId'),
        name=__ret__.get('name'),
        name_selectors=__ret__.get('nameSelectors'),
        tag_selectors=__ret__.get('tagSelectors'),
        tags=__ret__.get('tags'),
        id=__ret__.get('id'))
