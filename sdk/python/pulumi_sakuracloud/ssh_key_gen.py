# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class SSHKeyGen(pulumi.CustomResource):
    description: pulumi.Output[str]
    """
    The description of the resource.
    """
    fingerprint: pulumi.Output[str]
    name: pulumi.Output[str]
    """
    The name of the resource.
    """
    pass_phrase: pulumi.Output[str]
    """
    The path phrase of keys. 
    """
    private_key: pulumi.Output[str]
    """
    The body of the generated private key. 
    """
    public_key: pulumi.Output[str]
    """
    The body of the generated public key. 
    """
    def __init__(__self__, resource_name, opts=None, description=None, name=None, pass_phrase=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a SakuraCloud SSH Key resource. This can be used to create and delete SSH Keys.
        The private and public keys is generated on the Sakura Cloud platform.
        
        ## Import (not supported)
        
        Import of SSH Key Gen is not supported.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the resource.
        :param pulumi.Input[str] name: The name of the resource.
        :param pulumi.Input[str] pass_phrase: The path phrase of keys. 

        > This content is derived from https://github.com/terraform-providers/terraform-provider-sakuracloud/blob/master/website/docs/r/ssh_key_gen.html.markdown.
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
            __props__['name'] = name
            __props__['pass_phrase'] = pass_phrase
            __props__['fingerprint'] = None
            __props__['private_key'] = None
            __props__['public_key'] = None
        super(SSHKeyGen, __self__).__init__(
            'sakuracloud:index/sSHKeyGen:SSHKeyGen',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, description=None, fingerprint=None, name=None, pass_phrase=None, private_key=None, public_key=None):
        """
        Get an existing SSHKeyGen resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the resource.
        :param pulumi.Input[str] name: The name of the resource.
        :param pulumi.Input[str] pass_phrase: The path phrase of keys. 
        :param pulumi.Input[str] private_key: The body of the generated private key. 
        :param pulumi.Input[str] public_key: The body of the generated public key. 

        > This content is derived from https://github.com/terraform-providers/terraform-provider-sakuracloud/blob/master/website/docs/r/ssh_key_gen.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["description"] = description
        __props__["fingerprint"] = fingerprint
        __props__["name"] = name
        __props__["pass_phrase"] = pass_phrase
        __props__["private_key"] = private_key
        __props__["public_key"] = public_key
        return SSHKeyGen(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

