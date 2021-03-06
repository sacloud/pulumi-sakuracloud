# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = ['Subnet']


class Subnet(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 internet_id: Optional[pulumi.Input[str]] = None,
                 netmask: Optional[pulumi.Input[int]] = None,
                 next_hop: Optional[pulumi.Input[str]] = None,
                 zone: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a SakuraCloud Subnet.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sakuracloud as sakuracloud

        foobar_internet = sakuracloud.Internet("foobarInternet")
        foobar_subnet = sakuracloud.Subnet("foobarSubnet",
            internet_id=foobar_internet.id,
            next_hop=foobar_internet.min_ip_address)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] internet_id: The id of the switch+router resource that the subnet belongs. Changing this forces a new resource to be created.
        :param pulumi.Input[int] netmask: The bit length of the subnet to assign to the Subnet. This must be in the range [`26`-`28`]. Changing this forces a new resource to be created. Default:`28`.
        :param pulumi.Input[str] next_hop: The ip address of the next-hop at the subnet.
        :param pulumi.Input[str] zone: The name of zone that the Subnet will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            if internet_id is None and not opts.urn:
                raise TypeError("Missing required property 'internet_id'")
            __props__['internet_id'] = internet_id
            __props__['netmask'] = netmask
            if next_hop is None and not opts.urn:
                raise TypeError("Missing required property 'next_hop'")
            __props__['next_hop'] = next_hop
            __props__['zone'] = zone
            __props__['ip_addresses'] = None
            __props__['max_ip_address'] = None
            __props__['min_ip_address'] = None
            __props__['network_address'] = None
            __props__['switch_id'] = None
        super(Subnet, __self__).__init__(
            'sakuracloud:index/subnet:Subnet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            internet_id: Optional[pulumi.Input[str]] = None,
            ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            max_ip_address: Optional[pulumi.Input[str]] = None,
            min_ip_address: Optional[pulumi.Input[str]] = None,
            netmask: Optional[pulumi.Input[int]] = None,
            network_address: Optional[pulumi.Input[str]] = None,
            next_hop: Optional[pulumi.Input[str]] = None,
            switch_id: Optional[pulumi.Input[str]] = None,
            zone: Optional[pulumi.Input[str]] = None) -> 'Subnet':
        """
        Get an existing Subnet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] internet_id: The id of the switch+router resource that the subnet belongs. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ip_addresses: A list of assigned global address to the subnet.
        :param pulumi.Input[str] max_ip_address: Maximum IP address in assigned global addresses to the subnet.
        :param pulumi.Input[str] min_ip_address: Minimum IP address in assigned global addresses to the subnet.
        :param pulumi.Input[int] netmask: The bit length of the subnet to assign to the Subnet. This must be in the range [`26`-`28`]. Changing this forces a new resource to be created. Default:`28`.
        :param pulumi.Input[str] network_address: The IPv4 network address assigned to the Subnet.
        :param pulumi.Input[str] next_hop: The ip address of the next-hop at the subnet.
        :param pulumi.Input[str] switch_id: The id of the switch connected from the Subnet.
        :param pulumi.Input[str] zone: The name of zone that the Subnet will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["internet_id"] = internet_id
        __props__["ip_addresses"] = ip_addresses
        __props__["max_ip_address"] = max_ip_address
        __props__["min_ip_address"] = min_ip_address
        __props__["netmask"] = netmask
        __props__["network_address"] = network_address
        __props__["next_hop"] = next_hop
        __props__["switch_id"] = switch_id
        __props__["zone"] = zone
        return Subnet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="internetId")
    def internet_id(self) -> pulumi.Output[str]:
        """
        The id of the switch+router resource that the subnet belongs. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "internet_id")

    @property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of assigned global address to the subnet.
        """
        return pulumi.get(self, "ip_addresses")

    @property
    @pulumi.getter(name="maxIpAddress")
    def max_ip_address(self) -> pulumi.Output[str]:
        """
        Maximum IP address in assigned global addresses to the subnet.
        """
        return pulumi.get(self, "max_ip_address")

    @property
    @pulumi.getter(name="minIpAddress")
    def min_ip_address(self) -> pulumi.Output[str]:
        """
        Minimum IP address in assigned global addresses to the subnet.
        """
        return pulumi.get(self, "min_ip_address")

    @property
    @pulumi.getter
    def netmask(self) -> pulumi.Output[Optional[int]]:
        """
        The bit length of the subnet to assign to the Subnet. This must be in the range [`26`-`28`]. Changing this forces a new resource to be created. Default:`28`.
        """
        return pulumi.get(self, "netmask")

    @property
    @pulumi.getter(name="networkAddress")
    def network_address(self) -> pulumi.Output[str]:
        """
        The IPv4 network address assigned to the Subnet.
        """
        return pulumi.get(self, "network_address")

    @property
    @pulumi.getter(name="nextHop")
    def next_hop(self) -> pulumi.Output[str]:
        """
        The ip address of the next-hop at the subnet.
        """
        return pulumi.get(self, "next_hop")

    @property
    @pulumi.getter(name="switchId")
    def switch_id(self) -> pulumi.Output[str]:
        """
        The id of the switch connected from the Subnet.
        """
        return pulumi.get(self, "switch_id")

    @property
    @pulumi.getter
    def zone(self) -> pulumi.Output[str]:
        """
        The name of zone that the Subnet will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "zone")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

