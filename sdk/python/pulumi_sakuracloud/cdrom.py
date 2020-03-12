# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class CDROM(pulumi.CustomResource):
    content: pulumi.Output[str]
    """
    The content to upload to as the CD-ROM. This conflicts with [`iso_image_file`]
    """
    content_file_name: pulumi.Output[str]
    """
    The name of content file to upload to as the CD-ROM. This is only used when `content` is specified. This conflicts with
    [`iso_image_file`]
    """
    description: pulumi.Output[str]
    """
    The description of the CD-ROM. The length of this value must be in the range [`1`-`512`]
    """
    hash: pulumi.Output[str]
    """
    The md5 checksum calculated from the base64 encoded file body
    """
    icon_id: pulumi.Output[str]
    """
    The icon id to attach to the CD-ROM
    """
    iso_image_file: pulumi.Output[str]
    """
    The file path to upload to as the CD-ROM. This conflicts with [`content`]
    """
    name: pulumi.Output[str]
    """
    The name of the CD-ROM. The length of this value must be in the range [`1`-`64`]
    """
    size: pulumi.Output[float]
    """
    The size of CD-ROM in GiB. This must be one of [`5`/`10`]
    """
    tags: pulumi.Output[list]
    """
    Any tags to assign to the CD-ROM
    """
    zone: pulumi.Output[str]
    """
    The name of zone that the CD-ROM will be created (e.g. `is1a`, `tk1a`)
    """
    def __init__(__self__, resource_name, opts=None, content=None, content_file_name=None, description=None, hash=None, icon_id=None, iso_image_file=None, name=None, size=None, tags=None, zone=None, __props__=None, __name__=None, __opts__=None):
        """
        Create a CDROM resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] content: The content to upload to as the CD-ROM. This conflicts with [`iso_image_file`]
        :param pulumi.Input[str] content_file_name: The name of content file to upload to as the CD-ROM. This is only used when `content` is specified. This conflicts with
               [`iso_image_file`]
        :param pulumi.Input[str] description: The description of the CD-ROM. The length of this value must be in the range [`1`-`512`]
        :param pulumi.Input[str] hash: The md5 checksum calculated from the base64 encoded file body
        :param pulumi.Input[str] icon_id: The icon id to attach to the CD-ROM
        :param pulumi.Input[str] iso_image_file: The file path to upload to as the CD-ROM. This conflicts with [`content`]
        :param pulumi.Input[str] name: The name of the CD-ROM. The length of this value must be in the range [`1`-`64`]
        :param pulumi.Input[float] size: The size of CD-ROM in GiB. This must be one of [`5`/`10`]
        :param pulumi.Input[list] tags: Any tags to assign to the CD-ROM
        :param pulumi.Input[str] zone: The name of zone that the CD-ROM will be created (e.g. `is1a`, `tk1a`)
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

            __props__['content'] = content
            __props__['content_file_name'] = content_file_name
            __props__['description'] = description
            __props__['hash'] = hash
            __props__['icon_id'] = icon_id
            __props__['iso_image_file'] = iso_image_file
            __props__['name'] = name
            __props__['size'] = size
            __props__['tags'] = tags
            __props__['zone'] = zone
        super(CDROM, __self__).__init__(
            'sakuracloud:index/cDROM:CDROM',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, content=None, content_file_name=None, description=None, hash=None, icon_id=None, iso_image_file=None, name=None, size=None, tags=None, zone=None):
        """
        Get an existing CDROM resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] content: The content to upload to as the CD-ROM. This conflicts with [`iso_image_file`]
        :param pulumi.Input[str] content_file_name: The name of content file to upload to as the CD-ROM. This is only used when `content` is specified. This conflicts with
               [`iso_image_file`]
        :param pulumi.Input[str] description: The description of the CD-ROM. The length of this value must be in the range [`1`-`512`]
        :param pulumi.Input[str] hash: The md5 checksum calculated from the base64 encoded file body
        :param pulumi.Input[str] icon_id: The icon id to attach to the CD-ROM
        :param pulumi.Input[str] iso_image_file: The file path to upload to as the CD-ROM. This conflicts with [`content`]
        :param pulumi.Input[str] name: The name of the CD-ROM. The length of this value must be in the range [`1`-`64`]
        :param pulumi.Input[float] size: The size of CD-ROM in GiB. This must be one of [`5`/`10`]
        :param pulumi.Input[list] tags: Any tags to assign to the CD-ROM
        :param pulumi.Input[str] zone: The name of zone that the CD-ROM will be created (e.g. `is1a`, `tk1a`)
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["content"] = content
        __props__["content_file_name"] = content_file_name
        __props__["description"] = description
        __props__["hash"] = hash
        __props__["icon_id"] = icon_id
        __props__["iso_image_file"] = iso_image_file
        __props__["name"] = name
        __props__["size"] = size
        __props__["tags"] = tags
        __props__["zone"] = zone
        return CDROM(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

