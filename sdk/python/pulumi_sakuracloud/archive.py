# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = ['Archive']


class Archive(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 archive_file: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 hash: Optional[pulumi.Input[str]] = None,
                 icon_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[int]] = None,
                 source_archive_id: Optional[pulumi.Input[str]] = None,
                 source_archive_zone: Optional[pulumi.Input[str]] = None,
                 source_disk_id: Optional[pulumi.Input[str]] = None,
                 source_shared_key: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 zone: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a SakuraCloud Archive.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sakuracloud as sakuracloud

        # from archive/disk
        from_archive_or_disk = sakuracloud.Archive("from-archive-or-disk",
            description="description",
            source_archive_id="123456789012",
            source_archive_zone="tk1a",
            tags=[
                "tag1",
                "tag2",
            ])
        # from shared archive
        from_shared_archive = sakuracloud.Archive("from-shared-archive",
            description="description",
            source_shared_key="is1a:123456789012:xxx",
            tags=[
                "tag1",
                "tag2",
            ])
        # from local file
        foobar = sakuracloud.Archive("foobar",
            archive_file="test/dummy.raw",
            description="description",
            size=20,
            tags=[
                "tag1",
                "tag2",
            ])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] archive_file: The file path to upload to the SakuraCloud.
        :param pulumi.Input[str] description: The description of the archive. The length of this value must be in the range [`1`-`512`].
        :param pulumi.Input[str] hash: The md5 checksum calculated from the base64 encoded file body. Changing this forces a new resource to be created.
        :param pulumi.Input[str] icon_id: The icon id to attach to the archive.
        :param pulumi.Input[str] name: The name of the archive. The length of this value must be in the range [`1`-`64`].
        :param pulumi.Input[int] size: The size of archive in GiB. This must be one of [`20`/`40`/`60`/`80`/`100`/`250`/`500`/`750`/`1024`]. Changing this forces a new resource to be created. Default:`20`.
        :param pulumi.Input[str] source_archive_id: The id of the source archive. This conflicts with [`source_disk_id`]. Changing this forces a new resource to be created.
        :param pulumi.Input[str] source_archive_zone: The share key of source shared archive. Changing this forces a new resource to be created.
        :param pulumi.Input[str] source_disk_id: The id of the source disk. This conflicts with [`source_archive_id`]. Changing this forces a new resource to be created.
        :param pulumi.Input[str] source_shared_key: The share key of source shared archive. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Any tags to assign to the archive.
        :param pulumi.Input[str] zone: The name of zone that the archive will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
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

            __props__['archive_file'] = archive_file
            __props__['description'] = description
            __props__['hash'] = hash
            __props__['icon_id'] = icon_id
            __props__['name'] = name
            __props__['size'] = size
            __props__['source_archive_id'] = source_archive_id
            __props__['source_archive_zone'] = source_archive_zone
            __props__['source_disk_id'] = source_disk_id
            __props__['source_shared_key'] = source_shared_key
            __props__['tags'] = tags
            __props__['zone'] = zone
        super(Archive, __self__).__init__(
            'sakuracloud:index/archive:Archive',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            archive_file: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            hash: Optional[pulumi.Input[str]] = None,
            icon_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            size: Optional[pulumi.Input[int]] = None,
            source_archive_id: Optional[pulumi.Input[str]] = None,
            source_archive_zone: Optional[pulumi.Input[str]] = None,
            source_disk_id: Optional[pulumi.Input[str]] = None,
            source_shared_key: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            zone: Optional[pulumi.Input[str]] = None) -> 'Archive':
        """
        Get an existing Archive resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] archive_file: The file path to upload to the SakuraCloud.
        :param pulumi.Input[str] description: The description of the archive. The length of this value must be in the range [`1`-`512`].
        :param pulumi.Input[str] hash: The md5 checksum calculated from the base64 encoded file body. Changing this forces a new resource to be created.
        :param pulumi.Input[str] icon_id: The icon id to attach to the archive.
        :param pulumi.Input[str] name: The name of the archive. The length of this value must be in the range [`1`-`64`].
        :param pulumi.Input[int] size: The size of archive in GiB. This must be one of [`20`/`40`/`60`/`80`/`100`/`250`/`500`/`750`/`1024`]. Changing this forces a new resource to be created. Default:`20`.
        :param pulumi.Input[str] source_archive_id: The id of the source archive. This conflicts with [`source_disk_id`]. Changing this forces a new resource to be created.
        :param pulumi.Input[str] source_archive_zone: The share key of source shared archive. Changing this forces a new resource to be created.
        :param pulumi.Input[str] source_disk_id: The id of the source disk. This conflicts with [`source_archive_id`]. Changing this forces a new resource to be created.
        :param pulumi.Input[str] source_shared_key: The share key of source shared archive. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Any tags to assign to the archive.
        :param pulumi.Input[str] zone: The name of zone that the archive will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["archive_file"] = archive_file
        __props__["description"] = description
        __props__["hash"] = hash
        __props__["icon_id"] = icon_id
        __props__["name"] = name
        __props__["size"] = size
        __props__["source_archive_id"] = source_archive_id
        __props__["source_archive_zone"] = source_archive_zone
        __props__["source_disk_id"] = source_disk_id
        __props__["source_shared_key"] = source_shared_key
        __props__["tags"] = tags
        __props__["zone"] = zone
        return Archive(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="archiveFile")
    def archive_file(self) -> pulumi.Output[Optional[str]]:
        """
        The file path to upload to the SakuraCloud.
        """
        return pulumi.get(self, "archive_file")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the archive. The length of this value must be in the range [`1`-`512`].
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def hash(self) -> pulumi.Output[str]:
        """
        The md5 checksum calculated from the base64 encoded file body. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "hash")

    @property
    @pulumi.getter(name="iconId")
    def icon_id(self) -> pulumi.Output[Optional[str]]:
        """
        The icon id to attach to the archive.
        """
        return pulumi.get(self, "icon_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the archive. The length of this value must be in the range [`1`-`64`].
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def size(self) -> pulumi.Output[Optional[int]]:
        """
        The size of archive in GiB. This must be one of [`20`/`40`/`60`/`80`/`100`/`250`/`500`/`750`/`1024`]. Changing this forces a new resource to be created. Default:`20`.
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
    @pulumi.getter(name="sourceArchiveZone")
    def source_archive_zone(self) -> pulumi.Output[Optional[str]]:
        """
        The share key of source shared archive. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "source_archive_zone")

    @property
    @pulumi.getter(name="sourceDiskId")
    def source_disk_id(self) -> pulumi.Output[Optional[str]]:
        """
        The id of the source disk. This conflicts with [`source_archive_id`]. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "source_disk_id")

    @property
    @pulumi.getter(name="sourceSharedKey")
    def source_shared_key(self) -> pulumi.Output[Optional[str]]:
        """
        The share key of source shared archive. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "source_shared_key")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Any tags to assign to the archive.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def zone(self) -> pulumi.Output[str]:
        """
        The name of zone that the archive will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "zone")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

