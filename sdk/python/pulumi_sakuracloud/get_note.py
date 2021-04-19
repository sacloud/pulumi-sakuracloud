# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = [
    'GetNoteResult',
    'AwaitableGetNoteResult',
    'get_note',
]

@pulumi.output_type
class GetNoteResult:
    """
    A collection of values returned by getNote.
    """
    def __init__(__self__, class_=None, content=None, description=None, filter=None, icon_id=None, id=None, name=None, tags=None):
        if class_ and not isinstance(class_, str):
            raise TypeError("Expected argument 'class_' to be a str")
        pulumi.set(__self__, "class_", class_)
        if content and not isinstance(content, str):
            raise TypeError("Expected argument 'content' to be a str")
        pulumi.set(__self__, "content", content)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if filter and not isinstance(filter, dict):
            raise TypeError("Expected argument 'filter' to be a dict")
        pulumi.set(__self__, "filter", filter)
        if icon_id and not isinstance(icon_id, str):
            raise TypeError("Expected argument 'icon_id' to be a str")
        pulumi.set(__self__, "icon_id", icon_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="class")
    def class_(self) -> str:
        """
        The class of the Note. This will be one of [`shell`/`yaml_cloud_config`].
        """
        return pulumi.get(self, "class_")

    @property
    @pulumi.getter
    def content(self) -> str:
        """
        The content of the Note.
        """
        return pulumi.get(self, "content")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The description of the Note.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def filter(self) -> Optional['outputs.GetNoteFilterResult']:
        return pulumi.get(self, "filter")

    @property
    @pulumi.getter(name="iconId")
    def icon_id(self) -> str:
        """
        The icon id attached to the Note.
        """
        return pulumi.get(self, "icon_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the Note.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> Sequence[str]:
        """
        Any tags assigned to the Note.
        """
        return pulumi.get(self, "tags")


class AwaitableGetNoteResult(GetNoteResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNoteResult(
            class_=self.class_,
            content=self.content,
            description=self.description,
            filter=self.filter,
            icon_id=self.icon_id,
            id=self.id,
            name=self.name,
            tags=self.tags)


def get_note(filter: Optional[pulumi.InputType['GetNoteFilterArgs']] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNoteResult:
    """
    Get information about an existing Note.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_sakuracloud as sakuracloud

    foobar = sakuracloud.get_note(filter=sakuracloud.GetNoteFilterArgs(
        names=["foobar"],
    ))
    ```


    :param pulumi.InputType['GetNoteFilterArgs'] filter: One or more values used for filtering, as defined below.
    """
    __args__ = dict()
    __args__['filter'] = filter
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('sakuracloud:index/getNote:getNote', __args__, opts=opts, typ=GetNoteResult).value

    return AwaitableGetNoteResult(
        class_=__ret__.class_,
        content=__ret__.content,
        description=__ret__.description,
        filter=__ret__.filter,
        icon_id=__ret__.icon_id,
        id=__ret__.id,
        name=__ret__.name,
        tags=__ret__.tags)
