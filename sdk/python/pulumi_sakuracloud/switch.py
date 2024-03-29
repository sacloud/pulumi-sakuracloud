# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['SwitchArgs', 'Switch']

@pulumi.input_type
class SwitchArgs:
    def __init__(__self__, *,
                 bridge_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 icon_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 zone: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Switch resource.
        :param pulumi.Input[str] bridge_id: The bridge id attached to the Switch.
        :param pulumi.Input[str] description: The description of the Switch. The length of this value must be in the range [`1`-`512`].
        :param pulumi.Input[str] icon_id: The icon id to attach to the Switch.
        :param pulumi.Input[str] name: The name of the Switch. The length of this value must be in the range [`1`-`64`].
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Any tags to assign to the Switch.
        :param pulumi.Input[str] zone: The name of zone that the Switch will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        """
        if bridge_id is not None:
            pulumi.set(__self__, "bridge_id", bridge_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if icon_id is not None:
            pulumi.set(__self__, "icon_id", icon_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if zone is not None:
            pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter(name="bridgeId")
    def bridge_id(self) -> Optional[pulumi.Input[str]]:
        """
        The bridge id attached to the Switch.
        """
        return pulumi.get(self, "bridge_id")

    @bridge_id.setter
    def bridge_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bridge_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the Switch. The length of this value must be in the range [`1`-`512`].
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="iconId")
    def icon_id(self) -> Optional[pulumi.Input[str]]:
        """
        The icon id to attach to the Switch.
        """
        return pulumi.get(self, "icon_id")

    @icon_id.setter
    def icon_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "icon_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Switch. The length of this value must be in the range [`1`-`64`].
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Any tags to assign to the Switch.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[str]]:
        """
        The name of zone that the Switch will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "zone")

    @zone.setter
    def zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone", value)


@pulumi.input_type
class _SwitchState:
    def __init__(__self__, *,
                 bridge_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 icon_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 server_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 zone: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Switch resources.
        :param pulumi.Input[str] bridge_id: The bridge id attached to the Switch.
        :param pulumi.Input[str] description: The description of the Switch. The length of this value must be in the range [`1`-`512`].
        :param pulumi.Input[str] icon_id: The icon id to attach to the Switch.
        :param pulumi.Input[str] name: The name of the Switch. The length of this value must be in the range [`1`-`64`].
        :param pulumi.Input[Sequence[pulumi.Input[str]]] server_ids: A list of server id connected to the switch.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Any tags to assign to the Switch.
        :param pulumi.Input[str] zone: The name of zone that the Switch will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        """
        if bridge_id is not None:
            pulumi.set(__self__, "bridge_id", bridge_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if icon_id is not None:
            pulumi.set(__self__, "icon_id", icon_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if server_ids is not None:
            pulumi.set(__self__, "server_ids", server_ids)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if zone is not None:
            pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter(name="bridgeId")
    def bridge_id(self) -> Optional[pulumi.Input[str]]:
        """
        The bridge id attached to the Switch.
        """
        return pulumi.get(self, "bridge_id")

    @bridge_id.setter
    def bridge_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bridge_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the Switch. The length of this value must be in the range [`1`-`512`].
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="iconId")
    def icon_id(self) -> Optional[pulumi.Input[str]]:
        """
        The icon id to attach to the Switch.
        """
        return pulumi.get(self, "icon_id")

    @icon_id.setter
    def icon_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "icon_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Switch. The length of this value must be in the range [`1`-`64`].
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="serverIds")
    def server_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of server id connected to the switch.
        """
        return pulumi.get(self, "server_ids")

    @server_ids.setter
    def server_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "server_ids", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Any tags to assign to the Switch.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[str]]:
        """
        The name of zone that the Switch will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "zone")

    @zone.setter
    def zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone", value)


class Switch(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bridge_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 icon_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 zone: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a SakuraCloud Switch.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sakuracloud as sakuracloud

        foobar = sakuracloud.Switch("foobar",
            description="description",
            tags=[
                "tag1",
                "tag2",
            ])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bridge_id: The bridge id attached to the Switch.
        :param pulumi.Input[str] description: The description of the Switch. The length of this value must be in the range [`1`-`512`].
        :param pulumi.Input[str] icon_id: The icon id to attach to the Switch.
        :param pulumi.Input[str] name: The name of the Switch. The length of this value must be in the range [`1`-`64`].
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Any tags to assign to the Switch.
        :param pulumi.Input[str] zone: The name of zone that the Switch will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[SwitchArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a SakuraCloud Switch.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sakuracloud as sakuracloud

        foobar = sakuracloud.Switch("foobar",
            description="description",
            tags=[
                "tag1",
                "tag2",
            ])
        ```

        :param str resource_name: The name of the resource.
        :param SwitchArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SwitchArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bridge_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 icon_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
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
            __props__ = SwitchArgs.__new__(SwitchArgs)

            __props__.__dict__["bridge_id"] = bridge_id
            __props__.__dict__["description"] = description
            __props__.__dict__["icon_id"] = icon_id
            __props__.__dict__["name"] = name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["zone"] = zone
            __props__.__dict__["server_ids"] = None
        super(Switch, __self__).__init__(
            'sakuracloud:index/switch:Switch',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            bridge_id: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            icon_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            server_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            zone: Optional[pulumi.Input[str]] = None) -> 'Switch':
        """
        Get an existing Switch resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bridge_id: The bridge id attached to the Switch.
        :param pulumi.Input[str] description: The description of the Switch. The length of this value must be in the range [`1`-`512`].
        :param pulumi.Input[str] icon_id: The icon id to attach to the Switch.
        :param pulumi.Input[str] name: The name of the Switch. The length of this value must be in the range [`1`-`64`].
        :param pulumi.Input[Sequence[pulumi.Input[str]]] server_ids: A list of server id connected to the switch.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Any tags to assign to the Switch.
        :param pulumi.Input[str] zone: The name of zone that the Switch will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SwitchState.__new__(_SwitchState)

        __props__.__dict__["bridge_id"] = bridge_id
        __props__.__dict__["description"] = description
        __props__.__dict__["icon_id"] = icon_id
        __props__.__dict__["name"] = name
        __props__.__dict__["server_ids"] = server_ids
        __props__.__dict__["tags"] = tags
        __props__.__dict__["zone"] = zone
        return Switch(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="bridgeId")
    def bridge_id(self) -> pulumi.Output[Optional[str]]:
        """
        The bridge id attached to the Switch.
        """
        return pulumi.get(self, "bridge_id")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the Switch. The length of this value must be in the range [`1`-`512`].
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="iconId")
    def icon_id(self) -> pulumi.Output[Optional[str]]:
        """
        The icon id to attach to the Switch.
        """
        return pulumi.get(self, "icon_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Switch. The length of this value must be in the range [`1`-`64`].
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="serverIds")
    def server_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of server id connected to the switch.
        """
        return pulumi.get(self, "server_ids")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Any tags to assign to the Switch.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def zone(self) -> pulumi.Output[str]:
        """
        The name of zone that the Switch will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "zone")

