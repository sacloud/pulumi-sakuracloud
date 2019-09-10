# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class MobileGatewaySIMRoute(pulumi.CustomResource):
    mobile_gateway_id: pulumi.Output[str]
    """
    The ID of the Mobile Gateway to set SIM Route.
    """
    prefix: pulumi.Output[str]
    """
    The routing prefix (format:`CIDR`).
    """
    sim_id: pulumi.Output[str]
    """
    The ID of the routing destination SIM.
    """
    zone: pulumi.Output[str]
    """
    The ID of the zone to which the resource belongs.
    """
    def __init__(__self__, resource_name, opts=None, mobile_gateway_id=None, prefix=None, sim_id=None, zone=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a SakuraCloud Mobile Gateway SIM Route resource. This can be used to create, update, and delete Mobile Gateway SIM Routes.
        
        ## Import (not supported)
        
        Import of Mobile Gateway SIM Route is not supported.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] mobile_gateway_id: The ID of the Mobile Gateway to set SIM Route.
        :param pulumi.Input[str] prefix: The routing prefix (format:`CIDR`).
        :param pulumi.Input[str] sim_id: The ID of the routing destination SIM.
        :param pulumi.Input[str] zone: The ID of the zone to which the resource belongs.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-sakuracloud/blob/master/website/docs/r/mobile_gateway_sim_route.html.markdown.
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

            if mobile_gateway_id is None:
                raise TypeError("Missing required property 'mobile_gateway_id'")
            __props__['mobile_gateway_id'] = mobile_gateway_id
            if prefix is None:
                raise TypeError("Missing required property 'prefix'")
            __props__['prefix'] = prefix
            if sim_id is None:
                raise TypeError("Missing required property 'sim_id'")
            __props__['sim_id'] = sim_id
            __props__['zone'] = zone
        super(MobileGatewaySIMRoute, __self__).__init__(
            'sakuracloud:index/mobileGatewaySIMRoute:MobileGatewaySIMRoute',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, mobile_gateway_id=None, prefix=None, sim_id=None, zone=None):
        """
        Get an existing MobileGatewaySIMRoute resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] mobile_gateway_id: The ID of the Mobile Gateway to set SIM Route.
        :param pulumi.Input[str] prefix: The routing prefix (format:`CIDR`).
        :param pulumi.Input[str] sim_id: The ID of the routing destination SIM.
        :param pulumi.Input[str] zone: The ID of the zone to which the resource belongs.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-sakuracloud/blob/master/website/docs/r/mobile_gateway_sim_route.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["mobile_gateway_id"] = mobile_gateway_id
        __props__["prefix"] = prefix
        __props__["sim_id"] = sim_id
        __props__["zone"] = zone
        return MobileGatewaySIMRoute(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

