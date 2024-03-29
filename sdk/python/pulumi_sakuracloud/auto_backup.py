# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['AutoBackupArgs', 'AutoBackup']

@pulumi.input_type
class AutoBackupArgs:
    def __init__(__self__, *,
                 disk_id: pulumi.Input[str],
                 weekdays: pulumi.Input[Sequence[pulumi.Input[str]]],
                 description: Optional[pulumi.Input[str]] = None,
                 icon_id: Optional[pulumi.Input[str]] = None,
                 max_backup_num: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 zone: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AutoBackup resource.
        :param pulumi.Input[str] disk_id: The disk id to backed up. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] weekdays: A list of weekdays to backed up. The values in the list must be in [`sun`/`mon`/`tue`/`wed`/`thu`/`fri`/`sat`].
        :param pulumi.Input[str] description: The description of the AutoBackup. The length of this value must be in the range [`1`-`512`].
        :param pulumi.Input[str] icon_id: The icon id to attach to the AutoBackup.
        :param pulumi.Input[int] max_backup_num: The number backup files to keep. This must be in the range [`1`-`10`]. Default:`1`.
        :param pulumi.Input[str] name: The name of the AutoBackup. The length of this value must be in the range [`1`-`64`].
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Any tags to assign to the AutoBackup.
        :param pulumi.Input[str] zone: The name of zone that the AutoBackup will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        """
        pulumi.set(__self__, "disk_id", disk_id)
        pulumi.set(__self__, "weekdays", weekdays)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if icon_id is not None:
            pulumi.set(__self__, "icon_id", icon_id)
        if max_backup_num is not None:
            pulumi.set(__self__, "max_backup_num", max_backup_num)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if zone is not None:
            pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter(name="diskId")
    def disk_id(self) -> pulumi.Input[str]:
        """
        The disk id to backed up. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "disk_id")

    @disk_id.setter
    def disk_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "disk_id", value)

    @property
    @pulumi.getter
    def weekdays(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        A list of weekdays to backed up. The values in the list must be in [`sun`/`mon`/`tue`/`wed`/`thu`/`fri`/`sat`].
        """
        return pulumi.get(self, "weekdays")

    @weekdays.setter
    def weekdays(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "weekdays", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the AutoBackup. The length of this value must be in the range [`1`-`512`].
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="iconId")
    def icon_id(self) -> Optional[pulumi.Input[str]]:
        """
        The icon id to attach to the AutoBackup.
        """
        return pulumi.get(self, "icon_id")

    @icon_id.setter
    def icon_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "icon_id", value)

    @property
    @pulumi.getter(name="maxBackupNum")
    def max_backup_num(self) -> Optional[pulumi.Input[int]]:
        """
        The number backup files to keep. This must be in the range [`1`-`10`]. Default:`1`.
        """
        return pulumi.get(self, "max_backup_num")

    @max_backup_num.setter
    def max_backup_num(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_backup_num", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the AutoBackup. The length of this value must be in the range [`1`-`64`].
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Any tags to assign to the AutoBackup.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[str]]:
        """
        The name of zone that the AutoBackup will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "zone")

    @zone.setter
    def zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone", value)


