# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class SIM(pulumi.CustomResource):
    carriers: pulumi.Output[list]
    """
    The list of Carrier name.  
    Valid values are in followings: [ "docomo" / "kddi" / "softbank"]
    """
    description: pulumi.Output[str]
    """
    The description of the resource.
    """
    enabled: pulumi.Output[bool]
    """
    The flag of enable/disable the Server.
    """
    iccid: pulumi.Output[str]
    """
    The ICCID of the SIM.  
    """
    icon_id: pulumi.Output[str]
    """
    The ID of the icon.
    """
    imei: pulumi.Output[str]
    """
    The IMEI of the device that allows communication.
    """
    ipaddress: pulumi.Output[str]
    """
    The IP address of the SIM. Used when connect to mobile gateway.
    """
    mobile_gateway_id: pulumi.Output[str]
    """
    The ID of the Mobile Gateway to which the SIM belongs.
    """
    name: pulumi.Output[str]
    """
    The name of the resource.
    """
    passcode: pulumi.Output[str]
    """
    The Passcode of the SIM.  
    """
    tags: pulumi.Output[list]
    """
    The tag list of the resources.
    """
    def __init__(__self__, resource_name, opts=None, carriers=None, description=None, enabled=None, iccid=None, icon_id=None, imei=None, ipaddress=None, mobile_gateway_id=None, name=None, passcode=None, tags=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a SakuraCloud SIM resource. This can be used to create, update, and delete SIMs.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] carriers: The list of Carrier name.  
               Valid values are in followings: [ "docomo" / "kddi" / "softbank"]
        :param pulumi.Input[str] description: The description of the resource.
        :param pulumi.Input[bool] enabled: The flag of enable/disable the Server.
        :param pulumi.Input[str] iccid: The ICCID of the SIM.  
        :param pulumi.Input[str] icon_id: The ID of the icon.
        :param pulumi.Input[str] imei: The IMEI of the device that allows communication.
        :param pulumi.Input[str] ipaddress: The IP address of the SIM. Used when connect to mobile gateway.
        :param pulumi.Input[str] mobile_gateway_id: The ID of the Mobile Gateway to which the SIM belongs.
        :param pulumi.Input[str] name: The name of the resource.
        :param pulumi.Input[str] passcode: The Passcode of the SIM.  
        :param pulumi.Input[list] tags: The tag list of the resources.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-sakuracloud/blob/master/website/docs/r/sim.html.markdown.
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

            if carriers is None:
                raise TypeError("Missing required property 'carriers'")
            __props__['carriers'] = carriers
            __props__['description'] = description
            __props__['enabled'] = enabled
            if iccid is None:
                raise TypeError("Missing required property 'iccid'")
            __props__['iccid'] = iccid
            __props__['icon_id'] = icon_id
            __props__['imei'] = imei
            __props__['ipaddress'] = ipaddress
            __props__['mobile_gateway_id'] = mobile_gateway_id
            __props__['name'] = name
            if passcode is None:
                raise TypeError("Missing required property 'passcode'")
            __props__['passcode'] = passcode
            __props__['tags'] = tags
        super(SIM, __self__).__init__(
            'sakuracloud:index/sIM:SIM',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, carriers=None, description=None, enabled=None, iccid=None, icon_id=None, imei=None, ipaddress=None, mobile_gateway_id=None, name=None, passcode=None, tags=None):
        """
        Get an existing SIM resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] carriers: The list of Carrier name.  
               Valid values are in followings: [ "docomo" / "kddi" / "softbank"]
        :param pulumi.Input[str] description: The description of the resource.
        :param pulumi.Input[bool] enabled: The flag of enable/disable the Server.
        :param pulumi.Input[str] iccid: The ICCID of the SIM.  
        :param pulumi.Input[str] icon_id: The ID of the icon.
        :param pulumi.Input[str] imei: The IMEI of the device that allows communication.
        :param pulumi.Input[str] ipaddress: The IP address of the SIM. Used when connect to mobile gateway.
        :param pulumi.Input[str] mobile_gateway_id: The ID of the Mobile Gateway to which the SIM belongs.
        :param pulumi.Input[str] name: The name of the resource.
        :param pulumi.Input[str] passcode: The Passcode of the SIM.  
        :param pulumi.Input[list] tags: The tag list of the resources.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-sakuracloud/blob/master/website/docs/r/sim.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["carriers"] = carriers
        __props__["description"] = description
        __props__["enabled"] = enabled
        __props__["iccid"] = iccid
        __props__["icon_id"] = icon_id
        __props__["imei"] = imei
        __props__["ipaddress"] = ipaddress
        __props__["mobile_gateway_id"] = mobile_gateway_id
        __props__["name"] = name
        __props__["passcode"] = passcode
        __props__["tags"] = tags
        return SIM(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
