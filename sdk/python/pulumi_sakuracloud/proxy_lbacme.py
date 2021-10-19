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

__all__ = ['ProxyLBACME']


class ProxyLBACME(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 accept_tos: Optional[pulumi.Input[bool]] = None,
                 common_name: Optional[pulumi.Input[str]] = None,
                 proxylb_id: Optional[pulumi.Input[str]] = None,
                 subject_alt_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 update_delay_sec: Optional[pulumi.Input[int]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a SakuraCloud ProxyLB ACME Setting.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sakuracloud as sakuracloud

        foobar_proxy_lbacme = sakuracloud.ProxyLBACME("foobarProxyLBACME",
            proxylb_id=sakuracloud_proxylb["foobar"]["id"],
            accept_tos=True,
            common_name="www.example.com",
            subject_alt_names=["www1.example.com"],
            update_delay_sec=120)
        foobar_proxy_lb = sakuracloud.get_proxy_lb(filter=sakuracloud.GetProxyLBFilterArgs(
            names=["foobar"],
        ))
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] accept_tos: The flag to accept the current Let's Encrypt terms of service(see: https://letsencrypt.org/repository/). This must be set `true` explicitly. Changing this forces a new resource to be created.
        :param pulumi.Input[str] common_name: The FQDN used by ACME. This must set resolvable value. Changing this forces a new resource to be created.
        :param pulumi.Input[str] proxylb_id: The id of the ProxyLB that set ACME settings to. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subject_alt_names: The Subject alternative names used by ACME. Changing this forces a new resource to be created.
        :param pulumi.Input[int] update_delay_sec: The wait time in seconds. This typically used for waiting for a DNS propagation. Changing this forces a new resource to be created.
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

            if accept_tos is None and not opts.urn:
                raise TypeError("Missing required property 'accept_tos'")
            __props__['accept_tos'] = accept_tos
            if common_name is None and not opts.urn:
                raise TypeError("Missing required property 'common_name'")
            __props__['common_name'] = common_name
            if proxylb_id is None and not opts.urn:
                raise TypeError("Missing required property 'proxylb_id'")
            __props__['proxylb_id'] = proxylb_id
            __props__['subject_alt_names'] = subject_alt_names
            __props__['update_delay_sec'] = update_delay_sec
            __props__['certificates'] = None
        super(ProxyLBACME, __self__).__init__(
            'sakuracloud:index/proxyLBACME:ProxyLBACME',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            accept_tos: Optional[pulumi.Input[bool]] = None,
            certificates: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ProxyLBACMECertificateArgs']]]]] = None,
            common_name: Optional[pulumi.Input[str]] = None,
            proxylb_id: Optional[pulumi.Input[str]] = None,
            subject_alt_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            update_delay_sec: Optional[pulumi.Input[int]] = None) -> 'ProxyLBACME':
        """
        Get an existing ProxyLBACME resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] accept_tos: The flag to accept the current Let's Encrypt terms of service(see: https://letsencrypt.org/repository/). This must be set `true` explicitly. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ProxyLBACMECertificateArgs']]]] certificates: A list of `certificate` blocks as defined below.
        :param pulumi.Input[str] common_name: The FQDN used by ACME. This must set resolvable value. Changing this forces a new resource to be created.
        :param pulumi.Input[str] proxylb_id: The id of the ProxyLB that set ACME settings to. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subject_alt_names: The Subject alternative names used by ACME. Changing this forces a new resource to be created.
        :param pulumi.Input[int] update_delay_sec: The wait time in seconds. This typically used for waiting for a DNS propagation. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["accept_tos"] = accept_tos
        __props__["certificates"] = certificates
        __props__["common_name"] = common_name
        __props__["proxylb_id"] = proxylb_id
        __props__["subject_alt_names"] = subject_alt_names
        __props__["update_delay_sec"] = update_delay_sec
        return ProxyLBACME(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="acceptTos")
    def accept_tos(self) -> pulumi.Output[bool]:
        """
        The flag to accept the current Let's Encrypt terms of service(see: https://letsencrypt.org/repository/). This must be set `true` explicitly. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "accept_tos")

    @property
    @pulumi.getter
    def certificates(self) -> pulumi.Output[Sequence['outputs.ProxyLBACMECertificate']]:
        """
        A list of `certificate` blocks as defined below.
        """
        return pulumi.get(self, "certificates")

    @property
    @pulumi.getter(name="commonName")
    def common_name(self) -> pulumi.Output[str]:
        """
        The FQDN used by ACME. This must set resolvable value. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "common_name")

    @property
    @pulumi.getter(name="proxylbId")
    def proxylb_id(self) -> pulumi.Output[str]:
        """
        The id of the ProxyLB that set ACME settings to. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "proxylb_id")

    @property
    @pulumi.getter(name="subjectAltNames")
    def subject_alt_names(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The Subject alternative names used by ACME. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "subject_alt_names")

    @property
    @pulumi.getter(name="updateDelaySec")
    def update_delay_sec(self) -> pulumi.Output[Optional[int]]:
        """
        The wait time in seconds. This typically used for waiting for a DNS propagation. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "update_delay_sec")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

