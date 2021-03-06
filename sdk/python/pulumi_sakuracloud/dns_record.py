# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = ['DNSRecord']


class DNSRecord(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dns_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 ttl: Optional[pulumi.Input[int]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 weight: Optional[pulumi.Input[int]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a SakuraCloud DNS Record.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sakuracloud as sakuracloud

        foobar = sakuracloud.DNS("foobar", zone="example.com")
        record1 = sakuracloud.DNSRecord("record1",
            dns_id=foobar.id,
            type="A",
            value="192.168.0.1")
        record2 = sakuracloud.DNSRecord("record2",
            dns_id=foobar.id,
            type="A",
            value="192.168.0.2")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] dns_id: The id of the DNS resource. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name of the DNS Record resource. Changing this forces a new resource to be created.
        :param pulumi.Input[int] port: The number of port. This must be in the range [`1`-`65535`]. Changing this forces a new resource to be created.
        :param pulumi.Input[int] priority: The priority of target DNS Record. This must be in the range [`0`-`65535`]. Changing this forces a new resource to be created.
        :param pulumi.Input[int] ttl: The number of the TTL. Changing this forces a new resource to be created. Default:`3600`.
        :param pulumi.Input[str] type: The type of DNS Record. This must be one of [`A`/`AAAA`/`ALIAS`/`CNAME`/`NS`/`MX`/`TXT`/`SRV`/`CAA`/`PTR`]. Changing this forces a new resource to be created.
        :param pulumi.Input[str] value: The value of the DNS Record. Changing this forces a new resource to be created.
        :param pulumi.Input[int] weight: The weight of target DNS Record. This must be in the range [`0`-`65535`]. Changing this forces a new resource to be created.
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

            if dns_id is None and not opts.urn:
                raise TypeError("Missing required property 'dns_id'")
            __props__['dns_id'] = dns_id
            __props__['name'] = name
            __props__['port'] = port
            __props__['priority'] = priority
            __props__['ttl'] = ttl
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__['type'] = type
            if value is None and not opts.urn:
                raise TypeError("Missing required property 'value'")
            __props__['value'] = value
            __props__['weight'] = weight
        super(DNSRecord, __self__).__init__(
            'sakuracloud:index/dNSRecord:DNSRecord',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            dns_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            port: Optional[pulumi.Input[int]] = None,
            priority: Optional[pulumi.Input[int]] = None,
            ttl: Optional[pulumi.Input[int]] = None,
            type: Optional[pulumi.Input[str]] = None,
            value: Optional[pulumi.Input[str]] = None,
            weight: Optional[pulumi.Input[int]] = None) -> 'DNSRecord':
        """
        Get an existing DNSRecord resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] dns_id: The id of the DNS resource. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name of the DNS Record resource. Changing this forces a new resource to be created.
        :param pulumi.Input[int] port: The number of port. This must be in the range [`1`-`65535`]. Changing this forces a new resource to be created.
        :param pulumi.Input[int] priority: The priority of target DNS Record. This must be in the range [`0`-`65535`]. Changing this forces a new resource to be created.
        :param pulumi.Input[int] ttl: The number of the TTL. Changing this forces a new resource to be created. Default:`3600`.
        :param pulumi.Input[str] type: The type of DNS Record. This must be one of [`A`/`AAAA`/`ALIAS`/`CNAME`/`NS`/`MX`/`TXT`/`SRV`/`CAA`/`PTR`]. Changing this forces a new resource to be created.
        :param pulumi.Input[str] value: The value of the DNS Record. Changing this forces a new resource to be created.
        :param pulumi.Input[int] weight: The weight of target DNS Record. This must be in the range [`0`-`65535`]. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["dns_id"] = dns_id
        __props__["name"] = name
        __props__["port"] = port
        __props__["priority"] = priority
        __props__["ttl"] = ttl
        __props__["type"] = type
        __props__["value"] = value
        __props__["weight"] = weight
        return DNSRecord(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dnsId")
    def dns_id(self) -> pulumi.Output[str]:
        """
        The id of the DNS resource. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "dns_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the DNS Record resource. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def port(self) -> pulumi.Output[Optional[int]]:
        """
        The number of port. This must be in the range [`1`-`65535`]. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[Optional[int]]:
        """
        The priority of target DNS Record. This must be in the range [`0`-`65535`]. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter
    def ttl(self) -> pulumi.Output[Optional[int]]:
        """
        The number of the TTL. Changing this forces a new resource to be created. Default:`3600`.
        """
        return pulumi.get(self, "ttl")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of DNS Record. This must be one of [`A`/`AAAA`/`ALIAS`/`CNAME`/`NS`/`MX`/`TXT`/`SRV`/`CAA`/`PTR`]. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def value(self) -> pulumi.Output[str]:
        """
        The value of the DNS Record. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "value")

    @property
    @pulumi.getter
    def weight(self) -> pulumi.Output[Optional[int]]:
        """
        The weight of target DNS Record. This must be in the range [`0`-`65535`]. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "weight")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

