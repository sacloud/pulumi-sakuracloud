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
    'GetLocalRouterResult',
    'AwaitableGetLocalRouterResult',
    'get_local_router',
    'get_local_router_output',
]

@pulumi.output_type
class GetLocalRouterResult:
    """
    A collection of values returned by getLocalRouter.
    """
    def __init__(__self__, description=None, filter=None, icon_id=None, id=None, name=None, network_interfaces=None, peers=None, secret_keys=None, static_routes=None, switches=None, tags=None):
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
        if network_interfaces and not isinstance(network_interfaces, list):
            raise TypeError("Expected argument 'network_interfaces' to be a list")
        pulumi.set(__self__, "network_interfaces", network_interfaces)
        if peers and not isinstance(peers, list):
            raise TypeError("Expected argument 'peers' to be a list")
        pulumi.set(__self__, "peers", peers)
        if secret_keys and not isinstance(secret_keys, list):
            raise TypeError("Expected argument 'secret_keys' to be a list")
        pulumi.set(__self__, "secret_keys", secret_keys)
        if static_routes and not isinstance(static_routes, list):
            raise TypeError("Expected argument 'static_routes' to be a list")
        pulumi.set(__self__, "static_routes", static_routes)
        if switches and not isinstance(switches, list):
            raise TypeError("Expected argument 'switches' to be a list")
        pulumi.set(__self__, "switches", switches)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The description of the LocalRouter.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def filter(self) -> Optional['outputs.GetLocalRouterFilterResult']:
        return pulumi.get(self, "filter")

    @property
    @pulumi.getter(name="iconId")
    def icon_id(self) -> str:
        """
        The icon id attached to the LocalRouter.
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
        The name of the LocalRouter.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> Sequence['outputs.GetLocalRouterNetworkInterfaceResult']:
        """
        A list of `network_interface` blocks as defined below.
        """
        return pulumi.get(self, "network_interfaces")

    @property
    @pulumi.getter
    def peers(self) -> Sequence['outputs.GetLocalRouterPeerResult']:
        """
        A list of `peer` blocks as defined below.
        """
        return pulumi.get(self, "peers")

    @property
    @pulumi.getter(name="secretKeys")
    def secret_keys(self) -> Sequence[str]:
        """
        A list of secret key used for peering from other LocalRouters.
        """
        return pulumi.get(self, "secret_keys")

    @property
    @pulumi.getter(name="staticRoutes")
    def static_routes(self) -> Sequence['outputs.GetLocalRouterStaticRouteResult']:
        """
        A list of `static_route` blocks as defined below.
        """
        return pulumi.get(self, "static_routes")

    @property
    @pulumi.getter
    def switches(self) -> Sequence['outputs.GetLocalRouterSwitchResult']:
        """
        A list of `switch` blocks as defined below.
        """
        return pulumi.get(self, "switches")

    @property
    @pulumi.getter
    def tags(self) -> Sequence[str]:
        """
        Any tags assigned to the LocalRouter.
        """
        return pulumi.get(self, "tags")


class AwaitableGetLocalRouterResult(GetLocalRouterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLocalRouterResult(
            description=self.description,
            filter=self.filter,
            icon_id=self.icon_id,
            id=self.id,
            name=self.name,
            network_interfaces=self.network_interfaces,
            peers=self.peers,
            secret_keys=self.secret_keys,
            static_routes=self.static_routes,
            switches=self.switches,
            tags=self.tags)


def get_local_router(filter: Optional[pulumi.InputType['GetLocalRouterFilterArgs']] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLocalRouterResult:
    """
    Get information about an existing Local Router.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_sakuracloud as sakuracloud

    foobar = sakuracloud.get_local_router(filter=sakuracloud.GetLocalRouterFilterArgs(
        names=["foobar"],
    ))
    ```


    :param pulumi.InputType['GetLocalRouterFilterArgs'] filter: One or more values used for filtering, as defined below.
    """
    __args__ = dict()
    __args__['filter'] = filter
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('sakuracloud:index/getLocalRouter:getLocalRouter', __args__, opts=opts, typ=GetLocalRouterResult).value

    return AwaitableGetLocalRouterResult(
        description=__ret__.description,
        filter=__ret__.filter,
        icon_id=__ret__.icon_id,
        id=__ret__.id,
        name=__ret__.name,
        network_interfaces=__ret__.network_interfaces,
        peers=__ret__.peers,
        secret_keys=__ret__.secret_keys,
        static_routes=__ret__.static_routes,
        switches=__ret__.switches,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_local_router)
def get_local_router_output(filter: Optional[pulumi.Input[Optional[pulumi.InputType['GetLocalRouterFilterArgs']]]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLocalRouterResult]:
    """
    Get information about an existing Local Router.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_sakuracloud as sakuracloud

    foobar = sakuracloud.get_local_router(filter=sakuracloud.GetLocalRouterFilterArgs(
        names=["foobar"],
    ))
    ```


    :param pulumi.InputType['GetLocalRouterFilterArgs'] filter: One or more values used for filtering, as defined below.
    """
    ...