@pulumi.input_type
class _AutoBackupState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 disk_id: Optional[pulumi.Input[str]] = None,
                 icon_id: Optional[pulumi.Input[str]] = None,
                 max_backup_num: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 weekdays: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 zone: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering AutoBackup resources.
        :param pulumi.Input[str] description: The description of the AutoBackup. The length of this value must be in the range [`1`-`512`].
        :param pulumi.Input[str] disk_id: The disk id to backed up. Changing this forces a new resource to be created.
        :param pulumi.Input[str] icon_id: The icon id to attach to the AutoBackup.
        :param pulumi.Input[int] max_backup_num: The number backup files to keep. This must be in the range [`1`-`10`]. Default:`1`.
        :param pulumi.Input[str] name: The name of the AutoBackup. The length of this value must be in the range [`1`-`64`].
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Any tags to assign to the AutoBackup.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] weekdays: A list of weekdays to backed up. The values in the list must be in [`sun`/`mon`/`tue`/`wed`/`thu`/`fri`/`sat`].
        :param pulumi.Input[str] zone: The name of zone that the AutoBackup will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if disk_id is not None:
            pulumi.set(__self__, "disk_id", disk_id)
        if icon_id is not None:
            pulumi.set(__self__, "icon_id", icon_id)
        if max_backup_num is not None:
            pulumi.set(__self__, "max_backup_num", max_backup_num)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if weekdays is not None:
            pulumi.set(__self__, "weekdays", weekdays)
        if zone is not None:
            pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the AutoBackup. The length of this value must be in the range [`1`-`512`].
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="diskId")
    def disk_id(self) -> Optional[pulumi.Input[str]]:
        """
        The disk id to backed up. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "disk_id")

    @disk_id.setter
    def disk_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "disk_id", value)

    @property
    @pulumi.getter(name="iconId")
    def icon_id(self) -> Optional[pulumi.Input[str]]:
        """
        The icon id to attach to the AutoBackup.
        """
        return pulumi.get(self, "icon_id")

    @icon_id.setter
    def icon_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "icon_id", value)

    @property
    @pulumi.getter(name="maxBackupNum")
    def max_backup_num(self) -> Optional[pulumi.Input[int]]:
        """
        The number backup files to keep. This must be in the range [`1`-`10`]. Default:`1`.
        """
        return pulumi.get(self, "max_backup_num")

    @max_backup_num.setter
    def max_backup_num(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_backup_num", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the AutoBackup. The length of this value must be in the range [`1`-`64`].
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Any tags to assign to the AutoBackup.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def weekdays(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of weekdays to backed up. The values in the list must be in [`sun`/`mon`/`tue`/`wed`/`thu`/`fri`/`sat`].
        """
        return pulumi.get(self, "weekdays")

    @weekdays.setter
    def weekdays(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "weekdays", value)

    @property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[str]]:
        """
        The name of zone that the AutoBackup will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "zone")

    @zone.setter
    def zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone", value)


class AutoBackup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 disk_id: Optional[pulumi.Input[str]] = None,
                 icon_id: Optional[pulumi.Input[str]] = None,
                 max_backup_num: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 weekdays: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 zone: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a SakuraCloud Auto Backup.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sakuracloud as sakuracloud

        foobar_disk = sakuracloud.Disk("foobarDisk")
        foobar_auto_backup = sakuracloud.AutoBackup("foobarAutoBackup",
            disk_id=foobar_disk.id,
            weekdays=[
                "mon",
                "tue",
                "wed",
                "thu",
                "fri",
                "sat",
                "sun",
            ],
            max_backup_num=5,
            description="description",
            tags=[
                "tag1",
                "tag2",
            ])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the AutoBackup. The length of this value must be in the range [`1`-`512`].
        :param pulumi.Input[str] disk_id: The disk id to backed up. Changing this forces a new resource to be created.
        :param pulumi.Input[str] icon_id: The icon id to attach to the AutoBackup.
        :param pulumi.Input[int] max_backup_num: The number backup files to keep. This must be in the range [`1`-`10`]. Default:`1`.
        :param pulumi.Input[str] name: The name of the AutoBackup. The length of this value must be in the range [`1`-`64`].
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Any tags to assign to the AutoBackup.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] weekdays: A list of weekdays to backed up. The values in the list must be in [`sun`/`mon`/`tue`/`wed`/`thu`/`fri`/`sat`].
        :param pulumi.Input[str] zone: The name of zone that the AutoBackup will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AutoBackupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a SakuraCloud Auto Backup.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sakuracloud as sakuracloud

        foobar_disk = sakuracloud.Disk("foobarDisk")
        foobar_auto_backup = sakuracloud.AutoBackup("foobarAutoBackup",
            disk_id=foobar_disk.id,
            weekdays=[
                "mon",
                "tue",
                "wed",
                "thu",
                "fri",
                "sat",
                "sun",
            ],
            max_backup_num=5,
            description="description",
            tags=[
                "tag1",
                "tag2",
            ])
        ```

        :param str resource_name: The name of the resource.
        :param AutoBackupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AutoBackupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 disk_id: Optional[pulumi.Input[str]] = None,
                 icon_id: Optional[pulumi.Input[str]] = None,
                 max_backup_num: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 weekdays: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
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
            __props__ = AutoBackupArgs.__new__(AutoBackupArgs)

            __props__.__dict__["description"] = description
            if disk_id is None and not opts.urn:
                raise TypeError("Missing required property 'disk_id'")
            __props__.__dict__["disk_id"] = disk_id
            __props__.__dict__["icon_id"] = icon_id
            __props__.__dict__["max_backup_num"] = max_backup_num
            __props__.__dict__["name"] = name
            __props__.__dict__["tags"] = tags
            if weekdays is None and not opts.urn:
                raise TypeError("Missing required property 'weekdays'")
            __props__.__dict__["weekdays"] = weekdays
            __props__.__dict__["zone"] = zone
        super(AutoBackup, __self__).__init__(
            'sakuracloud:index/autoBackup:AutoBackup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            disk_id: Optional[pulumi.Input[str]] = None,
            icon_id: Optional[pulumi.Input[str]] = None,
            max_backup_num: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            weekdays: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            zone: Optional[pulumi.Input[str]] = None) -> 'AutoBackup':
        """
        Get an existing AutoBackup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the AutoBackup. The length of this value must be in the range [`1`-`512`].
        :param pulumi.Input[str] disk_id: The disk id to backed up. Changing this forces a new resource to be created.
        :param pulumi.Input[str] icon_id: The icon id to attach to the AutoBackup.
        :param pulumi.Input[int] max_backup_num: The number backup files to keep. This must be in the range [`1`-`10`]. Default:`1`.
        :param pulumi.Input[str] name: The name of the AutoBackup. The length of this value must be in the range [`1`-`64`].
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Any tags to assign to the AutoBackup.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] weekdays: A list of weekdays to backed up. The values in the list must be in [`sun`/`mon`/`tue`/`wed`/`thu`/`fri`/`sat`].
        :param pulumi.Input[str] zone: The name of zone that the AutoBackup will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AutoBackupState.__new__(_AutoBackupState)

        __props__.__dict__["description"] = description
        __props__.__dict__["disk_id"] = disk_id
        __props__.__dict__["icon_id"] = icon_id
        __props__.__dict__["max_backup_num"] = max_backup_num
        __props__.__dict__["name"] = name
        __props__.__dict__["tags"] = tags
        __props__.__dict__["weekdays"] = weekdays
        __props__.__dict__["zone"] = zone
        return AutoBackup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the AutoBackup. The length of this value must be in the range [`1`-`512`].
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="diskId")
    def disk_id(self) -> pulumi.Output[str]:
        """
        The disk id to backed up. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "disk_id")

    @property
    @pulumi.getter(name="iconId")
    def icon_id(self) -> pulumi.Output[Optional[str]]:
        """
        The icon id to attach to the AutoBackup.
        """
        return pulumi.get(self, "icon_id")

    @property
    @pulumi.getter(name="maxBackupNum")
    def max_backup_num(self) -> pulumi.Output[Optional[int]]:
        """
        The number backup files to keep. This must be in the range [`1`-`10`]. Default:`1`.
        """
        return pulumi.get(self, "max_backup_num")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the AutoBackup. The length of this value must be in the range [`1`-`64`].
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Any tags to assign to the AutoBackup.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def weekdays(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of weekdays to backed up. The values in the list must be in [`sun`/`mon`/`tue`/`wed`/`thu`/`fri`/`sat`].
        """
        return pulumi.get(self, "weekdays")

    @property
    @pulumi.getter
    def zone(self) -> pulumi.Output[str]:
        """
        The name of zone that the AutoBackup will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "zone")

