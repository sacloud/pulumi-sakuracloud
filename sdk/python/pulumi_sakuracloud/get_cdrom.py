# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = [
    'GetCDROMResult',
    'AwaitableGetCDROMResult',
    'get_cdrom',
    'get_cdrom_output',
]

@pulumi.output_type
class GetCDROMResult:
    """
    A collection of values returned by getCDROM.
    """
    def __init__(__self__, description=None, filter=None, icon_id=None, id=None, name=None, size=None, tags=None, zone=None):
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
        if size and not isinstance(size, int):
            raise TypeError("Expected argument 'size' to be a int")
        pulumi.set(__self__, "size", size)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if zone and not isinstance(zone, str):
            raise TypeError("Expected argument 'zone' to be a str")
        pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The description of the CD-ROM.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def filter(self) -> Optional['outputs.GetCDROMFilterResult']:
        return pulumi.get(self, "filter")

    @property
    @pulumi.getter(name="iconId")
    def icon_id(self) -> str:
        """
        The icon id attached to the CD-ROM.
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
        The name of the CD-ROM.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def size(self) -> int:
        """
        The size of CD-ROM in GiB.
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter
    def tags(self) -> Sequence[str]:
        """
        Any tags assigned to the CD-ROM.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def zone(self) -> str:
        return pulumi.get(self, "zone")


class AwaitableGetCDROMResult(GetCDROMResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCDROMResult(
            description=self.description,
            filter=self.filter,
            icon_id=self.icon_id,
            id=self.id,
            name=self.name,
            size=self.size,
            tags=self.tags,
            zone=self.zone)


def get_cdrom(filter: Optional[pulumi.InputType['GetCDROMFilterArgs']] = None,
              zone: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCDROMResult:
    """
    Get information about an existing CD-ROM.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_sakuracloud as sakuracloud

    foobar = sakuracloud.get_cdrom(filter=sakuracloud.GetCDROMFilterArgs(
        conditions=[sakuracloud.GetCDROMFilterConditionArgs(
            name="Name",
            values=["Parted Magic 2013_08_01"],
        )],
    ))
    ```


    :param pulumi.InputType['GetCDROMFilterArgs'] filter: One or more values used for filtering, as defined below.
    :param str zone: The name of zone that the CD-ROM is in (e.g. `is1a`, `tk1a`).
    """
    __args__ = dict()
    __args__['filter'] = filter
    __args__['zone'] = zone
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('sakuracloud:index/getCDROM:getCDROM', __args__, opts=opts, typ=GetCDROMResult).value

    return AwaitableGetCDROMResult(
        description=__ret__.description,
        filter=__ret__.filter,
        icon_id=__ret__.icon_id,
        id=__ret__.id,
        name=__ret__.name,
        size=__ret__.size,
        tags=__ret__.tags,
        zone=__ret__.zone)


@_utilities.lift_output_func(get_cdrom)
def get_cdrom_output(filter: Optional[pulumi.Input[Optional[pulumi.InputType['GetCDROMFilterArgs']]]] = None,
                     zone: Optional[pulumi.Input[Optional[str]]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCDROMResult]:
    """
    Get information about an existing CD-ROM.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_sakuracloud as sakuracloud

    foobar = sakuracloud.get_cdrom(filter=sakuracloud.GetCDROMFilterArgs(
        conditions=[sakuracloud.GetCDROMFilterConditionArgs(
            name="Name",
            values=["Parted Magic 2013_08_01"],
        )],
    ))
    ```


    :param pulumi.InputType['GetCDROMFilterArgs'] filter: One or more values used for filtering, as defined below.
    :param str zone: The name of zone that the CD-ROM is in (e.g. `is1a`, `tk1a`).
    """
    ...
