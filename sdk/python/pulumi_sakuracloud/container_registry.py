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

__all__ = ['ContainerRegistry']


class ContainerRegistry(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_level: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 icon_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 subdomain_label: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 users: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ContainerRegistryUserArgs']]]]] = None,
                 virtual_domain: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a SakuraCloud Container Registry.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_level: The level of access that allow to users. This must be one of [`readwrite`/`readonly`/`none`].
        :param pulumi.Input[str] description: The description of the Container Registry. The length of this value must be in the range [`1`-`512`].
        :param pulumi.Input[str] icon_id: The icon id to attach to the Container Registry.
        :param pulumi.Input[str] name: The name of the Container Registry. The length of this value must be in the range [`1`-`64`].
        :param pulumi.Input[str] subdomain_label: The label at the lowest of the FQDN used when be accessed from users. The length of this value must be in the range [`1`-`64`]. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Any tags to assign to the Container Registry.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ContainerRegistryUserArgs']]]] users: One or more `user` blocks as defined below.
        :param pulumi.Input[str] virtual_domain: The alias for accessing the container registry.
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

            if access_level is None and not opts.urn:
                raise TypeError("Missing required property 'access_level'")
            __props__['access_level'] = access_level
            __props__['description'] = description
            __props__['icon_id'] = icon_id
            __props__['name'] = name
            if subdomain_label is None and not opts.urn:
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
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            access_level: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            fqdn: Optional[pulumi.Input[str]] = None,
            icon_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            subdomain_label: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            users: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ContainerRegistryUserArgs']]]]] = None,
            virtual_domain: Optional[pulumi.Input[str]] = None) -> 'ContainerRegistry':
        """
        Get an existing ContainerRegistry resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_level: The level of access that allow to users. This must be one of [`readwrite`/`readonly`/`none`].
        :param pulumi.Input[str] description: The description of the Container Registry. The length of this value must be in the range [`1`-`512`].
        :param pulumi.Input[str] fqdn: The FQDN for accessing the Container Registry. FQDN is built from `subdomain_label` + `.sakuracr.jp`.
        :param pulumi.Input[str] icon_id: The icon id to attach to the Container Registry.
        :param pulumi.Input[str] name: The name of the Container Registry. The length of this value must be in the range [`1`-`64`].
        :param pulumi.Input[str] subdomain_label: The label at the lowest of the FQDN used when be accessed from users. The length of this value must be in the range [`1`-`64`]. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Any tags to assign to the Container Registry.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ContainerRegistryUserArgs']]]] users: One or more `user` blocks as defined below.
        :param pulumi.Input[str] virtual_domain: The alias for accessing the container registry.
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

    @property
    @pulumi.getter(name="accessLevel")
    def access_level(self) -> pulumi.Output[str]:
        """
        The level of access that allow to users. This must be one of [`readwrite`/`readonly`/`none`].
        """
        return pulumi.get(self, "access_level")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the Container Registry. The length of this value must be in the range [`1`-`512`].
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def fqdn(self) -> pulumi.Output[str]:
        """
        The FQDN for accessing the Container Registry. FQDN is built from `subdomain_label` + `.sakuracr.jp`.
        """
        return pulumi.get(self, "fqdn")

    @property
    @pulumi.getter(name="iconId")
    def icon_id(self) -> pulumi.Output[Optional[str]]:
        """
        The icon id to attach to the Container Registry.
        """
        return pulumi.get(self, "icon_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Container Registry. The length of this value must be in the range [`1`-`64`].
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="subdomainLabel")
    def subdomain_label(self) -> pulumi.Output[str]:
        """
        The label at the lowest of the FQDN used when be accessed from users. The length of this value must be in the range [`1`-`64`]. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "subdomain_label")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Any tags to assign to the Container Registry.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def users(self) -> pulumi.Output[Optional[Sequence['outputs.ContainerRegistryUser']]]:
        """
        One or more `user` blocks as defined below.
        """
        return pulumi.get(self, "users")

    @property
    @pulumi.getter(name="virtualDomain")
    def virtual_domain(self) -> pulumi.Output[Optional[str]]:
        """
        The alias for accessing the container registry.
        """
        return pulumi.get(self, "virtual_domain")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

