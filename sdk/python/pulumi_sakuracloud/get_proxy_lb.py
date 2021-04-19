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

__all__ = [
    'GetProxyLBResult',
    'AwaitableGetProxyLBResult',
    'get_proxy_lb',
]

@pulumi.output_type
class GetProxyLBResult:
    """
    A collection of values returned by getProxyLB.
    """
    def __init__(__self__, bind_ports=None, certificates=None, description=None, filter=None, fqdn=None, gzip=None, health_checks=None, icon_id=None, id=None, name=None, plan=None, proxy_networks=None, region=None, rules=None, servers=None, sorry_servers=None, sticky_session=None, tags=None, timeout=None, vip=None, vip_failover=None):
        if bind_ports and not isinstance(bind_ports, list):
            raise TypeError("Expected argument 'bind_ports' to be a list")
        pulumi.set(__self__, "bind_ports", bind_ports)
        if certificates and not isinstance(certificates, list):
            raise TypeError("Expected argument 'certificates' to be a list")
        pulumi.set(__self__, "certificates", certificates)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if filter and not isinstance(filter, dict):
            raise TypeError("Expected argument 'filter' to be a dict")
        pulumi.set(__self__, "filter", filter)
        if fqdn and not isinstance(fqdn, str):
            raise TypeError("Expected argument 'fqdn' to be a str")
        pulumi.set(__self__, "fqdn", fqdn)
        if gzip and not isinstance(gzip, bool):
            raise TypeError("Expected argument 'gzip' to be a bool")
        pulumi.set(__self__, "gzip", gzip)
        if health_checks and not isinstance(health_checks, list):
            raise TypeError("Expected argument 'health_checks' to be a list")
        pulumi.set(__self__, "health_checks", health_checks)
        if icon_id and not isinstance(icon_id, str):
            raise TypeError("Expected argument 'icon_id' to be a str")
        pulumi.set(__self__, "icon_id", icon_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if plan and not isinstance(plan, int):
            raise TypeError("Expected argument 'plan' to be a int")
        pulumi.set(__self__, "plan", plan)
        if proxy_networks and not isinstance(proxy_networks, list):
            raise TypeError("Expected argument 'proxy_networks' to be a list")
        pulumi.set(__self__, "proxy_networks", proxy_networks)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if rules and not isinstance(rules, list):
            raise TypeError("Expected argument 'rules' to be a list")
        pulumi.set(__self__, "rules", rules)
        if servers and not isinstance(servers, list):
            raise TypeError("Expected argument 'servers' to be a list")
        pulumi.set(__self__, "servers", servers)
        if sorry_servers and not isinstance(sorry_servers, list):
            raise TypeError("Expected argument 'sorry_servers' to be a list")
        pulumi.set(__self__, "sorry_servers", sorry_servers)
        if sticky_session and not isinstance(sticky_session, bool):
            raise TypeError("Expected argument 'sticky_session' to be a bool")
        pulumi.set(__self__, "sticky_session", sticky_session)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if timeout and not isinstance(timeout, int):
            raise TypeError("Expected argument 'timeout' to be a int")
        pulumi.set(__self__, "timeout", timeout)
        if vip and not isinstance(vip, str):
            raise TypeError("Expected argument 'vip' to be a str")
        pulumi.set(__self__, "vip", vip)
        if vip_failover and not isinstance(vip_failover, bool):
            raise TypeError("Expected argument 'vip_failover' to be a bool")
        pulumi.set(__self__, "vip_failover", vip_failover)

    @property
    @pulumi.getter(name="bindPorts")
    def bind_ports(self) -> Sequence['outputs.GetProxyLBBindPortResult']:
        """
        A list of `bind_port` blocks as defined below.
        """
        return pulumi.get(self, "bind_ports")

    @property
    @pulumi.getter
    def certificates(self) -> Sequence['outputs.GetProxyLBCertificateResult']:
        """
        A list of `certificate` blocks as defined below.
        """
        return pulumi.get(self, "certificates")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The description of the ProxyLB.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def filter(self) -> Optional['outputs.GetProxyLBFilterResult']:
        return pulumi.get(self, "filter")

    @property
    @pulumi.getter
    def fqdn(self) -> str:
        """
        The FQDN for accessing to the ProxyLB. This is typically used as value of CNAME record.
        """
        return pulumi.get(self, "fqdn")

    @property
    @pulumi.getter
    def gzip(self) -> bool:
        """
        The flag to enable gzip compression.
        """
        return pulumi.get(self, "gzip")

    @property
    @pulumi.getter(name="healthChecks")
    def health_checks(self) -> Sequence['outputs.GetProxyLBHealthCheckResult']:
        """
        A list of `health_check` blocks as defined below.
        """
        return pulumi.get(self, "health_checks")

    @property
    @pulumi.getter(name="iconId")
    def icon_id(self) -> str:
        """
        The icon id attached to the ProxyLB.
        """
        return pulumi.get(self, "icon_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the ProxyLB.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def plan(self) -> int:
        """
        The plan name of the ProxyLB. This will be one of [`100`/`500`/`1000`/`5000`/`10000`/`50000`/`100000`].
        """
        return pulumi.get(self, "plan")

    @property
    @pulumi.getter(name="proxyNetworks")
    def proxy_networks(self) -> Sequence[str]:
        """
        A list of CIDR block used by the ProxyLB to access the server.
        """
        return pulumi.get(self, "proxy_networks")

    @property
    @pulumi.getter
    def region(self) -> str:
        """
        The name of region that the proxy LB is in. This will be one of [`tk1`/`is1`/`anycast`].
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def rules(self) -> Sequence['outputs.GetProxyLBRuleResult']:
        """
        A list of `rule` blocks as defined below.
        """
        return pulumi.get(self, "rules")

    @property
    @pulumi.getter
    def servers(self) -> Sequence['outputs.GetProxyLBServerResult']:
        """
        A list of `server` blocks as defined below.
        """
        return pulumi.get(self, "servers")

    @property
    @pulumi.getter(name="sorryServers")
    def sorry_servers(self) -> Sequence['outputs.GetProxyLBSorryServerResult']:
        """
        A list of `sorry_server` blocks as defined below.
        """
        return pulumi.get(self, "sorry_servers")

    @property
    @pulumi.getter(name="stickySession")
    def sticky_session(self) -> bool:
        """
        The flag to enable sticky session.
        """
        return pulumi.get(self, "sticky_session")

    @property
    @pulumi.getter
    def tags(self) -> Sequence[str]:
        """
        Any tags assigned to the ProxyLB.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def timeout(self) -> int:
        """
        The timeout duration in seconds.
        """
        return pulumi.get(self, "timeout")

    @property
    @pulumi.getter
    def vip(self) -> str:
        """
        The virtual IP address assigned to the ProxyLB.
        """
        return pulumi.get(self, "vip")

    @property
    @pulumi.getter(name="vipFailover")
    def vip_failover(self) -> bool:
        """
        The flag to enable VIP fail-over.
        """
        return pulumi.get(self, "vip_failover")


class AwaitableGetProxyLBResult(GetProxyLBResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetProxyLBResult(
            bind_ports=self.bind_ports,
            certificates=self.certificates,
            description=self.description,
            filter=self.filter,
            fqdn=self.fqdn,
            gzip=self.gzip,
            health_checks=self.health_checks,
            icon_id=self.icon_id,
            id=self.id,
            name=self.name,
            plan=self.plan,
            proxy_networks=self.proxy_networks,
            region=self.region,
            rules=self.rules,
            servers=self.servers,
            sorry_servers=self.sorry_servers,
            sticky_session=self.sticky_session,
            tags=self.tags,
            timeout=self.timeout,
            vip=self.vip,
            vip_failover=self.vip_failover)


def get_proxy_lb(filter: Optional[pulumi.InputType['GetProxyLBFilterArgs']] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetProxyLBResult:
    """
    Get information about an existing ProxyLB.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_sakuracloud as sakuracloud

    foobar = sakuracloud.get_proxy_lb(filter=sakuracloud.GetProxyLBFilterArgs(
        names=["foobar"],
    ))
    ```


    :param pulumi.InputType['GetProxyLBFilterArgs'] filter: One or more values used for filtering, as defined below.
    """
    __args__ = dict()
    __args__['filter'] = filter
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('sakuracloud:index/getProxyLB:getProxyLB', __args__, opts=opts, typ=GetProxyLBResult).value

    return AwaitableGetProxyLBResult(
        bind_ports=__ret__.bind_ports,
        certificates=__ret__.certificates,
        description=__ret__.description,
        filter=__ret__.filter,
        fqdn=__ret__.fqdn,
        gzip=__ret__.gzip,
        health_checks=__ret__.health_checks,
        icon_id=__ret__.icon_id,
        id=__ret__.id,
        name=__ret__.name,
        plan=__ret__.plan,
        proxy_networks=__ret__.proxy_networks,
        region=__ret__.region,
        rules=__ret__.rules,
        servers=__ret__.servers,
        sorry_servers=__ret__.sorry_servers,
        sticky_session=__ret__.sticky_session,
        tags=__ret__.tags,
        timeout=__ret__.timeout,
        vip=__ret__.vip,
        vip_failover=__ret__.vip_failover)
