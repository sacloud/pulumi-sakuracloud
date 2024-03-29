# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

acceptLanguage: Optional[str]
"""
The value of AcceptLanguage header used when calling SakuraCloud API. It can also be sourced from the
`SAKURACLOUD_ACCEPT_LANGUAGE` environment variables, or via a shared credentials file if `profile` is specified
"""

apiRequestRateLimit: Optional[int]
"""
The maximum number of SakuraCloud API calls per second. It can also be sourced from the `SAKURACLOUD_RATE_LIMIT`
environment variables, or via a shared credentials file if `profile` is specified. Default:`10`
"""

apiRequestTimeout: Optional[int]
"""
The timeout seconds for each SakuraCloud API call. It can also be sourced from the `SAKURACLOUD_API_REQUEST_TIMEOUT`
environment variables, or via a shared credentials file if `profile` is specified. Default:`300`
"""

apiRootUrl: Optional[str]
"""
The root URL of SakuraCloud API. It can also be sourced from the `SAKURACLOUD_API_ROOT_URL` environment variables, or
via a shared credentials file if `profile` is specified. Default:`https://secure.sakura.ad.jp/cloud/zone`
"""

defaultZone: Optional[str]
"""
The name of zone to use as default for global resources. It must be provided, but it can also be sourced from the
`SAKURACLOUD_DEFAULT_ZONE` environment variables, or via a shared credentials file if `profile` is specified
"""

fakeMode: Optional[str]
"""
The flag to enable fake of SakuraCloud API call. It is for debugging or developping the provider. It can also be sourced
from the `FAKE_MODE` environment variables, or via a shared credentials file if `profile` is specified
"""

fakeStorePath: Optional[str]
"""
The file path used by SakuraCloud API fake driver for storing fake data. It is for debugging or developping the
provider. It can also be sourced from the `FAKE_STORE_PATH` environment variables, or via a shared credentials file if
`profile` is specified
"""

profile: str
"""
The profile name of your SakuraCloud account. Default:`default`
"""

retryMax: Optional[int]
"""
The maximum number of API call retries used when SakuraCloud API returns status code `423` or `503`. It can also be
sourced from the `SAKURACLOUD_RETRY_MAX` environment variables, or via a shared credentials file if `profile` is
specified. Default:`100`
"""

retryWaitMax: Optional[int]
"""
The maximum wait interval(in seconds) for retrying API call used when SakuraCloud API returns status code `423` or
`503`. It can also be sourced from the `SAKURACLOUD_RETRY_WAIT_MAX` environment variables, or via a shared credentials
file if `profile` is specified
"""

retryWaitMin: Optional[int]
"""
The minimum wait interval(in seconds) for retrying API call used when SakuraCloud API returns status code `423` or
`503`. It can also be sourced from the `SAKURACLOUD_RETRY_WAIT_MIN` environment variables, or via a shared credentials
file if `profile` is specified
"""

secret: str
"""
The API secret of your SakuraCloud account. It must be provided, but it can also be sourced from the
`SAKURACLOUD_ACCESS_TOKEN_SECRET` environment variables, or via a shared credentials file if `profile` is specified
"""

token: str
"""
The API token of your SakuraCloud account. It must be provided, but it can also be sourced from the
`SAKURACLOUD_ACCESS_TOKEN` environment variables, or via a shared credentials file if `profile` is specified
"""

trace: Optional[str]
"""
The flag to enable output trace log. It can also be sourced from the `SAKURACLOUD_TRACE` environment variables, or via a
shared credentials file if `profile` is specified
"""

zone: str
"""
The name of zone to use as default. It must be provided, but it can also be sourced from the `SAKURACLOUD_ZONE`
environment variables, or via a shared credentials file if `profile` is specified
"""

zones: Optional[str]
"""
A list of available SakuraCloud zone name. It can also be sourced via a shared credentials file if `profile` is
specified. Default:[`is1a`, `is1b`, `tk1a`, `tk1v`]
"""

