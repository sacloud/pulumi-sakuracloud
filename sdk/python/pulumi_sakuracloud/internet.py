# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['InternetArgs', 'Internet']

@pulumi.input_type
class InternetArgs:
    def __init__(__self__, *,
                 band_width: Optional[pulumi.Input[int]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enable_ipv6: Optional[pulumi.Input[bool]] = None,
                 icon_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 netmask: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 zone: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Internet resource.
        :param pulumi.Input[int] band_width: The bandwidth of the network connected to the Internet in Mbps. This must be one of [`100`/`250`/`500`/`1000`/`1500`/`2000`/`2500`/`3000`/`3500`/`4000`/`4500`/`5000`]. 
               If zone is `tk1b`, the following values can also be specified [`5500`/`6000`/`6500`/`7000`/`7500`/`8000`/`8500`/`9000`/`9500`/`10000`]. Default:`100`.
        :param pulumi.Input[str] description: The description of the Switch+Router. The length of this value must be in the range [`1`-`512`].
        :param pulumi.Input[bool] enable_ipv6: The flag to enable IPv6.
        :param pulumi.Input[str] icon_id: The icon id to attach to the Switch+Router.
        :param pulumi.Input[str] name: The name of the Switch+Router. The length of this value must be in the range [`1`-`64`].
        :param pulumi.Input[int] netmask: The bit length of the subnet assigned to the Switch+Router. `26`/`27`/`28`. Changing this forces a new resource to be created. Default:`28`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Any tags to assign to the Switch+Router.
        :param pulumi.Input[str] zone: The name of zone that the Switch+Router will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        """
        if band_width is not None:
            pulumi.set(__self__, "band_width", band_width)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if enable_ipv6 is not None:
            pulumi.set(__self__, "enable_ipv6", enable_ipv6)
        if icon_id is not None:
            pulumi.set(__self__, "icon_id", icon_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if netmask is not None:
            pulumi.set(__self__, "netmask", netmask)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if zone is not None:
            pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter(name="bandWidth")
    def band_width(self) -> Optional[pulumi.Input[int]]:
        """
        The bandwidth of the network connected to the Internet in Mbps. This must be one of [`100`/`250`/`500`/`1000`/`1500`/`2000`/`2500`/`3000`/`3500`/`4000`/`4500`/`5000`]. 
        If zone is `tk1b`, the following values can also be specified [`5500`/`6000`/`6500`/`7000`/`7500`/`8000`/`8500`/`9000`/`9500`/`10000`]. Default:`100`.
        """
        return pulumi.get(self, "band_width")

    @band_width.setter
    def band_width(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "band_width", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the Switch+Router. The length of this value must be in the range [`1`-`512`].
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="enableIpv6")
    def enable_ipv6(self) -> Optional[pulumi.Input[bool]]:
        """
        The flag to enable IPv6.
        """
        return pulumi.get(self, "enable_ipv6")

    @enable_ipv6.setter
    def enable_ipv6(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_ipv6", value)

    @property
    @pulumi.getter(name="iconId")
    def icon_id(self) -> Optional[pulumi.Input[str]]:
        """
        The icon id to attach to the Switch+Router.
        """
        return pulumi.get(self, "icon_id")

    @icon_id.setter
    def icon_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "icon_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Switch+Router. The length of this value must be in the range [`1`-`64`].
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def netmask(self) -> Optional[pulumi.Input[int]]:
        """
        The bit length of the subnet assigned to the Switch+Router. `26`/`27`/`28`. Changing this forces a new resource to be created. Default:`28`.
        """
        return pulumi.get(self, "netmask")

    @netmask.setter
    def netmask(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "netmask", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Any tags to assign to the Switch+Router.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[str]]:
        """
        The name of zone that the Switch+Router will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "zone")

    @zone.setter
    def zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone", value)


@pulumi.input_type
class _InternetState:
    def __init__(__self__, *,
                 band_width: Optional[pulumi.Input[int]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enable_ipv6: Optional[pulumi.Input[bool]] = None,
                 gateway: Optional[pulumi.Input[str]] = None,
                 icon_id: Optional[pulumi.Input[str]] = None,
                 ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 ipv6_network_address: Optional[pulumi.Input[str]] = None,
                 ipv6_prefix: Optional[pulumi.Input[str]] = None,
                 ipv6_prefix_len: Optional[pulumi.Input[int]] = None,
                 max_ip_address: Optional[pulumi.Input[str]] = None,
                 min_ip_address: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 netmask: Optional[pulumi.Input[int]] = None,
                 network_address: Optional[pulumi.Input[str]] = None,
                 server_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 switch_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 zone: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Internet resources.
        :param pulumi.Input[int] band_width: The bandwidth of the network connected to the Internet in Mbps. This must be one of [`100`/`250`/`500`/`1000`/`1500`/`2000`/`2500`/`3000`/`3500`/`4000`/`4500`/`5000`]. 
               If zone is `tk1b`, the following values can also be specified [`5500`/`6000`/`6500`/`7000`/`7500`/`8000`/`8500`/`9000`/`9500`/`10000`]. Default:`100`.
        :param pulumi.Input[str] description: The description of the Switch+Router. The length of this value must be in the range [`1`-`512`].
        :param pulumi.Input[bool] enable_ipv6: The flag to enable IPv6.
        :param pulumi.Input[str] gateway: The IP address of the gateway used by the Switch+Router.
        :param pulumi.Input[str] icon_id: The icon id to attach to the Switch+Router.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ip_addresses: A list of assigned global address to the Switch+Router.
        :param pulumi.Input[str] ipv6_network_address: The IPv6 network address assigned to the Switch+Router.
        :param pulumi.Input[str] ipv6_prefix: The network prefix of assigned IPv6 addresses to the Switch+Router.
        :param pulumi.Input[int] ipv6_prefix_len: The bit length of IPv6 network prefix.
        :param pulumi.Input[str] max_ip_address: Maximum IP address in assigned global addresses to the Switch+Router.
        :param pulumi.Input[str] min_ip_address: Minimum IP address in assigned global addresses to the Switch+Router.
        :param pulumi.Input[str] name: The name of the Switch+Router. The length of this value must be in the range [`1`-`64`].
        :param pulumi.Input[int] netmask: The bit length of the subnet assigned to the Switch+Router. `26`/`27`/`28`. Changing this forces a new resource to be created. Default:`28`.
        :param pulumi.Input[str] network_address: The IPv4 network address assigned to the Switch+Router.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] server_ids: A list of the ID of Servers connected to the Switch+Router.
        :param pulumi.Input[str] switch_id: The id of the switch.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Any tags to assign to the Switch+Router.
        :param pulumi.Input[str] zone: The name of zone that the Switch+Router will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        """
        if band_width is not None:
            pulumi.set(__self__, "band_width", band_width)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if enable_ipv6 is not None:
            pulumi.set(__self__, "enable_ipv6", enable_ipv6)
        if gateway is not None:
            pulumi.set(__self__, "gateway", gateway)
        if icon_id is not None:
            pulumi.set(__self__, "icon_id", icon_id)
        if ip_addresses is not None:
            pulumi.set(__self__, "ip_addresses", ip_addresses)
        if ipv6_network_address is not None:
            pulumi.set(__self__, "ipv6_network_address", ipv6_network_address)
        if ipv6_prefix is not None:
            pulumi.set(__self__, "ipv6_prefix", ipv6_prefix)
        if ipv6_prefix_len is not None:
            pulumi.set(__self__, "ipv6_prefix_len", ipv6_prefix_len)
        if max_ip_address is not None:
            pulumi.set(__self__, "max_ip_address", max_ip_address)
        if min_ip_address is not None:
            pulumi.set(__self__, "min_ip_address", min_ip_address)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if netmask is not None:
            pulumi.set(__self__, "netmask", netmask)
        if network_address is not None:
            pulumi.set(__self__, "network_address", network_address)
        if server_ids is not None:
            pulumi.set(__self__, "server_ids", server_ids)
        if switch_id is not None:
            pulumi.set(__self__, "switch_id", switch_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if zone is not None:
            pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter(name="bandWidth")
    def band_width(self) -> Optional[pulumi.Input[int]]:
        """
        The bandwidth of the network connected to the Internet in Mbps. This must be one of [`100`/`250`/`500`/`1000`/`1500`/`2000`/`2500`/`3000`/`3500`/`4000`/`4500`/`5000`]. 
        If zone is `tk1b`, the following values can also be specified [`5500`/`6000`/`6500`/`7000`/`7500`/`8000`/`8500`/`9000`/`9500`/`10000`]. Default:`100`.
        """
        return pulumi.get(self, "band_width")

    @band_width.setter
    def band_width(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "band_width", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the Switch+Router. The length of this value must be in the range [`1`-`512`].
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="enableIpv6")
    def enable_ipv6(self) -> Optional[pulumi.Input[bool]]:
        """
        The flag to enable IPv6.
        """
        return pulumi.get(self, "enable_ipv6")

    @enable_ipv6.setter
    def enable_ipv6(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_ipv6", value)

    @property
    @pulumi.getter
    def gateway(self) -> Optional[pulumi.Input[str]]:
        """
        The IP address of the gateway used by the Switch+Router.
        """
        return pulumi.get(self, "gateway")

    @gateway.setter
    def gateway(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "gateway", value)

    @property
    @pulumi.getter(name="iconId")
    def icon_id(self) -> Optional[pulumi.Input[str]]:
        """
        The icon id to attach to the Switch+Router.
        """
        return pulumi.get(self, "icon_id")

    @icon_id.setter
    def icon_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "icon_id", value)

    @property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of assigned global address to the Switch+Router.
        """
        return pulumi.get(self, "ip_addresses")

    @ip_addresses.setter
    def ip_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "ip_addresses", value)

    @property
    @pulumi.getter(name="ipv6NetworkAddress")
    def ipv6_network_address(self) -> Optional[pulumi.Input[str]]:
        """
        The IPv6 network address assigned to the Switch+Router.
        """
        return pulumi.get(self, "ipv6_network_address")

    @ipv6_network_address.setter
    def ipv6_network_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ipv6_network_address", value)

    @property
    @pulumi.getter(name="ipv6Prefix")
    def ipv6_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        The network prefix of assigned IPv6 addresses to the Switch+Router.
        """
        return pulumi.get(self, "ipv6_prefix")

    @ipv6_prefix.setter
    def ipv6_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ipv6_prefix", value)

    @property
    @pulumi.getter(name="ipv6PrefixLen")
    def ipv6_prefix_len(self) -> Optional[pulumi.Input[int]]:
        """
        The bit length of IPv6 network prefix.
        """
        return pulumi.get(self, "ipv6_prefix_len")

    @ipv6_prefix_len.setter
    def ipv6_prefix_len(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "ipv6_prefix_len", value)

    @property
    @pulumi.getter(name="maxIpAddress")
    def max_ip_address(self) -> Optional[pulumi.Input[str]]:
        """
        Maximum IP address in assigned global addresses to the Switch+Router.
        """
        return pulumi.get(self, "max_ip_address")

    @max_ip_address.setter
    def max_ip_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "max_ip_address", value)

    @property
    @pulumi.getter(name="minIpAddress")
    def min_ip_address(self) -> Optional[pulumi.Input[str]]:
        """
        Minimum IP address in assigned global addresses to the Switch+Router.
        """
        return pulumi.get(self, "min_ip_address")

    @min_ip_address.setter
    def min_ip_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "min_ip_address", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Switch+Router. The length of this value must be in the range [`1`-`64`].
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def netmask(self) -> Optional[pulumi.Input[int]]:
        """
        The bit length of the subnet assigned to the Switch+Router. `26`/`27`/`28`. Changing this forces a new resource to be created. Default:`28`.
        """
        return pulumi.get(self, "netmask")

    @netmask.setter
    def netmask(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "netmask", value)

    @property
    @pulumi.getter(name="networkAddress")
    def network_address(self) -> Optional[pulumi.Input[str]]:
        """
        The IPv4 network address assigned to the Switch+Router.
        """
        return pulumi.get(self, "network_address")

    @network_address.setter
    def network_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_address", value)

    @property
    @pulumi.getter(name="serverIds")
    def server_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of the ID of Servers connected to the Switch+Router.
        """
        return pulumi.get(self, "server_ids")

    @server_ids.setter
    def server_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "server_ids", value)

    @property
    @pulumi.getter(name="switchId")
    def switch_id(self) -> Optional[pulumi.Input[str]]:
        """
        The id of the switch.
        """
        return pulumi.get(self, "switch_id")

    @switch_id.setter
    def switch_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "switch_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Any tags to assign to the Switch+Router.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[str]]:
        """
        The name of zone that the Switch+Router will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "zone")

    @zone.setter
    def zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone", value)


class Internet(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 band_width: Optional[pulumi.Input[int]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enable_ipv6: Optional[pulumi.Input[bool]] = None,
                 icon_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 netmask: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 zone: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a SakuraCloud Switch+Router.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sakuracloud as sakuracloud

        foobar = sakuracloud.Internet("foobar",
            band_width=100,
            description="description",
            enable_ipv6=False,
            netmask=28,
            tags=[
                "tag1",
                "tag2",
            ])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] band_width: The bandwidth of the network connected to the Internet in Mbps. This must be one of [`100`/`250`/`500`/`1000`/`1500`/`2000`/`2500`/`3000`/`3500`/`4000`/`4500`/`5000`]. 
               If zone is `tk1b`, the following values can also be specified [`5500`/`6000`/`6500`/`7000`/`7500`/`8000`/`8500`/`9000`/`9500`/`10000`]. Default:`100`.
        :param pulumi.Input[str] description: The description of the Switch+Router. The length of this value must be in the range [`1`-`512`].
        :param pulumi.Input[bool] enable_ipv6: The flag to enable IPv6.
        :param pulumi.Input[str] icon_id: The icon id to attach to the Switch+Router.
        :param pulumi.Input[str] name: The name of the Switch+Router. The length of this value must be in the range [`1`-`64`].
        :param pulumi.Input[int] netmask: The bit length of the subnet assigned to the Switch+Router. `26`/`27`/`28`. Changing this forces a new resource to be created. Default:`28`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Any tags to assign to the Switch+Router.
        :param pulumi.Input[str] zone: The name of zone that the Switch+Router will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[InternetArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a SakuraCloud Switch+Router.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sakuracloud as sakuracloud

        foobar = sakuracloud.Internet("foobar",
            band_width=100,
            description="description",
            enable_ipv6=False,
            netmask=28,
            tags=[
                "tag1",
                "tag2",
            ])
        ```

        :param str resource_name: The name of the resource.
        :param InternetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InternetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 band_width: Optional[pulumi.Input[int]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enable_ipv6: Optional[pulumi.Input[bool]] = None,
                 icon_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 netmask: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 zone: Optional[pulumi.Input[str]] = None,
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
            __props__ = InternetArgs.__new__(InternetArgs)

            __props__.__dict__["band_width"] = band_width
            __props__.__dict__["description"] = description
            __props__.__dict__["enable_ipv6"] = enable_ipv6
            __props__.__dict__["icon_id"] = icon_id
            __props__.__dict__["name"] = name
            __props__.__dict__["netmask"] = netmask
            __props__.__dict__["tags"] = tags
            __props__.__dict__["zone"] = zone
            __props__.__dict__["gateway"] = None
            __props__.__dict__["ip_addresses"] = None
            __props__.__dict__["ipv6_network_address"] = None
            __props__.__dict__["ipv6_prefix"] = None
            __props__.__dict__["ipv6_prefix_len"] = None
            __props__.__dict__["max_ip_address"] = None
            __props__.__dict__["min_ip_address"] = None
            __props__.__dict__["network_address"] = None
            __props__.__dict__["server_ids"] = None
            __props__.__dict__["switch_id"] = None
        super(Internet, __self__).__init__(
            'sakuracloud:index/internet:Internet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            band_width: Optional[pulumi.Input[int]] = None,
            description: Optional[pulumi.Input[str]] = None,
            enable_ipv6: Optional[pulumi.Input[bool]] = None,
            gateway: Optional[pulumi.Input[str]] = None,
            icon_id: Optional[pulumi.Input[str]] = None,
            ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            ipv6_network_address: Optional[pulumi.Input[str]] = None,
            ipv6_prefix: Optional[pulumi.Input[str]] = None,
            ipv6_prefix_len: Optional[pulumi.Input[int]] = None,
            max_ip_address: Optional[pulumi.Input[str]] = None,
            min_ip_address: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            netmask: Optional[pulumi.Input[int]] = None,
            network_address: Optional[pulumi.Input[str]] = None,
            server_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            switch_id: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            zone: Optional[pulumi.Input[str]] = None) -> 'Internet':
        """
        Get an existing Internet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] band_width: The bandwidth of the network connected to the Internet in Mbps. This must be one of [`100`/`250`/`500`/`1000`/`1500`/`2000`/`2500`/`3000`/`3500`/`4000`/`4500`/`5000`]. 
               If zone is `tk1b`, the following values can also be specified [`5500`/`6000`/`6500`/`7000`/`7500`/`8000`/`8500`/`9000`/`9500`/`10000`]. Default:`100`.
        :param pulumi.Input[str] description: The description of the Switch+Router. The length of this value must be in the range [`1`-`512`].
        :param pulumi.Input[bool] enable_ipv6: The flag to enable IPv6.
        :param pulumi.Input[str] gateway: The IP address of the gateway used by the Switch+Router.
        :param pulumi.Input[str] icon_id: The icon id to attach to the Switch+Router.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ip_addresses: A list of assigned global address to the Switch+Router.
        :param pulumi.Input[str] ipv6_network_address: The IPv6 network address assigned to the Switch+Router.
        :param pulumi.Input[str] ipv6_prefix: The network prefix of assigned IPv6 addresses to the Switch+Router.
        :param pulumi.Input[int] ipv6_prefix_len: The bit length of IPv6 network prefix.
        :param pulumi.Input[str] max_ip_address: Maximum IP address in assigned global addresses to the Switch+Router.
        :param pulumi.Input[str] min_ip_address: Minimum IP address in assigned global addresses to the Switch+Router.
        :param pulumi.Input[str] name: The name of the Switch+Router. The length of this value must be in the range [`1`-`64`].
        :param pulumi.Input[int] netmask: The bit length of the subnet assigned to the Switch+Router. `26`/`27`/`28`. Changing this forces a new resource to be created. Default:`28`.
        :param pulumi.Input[str] network_address: The IPv4 network address assigned to the Switch+Router.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] server_ids: A list of the ID of Servers connected to the Switch+Router.
        :param pulumi.Input[str] switch_id: The id of the switch.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Any tags to assign to the Switch+Router.
        :param pulumi.Input[str] zone: The name of zone that the Switch+Router will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _InternetState.__new__(_InternetState)

        __props__.__dict__["band_width"] = band_width
        __props__.__dict__["description"] = description
        __props__.__dict__["enable_ipv6"] = enable_ipv6
        __props__.__dict__["gateway"] = gateway
        __props__.__dict__["icon_id"] = icon_id
        __props__.__dict__["ip_addresses"] = ip_addresses
        __props__.__dict__["ipv6_network_address"] = ipv6_network_address
        __props__.__dict__["ipv6_prefix"] = ipv6_prefix
        __props__.__dict__["ipv6_prefix_len"] = ipv6_prefix_len
        __props__.__dict__["max_ip_address"] = max_ip_address
        __props__.__dict__["min_ip_address"] = min_ip_address
        __props__.__dict__["name"] = name
        __props__.__dict__["netmask"] = netmask
        __props__.__dict__["network_address"] = network_address
        __props__.__dict__["server_ids"] = server_ids
        __props__.__dict__["switch_id"] = switch_id
        __props__.__dict__["tags"] = tags
        __props__.__dict__["zone"] = zone
        return Internet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="bandWidth")
    def band_width(self) -> pulumi.Output[Optional[int]]:
        """
        The bandwidth of the network connected to the Internet in Mbps. This must be one of [`100`/`250`/`500`/`1000`/`1500`/`2000`/`2500`/`3000`/`3500`/`4000`/`4500`/`5000`]. 
        If zone is `tk1b`, the following values can also be specified [`5500`/`6000`/`6500`/`7000`/`7500`/`8000`/`8500`/`9000`/`9500`/`10000`]. Default:`100`.
        """
        return pulumi.get(self, "band_width")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the Switch+Router. The length of this value must be in the range [`1`-`512`].
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="enableIpv6")
    def enable_ipv6(self) -> pulumi.Output[Optional[bool]]:
        """
        The flag to enable IPv6.
        """
        return pulumi.get(self, "enable_ipv6")

    @property
    @pulumi.getter
    def gateway(self) -> pulumi.Output[str]:
        """
        The IP address of the gateway used by the Switch+Router.
        """
        return pulumi.get(self, "gateway")

    @property
    @pulumi.getter(name="iconId")
    def icon_id(self) -> pulumi.Output[Optional[str]]:
        """
        The icon id to attach to the Switch+Router.
        """
        return pulumi.get(self, "icon_id")

    @property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of assigned global address to the Switch+Router.
        """
        return pulumi.get(self, "ip_addresses")

    @property
    @pulumi.getter(name="ipv6NetworkAddress")
    def ipv6_network_address(self) -> pulumi.Output[str]:
        """
        The IPv6 network address assigned to the Switch+Router.
        """
        return pulumi.get(self, "ipv6_network_address")

    @property
    @pulumi.getter(name="ipv6Prefix")
    def ipv6_prefix(self) -> pulumi.Output[str]:
        """
        The network prefix of assigned IPv6 addresses to the Switch+Router.
        """
        return pulumi.get(self, "ipv6_prefix")

    @property
    @pulumi.getter(name="ipv6PrefixLen")
    def ipv6_prefix_len(self) -> pulumi.Output[int]:
        """
        The bit length of IPv6 network prefix.
        """
        return pulumi.get(self, "ipv6_prefix_len")

    @property
    @pulumi.getter(name="maxIpAddress")
    def max_ip_address(self) -> pulumi.Output[str]:
        """
        Maximum IP address in assigned global addresses to the Switch+Router.
        """
        return pulumi.get(self, "max_ip_address")

    @property
    @pulumi.getter(name="minIpAddress")
    def min_ip_address(self) -> pulumi.Output[str]:
        """
        Minimum IP address in assigned global addresses to the Switch+Router.
        """
        return pulumi.get(self, "min_ip_address")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Switch+Router. The length of this value must be in the range [`1`-`64`].
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def netmask(self) -> pulumi.Output[Optional[int]]:
        """
        The bit length of the subnet assigned to the Switch+Router. `26`/`27`/`28`. Changing this forces a new resource to be created. Default:`28`.
        """
        return pulumi.get(self, "netmask")

    @property
    @pulumi.getter(name="networkAddress")
    def network_address(self) -> pulumi.Output[str]:
        """
        The IPv4 network address assigned to the Switch+Router.
        """
        return pulumi.get(self, "network_address")

    @property
    @pulumi.getter(name="serverIds")
    def server_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of the ID of Servers connected to the Switch+Router.
        """
        return pulumi.get(self, "server_ids")

    @property
    @pulumi.getter(name="switchId")
    def switch_id(self) -> pulumi.Output[str]:
        """
        The id of the switch.
        """
        return pulumi.get(self, "switch_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Any tags to assign to the Switch+Router.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def zone(self) -> pulumi.Output[str]:
        """
        The name of zone that the Switch+Router will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "zone")

