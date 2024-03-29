# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['DiskArgs', 'Disk']

@pulumi.input_type
class DiskArgs:
    def __init__(__self__, *,
                 connector: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 distant_froms: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 icon_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 plan: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[int]] = None,
                 source_archive_id: Optional[pulumi.Input[str]] = None,
                 source_disk_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 zone: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Disk resource.
        :param pulumi.Input[str] connector: The name of the disk connector. This must be one of [`virtio`/`ide`]. Changing this forces a new resource to be created. Default:`virtio`.
        :param pulumi.Input[str] description: The description of the disk. The length of this value must be in the range [`1`-`512`].
        :param pulumi.Input[Sequence[pulumi.Input[str]]] distant_froms: A list of disk id. The disk will be located to different storage from these disks. Changing this forces a new resource to be created.
        :param pulumi.Input[str] icon_id: The icon id to attach to the disk.
        :param pulumi.Input[str] name: The name of the disk. The length of this value must be in the range [`1`-`64`].
        :param pulumi.Input[str] plan: The plan name of the disk. This must be one of [`ssd`/`hdd`]. Changing this forces a new resource to be created. Default:`ssd`.
        :param pulumi.Input[int] size: The size of disk in GiB. Changing this forces a new resource to be created. Default:`20`.
        :param pulumi.Input[str] source_archive_id: The id of the source archive. This conflicts with [`source_disk_id`]. Changing this forces a new resource to be created.
        :param pulumi.Input[str] source_disk_id: The id of the source disk. This conflicts with [`source_archive_id`]. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Any tags to assign to the disk.
        :param pulumi.Input[str] zone: The name of zone that the disk will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        """
        if connector is not None:
            pulumi.set(__self__, "connector", connector)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if distant_froms is not None:
            pulumi.set(__self__, "distant_froms", distant_froms)
        if icon_id is not None:
            pulumi.set(__self__, "icon_id", icon_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if plan is not None:
            pulumi.set(__self__, "plan", plan)
        if size is not None:
            pulumi.set(__self__, "size", size)
        if source_archive_id is not None:
            pulumi.set(__self__, "source_archive_id", source_archive_id)
        if source_disk_id is not None:
            pulumi.set(__self__, "source_disk_id", source_disk_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if zone is not None:
            pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter
    def connector(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the disk connector. This must be one of [`virtio`/`ide`]. Changing this forces a new resource to be created. Default:`virtio`.
        """
        return pulumi.get(self, "connector")

    @connector.setter
    def connector(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connector", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the disk. The length of this value must be in the range [`1`-`512`].
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="distantFroms")
    def distant_froms(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of disk id. The disk will be located to different storage from these disks. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "distant_froms")

    @distant_froms.setter
    def distant_froms(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "distant_froms", value)

    @property
    @pulumi.getter(name="iconId")
    def icon_id(self) -> Optional[pulumi.Input[str]]:
        """
        The icon id to attach to the disk.
        """
        return pulumi.get(self, "icon_id")

    @icon_id.setter
    def icon_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "icon_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the disk. The length of this value must be in the range [`1`-`64`].
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def plan(self) -> Optional[pulumi.Input[str]]:
        """
        The plan name of the disk. This must be one of [`ssd`/`hdd`]. Changing this forces a new resource to be created. Default:`ssd`.
        """
        return pulumi.get(self, "plan")

    @plan.setter
    def plan(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "plan", value)

    @property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[int]]:
        """
        The size of disk in GiB. Changing this forces a new resource to be created. Default:`20`.
        """
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter(name="sourceArchiveId")
    def source_archive_id(self) -> Optional[pulumi.Input[str]]:
        """
        The id of the source archive. This conflicts with [`source_disk_id`]. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "source_archive_id")

    @source_archive_id.setter
    def source_archive_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_archive_id", value)

    @property
    @pulumi.getter(name="sourceDiskId")
    def source_disk_id(self) -> Optional[pulumi.Input[str]]:
        """
        The id of the source disk. This conflicts with [`source_archive_id`]. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "source_disk_id")

    @source_disk_id.setter
    def source_disk_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_disk_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Any tags to assign to the disk.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[str]]:
        """
        The name of zone that the disk will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "zone")

    @zone.setter
    def zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone", value)


@pulumi.input_type
class _DiskState:
    def __init__(__self__, *,
                 connector: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 distant_froms: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 icon_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 plan: Optional[pulumi.Input[str]] = None,
                 server_id: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[int]] = None,
                 source_archive_id: Optional[pulumi.Input[str]] = None,
                 source_disk_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 zone: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Disk resources.
        :param pulumi.Input[str] connector: The name of the disk connector. This must be one of [`virtio`/`ide`]. Changing this forces a new resource to be created. Default:`virtio`.
        :param pulumi.Input[str] description: The description of the disk. The length of this value must be in the range [`1`-`512`].
        :param pulumi.Input[Sequence[pulumi.Input[str]]] distant_froms: A list of disk id. The disk will be located to different storage from these disks. Changing this forces a new resource to be created.
        :param pulumi.Input[str] icon_id: The icon id to attach to the disk.
        :param pulumi.Input[str] name: The name of the disk. The length of this value must be in the range [`1`-`64`].
        :param pulumi.Input[str] plan: The plan name of the disk. This must be one of [`ssd`/`hdd`]. Changing this forces a new resource to be created. Default:`ssd`.
        :param pulumi.Input[str] server_id: The id of the Server connected to the disk.
        :param pulumi.Input[int] size: The size of disk in GiB. Changing this forces a new resource to be created. Default:`20`.
        :param pulumi.Input[str] source_archive_id: The id of the source archive. This conflicts with [`source_disk_id`]. Changing this forces a new resource to be created.
        :param pulumi.Input[str] source_disk_id: The id of the source disk. This conflicts with [`source_archive_id`]. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Any tags to assign to the disk.
        :param pulumi.Input[str] zone: The name of zone that the disk will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        """
        if connector is not None:
            pulumi.set(__self__, "connector", connector)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if distant_froms is not None:
            pulumi.set(__self__, "distant_froms", distant_froms)
        if icon_id is not None:
            pulumi.set(__self__, "icon_id", icon_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if plan is not None:
            pulumi.set(__self__, "plan", plan)
        if server_id is not None:
            pulumi.set(__self__, "server_id", server_id)
        if size is not None:
            pulumi.set(__self__, "size", size)
        if source_archive_id is not None:
            pulumi.set(__self__, "source_archive_id", source_archive_id)
        if source_disk_id is not None:
            pulumi.set(__self__, "source_disk_id", source_disk_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if zone is not None:
            pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter
    def connector(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the disk connector. This must be one of [`virtio`/`ide`]. Changing this forces a new resource to be created. Default:`virtio`.
        """
        return pulumi.get(self, "connector")

    @connector.setter
    def connector(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connector", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the disk. The length of this value must be in the range [`1`-`512`].
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="distantFroms")
    def distant_froms(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of disk id. The disk will be located to different storage from these disks. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "distant_froms")

    @distant_froms.setter
    def distant_froms(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "distant_froms", value)

    @property
    @pulumi.getter(name="iconId")
    def icon_id(self) -> Optional[pulumi.Input[str]]:
        """
        The icon id to attach to the disk.
        """
        return pulumi.get(self, "icon_id")

    @icon_id.setter
    def icon_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "icon_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the disk. The length of this value must be in the range [`1`-`64`].
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def plan(self) -> Optional[pulumi.Input[str]]:
        """
        The plan name of the disk. This must be one of [`ssd`/`hdd`]. Changing this forces a new resource to be created. Default:`ssd`.
        """
        return pulumi.get(self, "plan")

    @plan.setter
    def plan(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "plan", value)

    @property
    @pulumi.getter(name="serverId")
    def server_id(self) -> Optional[pulumi.Input[str]]:
        """
        The id of the Server connected to the disk.
        """
        return pulumi.get(self, "server_id")

    @server_id.setter
    def server_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "server_id", value)

    @property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[int]]:
        """
        The size of disk in GiB. Changing this forces a new resource to be created. Default:`20`.
        """
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter(name="sourceArchiveId")
    def source_archive_id(self) -> Optional[pulumi.Input[str]]:
        """
        The id of the source archive. This conflicts with [`source_disk_id`]. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "source_archive_id")

    @source_archive_id.setter
    def source_archive_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_archive_id", value)

    @property
    @pulumi.getter(name="sourceDiskId")
    def source_disk_id(self) -> Optional[pulumi.Input[str]]:
        """
        The id of the source disk. This conflicts with [`source_archive_id`]. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "source_disk_id")

    @source_disk_id.setter
    def source_disk_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_disk_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Any tags to assign to the disk.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[str]]:
        """
        The name of zone that the disk will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "zone")

    @zone.setter
    def zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone", value)


class Disk(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connector: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 distant_froms: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 icon_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 plan: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[int]] = None,
                 source_archive_id: Optional[pulumi.Input[str]] = None,
                 source_disk_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 zone: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a SakuraCloud Disk.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sakuracloud as sakuracloud

        ubuntu = sakuracloud.get_archive(os_type="ubuntu2004")
        foobar = sakuracloud.Disk("foobar",
            plan="ssd",
            connector="virtio",
            size=20,
            source_archive_id=ubuntu.id,
            description="description",
            tags=[
                "tag1",
                "tag2",
            ])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] connector: The name of the disk connector. This must be one of [`virtio`/`ide`]. Changing this forces a new resource to be created. Default:`virtio`.
        :param pulumi.Input[str] description: The description of the disk. The length of this value must be in the range [`1`-`512`].
        :param pulumi.Input[Sequence[pulumi.Input[str]]] distant_froms: A list of disk id. The disk will be located to different storage from these disks. Changing this forces a new resource to be created.
        :param pulumi.Input[str] icon_id: The icon id to attach to the disk.
        :param pulumi.Input[str] name: The name of the disk. The length of this value must be in the range [`1`-`64`].
        :param pulumi.Input[str] plan: The plan name of the disk. This must be one of [`ssd`/`hdd`]. Changing this forces a new resource to be created. Default:`ssd`.
        :param pulumi.Input[int] size: The size of disk in GiB. Changing this forces a new resource to be created. Default:`20`.
        :param pulumi.Input[str] source_archive_id: The id of the source archive. This conflicts with [`source_disk_id`]. Changing this forces a new resource to be created.
        :param pulumi.Input[str] source_disk_id: The id of the source disk. This conflicts with [`source_archive_id`]. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Any tags to assign to the disk.
        :param pulumi.Input[str] zone: The name of zone that the disk will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[DiskArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a SakuraCloud Disk.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sakuracloud as sakuracloud

        ubuntu = sakuracloud.get_archive(os_type="ubuntu2004")
        foobar = sakuracloud.Disk("foobar",
            plan="ssd",
            connector="virtio",
            size=20,
            source_archive_id=ubuntu.id,
            description="description",
            tags=[
                "tag1",
                "tag2",
            ])
        ```

        :param str resource_name: The name of the resource.
        :param DiskArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DiskArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connector: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 distant_froms: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 icon_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 plan: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[int]] = None,
                 source_archive_id: Optional[pulumi.Input[str]] = None,
                 source_disk_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = DiskArgs.__new__(DiskArgs)

            __props__.__dict__["connector"] = connector
            __props__.__dict__["description"] = description
            __props__.__dict__["distant_froms"] = distant_froms
            __props__.__dict__["icon_id"] = icon_id
            __props__.__dict__["name"] = name
            __props__.__dict__["plan"] = plan
            __props__.__dict__["size"] = size
            __props__.__dict__["source_archive_id"] = source_archive_id
            __props__.__dict__["source_disk_id"] = source_disk_id
            __props__.__dict__["tags"] = tags
            __props__.__dict__["zone"] = zone
            __props__.__dict__["server_id"] = None
        super(Disk, __self__).__init__(
            'sakuracloud:index/disk:Disk',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            connector: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            distant_froms: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            icon_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            plan: Optional[pulumi.Input[str]] = None,
            server_id: Optional[pulumi.Input[str]] = None,
            size: Optional[pulumi.Input[int]] = None,
            source_archive_id: Optional[pulumi.Input[str]] = None,
            source_disk_id: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            zone: Optional[pulumi.Input[str]] = None) -> 'Disk':
        """
        Get an existing Disk resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] connector: The name of the disk connector. This must be one of [`virtio`/`ide`]. Changing this forces a new resource to be created. Default:`virtio`.
        :param pulumi.Input[str] description: The description of the disk. The length of this value must be in the range [`1`-`512`].
        :param pulumi.Input[Sequence[pulumi.Input[str]]] distant_froms: A list of disk id. The disk will be located to different storage from these disks. Changing this forces a new resource to be created.
        :param pulumi.Input[str] icon_id: The icon id to attach to the disk.
        :param pulumi.Input[str] name: The name of the disk. The length of this value must be in the range [`1`-`64`].
        :param pulumi.Input[str] plan: The plan name of the disk. This must be one of [`ssd`/`hdd`]. Changing this forces a new resource to be created. Default:`ssd`.
        :param pulumi.Input[str] server_id: The id of the Server connected to the disk.
        :param pulumi.Input[int] size: The size of disk in GiB. Changing this forces a new resource to be created. Default:`20`.
        :param pulumi.Input[str] source_archive_id: The id of the source archive. This conflicts with [`source_disk_id`]. Changing this forces a new resource to be created.
        :param pulumi.Input[str] source_disk_id: The id of the source disk. This conflicts with [`source_archive_id`]. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Any tags to assign to the disk.
        :param pulumi.Input[str] zone: The name of zone that the disk will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DiskState.__new__(_DiskState)

        __props__.__dict__["connector"] = connector
        __props__.__dict__["description"] = description
        __props__.__dict__["distant_froms"] = distant_froms
        __props__.__dict__["icon_id"] = icon_id
        __props__.__dict__["name"] = name
        __props__.__dict__["plan"] = plan
        __props__.__dict__["server_id"] = server_id
        __props__.__dict__["size"] = size
        __props__.__dict__["source_archive_id"] = source_archive_id
        __props__.__dict__["source_disk_id"] = source_disk_id
        __props__.__dict__["tags"] = tags
        __props__.__dict__["zone"] = zone
        return Disk(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def connector(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the disk connector. This must be one of [`virtio`/`ide`]. Changing this forces a new resource to be created. Default:`virtio`.
        """
        return pulumi.get(self, "connector")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the disk. The length of this value must be in the range [`1`-`512`].
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="distantFroms")
    def distant_froms(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of disk id. The disk will be located to different storage from these disks. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "distant_froms")

    @property
    @pulumi.getter(name="iconId")
    def icon_id(self) -> pulumi.Output[Optional[str]]:
        """
        The icon id to attach to the disk.
        """
        return pulumi.get(self, "icon_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the disk. The length of this value must be in the range [`1`-`64`].
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def plan(self) -> pulumi.Output[Optional[str]]:
        """
        The plan name of the disk. This must be one of [`ssd`/`hdd`]. Changing this forces a new resource to be created. Default:`ssd`.
        """
        return pulumi.get(self, "plan")

    @property
    @pulumi.getter(name="serverId")
    def server_id(self) -> pulumi.Output[str]:
        """
        The id of the Server connected to the disk.
        """
        return pulumi.get(self, "server_id")

    @property
    @pulumi.getter
    def size(self) -> pulumi.Output[Optional[int]]:
        """
        The size of disk in GiB. Changing this forces a new resource to be created. Default:`20`.
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter(name="sourceArchiveId")
    def source_archive_id(self) -> pulumi.Output[Optional[str]]:
        """
        The id of the source archive. This conflicts with [`source_disk_id`]. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "source_archive_id")

    @property
    @pulumi.getter(name="sourceDiskId")
    def source_disk_id(self) -> pulumi.Output[Optional[str]]:
        """
        The id of the source disk. This conflicts with [`source_archive_id`]. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "source_disk_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Any tags to assign to the disk.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def zone(self) -> pulumi.Output[str]:
        """
        The name of zone that the disk will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "zone")

