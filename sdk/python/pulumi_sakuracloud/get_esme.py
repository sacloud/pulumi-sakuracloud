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
    'GetESMEResult',
    'AwaitableGetESMEResult',
    'get_esme',
]

@pulumi.output_type
class GetESMEResult:
    """
    A collection of values returned by getESME.
    """
    def __init__(__self__, description=None, filter=None, icon_id=None, id=None, name=None, send_message_with_generated_otp_api_url=None, send_message_with_inputted_otp_api_url=None, tags=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if filter and not isinstance(filter, dict):
            raise TypeError("Expected argument 'filter' to be a dict")
        pulumi.set(__self__, "filter", filter)
        if icon_id and not isinstance(icon_id, str):
            raise TypeError("Expected argument 'icon_id' to be a str")
        pulumi.set(__self__, "icon_id", icon_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if send_message_with_generated_otp_api_url and not isinstance(send_message_with_generated_otp_api_url, str):
            raise TypeError("Expected argument 'send_message_with_generated_otp_api_url' to be a str")
        pulumi.set(__self__, "send_message_with_generated_otp_api_url", send_message_with_generated_otp_api_url)
        if send_message_with_inputted_otp_api_url and not isinstance(send_message_with_inputted_otp_api_url, str):
            raise TypeError("Expected argument 'send_message_with_inputted_otp_api_url' to be a str")
        pulumi.set(__self__, "send_message_with_inputted_otp_api_url", send_message_with_inputted_otp_api_url)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The description of the ESME.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def filter(self) -> Optional['outputs.GetESMEFilterResult']:
        return pulumi.get(self, "filter")

    @property
    @pulumi.getter(name="iconId")
    def icon_id(self) -> str:
        """
        The icon id attached to the ESME.
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
        The name of the ESME.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="sendMessageWithGeneratedOtpApiUrl")
    def send_message_with_generated_otp_api_url(self) -> str:
        """
        The API URL for send SMS with generated OTP.
        """
        return pulumi.get(self, "send_message_with_generated_otp_api_url")

    @property
    @pulumi.getter(name="sendMessageWithInputtedOtpApiUrl")
    def send_message_with_inputted_otp_api_url(self) -> str:
        """
        The API URL for send SMS with inputted OTP.
        """
        return pulumi.get(self, "send_message_with_inputted_otp_api_url")

    @property
    @pulumi.getter
    def tags(self) -> Sequence[str]:
        """
        Any tags assigned to the ESME.
        """
        return pulumi.get(self, "tags")


class AwaitableGetESMEResult(GetESMEResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetESMEResult(
            description=self.description,
            filter=self.filter,
            icon_id=self.icon_id,
            id=self.id,
            name=self.name,
            send_message_with_generated_otp_api_url=self.send_message_with_generated_otp_api_url,
            send_message_with_inputted_otp_api_url=self.send_message_with_inputted_otp_api_url,
            tags=self.tags)


def get_esme(filter: Optional[pulumi.InputType['GetESMEFilterArgs']] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetESMEResult:
    """
    Get information about an existing ESME.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_sakuracloud as sakuracloud

    foobar = sakuracloud.get_esme(filter=sakuracloud.GetESMEFilterArgs(
        names=["foobar"],
    ))
    ```


    :param pulumi.InputType['GetESMEFilterArgs'] filter: One or more values used for filtering, as defined below.
    """
    __args__ = dict()
    __args__['filter'] = filter
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('sakuracloud:index/getESME:getESME', __args__, opts=opts, typ=GetESMEResult).value

    return AwaitableGetESMEResult(
        description=__ret__.description,
        filter=__ret__.filter,
        icon_id=__ret__.icon_id,
        id=__ret__.id,
        name=__ret__.name,
        send_message_with_generated_otp_api_url=__ret__.send_message_with_generated_otp_api_url,
        send_message_with_inputted_otp_api_url=__ret__.send_message_with_inputted_otp_api_url,
        tags=__ret__.tags)
