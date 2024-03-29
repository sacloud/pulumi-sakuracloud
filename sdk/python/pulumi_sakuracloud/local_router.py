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

__all__ = ['LocalRouterArgs', 'LocalRouter']

@pulumi.input_type
class LocalRouterArgs:
    def __init__(__self__, *,
                 network_interface: pulumi.Input['LocalRouterNetworkInterfaceArgs'],
                 switch: pulumi.Input['LocalRouterSwitchArgs'],
                 description: Optional[pulumi.Input[str]] = None,
                 icon_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 peers: Optional[pulumi.Input[Sequence[pulumi.Input['LocalRouterPeerArgs']]]] = None,
                 static_routes: Optional[pulumi.Input[Sequence[pulumi.Input['LocalRouterStaticRouteArgs']]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a LocalRouter resource.
        :param pulumi.Input['LocalRouterNetworkInterfaceArgs'] network_interface: An `network_interface` block as defined below.
        :param pulumi.Input['LocalRouterSwitchArgs'] switch: A `switch` block as defined below.
        :param pulumi.Input[str] description: The description of the LocalRouter. The length of this value must be in the range [`1`-`512`].
        :param pulumi.Input[str] icon_id: The icon id to attach to the LoadBalancer.
        :param pulumi.Input[str] name: The name of the LocalRouter. The length of this value must be in the range [`1`-`64`].
        :param pulumi.Input[Sequence[pulumi.Input['LocalRouterPeerArgs']]] peers: One or more `peer` blocks as defined below.
        :param pulumi.Input[Sequence[pulumi.Input['LocalRouterStaticRouteArgs']]] static_routes: One or more `static_route` blocks as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Any tags to assign to the LoadBalancer.
        """
        pulumi.set(__self__, "network_interface", network_interface)
        pulumi.set(__self__, "switch", switch)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if icon_id is not None:
            pulumi.set(__self__, "icon_id", icon_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if peers is not None:
            pulumi.set(__self__, "peers", peers)
        if static_routes is not None:
            pulumi.set(__self__, "static_routes", static_routes)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="networkInterface")
    def network_interface(self) -> pulumi.Input['LocalRouterNetworkInterfaceArgs']:
        """
        An `network_interface` block as defined below.
        """
        return pulumi.get(self, "network_interface")

    @network_interface.setter
    def network_interface(self, value: pulumi.Input['LocalRouterNetworkInterfaceArgs']):
        pulumi.set(self, "network_interface", value)

    @property
    @pulumi.getter
    def switch(self) -> pulumi.Input['LocalRouterSwitchArgs']:
        """
        A `switch` block as defined below.
        """
        return pulumi.get(self, "switch")

    @switch.setter
    def switch(self, value: pulumi.Input['LocalRouterSwitchArgs']):
        pulumi.set(self, "switch", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the LocalRouter. The length of this value must be in the range [`1`-`512`].
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="iconId")
    def icon_id(self) -> Optional[pulumi.Input[str]]:
        """
        The icon id to attach to the LoadBalancer.
        """
        return pulumi.get(self, "icon_id")

    @icon_id.setter
    def icon_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "icon_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the LocalRouter. The length of this value must be in the range [`1`-`64`].
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def peers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['LocalRouterPeerArgs']]]]:
        """
        One or more `peer` blocks as defined below.
        """
        return pulumi.get(self, "peers")

    @peers.setter
    def peers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['LocalRouterPeerArgs']]]]):
        pulumi.set(self, "peers", value)

    @property
    @pulumi.getter(name="staticRoutes")
    def static_routes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['LocalRouterStaticRouteArgs']]]]:
        """
        One or more `static_route` blocks as defined below.
        """
        return pulumi.get(self, "static_routes")

    @static_routes.setter
    def static_routes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['LocalRouterStaticRouteArgs']]]]):
        pulumi.set(self, "static_routes", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Any tags to assign to the LoadBalancer.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _LocalRouterState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 icon_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_interface: Optional[pulumi.Input['LocalRouterNetworkInterfaceArgs']] = None,
                 peers: Optional[pulumi.Input[Sequence[pulumi.Input['LocalRouterPeerArgs']]]] = None,
                 secret_keys: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 static_routes: Optional[pulumi.Input[Sequence[pulumi.Input['LocalRouterStaticRouteArgs']]]] = None,
                 switch: Optional[pulumi.Input['LocalRouterSwitchArgs']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering LocalRouter resources.
        :param pulumi.Input[str] description: The description of the LocalRouter. The length of this value must be in the range [`1`-`512`].
        :param pulumi.Input[str] icon_id: The icon id to attach to the LoadBalancer.
        :param pulumi.Input[str] name: The name of the LocalRouter. The length of this value must be in the range [`1`-`64`].
        :param pulumi.Input['LocalRouterNetworkInterfaceArgs'] network_interface: An `network_interface` block as defined below.
        :param pulumi.Input[Sequence[pulumi.Input['LocalRouterPeerArgs']]] peers: One or more `peer` blocks as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] secret_keys: A list of secret key used for peering from other LocalRouters.
        :param pulumi.Input[Sequence[pulumi.Input['LocalRouterStaticRouteArgs']]] static_routes: One or more `static_route` blocks as defined below.
        :param pulumi.Input['LocalRouterSwitchArgs'] switch: A `switch` block as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Any tags to assign to the LoadBalancer.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if icon_id is not None:
            pulumi.set(__self__, "icon_id", icon_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if network_interface is not None:
            pulumi.set(__self__, "network_interface", network_interface)
        if peers is not None:
            pulumi.set(__self__, "peers", peers)
        if secret_keys is not None:
            pulumi.set(__self__, "secret_keys", secret_keys)
        if static_routes is not None:
            pulumi.set(__self__, "static_routes", static_routes)
        if switch is not None:
            pulumi.set(__self__, "switch", switch)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the LocalRouter. The length of this value must be in the range [`1`-`512`].
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="iconId")
    def icon_id(self) -> Optional[pulumi.Input[str]]:
        """
        The icon id to attach to the LoadBalancer.
        """
        return pulumi.get(self, "icon_id")

    @icon_id.setter
    def icon_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "icon_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the LocalRouter. The length of this value must be in the range [`1`-`64`].
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="networkInterface")
    def network_interface(self) -> Optional[pulumi.Input['LocalRouterNetworkInterfaceArgs']]:
        """
        An `network_interface` block as defined below.
        """
        return pulumi.get(self, "network_interface")

    @network_interface.setter
    def network_interface(self, value: Optional[pulumi.Input['LocalRouterNetworkInterfaceArgs']]):
        pulumi.set(self, "network_interface", value)

    @property
    @pulumi.getter
    def peers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['LocalRouterPeerArgs']]]]:
        """
        One or more `peer` blocks as defined below.
        """
        return pulumi.get(self, "peers")

    @peers.setter
    def peers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['LocalRouterPeerArgs']]]]):
        pulumi.set(self, "peers", value)

    @property
    @pulumi.getter(name="secretKeys")
    def secret_keys(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of secret key used for peering from other LocalRouters.
        """
        return pulumi.get(self, "secret_keys")

    @secret_keys.setter
    def secret_keys(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "secret_keys", value)

    @property
    @pulumi.getter(name="staticRoutes")
    def static_routes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['LocalRouterStaticRouteArgs']]]]:
        """
        One or more `static_route` blocks as defined below.
        """
        return pulumi.get(self, "static_routes")

    @static_routes.setter
    def static_routes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['LocalRouterStaticRouteArgs']]]]):
        pulumi.set(self, "static_routes", value)

    @property
    @pulumi.getter
    def switch(self) -> Optional[pulumi.Input['LocalRouterSwitchArgs']]:
        """
        A `switch` block as defined below.
        """
        return pulumi.get(self, "switch")

    @switch.setter
    def switch(self, value: Optional[pulumi.Input['LocalRouterSwitchArgs']]):
        pulumi.set(self, "switch", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Any tags to assign to the LoadBalancer.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class LocalRouter(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 icon_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_interface: Optional[pulumi.Input[pulumi.InputType['LocalRouterNetworkInterfaceArgs']]] = None,
                 peers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LocalRouterPeerArgs']]]]] = None,
                 static_routes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LocalRouterStaticRouteArgs']]]]] = None,
                 switch: Optional[pulumi.Input[pulumi.InputType['LocalRouterSwitchArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Manages a SakuraCloud Local Router.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sakuracloud as sakuracloud

        foobar_switch = sakuracloud.Switch("foobarSwitch")
        peer = sakuracloud.get_local_router(filter=sakuracloud.GetLocalRouterFilterArgs(
            names=["peer"],
        ))
        foobar_local_router = sakuracloud.LocalRouter("foobarLocalRouter",
            description="descriptio",
            tags=[
                "tag1",
                "tag2",
            ],
            switch=sakuracloud.LocalRouterSwitchArgs(
                code=foobar_switch.id,
                category="cloud",
                zone_id="is1a",
            ),
            network_interface=sakuracloud.LocalRouterNetworkInterfaceArgs(
                vip="192.168.11.1",
                ip_addresses=[
                    "192.168.11.11",
                    "192.168.11.12",
                ],
                netmask=24,
                vrid=101,
            ),
            static_routes=[
                sakuracloud.LocalRouterStaticRouteArgs(
                    prefix="10.0.0.0/24",
                    next_hop="192.168.11.2",
                ),
                sakuracloud.LocalRouterStaticRouteArgs(
                    prefix="172.16.0.0/16",
                    next_hop="192.168.11.3",
                ),
            ],
            peers=[sakuracloud.LocalRouterPeerArgs(
                peer_id=peer.id,
                secret_key=peer.secret_keys[0],
                description="description",
            )])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the LocalRouter. The length of this value must be in the range [`1`-`512`].
        :param pulumi.Input[str] icon_id: The icon id to attach to the LoadBalancer.
        :param pulumi.Input[str] name: The name of the LocalRouter. The length of this value must be in the range [`1`-`64`].
        :param pulumi.Input[pulumi.InputType['LocalRouterNetworkInterfaceArgs']] network_interface: An `network_interface` block as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LocalRouterPeerArgs']]]] peers: One or more `peer` blocks as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LocalRouterStaticRouteArgs']]]] static_routes: One or more `static_route` blocks as defined below.
        :param pulumi.Input[pulumi.InputType['LocalRouterSwitchArgs']] switch: A `switch` block as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Any tags to assign to the LoadBalancer.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LocalRouterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a SakuraCloud Local Router.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sakuracloud as sakuracloud

        foobar_switch = sakuracloud.Switch("foobarSwitch")
        peer = sakuracloud.get_local_router(filter=sakuracloud.GetLocalRouterFilterArgs(
            names=["peer"],
        ))
        foobar_local_router = sakuracloud.LocalRouter("foobarLocalRouter",
            description="descriptio",
            tags=[
                "tag1",
                "tag2",
            ],
            switch=sakuracloud.LocalRouterSwitchArgs(
                code=foobar_switch.id,
                category="cloud",
                zone_id="is1a",
            ),
            network_interface=sakuracloud.LocalRouterNetworkInterfaceArgs(
                vip="192.168.11.1",
                ip_addresses=[
                    "192.168.11.11",
                    "192.168.11.12",
                ],
                netmask=24,
                vrid=101,
            ),
            static_routes=[
                sakuracloud.LocalRouterStaticRouteArgs(
                    prefix="10.0.0.0/24",
                    next_hop="192.168.11.2",
                ),
                sakuracloud.LocalRouterStaticRouteArgs(
                    prefix="172.16.0.0/16",
                    next_hop="192.168.11.3",
                ),
            ],
            peers=[sakuracloud.LocalRouterPeerArgs(
                peer_id=peer.id,
                secret_key=peer.secret_keys[0],
                description="description",
            )])
        ```

        :param str resource_name: The name of the resource.
        :param LocalRouterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LocalRouterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 icon_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_interface: Optional[pulumi.Input[pulumi.InputType['LocalRouterNetworkInterfaceArgs']]] = None,
                 peers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LocalRouterPeerArgs']]]]] = None,
                 static_routes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LocalRouterStaticRouteArgs']]]]] = None,
                 switch: Optional[pulumi.Input[pulumi.InputType['LocalRouterSwitchArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LocalRouterArgs.__new__(LocalRouterArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["icon_id"] = icon_id
            __props__.__dict__["name"] = name
            if network_interface is None and not opts.urn:
                raise TypeError("Missing required property 'network_interface'")
            __props__.__dict__["network_interface"] = network_interface
            __props__.__dict__["peers"] = peers
            __props__.__dict__["static_routes"] = static_routes
            if switch is None and not opts.urn:
                raise TypeError("Missing required property 'switch'")
            __props__.__dict__["switch"] = switch
            __props__.__dict__["tags"] = tags
            __props__.__dict__["secret_keys"] = None
        super(LocalRouter, __self__).__init__(
            'sakuracloud:index/localRouter:LocalRouter',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            icon_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            network_interface: Optional[pulumi.Input[pulumi.InputType['LocalRouterNetworkInterfaceArgs']]] = None,
            peers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LocalRouterPeerArgs']]]]] = None,
            secret_keys: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            static_routes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LocalRouterStaticRouteArgs']]]]] = None,
            switch: Optional[pulumi.Input[pulumi.InputType['LocalRouterSwitchArgs']]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'LocalRouter':
        """
        Get an existing LocalRouter resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the LocalRouter. The length of this value must be in the range [`1`-`512`].
        :param pulumi.Input[str] icon_id: The icon id to attach to the LoadBalancer.
        :param pulumi.Input[str] name: The name of the LocalRouter. The length of this value must be in the range [`1`-`64`].
        :param pulumi.Input[pulumi.InputType['LocalRouterNetworkInterfaceArgs']] network_interface: An `network_interface` block as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LocalRouterPeerArgs']]]] peers: One or more `peer` blocks as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] secret_keys: A list of secret key used for peering from other LocalRouters.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LocalRouterStaticRouteArgs']]]] static_routes: One or more `static_route` blocks as defined below.
        :param pulumi.Input[pulumi.InputType['LocalRouterSwitchArgs']] switch: A `switch` block as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Any tags to assign to the LoadBalancer.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _LocalRouterState.__new__(_LocalRouterState)

        __props__.__dict__["description"] = description
        __props__.__dict__["icon_id"] = icon_id
        __props__.__dict__["name"] = name
        __props__.__dict__["network_interface"] = network_interface
        __props__.__dict__["peers"] = peers
        __props__.__dict__["secret_keys"] = secret_keys
        __props__.__dict__["static_routes"] = static_routes
        __props__.__dict__["switch"] = switch
        __props__.__dict__["tags"] = tags
        return LocalRouter(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the LocalRouter. The length of this value must be in the range [`1`-`512`].
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="iconId")
    def icon_id(self) -> pulumi.Output[Optional[str]]:
        """
        The icon id to attach to the LoadBalancer.
        """
        return pulumi.get(self, "icon_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the LocalRouter. The length of this value must be in the range [`1`-`64`].
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkInterface")
    def network_interface(self) -> pulumi.Output['outputs.LocalRouterNetworkInterface']:
        """
        An `network_interface` block as defined below.
        """
        return pulumi.get(self, "network_interface")

    @property
    @pulumi.getter
    def peers(self) -> pulumi.Output[Optional[Sequence['outputs.LocalRouterPeer']]]:
        """
        One or more `peer` blocks as defined below.
        """
        return pulumi.get(self, "peers")

    @property
    @pulumi.getter(name="secretKeys")
    def secret_keys(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of secret key used for peering from other LocalRouters.
        """
        return pulumi.get(self, "secret_keys")

    @property
    @pulumi.getter(name="staticRoutes")
    def static_routes(self) -> pulumi.Output[Optional[Sequence['outputs.LocalRouterStaticRoute']]]:
        """
        One or more `static_route` blocks as defined below.
        """
        return pulumi.get(self, "static_routes")

    @property
    @pulumi.getter
    def switch(self) -> pulumi.Output['outputs.LocalRouterSwitch']:
        """
        A `switch` block as defined below.
        """
        return pulumi.get(self, "switch")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Any tags to assign to the LoadBalancer.
        """
        return pulumi.get(self, "tags")

