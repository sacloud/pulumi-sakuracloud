# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class MobileGateway(pulumi.CustomResource):
    description: pulumi.Output[str]
    """
    The description of the MobileGateway. The length of this value must be in the range [`1`-`512`]
    """
    dns_servers: pulumi.Output[list]
    """
    A list of IP address used by each connected devices
    """
    icon_id: pulumi.Output[str]
    """
    The icon id to attach to the MobileGateway
    """
    inter_device_communication: pulumi.Output[bool]
    """
    The flag to allow communication between each connected devices
    """
    internet_connection: pulumi.Output[bool]
    """
    The flag to enable connect to the Internet
    """
    name: pulumi.Output[str]
    """
    The name of the MobileGateway. The length of this value must be in the range [`1`-`64`]
    """
    private_network_interface: pulumi.Output[dict]
    public_ip: pulumi.Output[str]
    """
    The public IP address assigned to the MobileGateway
    """
    public_netmask: pulumi.Output[float]
    """
    The bit length of the subnet assigned to the MobileGateway
    """
    sim_routes: pulumi.Output[list]
    sims: pulumi.Output[list]
    static_routes: pulumi.Output[list]
    tags: pulumi.Output[list]
    """
    Any tags to assign to the MobileGateway
    """
    traffic_control: pulumi.Output[dict]
    zone: pulumi.Output[str]
    """
    The name of zone that the MobileGateway will be created (e.g. `is1a`, `tk1a`)
    """
    def __init__(__self__, resource_name, opts=None, description=None, dns_servers=None, icon_id=None, inter_device_communication=None, internet_connection=None, name=None, private_network_interface=None, sim_routes=None, sims=None, static_routes=None, tags=None, traffic_control=None, zone=None, __props__=None, __name__=None, __opts__=None):
        """
        Create a MobileGateway resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the MobileGateway. The length of this value must be in the range [`1`-`512`]
        :param pulumi.Input[list] dns_servers: A list of IP address used by each connected devices
        :param pulumi.Input[str] icon_id: The icon id to attach to the MobileGateway
        :param pulumi.Input[bool] inter_device_communication: The flag to allow communication between each connected devices
        :param pulumi.Input[bool] internet_connection: The flag to enable connect to the Internet
        :param pulumi.Input[str] name: The name of the MobileGateway. The length of this value must be in the range [`1`-`64`]
        :param pulumi.Input[list] tags: Any tags to assign to the MobileGateway
        :param pulumi.Input[str] zone: The name of zone that the MobileGateway will be created (e.g. `is1a`, `tk1a`)

        The **private_network_interface** object supports the following:

          * `ip_address` (`pulumi.Input[str]`)
          * `netmask` (`pulumi.Input[float]`)
          * `switch_id` (`pulumi.Input[str]`)

        The **sim_routes** object supports the following:

          * `prefix` (`pulumi.Input[str]`)
          * `simId` (`pulumi.Input[str]`)

        The **sims** object supports the following:

          * `ip_address` (`pulumi.Input[str]`)
          * `simId` (`pulumi.Input[str]`)

        The **static_routes** object supports the following:

          * `next_hop` (`pulumi.Input[str]`)
          * `prefix` (`pulumi.Input[str]`)

        The **traffic_control** object supports the following:

          * `autoTrafficShaping` (`pulumi.Input[bool]`)
          * `bandWidthLimit` (`pulumi.Input[float]`)
          * `enableEmail` (`pulumi.Input[bool]`)
          * `enableSlack` (`pulumi.Input[bool]`)
          * `quota` (`pulumi.Input[float]`)
          * `slackWebhook` (`pulumi.Input[str]`)
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
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['description'] = description
            if dns_servers is None:
                raise TypeError("Missing required property 'dns_servers'")
            __props__['dns_servers'] = dns_servers
            __props__['icon_id'] = icon_id
            __props__['inter_device_communication'] = inter_device_communication
            __props__['internet_connection'] = internet_connection
            __props__['name'] = name
            __props__['private_network_interface'] = private_network_interface
            __props__['sim_routes'] = sim_routes
            __props__['sims'] = sims
            __props__['static_routes'] = static_routes
            __props__['tags'] = tags
            __props__['traffic_control'] = traffic_control
            __props__['zone'] = zone
            __props__['public_ip'] = None
            __props__['public_netmask'] = None
        super(MobileGateway, __self__).__init__(
            'sakuracloud:index/mobileGateway:MobileGateway',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, description=None, dns_servers=None, icon_id=None, inter_device_communication=None, internet_connection=None, name=None, private_network_interface=None, public_ip=None, public_netmask=None, sim_routes=None, sims=None, static_routes=None, tags=None, traffic_control=None, zone=None):
        """
        Get an existing MobileGateway resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the MobileGateway. The length of this value must be in the range [`1`-`512`]
        :param pulumi.Input[list] dns_servers: A list of IP address used by each connected devices
        :param pulumi.Input[str] icon_id: The icon id to attach to the MobileGateway
        :param pulumi.Input[bool] inter_device_communication: The flag to allow communication between each connected devices
        :param pulumi.Input[bool] internet_connection: The flag to enable connect to the Internet
        :param pulumi.Input[str] name: The name of the MobileGateway. The length of this value must be in the range [`1`-`64`]
        :param pulumi.Input[str] public_ip: The public IP address assigned to the MobileGateway
        :param pulumi.Input[float] public_netmask: The bit length of the subnet assigned to the MobileGateway
        :param pulumi.Input[list] tags: Any tags to assign to the MobileGateway
        :param pulumi.Input[str] zone: The name of zone that the MobileGateway will be created (e.g. `is1a`, `tk1a`)

        The **private_network_interface** object supports the following:

          * `ip_address` (`pulumi.Input[str]`)
          * `netmask` (`pulumi.Input[float]`)
          * `switch_id` (`pulumi.Input[str]`)

        The **sim_routes** object supports the following:

          * `prefix` (`pulumi.Input[str]`)
          * `simId` (`pulumi.Input[str]`)

        The **sims** object supports the following:

          * `ip_address` (`pulumi.Input[str]`)
          * `simId` (`pulumi.Input[str]`)

        The **static_routes** object supports the following:

          * `next_hop` (`pulumi.Input[str]`)
          * `prefix` (`pulumi.Input[str]`)

        The **traffic_control** object supports the following:

          * `autoTrafficShaping` (`pulumi.Input[bool]`)
          * `bandWidthLimit` (`pulumi.Input[float]`)
          * `enableEmail` (`pulumi.Input[bool]`)
          * `enableSlack` (`pulumi.Input[bool]`)
          * `quota` (`pulumi.Input[float]`)
          * `slackWebhook` (`pulumi.Input[str]`)
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["description"] = description
        __props__["dns_servers"] = dns_servers
        __props__["icon_id"] = icon_id
        __props__["inter_device_communication"] = inter_device_communication
        __props__["internet_connection"] = internet_connection
        __props__["name"] = name
        __props__["private_network_interface"] = private_network_interface
        __props__["public_ip"] = public_ip
        __props__["public_netmask"] = public_netmask
        __props__["sim_routes"] = sim_routes
        __props__["sims"] = sims
        __props__["static_routes"] = static_routes
        __props__["tags"] = tags
        __props__["traffic_control"] = traffic_control
        __props__["zone"] = zone
        return MobileGateway(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

