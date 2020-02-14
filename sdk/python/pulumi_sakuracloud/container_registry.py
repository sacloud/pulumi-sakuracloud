# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class ContainerRegistry(pulumi.CustomResource):
    access_level: pulumi.Output[str]
    """
    The level of access that allow to users. This must be one of [`readwrite`/`readonly`/`none`]
    """
    description: pulumi.Output[str]
    """
    The description of the Container Registry. The length of this value must be in the range [`1`-`512`]
    """
    fqdn: pulumi.Output[str]
    """
    The FQDN for accessing the Container Registry. FQDN is built from `subdomain_label` + `.sakuracr.jp`
    """
    icon_id: pulumi.Output[str]
    """
    The icon id to attach to the Container Registry
    """
    name: pulumi.Output[str]
    """
    The name of the Container Registry. The length of this value must be in the range [`1`-`64`]
    """
    subdomain_label: pulumi.Output[str]
    """
    The label at the lowest of the FQDN used when be accessed from users. The length of this value must be in the range
    [`1`-`64`]
    """
    tags: pulumi.Output[list]
    """
    Any tags to assign to the Container Registry
    """
    users: pulumi.Output[list]
    virtual_domain: pulumi.Output[str]
    """
    The alias for accessing the container registry
    """
    def __init__(__self__, resource_name, opts=None, access_level=None, description=None, icon_id=None, name=None, subdomain_label=None, tags=None, users=None, virtual_domain=None, __props__=None, __name__=None, __opts__=None):
        """
        Create a ContainerRegistry resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_level: The level of access that allow to users. This must be one of [`readwrite`/`readonly`/`none`]
        :param pulumi.Input[str] description: The description of the Container Registry. The length of this value must be in the range [`1`-`512`]
        :param pulumi.Input[str] icon_id: The icon id to attach to the Container Registry
        :param pulumi.Input[str] name: The name of the Container Registry. The length of this value must be in the range [`1`-`64`]
        :param pulumi.Input[str] subdomain_label: The label at the lowest of the FQDN used when be accessed from users. The length of this value must be in the range
               [`1`-`64`]
        :param pulumi.Input[list] tags: Any tags to assign to the Container Registry
        :param pulumi.Input[str] virtual_domain: The alias for accessing the container registry

        The **users** object supports the following:

          * `name` (`pulumi.Input[str]`)
          * `password` (`pulumi.Input[str]`)
          * `permission` (`pulumi.Input[str]`)
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

            if access_level is None:
                raise TypeError("Missing required property 'access_level'")
            __props__['access_level'] = access_level
            __props__['description'] = description
            __props__['icon_id'] = icon_id
            __props__['name'] = name
            if subdomain_label is None:
                raise TypeError("Missing required property 'subdomain_label'")
            __props__['subdomain_label'] = subdomain_label
            __props__['tags'] = tags
            __props__['users'] = users
            __props__['virtual_domain'] = virtual_domain
            __props__['fqdn'] = None
        super(ContainerRegistry, __self__).__init__(
            'sakuracloud:index/containerRegistry:ContainerRegistry',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, access_level=None, description=None, fqdn=None, icon_id=None, name=None, subdomain_label=None, tags=None, users=None, virtual_domain=None):
        """
        Get an existing ContainerRegistry resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_level: The level of access that allow to users. This must be one of [`readwrite`/`readonly`/`none`]
        :param pulumi.Input[str] description: The description of the Container Registry. The length of this value must be in the range [`1`-`512`]
        :param pulumi.Input[str] fqdn: The FQDN for accessing the Container Registry. FQDN is built from `subdomain_label` + `.sakuracr.jp`
        :param pulumi.Input[str] icon_id: The icon id to attach to the Container Registry
        :param pulumi.Input[str] name: The name of the Container Registry. The length of this value must be in the range [`1`-`64`]
        :param pulumi.Input[str] subdomain_label: The label at the lowest of the FQDN used when be accessed from users. The length of this value must be in the range
               [`1`-`64`]
        :param pulumi.Input[list] tags: Any tags to assign to the Container Registry
        :param pulumi.Input[str] virtual_domain: The alias for accessing the container registry

        The **users** object supports the following:

          * `name` (`pulumi.Input[str]`)
          * `password` (`pulumi.Input[str]`)
          * `permission` (`pulumi.Input[str]`)
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["access_level"] = access_level
        __props__["description"] = description
        __props__["fqdn"] = fqdn
        __props__["icon_id"] = icon_id
        __props__["name"] = name
        __props__["subdomain_label"] = subdomain_label
        __props__["tags"] = tags
        __props__["users"] = users
        __props__["virtual_domain"] = virtual_domain
        return ContainerRegistry(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

