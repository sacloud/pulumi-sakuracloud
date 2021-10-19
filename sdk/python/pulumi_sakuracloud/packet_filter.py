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

__all__ = ['PacketFilterArgs', 'PacketFilter']

@pulumi.input_type
class PacketFilterArgs:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 expressions: Optional[pulumi.Input[Sequence[pulumi.Input['PacketFilterExpressionArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 zone: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a PacketFilter resource.
        :param pulumi.Input[str] description: The description of the expression.
        :param pulumi.Input[Sequence[pulumi.Input['PacketFilterExpressionArgs']]] expressions: One or more `expression` blocks as defined below.
        :param pulumi.Input[str] name: The name of the packetFilter. The length of this value must be in the range [`1`-`64`].
        :param pulumi.Input[str] zone: The name of zone that the packetFilter will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if expressions is not None:
            pulumi.set(__self__, "expressions", expressions)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if zone is not None:
            pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the expression.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def expressions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PacketFilterExpressionArgs']]]]:
        """
        One or more `expression` blocks as defined below.
        """
        return pulumi.get(self, "expressions")

    @expressions.setter
    def expressions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PacketFilterExpressionArgs']]]]):
        pulumi.set(self, "expressions", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the packetFilter. The length of this value must be in the range [`1`-`64`].
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[str]]:
        """
        The name of zone that the packetFilter will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "zone")

    @zone.setter
    def zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone", value)


@pulumi.input_type
class _PacketFilterState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 expressions: Optional[pulumi.Input[Sequence[pulumi.Input['PacketFilterExpressionArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 zone: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering PacketFilter resources.
        :param pulumi.Input[str] description: The description of the expression.
        :param pulumi.Input[Sequence[pulumi.Input['PacketFilterExpressionArgs']]] expressions: One or more `expression` blocks as defined below.
        :param pulumi.Input[str] name: The name of the packetFilter. The length of this value must be in the range [`1`-`64`].
        :param pulumi.Input[str] zone: The name of zone that the packetFilter will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if expressions is not None:
            pulumi.set(__self__, "expressions", expressions)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if zone is not None:
            pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the expression.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def expressions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PacketFilterExpressionArgs']]]]:
        """
        One or more `expression` blocks as defined below.
        """
        return pulumi.get(self, "expressions")

    @expressions.setter
    def expressions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PacketFilterExpressionArgs']]]]):
        pulumi.set(self, "expressions", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the packetFilter. The length of this value must be in the range [`1`-`64`].
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[str]]:
        """
        The name of zone that the packetFilter will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "zone")

    @zone.setter
    def zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone", value)


class PacketFilter(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 expressions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PacketFilterExpressionArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 zone: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a SakuraCloud Packet Filter.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sakuracloud as sakuracloud

        foobar = sakuracloud.PacketFilter("foobar",
            description="description",
            expressions=[
                sakuracloud.PacketFilterExpressionArgs(
                    destination_port="22",
                    protocol="tcp",
                ),
                sakuracloud.PacketFilterExpressionArgs(
                    destination_port="80",
                    protocol="tcp",
                ),
                sakuracloud.PacketFilterExpressionArgs(
                    destination_port="443",
                    protocol="tcp",
                ),
                sakuracloud.PacketFilterExpressionArgs(
                    protocol="icmp",
                ),
                sakuracloud.PacketFilterExpressionArgs(
                    protocol="fragment",
                ),
                sakuracloud.PacketFilterExpressionArgs(
                    protocol="udp",
                    source_port="123",
                ),
                sakuracloud.PacketFilterExpressionArgs(
                    destination_port="32768-61000",
                    protocol="tcp",
                ),
                sakuracloud.PacketFilterExpressionArgs(
                    destination_port="32768-61000",
                    protocol="udp",
                ),
                sakuracloud.PacketFilterExpressionArgs(
                    allow=False,
                    description="Deny ALL",
                    protocol="ip",
                ),
            ])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the expression.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PacketFilterExpressionArgs']]]] expressions: One or more `expression` blocks as defined below.
        :param pulumi.Input[str] name: The name of the packetFilter. The length of this value must be in the range [`1`-`64`].
        :param pulumi.Input[str] zone: The name of zone that the packetFilter will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[PacketFilterArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a SakuraCloud Packet Filter.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sakuracloud as sakuracloud

        foobar = sakuracloud.PacketFilter("foobar",
            description="description",
            expressions=[
                sakuracloud.PacketFilterExpressionArgs(
                    destination_port="22",
                    protocol="tcp",
                ),
                sakuracloud.PacketFilterExpressionArgs(
                    destination_port="80",
                    protocol="tcp",
                ),
                sakuracloud.PacketFilterExpressionArgs(
                    destination_port="443",
                    protocol="tcp",
                ),
                sakuracloud.PacketFilterExpressionArgs(
                    protocol="icmp",
                ),
                sakuracloud.PacketFilterExpressionArgs(
                    protocol="fragment",
                ),
                sakuracloud.PacketFilterExpressionArgs(
                    protocol="udp",
                    source_port="123",
                ),
                sakuracloud.PacketFilterExpressionArgs(
                    destination_port="32768-61000",
                    protocol="tcp",
                ),
                sakuracloud.PacketFilterExpressionArgs(
                    destination_port="32768-61000",
                    protocol="udp",
                ),
                sakuracloud.PacketFilterExpressionArgs(
                    allow=False,
                    description="Deny ALL",
                    protocol="ip",
                ),
            ])
        ```

        :param str resource_name: The name of the resource.
        :param PacketFilterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PacketFilterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 expressions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PacketFilterExpressionArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
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
            __props__ = PacketFilterArgs.__new__(PacketFilterArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["expressions"] = expressions
            __props__.__dict__["name"] = name
            __props__.__dict__["zone"] = zone
        super(PacketFilter, __self__).__init__(
            'sakuracloud:index/packetFilter:PacketFilter',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            expressions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PacketFilterExpressionArgs']]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            zone: Optional[pulumi.Input[str]] = None) -> 'PacketFilter':
        """
        Get an existing PacketFilter resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the expression.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PacketFilterExpressionArgs']]]] expressions: One or more `expression` blocks as defined below.
        :param pulumi.Input[str] name: The name of the packetFilter. The length of this value must be in the range [`1`-`64`].
        :param pulumi.Input[str] zone: The name of zone that the packetFilter will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _PacketFilterState.__new__(_PacketFilterState)

        __props__.__dict__["description"] = description
        __props__.__dict__["expressions"] = expressions
        __props__.__dict__["name"] = name
        __props__.__dict__["zone"] = zone
        return PacketFilter(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the expression.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def expressions(self) -> pulumi.Output[Sequence['outputs.PacketFilterExpression']]:
        """
        One or more `expression` blocks as defined below.
        """
        return pulumi.get(self, "expressions")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the packetFilter. The length of this value must be in the range [`1`-`64`].
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def zone(self) -> pulumi.Output[str]:
        """
        The name of zone that the packetFilter will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "zone")

