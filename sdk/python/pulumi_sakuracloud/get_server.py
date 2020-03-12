# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class GetServerResult:
    """
    A collection of values returned by getServer.
    """
    def __init__(__self__, cdrom_id=None, commitment=None, core=None, description=None, disks=None, dns_servers=None, filter=None, gateway=None, hostname=None, icon_id=None, id=None, interface_driver=None, ip_address=None, memory=None, name=None, netmask=None, network_address=None, network_interfaces=None, private_host_id=None, private_host_name=None, tags=None, zone=None):
        if cdrom_id and not isinstance(cdrom_id, str):
            raise TypeError("Expected argument 'cdrom_id' to be a str")
        __self__.cdrom_id = cdrom_id
        if commitment and not isinstance(commitment, str):
            raise TypeError("Expected argument 'commitment' to be a str")
        __self__.commitment = commitment
        if core and not isinstance(core, float):
            raise TypeError("Expected argument 'core' to be a float")
        __self__.core = core
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        __self__.description = description
        if disks and not isinstance(disks, list):
            raise TypeError("Expected argument 'disks' to be a list")
        __self__.disks = disks
        if dns_servers and not isinstance(dns_servers, list):
            raise TypeError("Expected argument 'dns_servers' to be a list")
        __self__.dns_servers = dns_servers
        if filter and not isinstance(filter, dict):
            raise TypeError("Expected argument 'filter' to be a dict")
        __self__.filter = filter
        if gateway and not isinstance(gateway, str):
            raise TypeError("Expected argument 'gateway' to be a str")
        __self__.gateway = gateway
        if hostname and not isinstance(hostname, str):
            raise TypeError("Expected argument 'hostname' to be a str")
        __self__.hostname = hostname
        if icon_id and not isinstance(icon_id, str):
            raise TypeError("Expected argument 'icon_id' to be a str")
        __self__.icon_id = icon_id
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """
        if interface_driver and not isinstance(interface_driver, str):
            raise TypeError("Expected argument 'interface_driver' to be a str")
        __self__.interface_driver = interface_driver
        if ip_address and not isinstance(ip_address, str):
            raise TypeError("Expected argument 'ip_address' to be a str")
        __self__.ip_address = ip_address
        if memory and not isinstance(memory, float):
            raise TypeError("Expected argument 'memory' to be a float")
        __self__.memory = memory
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        if netmask and not isinstance(netmask, float):
            raise TypeError("Expected argument 'netmask' to be a float")
        __self__.netmask = netmask
        if network_address and not isinstance(network_address, str):
            raise TypeError("Expected argument 'network_address' to be a str")
        __self__.network_address = network_address
        if network_interfaces and not isinstance(network_interfaces, list):
            raise TypeError("Expected argument 'network_interfaces' to be a list")
        __self__.network_interfaces = network_interfaces
        if private_host_id and not isinstance(private_host_id, str):
            raise TypeError("Expected argument 'private_host_id' to be a str")
        __self__.private_host_id = private_host_id
        if private_host_name and not isinstance(private_host_name, str):
            raise TypeError("Expected argument 'private_host_name' to be a str")
        __self__.private_host_name = private_host_name
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        __self__.tags = tags
        if zone and not isinstance(zone, str):
            raise TypeError("Expected argument 'zone' to be a str")
        __self__.zone = zone
class AwaitableGetServerResult(GetServerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServerResult(
            cdrom_id=self.cdrom_id,
            commitment=self.commitment,
            core=self.core,
            description=self.description,
            disks=self.disks,
            dns_servers=self.dns_servers,
            filter=self.filter,
            gateway=self.gateway,
            hostname=self.hostname,
            icon_id=self.icon_id,
            id=self.id,
            interface_driver=self.interface_driver,
            ip_address=self.ip_address,
            memory=self.memory,
            name=self.name,
            netmask=self.netmask,
            network_address=self.network_address,
            network_interfaces=self.network_interfaces,
            private_host_id=self.private_host_id,
            private_host_name=self.private_host_name,
            tags=self.tags,
            zone=self.zone)

def get_server(filter=None,zone=None,opts=None):
    """
    Use this data source to access information about an existing resource.


    The **filter** object supports the following:

      * `conditions` (`list`)
        * `name` (`str`)
        * `values` (`list`)

      * `id` (`str`)
      * `names` (`list`)
      * `tags` (`list`)
    """
    __args__ = dict()


    __args__['filter'] = filter
    __args__['zone'] = zone
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('sakuracloud:index/getServer:getServer', __args__, opts=opts).value

    return AwaitableGetServerResult(
        cdrom_id=__ret__.get('cdromId'),
        commitment=__ret__.get('commitment'),
        core=__ret__.get('core'),
        description=__ret__.get('description'),
        disks=__ret__.get('disks'),
        dns_servers=__ret__.get('dnsServers'),
        filter=__ret__.get('filter'),
        gateway=__ret__.get('gateway'),
        hostname=__ret__.get('hostname'),
        icon_id=__ret__.get('iconId'),
        id=__ret__.get('id'),
        interface_driver=__ret__.get('interfaceDriver'),
        ip_address=__ret__.get('ipAddress'),
        memory=__ret__.get('memory'),
        name=__ret__.get('name'),
        netmask=__ret__.get('netmask'),
        network_address=__ret__.get('networkAddress'),
        network_interfaces=__ret__.get('networkInterfaces'),
        private_host_id=__ret__.get('privateHostId'),
        private_host_name=__ret__.get('privateHostName'),
        tags=__ret__.get('tags'),
        zone=__ret__.get('zone'))
