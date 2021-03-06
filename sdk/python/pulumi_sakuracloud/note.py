# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = ['Note']


class Note(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 class_: Optional[pulumi.Input[str]] = None,
                 content: Optional[pulumi.Input[str]] = None,
                 icon_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a SakuraCloud Note.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sakuracloud as sakuracloud

        foobar = sakuracloud.Note("foobar", content=(lambda path: open(path).read())("startup-script.sh"))
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] class_: The class of the Note. This must be one of `shell`/`yaml_cloud_config`. Default:`shell`.
        :param pulumi.Input[str] content: The content of the Note. This must be specified as a shell script or as a cloud-config.
        :param pulumi.Input[str] icon_id: The icon id to attach to the Note.
        :param pulumi.Input[str] name: The name of the Note. The length of this value must be in the range [`1`-`64`].
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Any tags to assign to the Note.
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

            __props__['class_'] = class_
            if content is None and not opts.urn:
                raise TypeError("Missing required property 'content'")
            __props__['content'] = content
            __props__['icon_id'] = icon_id
            __props__['name'] = name
            __props__['tags'] = tags
            __props__['description'] = None
        super(Note, __self__).__init__(
            'sakuracloud:index/note:Note',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            class_: Optional[pulumi.Input[str]] = None,
            content: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            icon_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'Note':
        """
        Get an existing Note resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] class_: The class of the Note. This must be one of `shell`/`yaml_cloud_config`. Default:`shell`.
        :param pulumi.Input[str] content: The content of the Note. This must be specified as a shell script or as a cloud-config.
        :param pulumi.Input[str] description: The description of the Note. This will be computed from special tags within body of `content`.
        :param pulumi.Input[str] icon_id: The icon id to attach to the Note.
        :param pulumi.Input[str] name: The name of the Note. The length of this value must be in the range [`1`-`64`].
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Any tags to assign to the Note.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["class_"] = class_
        __props__["content"] = content
        __props__["description"] = description
        __props__["icon_id"] = icon_id
        __props__["name"] = name
        __props__["tags"] = tags
        return Note(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="class")
    def class_(self) -> pulumi.Output[Optional[str]]:
        """
        The class of the Note. This must be one of `shell`/`yaml_cloud_config`. Default:`shell`.
        """
        return pulumi.get(self, "class_")

    @property
    @pulumi.getter
    def content(self) -> pulumi.Output[str]:
        """
        The content of the Note. This must be specified as a shell script or as a cloud-config.
        """
        return pulumi.get(self, "content")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        The description of the Note. This will be computed from special tags within body of `content`.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="iconId")
    def icon_id(self) -> pulumi.Output[Optional[str]]:
        """
        The icon id to attach to the Note.
        """
        return pulumi.get(self, "icon_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Note. The length of this value must be in the range [`1`-`64`].
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Any tags to assign to the Note.
        """
        return pulumi.get(self, "tags")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

