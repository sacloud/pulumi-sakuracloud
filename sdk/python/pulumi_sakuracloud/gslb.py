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

__all__ = ['GSLB']


class GSLB(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 health_check: Optional[pulumi.Input[pulumi.InputType['GSLBHealthCheckArgs']]] = None,
                 icon_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 servers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GSLBServerArgs']]]]] = None,
                 sorry_server: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 weighted: Optional[pulumi.Input[bool]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a SakuraCloud GSLB.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sakuracloud as sakuracloud

        foobar = sakuracloud.GSLB("foobar",
            description="description",
            health_check=sakuracloud.GSLBHealthCheckArgs(
                delay_loop=10,
                host_header="example.com",
                path="/",
                protocol="http",
                status="200",
            ),
            servers=[
                sakuracloud.GSLBServerArgs(
                    enabled=True,
                    ip_address="192.2.0.11",
                    weight=1,
                ),
                sakuracloud.GSLBServerArgs(
                    enabled=True,
                    ip_address="192.2.0.12",
                    weight=1,
                ),
            ],
            sorry_server="192.2.0.1",
            tags=[
                "tag1",
                "tag2",
            ])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the GSLB. The length of this value must be in the range [`1`-`512`].
        :param pulumi.Input[pulumi.InputType['GSLBHealthCheckArgs']] health_check: A `health_check` block as defined below.
        :param pulumi.Input[str] icon_id: The icon id to attach to the GSLB.
        :param pulumi.Input[str] name: The name of the GSLB. The length of this value must be in the range [`1`-`64`].
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GSLBServerArgs']]]] servers: One or more `server` blocks as defined below.
        :param pulumi.Input[str] sorry_server: The IP address of the SorryServer. This will be used when all servers are down.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Any tags to assign to the GSLB.
        :param pulumi.Input[bool] weighted: The flag to enable weighted load-balancing.
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

            __props__['description'] = description
            if health_check is None and not opts.urn:
                raise TypeError("Missing required property 'health_check'")
            __props__['health_check'] = health_check
            __props__['icon_id'] = icon_id
            __props__['name'] = name
            __props__['servers'] = servers
            __props__['sorry_server'] = sorry_server
            __props__['tags'] = tags
            __props__['weighted'] = weighted
            __props__['fqdn'] = None
        super(GSLB, __self__).__init__(
            'sakuracloud:index/gSLB:GSLB',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            fqdn: Optional[pulumi.Input[str]] = None,
            health_check: Optional[pulumi.Input[pulumi.InputType['GSLBHealthCheckArgs']]] = None,
            icon_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            servers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GSLBServerArgs']]]]] = None,
            sorry_server: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            weighted: Optional[pulumi.Input[bool]] = None) -> 'GSLB':
        """
        Get an existing GSLB resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the GSLB. The length of this value must be in the range [`1`-`512`].
        :param pulumi.Input[str] fqdn: The FQDN for accessing to the GSLB. This is typically used as value of CNAME record.
        :param pulumi.Input[pulumi.InputType['GSLBHealthCheckArgs']] health_check: A `health_check` block as defined below.
        :param pulumi.Input[str] icon_id: The icon id to attach to the GSLB.
        :param pulumi.Input[str] name: The name of the GSLB. The length of this value must be in the range [`1`-`64`].
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GSLBServerArgs']]]] servers: One or more `server` blocks as defined below.
        :param pulumi.Input[str] sorry_server: The IP address of the SorryServer. This will be used when all servers are down.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Any tags to assign to the GSLB.
        :param pulumi.Input[bool] weighted: The flag to enable weighted load-balancing.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["description"] = description
        __props__["fqdn"] = fqdn
        __props__["health_check"] = health_check
        __props__["icon_id"] = icon_id
        __props__["name"] = name
        __props__["servers"] = servers
        __props__["sorry_server"] = sorry_server
        __props__["tags"] = tags
        __props__["weighted"] = weighted
        return GSLB(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the GSLB. The length of this value must be in the range [`1`-`512`].
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def fqdn(self) -> pulumi.Output[str]:
        """
        The FQDN for accessing to the GSLB. This is typically used as value of CNAME record.
        """
        return pulumi.get(self, "fqdn")

    @property
    @pulumi.getter(name="healthCheck")
    def health_check(self) -> pulumi.Output['outputs.GSLBHealthCheck']:
        """
        A `health_check` block as defined below.
        """
        return pulumi.get(self, "health_check")

    @property
    @pulumi.getter(name="iconId")
    def icon_id(self) -> pulumi.Output[Optional[str]]:
        """
        The icon id to attach to the GSLB.
        """
        return pulumi.get(self, "icon_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the GSLB. The length of this value must be in the range [`1`-`64`].
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def servers(self) -> pulumi.Output[Optional[Sequence['outputs.GSLBServer']]]:
        """
        One or more `server` blocks as defined below.
        """
        return pulumi.get(self, "servers")

    @property
    @pulumi.getter(name="sorryServer")
    def sorry_server(self) -> pulumi.Output[Optional[str]]:
        """
        The IP address of the SorryServer. This will be used when all servers are down.
        """
        return pulumi.get(self, "sorry_server")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Any tags to assign to the GSLB.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def weighted(self) -> pulumi.Output[Optional[bool]]:
        """
        The flag to enable weighted load-balancing.
        """
        return pulumi.get(self, "weighted")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

