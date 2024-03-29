# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['NFSArgs', 'NFS']

@pulumi.input_type
class NFSArgs:
    def __init__(__self__, *,
                 network_interface: pulumi.Input['NFSNetworkInterfaceArgs'],
                 description: Optional[pulumi.Input[str]] = None,
                 icon_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 plan: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 zone: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a NFS resource.
        :param pulumi.Input['NFSNetworkInterfaceArgs'] network_interface: An `network_interface` block as defined below.
        :param pulumi.Input[str] description: The description of the NFS. The length of this value must be in the range [`1`-`512`].
        :param pulumi.Input[str] icon_id: The icon id to attach to the NFS.
        :param pulumi.Input[str] name: The name of the NFS. The length of this value must be in the range [`1`-`64`].
        :param pulumi.Input[str] plan: The plan name of the NFS. This must be one of [`hdd`/`ssd`]. Changing this forces a new resource to be created. Default:`hdd`.
        :param pulumi.Input[int] size: The size of NFS in GiB. Changing this forces a new resource to be created. Default:`100`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Any tags to assign to the NFS.
        :param pulumi.Input[str] zone: The name of zone that the NFS will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        """
        pulumi.set(__self__, "network_interface", network_interface)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if icon_id is not None:
            pulumi.set(__self__, "icon_id", icon_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if plan is not None:
            pulumi.set(__self__, "plan", plan)
        if size is not None:
            pulumi.set(__self__, "size", size)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if zone is not None:
            pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter(name="networkInterface")
    def network_interface(self) -> pulumi.Input['NFSNetworkInterfaceArgs']:
        """
        An `network_interface` block as defined below.
        """
        return pulumi.get(self, "network_interface")

    @network_interface.setter
    def network_interface(self, value: pulumi.Input['NFSNetworkInterfaceArgs']):
        pulumi.set(self, "network_interface", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the NFS. The length of this value must be in the range [`1`-`512`].
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="iconId")
    def icon_id(self) -> Optional[pulumi.Input[str]]:
        """
        The icon id to attach to the NFS.
        """
        return pulumi.get(self, "icon_id")

    @icon_id.setter
    def icon_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "icon_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the NFS. The length of this value must be in the range [`1`-`64`].
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def plan(self) -> Optional[pulumi.Input[str]]:
        """
        The plan name of the NFS. This must be one of [`hdd`/`ssd`]. Changing this forces a new resource to be created. Default:`hdd`.
        """
        return pulumi.get(self, "plan")

    @plan.setter
    def plan(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "plan", value)

    @property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[int]]:
        """
        The size of NFS in GiB. Changing this forces a new resource to be created. Default:`100`.
        """
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Any tags to assign to the NFS.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[str]]:
        """
        The name of zone that the NFS will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "zone")

    @zone.setter
    def zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone", value)


