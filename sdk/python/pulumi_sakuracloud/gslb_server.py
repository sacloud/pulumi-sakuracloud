# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class GSLBServer(pulumi.CustomResource):
    enabled: pulumi.Output[bool]
    """
    The flag for enable/disable the GSLB Server (default:`true`).
    """
    gslb_id: pulumi.Output[str]
    """
    The ID of the GSLB to which the GSLB Server belongs.
    """
    ipaddress: pulumi.Output[str]
    """
    The IP address of the GSLB Server.
    """
    weight: pulumi.Output[float]
    """
    The weight of GSLB server used when weighting is enabled in the GSLB.
    """
    def __init__(__self__, resource_name, opts=None, enabled=None, gslb_id=None, ipaddress=None, weight=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a SakuraCloud GSLB Server resource. This can be used to create and delete GSLB Servers.
        
        ## Import (not supported)
        
        Import of GSLB Server is not supported.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enabled: The flag for enable/disable the GSLB Server (default:`true`).
        :param pulumi.Input[str] gslb_id: The ID of the GSLB to which the GSLB Server belongs.
        :param pulumi.Input[str] ipaddress: The IP address of the GSLB Server.
        :param pulumi.Input[float] weight: The weight of GSLB server used when weighting is enabled in the GSLB.

        > This content is derived from https://github.com/sacloud/terraform-provider-sakuracloud/blob/master/website/docs/r/gslb_server.html.markdown.
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

            __props__['enabled'] = enabled
            if gslb_id is None:
                raise TypeError("Missing required property 'gslb_id'")
            __props__['gslb_id'] = gslb_id
            if ipaddress is None:
                raise TypeError("Missing required property 'ipaddress'")
            __props__['ipaddress'] = ipaddress
            __props__['weight'] = weight
        super(GSLBServer, __self__).__init__(
            'sakuracloud:index/gSLBServer:GSLBServer',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, enabled=None, gslb_id=None, ipaddress=None, weight=None):
        """
        Get an existing GSLBServer resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enabled: The flag for enable/disable the GSLB Server (default:`true`).
        :param pulumi.Input[str] gslb_id: The ID of the GSLB to which the GSLB Server belongs.
        :param pulumi.Input[str] ipaddress: The IP address of the GSLB Server.
        :param pulumi.Input[float] weight: The weight of GSLB server used when weighting is enabled in the GSLB.

        > This content is derived from https://github.com/sacloud/terraform-provider-sakuracloud/blob/master/website/docs/r/gslb_server.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["enabled"] = enabled
        __props__["gslb_id"] = gslb_id
        __props__["ipaddress"] = ipaddress
        __props__["weight"] = weight
        return GSLBServer(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

