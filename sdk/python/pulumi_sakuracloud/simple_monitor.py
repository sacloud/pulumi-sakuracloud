# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class SimpleMonitor(pulumi.CustomResource):
    description: pulumi.Output[str]
    """
    The description of the resource.
    """
    enabled: pulumi.Output[bool]
    """
    The flag of enable/disable monitoring.
    """
    health_check: pulumi.Output[dict]
    """
    Health check rules. It contains some attributes to Health Check.
    
      * `community` (`str`) - The community name used in snmp health check.
      * `delayLoop` (`float`) - Health check access interval (unit:`second`). 
      * `excepctedData` (`str`) - The expect value used in dns/snmp health check.
      * `hostHeader` (`str`) - The value of `Host` header used in http/https health check access.
      * `oid` (`str`) - The OID used in snmp health check.
      * `password` (`str`) - The Basic Auth Password request path used in http/https health check access.
      * `path` (`str`) - The request path used in http/https health check access.
      * `port` (`float`) - Port number used in health check access.
      * `protocol` (`str`) - Protocol used in health check.  
        Valid value is one of the following: [ "http" / "https" / "ping" / "tcp" / "dns" / "ssh" / "smtp" / "pop3" / "snmp" / "sslcertificate" ]
      * `qname` (`str`) - The QName value used in dns health check access.
      * `remainingDays` (`float`) - The number of remaining days used in ssh-certificate check.
      * `sni` (`bool`) - The flag of enable/disable SNI.
      * `snmpVersion` (`str`) - SNMP cersion used in snmp health check.
      * `status` (`str`) - HTTP status code expected by health check access.
      * `username` (`str`) - The Basic Auth Username used in http/https health check access.
    """
    icon_id: pulumi.Output[str]
    """
    The ID of the icon of the resource.
    """
    notify_email_enabled: pulumi.Output[bool]
    """
    The flag of enable/disable notification by E-mail.
    """
    notify_email_html: pulumi.Output[bool]
    """
    The flag of enable/disable HTML format for E-mail.
    """
    notify_slack_enabled: pulumi.Output[bool]
    """
    The flag of enable/disable notification by slack.
    """
    notify_slack_webhook: pulumi.Output[str]
    """
    The webhook URL of destination of slack notification.
    """
    tags: pulumi.Output[list]
    """
    The tag list of the resources.
    """
    target: pulumi.Output[str]
    """
    The HostName or IP address of monitoring target.
    """
    def __init__(__self__, resource_name, opts=None, description=None, enabled=None, health_check=None, icon_id=None, notify_email_enabled=None, notify_email_html=None, notify_slack_enabled=None, notify_slack_webhook=None, tags=None, target=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a SakuraCloud Simple Monitor resource. This can be used to create, update, and delete Simple Monitors.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the resource.
        :param pulumi.Input[bool] enabled: The flag of enable/disable monitoring.
        :param pulumi.Input[dict] health_check: Health check rules. It contains some attributes to Health Check.
        :param pulumi.Input[str] icon_id: The ID of the icon of the resource.
        :param pulumi.Input[bool] notify_email_enabled: The flag of enable/disable notification by E-mail.
        :param pulumi.Input[bool] notify_email_html: The flag of enable/disable HTML format for E-mail.
        :param pulumi.Input[bool] notify_slack_enabled: The flag of enable/disable notification by slack.
        :param pulumi.Input[str] notify_slack_webhook: The webhook URL of destination of slack notification.
        :param pulumi.Input[list] tags: The tag list of the resources.
        :param pulumi.Input[str] target: The HostName or IP address of monitoring target.
        
        The **health_check** object supports the following:
        
          * `community` (`pulumi.Input[str]`) - The community name used in snmp health check.
          * `delayLoop` (`pulumi.Input[float]`) - Health check access interval (unit:`second`). 
          * `excepctedData` (`pulumi.Input[str]`) - The expect value used in dns/snmp health check.
          * `hostHeader` (`pulumi.Input[str]`) - The value of `Host` header used in http/https health check access.
          * `oid` (`pulumi.Input[str]`) - The OID used in snmp health check.
          * `password` (`pulumi.Input[str]`) - The Basic Auth Password request path used in http/https health check access.
          * `path` (`pulumi.Input[str]`) - The request path used in http/https health check access.
          * `port` (`pulumi.Input[float]`) - Port number used in health check access.
          * `protocol` (`pulumi.Input[str]`) - Protocol used in health check.  
            Valid value is one of the following: [ "http" / "https" / "ping" / "tcp" / "dns" / "ssh" / "smtp" / "pop3" / "snmp" / "sslcertificate" ]
          * `qname` (`pulumi.Input[str]`) - The QName value used in dns health check access.
          * `remainingDays` (`pulumi.Input[float]`) - The number of remaining days used in ssh-certificate check.
          * `sni` (`pulumi.Input[bool]`) - The flag of enable/disable SNI.
          * `snmpVersion` (`pulumi.Input[str]`) - SNMP cersion used in snmp health check.
          * `status` (`pulumi.Input[str]`) - HTTP status code expected by health check access.
          * `username` (`pulumi.Input[str]`) - The Basic Auth Username used in http/https health check access.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-sakuracloud/blob/master/website/docs/r/simple_monitor.html.markdown.
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
            __props__['enabled'] = enabled
            if health_check is None:
                raise TypeError("Missing required property 'health_check'")
            __props__['health_check'] = health_check
            __props__['icon_id'] = icon_id
            __props__['notify_email_enabled'] = notify_email_enabled
            __props__['notify_email_html'] = notify_email_html
            __props__['notify_slack_enabled'] = notify_slack_enabled
            __props__['notify_slack_webhook'] = notify_slack_webhook
            __props__['tags'] = tags
            if target is None:
                raise TypeError("Missing required property 'target'")
            __props__['target'] = target
        super(SimpleMonitor, __self__).__init__(
            'sakuracloud:index/simpleMonitor:SimpleMonitor',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, description=None, enabled=None, health_check=None, icon_id=None, notify_email_enabled=None, notify_email_html=None, notify_slack_enabled=None, notify_slack_webhook=None, tags=None, target=None):
        """
        Get an existing SimpleMonitor resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the resource.
        :param pulumi.Input[bool] enabled: The flag of enable/disable monitoring.
        :param pulumi.Input[dict] health_check: Health check rules. It contains some attributes to Health Check.
        :param pulumi.Input[str] icon_id: The ID of the icon of the resource.
        :param pulumi.Input[bool] notify_email_enabled: The flag of enable/disable notification by E-mail.
        :param pulumi.Input[bool] notify_email_html: The flag of enable/disable HTML format for E-mail.
        :param pulumi.Input[bool] notify_slack_enabled: The flag of enable/disable notification by slack.
        :param pulumi.Input[str] notify_slack_webhook: The webhook URL of destination of slack notification.
        :param pulumi.Input[list] tags: The tag list of the resources.
        :param pulumi.Input[str] target: The HostName or IP address of monitoring target.
        
        The **health_check** object supports the following:
        
          * `community` (`pulumi.Input[str]`) - The community name used in snmp health check.
          * `delayLoop` (`pulumi.Input[float]`) - Health check access interval (unit:`second`). 
          * `excepctedData` (`pulumi.Input[str]`) - The expect value used in dns/snmp health check.
          * `hostHeader` (`pulumi.Input[str]`) - The value of `Host` header used in http/https health check access.
          * `oid` (`pulumi.Input[str]`) - The OID used in snmp health check.
          * `password` (`pulumi.Input[str]`) - The Basic Auth Password request path used in http/https health check access.
          * `path` (`pulumi.Input[str]`) - The request path used in http/https health check access.
          * `port` (`pulumi.Input[float]`) - Port number used in health check access.
          * `protocol` (`pulumi.Input[str]`) - Protocol used in health check.  
            Valid value is one of the following: [ "http" / "https" / "ping" / "tcp" / "dns" / "ssh" / "smtp" / "pop3" / "snmp" / "sslcertificate" ]
          * `qname` (`pulumi.Input[str]`) - The QName value used in dns health check access.
          * `remainingDays` (`pulumi.Input[float]`) - The number of remaining days used in ssh-certificate check.
          * `sni` (`pulumi.Input[bool]`) - The flag of enable/disable SNI.
          * `snmpVersion` (`pulumi.Input[str]`) - SNMP cersion used in snmp health check.
          * `status` (`pulumi.Input[str]`) - HTTP status code expected by health check access.
          * `username` (`pulumi.Input[str]`) - The Basic Auth Username used in http/https health check access.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-sakuracloud/blob/master/website/docs/r/simple_monitor.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["description"] = description
        __props__["enabled"] = enabled
        __props__["health_check"] = health_check
        __props__["icon_id"] = icon_id
        __props__["notify_email_enabled"] = notify_email_enabled
        __props__["notify_email_html"] = notify_email_html
        __props__["notify_slack_enabled"] = notify_slack_enabled
        __props__["notify_slack_webhook"] = notify_slack_webhook
        __props__["tags"] = tags
        __props__["target"] = target
        return SimpleMonitor(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
