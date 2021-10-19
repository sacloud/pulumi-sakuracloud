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
    'GetEnhancedDBResult',
    'AwaitableGetEnhancedDBResult',
    'get_enhanced_db',
    'get_enhanced_db_output',
]

@pulumi.output_type
class GetEnhancedDBResult:
    """
    A collection of values returned by getEnhancedDB.
    """
    def __init__(__self__, database_name=None, database_type=None, description=None, filter=None, hostname=None, icon_id=None, id=None, max_connections=None, name=None, region=None, tags=None):
        if database_name and not isinstance(database_name, str):
            raise TypeError("Expected argument 'database_name' to be a str")
        pulumi.set(__self__, "database_name", database_name)
        if database_type and not isinstance(database_type, str):
            raise TypeError("Expected argument 'database_type' to be a str")
        pulumi.set(__self__, "database_type", database_type)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if filter and not isinstance(filter, dict):
            raise TypeError("Expected argument 'filter' to be a dict")
        pulumi.set(__self__, "filter", filter)
        if hostname and not isinstance(hostname, str):
            raise TypeError("Expected argument 'hostname' to be a str")
        pulumi.set(__self__, "hostname", hostname)
        if icon_id and not isinstance(icon_id, str):
            raise TypeError("Expected argument 'icon_id' to be a str")
        pulumi.set(__self__, "icon_id", icon_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if max_connections and not isinstance(max_connections, int):
            raise TypeError("Expected argument 'max_connections' to be a int")
        pulumi.set(__self__, "max_connections", max_connections)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> str:
        """
        The name of database.
        """
        return pulumi.get(self, "database_name")

    @property
    @pulumi.getter(name="databaseType")
    def database_type(self) -> str:
        """
        The type of database.
        """
        return pulumi.get(self, "database_type")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The description of the EnhancedDB.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def filter(self) -> Optional['outputs.GetEnhancedDBFilterResult']:
        return pulumi.get(self, "filter")

    @property
    @pulumi.getter
    def hostname(self) -> str:
        """
        The name of database host. This will be built from `database_name` + `tidb-is1.db.sakurausercontent.com`.
        """
        return pulumi.get(self, "hostname")

    @property
    @pulumi.getter(name="iconId")
    def icon_id(self) -> str:
        """
        The icon id attached to the EnhancedDB.
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
    @pulumi.getter(name="maxConnections")
    def max_connections(self) -> int:
        """
        The value of max connections setting.
        """
        return pulumi.get(self, "max_connections")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the EnhancedDB.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def region(self) -> str:
        """
        The region name.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def tags(self) -> Sequence[str]:
        """
        Any tags assigned to the EnhancedDB.
        """
        return pulumi.get(self, "tags")


class AwaitableGetEnhancedDBResult(GetEnhancedDBResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEnhancedDBResult(
            database_name=self.database_name,
            database_type=self.database_type,
            description=self.description,
            filter=self.filter,
            hostname=self.hostname,
            icon_id=self.icon_id,
            id=self.id,
            max_connections=self.max_connections,
            name=self.name,
            region=self.region,
            tags=self.tags)


def get_enhanced_db(filter: Optional[pulumi.InputType['GetEnhancedDBFilterArgs']] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEnhancedDBResult:
    """
    Get information about an existing Enhanced Database.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_sakuracloud as sakuracloud

    foobar = sakuracloud.get_enhanced_db(filter=sakuracloud.GetEnhancedDBFilterArgs(
        names=["foobar"],
    ))
    ```


    :param pulumi.InputType['GetEnhancedDBFilterArgs'] filter: One or more values used for filtering, as defined below.
    """
    __args__ = dict()
    __args__['filter'] = filter
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('sakuracloud:index/getEnhancedDB:getEnhancedDB', __args__, opts=opts, typ=GetEnhancedDBResult).value

    return AwaitableGetEnhancedDBResult(
        database_name=__ret__.database_name,
        database_type=__ret__.database_type,
        description=__ret__.description,
        filter=__ret__.filter,
        hostname=__ret__.hostname,
        icon_id=__ret__.icon_id,
        id=__ret__.id,
        max_connections=__ret__.max_connections,
        name=__ret__.name,
        region=__ret__.region,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_enhanced_db)
def get_enhanced_db_output(filter: Optional[pulumi.Input[Optional[pulumi.InputType['GetEnhancedDBFilterArgs']]]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetEnhancedDBResult]:
    """
    Get information about an existing Enhanced Database.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_sakuracloud as sakuracloud

    foobar = sakuracloud.get_enhanced_db(filter=sakuracloud.GetEnhancedDBFilterArgs(
        names=["foobar"],
    ))
    ```


    :param pulumi.InputType['GetEnhancedDBFilterArgs'] filter: One or more values used for filtering, as defined below.
    """
    ...
