# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class Database(pulumi.CustomResource):
    allow_networks: pulumi.Output[list]
    """
    The network address list that allowed connections to the database.
    """
    backup_time: pulumi.Output[str]
    """
    The time to perform backup (format:`HH:mm`).
    """
    backup_weekdays: pulumi.Output[list]
    """
    Day of the week to get backup.  
    Valid values are the following: ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    """
    database_type: pulumi.Output[str]
    """
    The Database type.  
    Valid value is one of the following: [ "postgresql" (default) / "mariadb"]
    """
    default_route: pulumi.Output[str]
    """
    The default route IP address of the database.
    """
    description: pulumi.Output[str]
    """
    The description of the resource.
    """
    graceful_shutdown_timeout: pulumi.Output[float]
    """
    The wait time (seconds) to do graceful shutdown the Database.
    """
    icon_id: pulumi.Output[str]
    """
    The ID of the icon.
    """
    ipaddress1: pulumi.Output[str]
    """
    The IP address of the database.
    """
    name: pulumi.Output[str]
    """
    The name of the resource.
    """
    nw_mask_len: pulumi.Output[float]
    """
    The network mask length of the database.
    """
    plan: pulumi.Output[str]
    """
    The plan (size) of the Database.   
    Valid value is one of the following: [ "10g" (default) / "30g" / "90g" / "240g" / "500g" / "1t" ]
    """
    port: pulumi.Output[float]
    """
    The number of the port on which the database is listening (default:`5432`).
    """
    replica_password: pulumi.Output[str]
    replica_user: pulumi.Output[str]
    switch_id: pulumi.Output[str]
    """
    The ID of the switch connected to the database.
    """
    tags: pulumi.Output[list]
    """
    The tag list of the resources.
    """
    user_name: pulumi.Output[str]
    """
    The username to access database.
    """
    user_password: pulumi.Output[str]
    """
    The password to access database.
    """
    zone: pulumi.Output[str]
    """
    The ID of the zone to which the resource belongs.
    """
    def __init__(__self__, resource_name, opts=None, allow_networks=None, backup_time=None, backup_weekdays=None, database_type=None, default_route=None, description=None, graceful_shutdown_timeout=None, icon_id=None, ipaddress1=None, name=None, nw_mask_len=None, plan=None, port=None, replica_password=None, switch_id=None, tags=None, user_name=None, user_password=None, zone=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a SakuraCloud Database resource. This can be used to create, update, and delete Databases.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] allow_networks: The network address list that allowed connections to the database.
        :param pulumi.Input[str] backup_time: The time to perform backup (format:`HH:mm`).
        :param pulumi.Input[list] backup_weekdays: Day of the week to get backup.  
               Valid values are the following: ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
        :param pulumi.Input[str] database_type: The Database type.  
               Valid value is one of the following: [ "postgresql" (default) / "mariadb"]
        :param pulumi.Input[str] default_route: The default route IP address of the database.
        :param pulumi.Input[str] description: The description of the resource.
        :param pulumi.Input[float] graceful_shutdown_timeout: The wait time (seconds) to do graceful shutdown the Database.
        :param pulumi.Input[str] icon_id: The ID of the icon.
        :param pulumi.Input[str] ipaddress1: The IP address of the database.
        :param pulumi.Input[str] name: The name of the resource.
        :param pulumi.Input[float] nw_mask_len: The network mask length of the database.
        :param pulumi.Input[str] plan: The plan (size) of the Database.   
               Valid value is one of the following: [ "10g" (default) / "30g" / "90g" / "240g" / "500g" / "1t" ]
        :param pulumi.Input[float] port: The number of the port on which the database is listening (default:`5432`).
        :param pulumi.Input[str] switch_id: The ID of the switch connected to the database.
        :param pulumi.Input[list] tags: The tag list of the resources.
        :param pulumi.Input[str] user_name: The username to access database.
        :param pulumi.Input[str] user_password: The password to access database.
        :param pulumi.Input[str] zone: The ID of the zone to which the resource belongs.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-sakuracloud/blob/master/website/docs/r/database.html.markdown.
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

            __props__['allow_networks'] = allow_networks
            __props__['backup_time'] = backup_time
            __props__['backup_weekdays'] = backup_weekdays
            __props__['database_type'] = database_type
            if default_route is None:
                raise TypeError("Missing required property 'default_route'")
            __props__['default_route'] = default_route
            __props__['description'] = description
            __props__['graceful_shutdown_timeout'] = graceful_shutdown_timeout
            __props__['icon_id'] = icon_id
            if ipaddress1 is None:
                raise TypeError("Missing required property 'ipaddress1'")
            __props__['ipaddress1'] = ipaddress1
            __props__['name'] = name
            if nw_mask_len is None:
                raise TypeError("Missing required property 'nw_mask_len'")
            __props__['nw_mask_len'] = nw_mask_len
            __props__['plan'] = plan
            __props__['port'] = port
            __props__['replica_password'] = replica_password
            if switch_id is None:
                raise TypeError("Missing required property 'switch_id'")
            __props__['switch_id'] = switch_id
            __props__['tags'] = tags
            if user_name is None:
                raise TypeError("Missing required property 'user_name'")
            __props__['user_name'] = user_name
            if user_password is None:
                raise TypeError("Missing required property 'user_password'")
            __props__['user_password'] = user_password
            __props__['zone'] = zone
            __props__['replica_user'] = None
        super(Database, __self__).__init__(
            'sakuracloud:index/database:Database',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, allow_networks=None, backup_time=None, backup_weekdays=None, database_type=None, default_route=None, description=None, graceful_shutdown_timeout=None, icon_id=None, ipaddress1=None, name=None, nw_mask_len=None, plan=None, port=None, replica_password=None, replica_user=None, switch_id=None, tags=None, user_name=None, user_password=None, zone=None):
        """
        Get an existing Database resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] allow_networks: The network address list that allowed connections to the database.
        :param pulumi.Input[str] backup_time: The time to perform backup (format:`HH:mm`).
        :param pulumi.Input[list] backup_weekdays: Day of the week to get backup.  
               Valid values are the following: ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
        :param pulumi.Input[str] database_type: The Database type.  
               Valid value is one of the following: [ "postgresql" (default) / "mariadb"]
        :param pulumi.Input[str] default_route: The default route IP address of the database.
        :param pulumi.Input[str] description: The description of the resource.
        :param pulumi.Input[float] graceful_shutdown_timeout: The wait time (seconds) to do graceful shutdown the Database.
        :param pulumi.Input[str] icon_id: The ID of the icon.
        :param pulumi.Input[str] ipaddress1: The IP address of the database.
        :param pulumi.Input[str] name: The name of the resource.
        :param pulumi.Input[float] nw_mask_len: The network mask length of the database.
        :param pulumi.Input[str] plan: The plan (size) of the Database.   
               Valid value is one of the following: [ "10g" (default) / "30g" / "90g" / "240g" / "500g" / "1t" ]
        :param pulumi.Input[float] port: The number of the port on which the database is listening (default:`5432`).
        :param pulumi.Input[str] switch_id: The ID of the switch connected to the database.
        :param pulumi.Input[list] tags: The tag list of the resources.
        :param pulumi.Input[str] user_name: The username to access database.
        :param pulumi.Input[str] user_password: The password to access database.
        :param pulumi.Input[str] zone: The ID of the zone to which the resource belongs.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-sakuracloud/blob/master/website/docs/r/database.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["allow_networks"] = allow_networks
        __props__["backup_time"] = backup_time
        __props__["backup_weekdays"] = backup_weekdays
        __props__["database_type"] = database_type
        __props__["default_route"] = default_route
        __props__["description"] = description
        __props__["graceful_shutdown_timeout"] = graceful_shutdown_timeout
        __props__["icon_id"] = icon_id
        __props__["ipaddress1"] = ipaddress1
        __props__["name"] = name
        __props__["nw_mask_len"] = nw_mask_len
        __props__["plan"] = plan
        __props__["port"] = port
        __props__["replica_password"] = replica_password
        __props__["replica_user"] = replica_user
        __props__["switch_id"] = switch_id
        __props__["tags"] = tags
        __props__["user_name"] = user_name
        __props__["user_password"] = user_password
        __props__["zone"] = zone
        return Database(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

