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
    'GetArchiveResult',
    'AwaitableGetArchiveResult',
    'get_archive',
]

@pulumi.output_type
class GetArchiveResult:
    """
    A collection of values returned by getArchive.
    """
    def __init__(__self__, description=None, filter=None, icon_id=None, id=None, name=None, os_type=None, size=None, tags=None, zone=None):
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
        if os_type and not isinstance(os_type, str):
            raise TypeError("Expected argument 'os_type' to be a str")
        pulumi.set(__self__, "os_type", os_type)
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
        The description of the Archive.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def filter(self) -> Optional['outputs.GetArchiveFilterResult']:
        return pulumi.get(self, "filter")

    @property
    @pulumi.getter(name="iconId")
    def icon_id(self) -> str:
        """
        The icon id attached to the Archive.
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
        The name of the Archive.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[str]:
        return pulumi.get(self, "os_type")

    @property
    @pulumi.getter
    def size(self) -> int:
        """
        The size of Archive in GiB.
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter
    def tags(self) -> Sequence[str]:
        """
        Any tags assigned to the Archive.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def zone(self) -> str:
        return pulumi.get(self, "zone")


class AwaitableGetArchiveResult(GetArchiveResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetArchiveResult(
            description=self.description,
            filter=self.filter,
            icon_id=self.icon_id,
            id=self.id,
            name=self.name,
            os_type=self.os_type,
            size=self.size,
            tags=self.tags,
            zone=self.zone)


def get_archive(filter: Optional[pulumi.InputType['GetArchiveFilterArgs']] = None,
                os_type: Optional[str] = None,
                zone: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetArchiveResult:
    """
    Get information about an existing Archive.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_sakuracloud as sakuracloud

    foobar = sakuracloud.get_archive(os_type="centos8")
    ```


    :param pulumi.InputType['GetArchiveFilterArgs'] filter: One or more values used for filtering, as defined below.
    :param str os_type: The criteria used to filter SakuraCloud archives. This must be one of following:  
           - **CentOS**: [`centos`/`centos8`/`centos8stream`/`centos7`]
           - **Alt RHEL/CentOS**: [`almalinux`/`rockylinux`/`miracle`/`miraclelinux`]
           - **Ubuntu**: [`ubuntu`/`ubuntu2004`/`ubuntu1804`]
           - **Debian**: [`debian`/`debian10`/`debian11`]
           - **CoreOS/ContainerLinux**: `coreos`
           - **RancherOS**: `rancheros`
           - **k3OS**: `k3os`
           - **FreeBSD**: `freebsd`
           - **Kusanagi**: `kusanagi`
           - **Windows2016**: [`windows2016`/`windows2016-rds`/`windows2016-rds-office`]
           - **Windows2016+SQLServer**:  [`windows2016-sql-web`/`windows2016-sql-standard`/`windows2016-sql-standard-all`]
           - **Windows2016+SQLServer2017**: [`windows2016-sql2017-standard`/`windows2016-sql2017-enterprise`/`windows2016-sql2017-standard-all`]
           - **Windows2019**: [`windows2019`/`windows2019-rds`/`windows2019-rds-office2016`/`windows2019-rds-office2019`]
           - **Windows2019+SQLServer2017**: [`windows2019-sql2017-web`/`windows2019-sql2017-standard`/`windows2019-sql2017-enterprise`/`windows2019-sql2017-standard-all`]
           - **Windows2019+SQLServer2019**: [`windows2019-sql2019-web`/`windows2019-sql2019-standard`/`windows2019-sql2019-enterprise`/`windows2019-sql2019-standard-all`]
    :param str zone: The name of zone that the Archive is in (e.g. `is1a`, `tk1a`).
    """
    __args__ = dict()
    __args__['filter'] = filter
    __args__['osType'] = os_type
    __args__['zone'] = zone
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('sakuracloud:index/getArchive:getArchive', __args__, opts=opts, typ=GetArchiveResult).value

    return AwaitableGetArchiveResult(
        description=__ret__.description,
        filter=__ret__.filter,
        icon_id=__ret__.icon_id,
        id=__ret__.id,
        name=__ret__.name,
        os_type=__ret__.os_type,
        size=__ret__.size,
        tags=__ret__.tags,
        zone=__ret__.zone)