@pulumi.input_type
class _NFSState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 icon_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_interface: Optional[pulumi.Input['NFSNetworkInterfaceArgs']] = None,
                 plan: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 zone: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering NFS resources.
        :param pulumi.Input[str] description: The description of the NFS. The length of this value must be in the range [`1`-`512`].
        :param pulumi.Input[str] icon_id: The icon id to attach to the NFS.
        :param pulumi.Input[str] name: The name of the NFS. The length of this value must be in the range [`1`-`64`].
        :param pulumi.Input['NFSNetworkInterfaceArgs'] network_interface: An `network_interface` block as defined below.
        :param pulumi.Input[str] plan: The plan name of the NFS. This must be one of [`hdd`/`ssd`]. Changing this forces a new resource to be created. Default:`hdd`.
        :param pulumi.Input[int] size: The size of NFS in GiB. Changing this forces a new resource to be created. Default:`100`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Any tags to assign to the NFS.
        :param pulumi.Input[str] zone: The name of zone that the NFS will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if icon_id is not None:
            pulumi.set(__self__, "icon_id", icon_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if network_interface is not None:
            pulumi.set(__self__, "network_interface", network_interface)
        if plan is not None:
            pulumi.set(__self__, "plan", plan)
        if size is not None:
            pulumi.set(__self__, "size", size)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if zone is not None:
            pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the NFS. The length of this value must be in the range [`1`-`512`].
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="iconId")
    def icon_id(self) -> Optional[pulumi.Input[str]]:
        """
        The icon id to attach to the NFS.
        """
        return pulumi.get(self, "icon_id")

    @icon_id.setter
    def icon_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "icon_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the NFS. The length of this value must be in the range [`1`-`64`].
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="networkInterface")
    def network_interface(self) -> Optional[pulumi.Input['NFSNetworkInterfaceArgs']]:
        """
        An `network_interface` block as defined below.
        """
        return pulumi.get(self, "network_interface")

    @network_interface.setter
    def network_interface(self, value: Optional[pulumi.Input['NFSNetworkInterfaceArgs']]):
        pulumi.set(self, "network_interface", value)

    @property
    @pulumi.getter
    def plan(self) -> Optional[pulumi.Input[str]]:
        """
        The plan name of the NFS. This must be one of [`hdd`/`ssd`]. Changing this forces a new resource to be created. Default:`hdd`.
        """
        return pulumi.get(self, "plan")

    @plan.setter
    def plan(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "plan", value)

    @property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[int]]:
        """
        The size of NFS in GiB. Changing this forces a new resource to be created. Default:`100`.
        """
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Any tags to assign to the NFS.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[str]]:
        """
        The name of zone that the NFS will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "zone")

    @zone.setter
    def zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone", value)


class NFS(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 icon_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_interface: Optional[pulumi.Input[pulumi.InputType['NFSNetworkInterfaceArgs']]] = None,
                 plan: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 zone: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a SakuraCloud NFS.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sakuracloud as sakuracloud

        foobar_switch = sakuracloud.Switch("foobarSwitch")
        foobar_nfs = sakuracloud.NFS("foobarNFS",
            plan="ssd",
            size=500,
            network_interface=sakuracloud.NFSNetworkInterfaceArgs(
                switch_id=foobar_switch.id,
                ip_address="192.168.11.101",
                netmask=24,
                gateway="192.168.11.1",
            ),
            description="description",
            tags=[
                "tag1",
                "tag2",
            ])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the NFS. The length of this value must be in the range [`1`-`512`].
        :param pulumi.Input[str] icon_id: The icon id to attach to the NFS.
        :param pulumi.Input[str] name: The name of the NFS. The length of this value must be in the range [`1`-`64`].
        :param pulumi.Input[pulumi.InputType['NFSNetworkInterfaceArgs']] network_interface: An `network_interface` block as defined below.
        :param pulumi.Input[str] plan: The plan name of the NFS. This must be one of [`hdd`/`ssd`]. Changing this forces a new resource to be created. Default:`hdd`.
        :param pulumi.Input[int] size: The size of NFS in GiB. Changing this forces a new resource to be created. Default:`100`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Any tags to assign to the NFS.
        :param pulumi.Input[str] zone: The name of zone that the NFS will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NFSArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a SakuraCloud NFS.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sakuracloud as sakuracloud

        foobar_switch = sakuracloud.Switch("foobarSwitch")
        foobar_nfs = sakuracloud.NFS("foobarNFS",
            plan="ssd",
            size=500,
            network_interface=sakuracloud.NFSNetworkInterfaceArgs(
                switch_id=foobar_switch.id,
                ip_address="192.168.11.101",
                netmask=24,
                gateway="192.168.11.1",
            ),
            description="description",
            tags=[
                "tag1",
                "tag2",
            ])
        ```

        :param str resource_name: The name of the resource.
        :param NFSArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NFSArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 icon_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_interface: Optional[pulumi.Input[pulumi.InputType['NFSNetworkInterfaceArgs']]] = None,
                 plan: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 zone: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NFSArgs.__new__(NFSArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["icon_id"] = icon_id
            __props__.__dict__["name"] = name
            if network_interface is None and not opts.urn:
                raise TypeError("Missing required property 'network_interface'")
            __props__.__dict__["network_interface"] = network_interface
            __props__.__dict__["plan"] = plan
            __props__.__dict__["size"] = size
            __props__.__dict__["tags"] = tags
            __props__.__dict__["zone"] = zone
        super(NFS, __self__).__init__(
            'sakuracloud:index/nFS:NFS',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            icon_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            network_interface: Optional[pulumi.Input[pulumi.InputType['NFSNetworkInterfaceArgs']]] = None,
            plan: Optional[pulumi.Input[str]] = None,
            size: Optional[pulumi.Input[int]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            zone: Optional[pulumi.Input[str]] = None) -> 'NFS':
        """
        Get an existing NFS resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the NFS. The length of this value must be in the range [`1`-`512`].
        :param pulumi.Input[str] icon_id: The icon id to attach to the NFS.
        :param pulumi.Input[str] name: The name of the NFS. The length of this value must be in the range [`1`-`64`].
        :param pulumi.Input[pulumi.InputType['NFSNetworkInterfaceArgs']] network_interface: An `network_interface` block as defined below.
        :param pulumi.Input[str] plan: The plan name of the NFS. This must be one of [`hdd`/`ssd`]. Changing this forces a new resource to be created. Default:`hdd`.
        :param pulumi.Input[int] size: The size of NFS in GiB. Changing this forces a new resource to be created. Default:`100`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Any tags to assign to the NFS.
        :param pulumi.Input[str] zone: The name of zone that the NFS will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _NFSState.__new__(_NFSState)

        __props__.__dict__["description"] = description
        __props__.__dict__["icon_id"] = icon_id
        __props__.__dict__["name"] = name
        __props__.__dict__["network_interface"] = network_interface
        __props__.__dict__["plan"] = plan
        __props__.__dict__["size"] = size
        __props__.__dict__["tags"] = tags
        __props__.__dict__["zone"] = zone
        return NFS(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the NFS. The length of this value must be in the range [`1`-`512`].
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="iconId")
    def icon_id(self) -> pulumi.Output[Optional[str]]:
        """
        The icon id to attach to the NFS.
        """
        return pulumi.get(self, "icon_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the NFS. The length of this value must be in the range [`1`-`64`].
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkInterface")
    def network_interface(self) -> pulumi.Output['outputs.NFSNetworkInterface']:
        """
        An `network_interface` block as defined below.
        """
        return pulumi.get(self, "network_interface")

    @property
    @pulumi.getter
    def plan(self) -> pulumi.Output[Optional[str]]:
        """
        The plan name of the NFS. This must be one of [`hdd`/`ssd`]. Changing this forces a new resource to be created. Default:`hdd`.
        """
        return pulumi.get(self, "plan")

    @property
    @pulumi.getter
    def size(self) -> pulumi.Output[Optional[int]]:
        """
        The size of NFS in GiB. Changing this forces a new resource to be created. Default:`100`.
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Any tags to assign to the NFS.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def zone(self) -> pulumi.Output[str]:
        """
        The name of zone that the NFS will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "zone")

