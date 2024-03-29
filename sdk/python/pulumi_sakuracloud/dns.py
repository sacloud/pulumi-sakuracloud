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

__all__ = ['DNSArgs', 'DNS']

@pulumi.input_type
class DNSArgs:
    def __init__(__self__, *,
                 zone: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 icon_id: Optional[pulumi.Input[str]] = None,
                 records: Optional[pulumi.Input[Sequence[pulumi.Input['DNSRecordArgs']]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a DNS resource.
        :param pulumi.Input[str] zone: The target zone. (e.g. `example.com`). Changing this forces a new resource to be created.
        :param pulumi.Input[str] description: The description of the DNS. The length of this value must be in the range [`1`-`512`].
        :param pulumi.Input[str] icon_id: The icon id to attach to the DNS.
        :param pulumi.Input[Sequence[pulumi.Input['DNSRecordArgs']]] records: One or more `record` blocks as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Any tags to assign to the DNS.
        """
        pulumi.set(__self__, "zone", zone)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if icon_id is not None:
            pulumi.set(__self__, "icon_id", icon_id)
        if records is not None:
            pulumi.set(__self__, "records", records)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def zone(self) -> pulumi.Input[str]:
        """
        The target zone. (e.g. `example.com`). Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "zone")

    @zone.setter
    def zone(self, value: pulumi.Input[str]):
        pulumi.set(self, "zone", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the DNS. The length of this value must be in the range [`1`-`512`].
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="iconId")
    def icon_id(self) -> Optional[pulumi.Input[str]]:
        """
        The icon id to attach to the DNS.
        """
        return pulumi.get(self, "icon_id")

    @icon_id.setter
    def icon_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "icon_id", value)

    @property
    @pulumi.getter
    def records(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DNSRecordArgs']]]]:
        """
        One or more `record` blocks as defined below.
        """
        return pulumi.get(self, "records")

    @records.setter
    def records(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DNSRecordArgs']]]]):
        pulumi.set(self, "records", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Any tags to assign to the DNS.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _DNSState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 dns_servers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 icon_id: Optional[pulumi.Input[str]] = None,
                 records: Optional[pulumi.Input[Sequence[pulumi.Input['DNSRecordArgs']]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 zone: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering DNS resources.
        :param pulumi.Input[str] description: The description of the DNS. The length of this value must be in the range [`1`-`512`].
        :param pulumi.Input[Sequence[pulumi.Input[str]]] dns_servers: A list of IP address of DNS server that manage this zone.
        :param pulumi.Input[str] icon_id: The icon id to attach to the DNS.
        :param pulumi.Input[Sequence[pulumi.Input['DNSRecordArgs']]] records: One or more `record` blocks as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Any tags to assign to the DNS.
        :param pulumi.Input[str] zone: The target zone. (e.g. `example.com`). Changing this forces a new resource to be created.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if dns_servers is not None:
            pulumi.set(__self__, "dns_servers", dns_servers)
        if icon_id is not None:
            pulumi.set(__self__, "icon_id", icon_id)
        if records is not None:
            pulumi.set(__self__, "records", records)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if zone is not None:
            pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the DNS. The length of this value must be in the range [`1`-`512`].
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="dnsServers")
    def dns_servers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of IP address of DNS server that manage this zone.
        """
        return pulumi.get(self, "dns_servers")

    @dns_servers.setter
    def dns_servers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "dns_servers", value)

    @property
    @pulumi.getter(name="iconId")
    def icon_id(self) -> Optional[pulumi.Input[str]]:
        """
        The icon id to attach to the DNS.
        """
        return pulumi.get(self, "icon_id")

    @icon_id.setter
    def icon_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "icon_id", value)

    @property
    @pulumi.getter
    def records(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DNSRecordArgs']]]]:
        """
        One or more `record` blocks as defined below.
        """
        return pulumi.get(self, "records")

    @records.setter
    def records(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DNSRecordArgs']]]]):
        pulumi.set(self, "records", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Any tags to assign to the DNS.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[str]]:
        """
        The target zone. (e.g. `example.com`). Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "zone")

    @zone.setter
    def zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone", value)


class DNS(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 icon_id: Optional[pulumi.Input[str]] = None,
                 records: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DNSRecordArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 zone: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a SakuraCloud DNS.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sakuracloud as sakuracloud

        foobar = sakuracloud.DNS("foobar",
            description="description",
            records=[
                sakuracloud.DNSRecordArgs(
                    name="www",
                    type="A",
                    value="192.168.11.1",
                ),
                sakuracloud.DNSRecordArgs(
                    name="www",
                    type="A",
                    value="192.168.11.2",
                ),
            ],
            tags=[
                "tag1",
                "tag2",
            ],
            zone="example.com")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the DNS. The length of this value must be in the range [`1`-`512`].
        :param pulumi.Input[str] icon_id: The icon id to attach to the DNS.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DNSRecordArgs']]]] records: One or more `record` blocks as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Any tags to assign to the DNS.
        :param pulumi.Input[str] zone: The target zone. (e.g. `example.com`). Changing this forces a new resource to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DNSArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a SakuraCloud DNS.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sakuracloud as sakuracloud

        foobar = sakuracloud.DNS("foobar",
            description="description",
            records=[
                sakuracloud.DNSRecordArgs(
                    name="www",
                    type="A",
                    value="192.168.11.1",
                ),
                sakuracloud.DNSRecordArgs(
                    name="www",
                    type="A",
                    value="192.168.11.2",
                ),
            ],
            tags=[
                "tag1",
                "tag2",
            ],
            zone="example.com")
        ```

        :param str resource_name: The name of the resource.
        :param DNSArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DNSArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 icon_id: Optional[pulumi.Input[str]] = None,
                 records: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DNSRecordArgs']]]]] = None,
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
            __props__ = DNSArgs.__new__(DNSArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["icon_id"] = icon_id
            __props__.__dict__["records"] = records
            __props__.__dict__["tags"] = tags
            if zone is None and not opts.urn:
                raise TypeError("Missing required property 'zone'")
            __props__.__dict__["zone"] = zone
            __props__.__dict__["dns_servers"] = None
        super(DNS, __self__).__init__(
            'sakuracloud:index/dNS:DNS',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            dns_servers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            icon_id: Optional[pulumi.Input[str]] = None,
            records: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DNSRecordArgs']]]]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            zone: Optional[pulumi.Input[str]] = None) -> 'DNS':
        """
        Get an existing DNS resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the DNS. The length of this value must be in the range [`1`-`512`].
        :param pulumi.Input[Sequence[pulumi.Input[str]]] dns_servers: A list of IP address of DNS server that manage this zone.
        :param pulumi.Input[str] icon_id: The icon id to attach to the DNS.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DNSRecordArgs']]]] records: One or more `record` blocks as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Any tags to assign to the DNS.
        :param pulumi.Input[str] zone: The target zone. (e.g. `example.com`). Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DNSState.__new__(_DNSState)

        __props__.__dict__["description"] = description
        __props__.__dict__["dns_servers"] = dns_servers
        __props__.__dict__["icon_id"] = icon_id
        __props__.__dict__["records"] = records
        __props__.__dict__["tags"] = tags
        __props__.__dict__["zone"] = zone
        return DNS(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the DNS. The length of this value must be in the range [`1`-`512`].
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="dnsServers")
    def dns_servers(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of IP address of DNS server that manage this zone.
        """
        return pulumi.get(self, "dns_servers")

    @property
    @pulumi.getter(name="iconId")
    def icon_id(self) -> pulumi.Output[Optional[str]]:
        """
        The icon id to attach to the DNS.
        """
        return pulumi.get(self, "icon_id")

    @property
    @pulumi.getter
    def records(self) -> pulumi.Output[Sequence['outputs.DNSRecord']]:
        """
        One or more `record` blocks as defined below.
        """
        return pulumi.get(self, "records")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Any tags to assign to the DNS.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def zone(self) -> pulumi.Output[str]:
        """
        The target zone. (e.g. `example.com`). Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "zone")

