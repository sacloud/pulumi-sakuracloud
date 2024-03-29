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
    'GetGSLBResult',
    'AwaitableGetGSLBResult',
    'get_gslb',
    'get_gslb_output',
]

@pulumi.output_type
class GetGSLBResult:
    """
    A collection of values returned by getGSLB.
    """
    def __init__(__self__, description=None, filter=None, fqdn=None, health_checks=None, icon_id=None, id=None, name=None, servers=None, sorry_server=None, tags=None, weighted=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if filter and not isinstance(filter, dict):
            raise TypeError("Expected argument 'filter' to be a dict")
        pulumi.set(__self__, "filter", filter)
        if fqdn and not isinstance(fqdn, str):
            raise TypeError("Expected argument 'fqdn' to be a str")
        pulumi.set(__self__, "fqdn", fqdn)
        if health_checks and not isinstance(health_checks, list):
            raise TypeError("Expected argument 'health_checks' to be a list")
        pulumi.set(__self__, "health_checks", health_checks)
        if icon_id and not isinstance(icon_id, str):
            raise TypeError("Expected argument 'icon_id' to be a str")
        pulumi.set(__self__, "icon_id", icon_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if servers and not isinstance(servers, list):
            raise TypeError("Expected argument 'servers' to be a list")
        pulumi.set(__self__, "servers", servers)
        if sorry_server and not isinstance(sorry_server, str):
            raise TypeError("Expected argument 'sorry_server' to be a str")
        pulumi.set(__self__, "sorry_server", sorry_server)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if weighted and not isinstance(weighted, bool):
            raise TypeError("Expected argument 'weighted' to be a bool")
        pulumi.set(__self__, "weighted", weighted)

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The description of the GSLB.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def filter(self) -> Optional['outputs.GetGSLBFilterResult']:
        return pulumi.get(self, "filter")

    @property
    @pulumi.getter
    def fqdn(self) -> str:
        """
        The FQDN for accessing to the GSLB. This is typically used as value of CNAME record.
        """
        return pulumi.get(self, "fqdn")

    @property
    @pulumi.getter(name="healthChecks")
    def health_checks(self) -> Sequence['outputs.GetGSLBHealthCheckResult']:
        """
        A list of `health_check` blocks as defined below.
        """
        return pulumi.get(self, "health_checks")

    @property
    @pulumi.getter(name="iconId")
    def icon_id(self) -> str:
        """
        The icon id attached to the GSLB.
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
        The name of the GSLB.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def servers(self) -> Sequence['outputs.GetGSLBServerResult']:
        """
        A list of `server` blocks as defined below.
        """
        return pulumi.get(self, "servers")

    @property
    @pulumi.getter(name="sorryServer")
    def sorry_server(self) -> str:
        """
        The IP address of the SorryServer. This will be used when all servers are down.
        """
        return pulumi.get(self, "sorry_server")

    @property
    @pulumi.getter
    def tags(self) -> Sequence[str]:
        """
        Any tags assigned to the GSLB.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def weighted(self) -> bool:
        """
        The flag to enable weighted load-balancing.
        """
        return pulumi.get(self, "weighted")


class AwaitableGetGSLBResult(GetGSLBResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGSLBResult(
            description=self.description,
            filter=self.filter,
            fqdn=self.fqdn,
            health_checks=self.health_checks,
            icon_id=self.icon_id,
            id=self.id,
            name=self.name,
            servers=self.servers,
            sorry_server=self.sorry_server,
            tags=self.tags,
            weighted=self.weighted)


def get_gslb(filter: Optional[pulumi.InputType['GetGSLBFilterArgs']] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetGSLBResult:
    """
    Get information about an existing GSLB.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_sakuracloud as sakuracloud

    foobar = sakuracloud.get_gslb(filter=sakuracloud.GetGSLBFilterArgs(
        names=["foobar"],
    ))
    ```


    :param pulumi.InputType['GetGSLBFilterArgs'] filter: One or more values used for filtering, as defined below.
    """
    __args__ = dict()
    __args__['filter'] = filter
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('sakuracloud:index/getGSLB:getGSLB', __args__, opts=opts, typ=GetGSLBResult).value

    return AwaitableGetGSLBResult(
        description=__ret__.description,
        filter=__ret__.filter,
        fqdn=__ret__.fqdn,
        health_checks=__ret__.health_checks,
        icon_id=__ret__.icon_id,
        id=__ret__.id,
        name=__ret__.name,
        servers=__ret__.servers,
        sorry_server=__ret__.sorry_server,
        tags=__ret__.tags,
        weighted=__ret__.weighted)


@_utilities.lift_output_func(get_gslb)
def get_gslb_output(filter: Optional[pulumi.Input[Optional[pulumi.InputType['GetGSLBFilterArgs']]]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetGSLBResult]:
    """
    Get information about an existing GSLB.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_sakuracloud as sakuracloud

    foobar = sakuracloud.get_gslb(filter=sakuracloud.GetGSLBFilterArgs(
        names=["foobar"],
    ))
    ```


    :param pulumi.InputType['GetGSLBFilterArgs'] filter: One or more values used for filtering, as defined below.
    """
    ...
