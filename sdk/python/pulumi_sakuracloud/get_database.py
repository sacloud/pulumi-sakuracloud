# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class GetDatabaseResult:
    """
    A collection of values returned by getDatabase.
    """
    def __init__(__self__, allow_networks=None, backup_time=None, backup_weekdays=None, default_route=None, description=None, filters=None, icon_id=None, ipaddress1=None, name=None, name_selectors=None, nw_mask_len=None, plan=None, port=None, replica_password=None, replica_user=None, switch_id=None, tag_selectors=None, tags=None, user_name=None, user_password=None, zone=None, id=None):
        if allow_networks and not isinstance(allow_networks, list):
            raise TypeError("Expected argument 'allow_networks' to be a list")
        __self__.allow_networks = allow_networks
        """
        The network address list that allowed connections to the database.
        """
        if backup_time and not isinstance(backup_time, str):
            raise TypeError("Expected argument 'backup_time' to be a str")
        __self__.backup_time = backup_time
        """
        The time to perform backup.
        """
        if backup_weekdays and not isinstance(backup_weekdays, list):
            raise TypeError("Expected argument 'backup_weekdays' to be a list")
        __self__.backup_weekdays = backup_weekdays
        """
        Day of the week to get backup.  
        """
        if default_route and not isinstance(default_route, str):
            raise TypeError("Expected argument 'default_route' to be a str")
        __self__.default_route = default_route
        """
        The default route IP address of the database.
        """
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        __self__.description = description
        """
        The description of the resource.
        """
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        __self__.filters = filters
        if icon_id and not isinstance(icon_id, str):
            raise TypeError("Expected argument 'icon_id' to be a str")
        __self__.icon_id = icon_id
        """
        The ID of the icon of the resource.
        """
        if ipaddress1 and not isinstance(ipaddress1, str):
            raise TypeError("Expected argument 'ipaddress1' to be a str")
        __self__.ipaddress1 = ipaddress1
        """
        The IP address of the database.
        """
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        """
        The name of the resource.
        """
        if name_selectors and not isinstance(name_selectors, list):
            raise TypeError("Expected argument 'name_selectors' to be a list")
        __self__.name_selectors = name_selectors
        if nw_mask_len and not isinstance(nw_mask_len, float):
            raise TypeError("Expected argument 'nw_mask_len' to be a float")
        __self__.nw_mask_len = nw_mask_len
        """
        The network mask length of the database.
        """
        if plan and not isinstance(plan, str):
            raise TypeError("Expected argument 'plan' to be a str")
        __self__.plan = plan
        """
        The name of the resource plan.
        """
        if port and not isinstance(port, float):
            raise TypeError("Expected argument 'port' to be a float")
        __self__.port = port
        """
        The number of the port on which the database is listening.
        """
        if replica_password and not isinstance(replica_password, str):
            raise TypeError("Expected argument 'replica_password' to be a str")
        __self__.replica_password = replica_password
        if replica_user and not isinstance(replica_user, str):
            raise TypeError("Expected argument 'replica_user' to be a str")
        __self__.replica_user = replica_user
        if switch_id and not isinstance(switch_id, str):
            raise TypeError("Expected argument 'switch_id' to be a str")
        __self__.switch_id = switch_id
        """
        The ID of the switch connected to the database.
        """
        if tag_selectors and not isinstance(tag_selectors, list):
            raise TypeError("Expected argument 'tag_selectors' to be a list")
        __self__.tag_selectors = tag_selectors
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        __self__.tags = tags
        """
        The tag list of the resources.
        """
        if user_name and not isinstance(user_name, str):
            raise TypeError("Expected argument 'user_name' to be a str")
        __self__.user_name = user_name
        """
        The username to access database.
        """
        if user_password and not isinstance(user_password, str):
            raise TypeError("Expected argument 'user_password' to be a str")
        __self__.user_password = user_password
        """
        The password to access database.
        """
        if zone and not isinstance(zone, str):
            raise TypeError("Expected argument 'zone' to be a str")
        __self__.zone = zone
        """
        The ID of the zone to which the resource belongs.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """
class AwaitableGetDatabaseResult(GetDatabaseResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDatabaseResult(
            allow_networks=self.allow_networks,
            backup_time=self.backup_time,
            backup_weekdays=self.backup_weekdays,
            default_route=self.default_route,
            description=self.description,
            filters=self.filters,
            icon_id=self.icon_id,
            ipaddress1=self.ipaddress1,
            name=self.name,
            name_selectors=self.name_selectors,
            nw_mask_len=self.nw_mask_len,
            plan=self.plan,
            port=self.port,
            replica_password=self.replica_password,
            replica_user=self.replica_user,
            switch_id=self.switch_id,
            tag_selectors=self.tag_selectors,
            tags=self.tags,
            user_name=self.user_name,
            user_password=self.user_password,
            zone=self.zone,
            id=self.id)

def get_database(filters=None,name_selectors=None,tag_selectors=None,zone=None,opts=None):
    """
    Use this data source to retrieve information about a SakuraCloud Database.
    
    :param list filters: The map of filter key and value.
    :param list name_selectors: The list of names to filtering.
    :param list tag_selectors: The list of tags to filtering.
    :param str zone: The ID of the zone.
    
    The **filters** object supports the following:
    
      * `name` (`str`) - The name of the resource.
      * `values` (`list`)

    > This content is derived from https://github.com/terraform-providers/terraform-provider-sakuracloud/blob/master/website/docs/d/database.html.markdown.
    """
    __args__ = dict()

    __args__['filters'] = filters
    __args__['nameSelectors'] = name_selectors
    __args__['tagSelectors'] = tag_selectors
    __args__['zone'] = zone
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('sakuracloud:index/getDatabase:getDatabase', __args__, opts=opts).value

    return AwaitableGetDatabaseResult(
        allow_networks=__ret__.get('allowNetworks'),
        backup_time=__ret__.get('backupTime'),
        backup_weekdays=__ret__.get('backupWeekdays'),
        default_route=__ret__.get('defaultRoute'),
        description=__ret__.get('description'),
        filters=__ret__.get('filters'),
        icon_id=__ret__.get('iconId'),
        ipaddress1=__ret__.get('ipaddress1'),
        name=__ret__.get('name'),
        name_selectors=__ret__.get('nameSelectors'),
        nw_mask_len=__ret__.get('nwMaskLen'),
        plan=__ret__.get('plan'),
        port=__ret__.get('port'),
        replica_password=__ret__.get('replicaPassword'),
        replica_user=__ret__.get('replicaUser'),
        switch_id=__ret__.get('switchId'),
        tag_selectors=__ret__.get('tagSelectors'),
        tags=__ret__.get('tags'),
        user_name=__ret__.get('userName'),
        user_password=__ret__.get('userPassword'),
        zone=__ret__.get('zone'),
        id=__ret__.get('id'))
