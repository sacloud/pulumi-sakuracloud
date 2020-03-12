# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class GetSSHKeyResult:
    """
    A collection of values returned by getSSHKey.
    """
    def __init__(__self__, description=None, filter=None, fingerprint=None, id=None, name=None, public_key=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        __self__.description = description
        if filter and not isinstance(filter, dict):
            raise TypeError("Expected argument 'filter' to be a dict")
        __self__.filter = filter
        if fingerprint and not isinstance(fingerprint, str):
            raise TypeError("Expected argument 'fingerprint' to be a str")
        __self__.fingerprint = fingerprint
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        if public_key and not isinstance(public_key, str):
            raise TypeError("Expected argument 'public_key' to be a str")
        __self__.public_key = public_key
class AwaitableGetSSHKeyResult(GetSSHKeyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSSHKeyResult(
            description=self.description,
            filter=self.filter,
            fingerprint=self.fingerprint,
            id=self.id,
            name=self.name,
            public_key=self.public_key)

def get_ssh_key(filter=None,opts=None):
    """
    Use this data source to access information about an existing resource.


    The **filter** object supports the following:

      * `conditions` (`list`)
        * `name` (`str`)
        * `values` (`list`)

      * `id` (`str`)
      * `names` (`list`)
    """
    __args__ = dict()


    __args__['filter'] = filter
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('sakuracloud:index/getSSHKey:getSSHKey', __args__, opts=opts).value

    return AwaitableGetSSHKeyResult(
        description=__ret__.get('description'),
        filter=__ret__.get('filter'),
        fingerprint=__ret__.get('fingerprint'),
        id=__ret__.get('id'),
        name=__ret__.get('name'),
        public_key=__ret__.get('publicKey'))
