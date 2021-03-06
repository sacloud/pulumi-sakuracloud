# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = ['Disk']


class Disk(pulumi.CustomResource):
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
                 __props__=None,
                 __name__=None,
                 __opts__=None):
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
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['connector'] = connector
            __props__['description'] = description
            __props__['distant_froms'] = distant_froms
            __props__['icon_id'] = icon_id
            __props__['name'] = name
            __props__['plan'] = plan
            __props__['size'] = size
            __props__['source_archive_id'] = source_archive_id
            __props__['source_disk_id'] = source_disk_id
            __props__['tags'] = tags
            __props__['zone'] = zone
            __props__['server_id'] = None
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

        __props__ = dict()

        __props__["connector"] = connector
        __props__["description"] = description
        __props__["distant_froms"] = distant_froms
        __props__["icon_id"] = icon_id
        __props__["name"] = name
        __props__["plan"] = plan
        __props__["server_id"] = server_id
        __props__["size"] = size
        __props__["source_archive_id"] = source_archive_id
        __props__["source_disk_id"] = source_disk_id
        __props__["tags"] = tags
        __props__["zone"] = zone
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

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

