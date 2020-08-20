// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package sakuracloud

import (
	"reflect"

	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

type Archive struct {
	pulumi.CustomResourceState

	// The file path to upload to the SakuraCloud
	ArchiveFile pulumi.StringPtrOutput `pulumi:"archiveFile"`
	// The description of the archive. The length of this value must be in the range [`1`-`512`]
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The md5 checksum calculated from the base64 encoded file body
	Hash pulumi.StringOutput `pulumi:"hash"`
	// The icon id to attach to the archive
	IconId pulumi.StringPtrOutput `pulumi:"iconId"`
	// The name of the archive. The length of this value must be in the range [`1`-`64`]
	Name pulumi.StringOutput `pulumi:"name"`
	// The size of archive in GiB. This must be one of [`20`/`40`/`60`/`80`/`100`/`250`/`500`/`750`/`1024`]
	Size pulumi.IntPtrOutput `pulumi:"size"`
	// The id of the source archive. This conflicts with [`source_disk_id`]
	SourceArchiveId pulumi.StringPtrOutput `pulumi:"sourceArchiveId"`
	// The share key of source shared archive
	SourceArchiveZone pulumi.StringPtrOutput `pulumi:"sourceArchiveZone"`
	// The id of the source disk. This conflicts with [`source_archive_id`]
	SourceDiskId pulumi.StringPtrOutput `pulumi:"sourceDiskId"`
	// The share key of source shared archive
	SourceSharedKey pulumi.StringPtrOutput `pulumi:"sourceSharedKey"`
	// Any tags to assign to the archive
	Tags pulumi.StringArrayOutput `pulumi:"tags"`
	// The name of zone that the archive will be created (e.g. `is1a`, `tk1a`)
	Zone pulumi.StringOutput `pulumi:"zone"`
}

// NewArchive registers a new resource with the given unique name, arguments, and options.
func NewArchive(ctx *pulumi.Context,
	name string, args *ArchiveArgs, opts ...pulumi.ResourceOption) (*Archive, error) {
	if args == nil {
		args = &ArchiveArgs{}
	}
	var resource Archive
	err := ctx.RegisterResource("sakuracloud:index/archive:Archive", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetArchive gets an existing Archive resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetArchive(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ArchiveState, opts ...pulumi.ResourceOption) (*Archive, error) {
	var resource Archive
	err := ctx.ReadResource("sakuracloud:index/archive:Archive", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Archive resources.
type archiveState struct {
	// The file path to upload to the SakuraCloud
	ArchiveFile *string `pulumi:"archiveFile"`
	// The description of the archive. The length of this value must be in the range [`1`-`512`]
	Description *string `pulumi:"description"`
	// The md5 checksum calculated from the base64 encoded file body
	Hash *string `pulumi:"hash"`
	// The icon id to attach to the archive
	IconId *string `pulumi:"iconId"`
	// The name of the archive. The length of this value must be in the range [`1`-`64`]
	Name *string `pulumi:"name"`
	// The size of archive in GiB. This must be one of [`20`/`40`/`60`/`80`/`100`/`250`/`500`/`750`/`1024`]
	Size *int `pulumi:"size"`
	// The id of the source archive. This conflicts with [`source_disk_id`]
	SourceArchiveId *string `pulumi:"sourceArchiveId"`
	// The share key of source shared archive
	SourceArchiveZone *string `pulumi:"sourceArchiveZone"`
	// The id of the source disk. This conflicts with [`source_archive_id`]
	SourceDiskId *string `pulumi:"sourceDiskId"`
	// The share key of source shared archive
	SourceSharedKey *string `pulumi:"sourceSharedKey"`
	// Any tags to assign to the archive
	Tags []string `pulumi:"tags"`
	// The name of zone that the archive will be created (e.g. `is1a`, `tk1a`)
	Zone *string `pulumi:"zone"`
}

type ArchiveState struct {
	// The file path to upload to the SakuraCloud
	ArchiveFile pulumi.StringPtrInput
	// The description of the archive. The length of this value must be in the range [`1`-`512`]
	Description pulumi.StringPtrInput
	// The md5 checksum calculated from the base64 encoded file body
	Hash pulumi.StringPtrInput
	// The icon id to attach to the archive
	IconId pulumi.StringPtrInput
	// The name of the archive. The length of this value must be in the range [`1`-`64`]
	Name pulumi.StringPtrInput
	// The size of archive in GiB. This must be one of [`20`/`40`/`60`/`80`/`100`/`250`/`500`/`750`/`1024`]
	Size pulumi.IntPtrInput
	// The id of the source archive. This conflicts with [`source_disk_id`]
	SourceArchiveId pulumi.StringPtrInput
	// The share key of source shared archive
	SourceArchiveZone pulumi.StringPtrInput
	// The id of the source disk. This conflicts with [`source_archive_id`]
	SourceDiskId pulumi.StringPtrInput
	// The share key of source shared archive
	SourceSharedKey pulumi.StringPtrInput
	// Any tags to assign to the archive
	Tags pulumi.StringArrayInput
	// The name of zone that the archive will be created (e.g. `is1a`, `tk1a`)
	Zone pulumi.StringPtrInput
}

func (ArchiveState) ElementType() reflect.Type {
	return reflect.TypeOf((*archiveState)(nil)).Elem()
}

type archiveArgs struct {
	// The file path to upload to the SakuraCloud
	ArchiveFile *string `pulumi:"archiveFile"`
	// The description of the archive. The length of this value must be in the range [`1`-`512`]
	Description *string `pulumi:"description"`
	// The md5 checksum calculated from the base64 encoded file body
	Hash *string `pulumi:"hash"`
	// The icon id to attach to the archive
	IconId *string `pulumi:"iconId"`
	// The name of the archive. The length of this value must be in the range [`1`-`64`]
	Name *string `pulumi:"name"`
	// The size of archive in GiB. This must be one of [`20`/`40`/`60`/`80`/`100`/`250`/`500`/`750`/`1024`]
	Size *int `pulumi:"size"`
	// The id of the source archive. This conflicts with [`source_disk_id`]
	SourceArchiveId *string `pulumi:"sourceArchiveId"`
	// The share key of source shared archive
	SourceArchiveZone *string `pulumi:"sourceArchiveZone"`
	// The id of the source disk. This conflicts with [`source_archive_id`]
	SourceDiskId *string `pulumi:"sourceDiskId"`
	// The share key of source shared archive
	SourceSharedKey *string `pulumi:"sourceSharedKey"`
	// Any tags to assign to the archive
	Tags []string `pulumi:"tags"`
	// The name of zone that the archive will be created (e.g. `is1a`, `tk1a`)
	Zone *string `pulumi:"zone"`
}

// The set of arguments for constructing a Archive resource.
type ArchiveArgs struct {
	// The file path to upload to the SakuraCloud
	ArchiveFile pulumi.StringPtrInput
	// The description of the archive. The length of this value must be in the range [`1`-`512`]
	Description pulumi.StringPtrInput
	// The md5 checksum calculated from the base64 encoded file body
	Hash pulumi.StringPtrInput
	// The icon id to attach to the archive
	IconId pulumi.StringPtrInput
	// The name of the archive. The length of this value must be in the range [`1`-`64`]
	Name pulumi.StringPtrInput
	// The size of archive in GiB. This must be one of [`20`/`40`/`60`/`80`/`100`/`250`/`500`/`750`/`1024`]
	Size pulumi.IntPtrInput
	// The id of the source archive. This conflicts with [`source_disk_id`]
	SourceArchiveId pulumi.StringPtrInput
	// The share key of source shared archive
	SourceArchiveZone pulumi.StringPtrInput
	// The id of the source disk. This conflicts with [`source_archive_id`]
	SourceDiskId pulumi.StringPtrInput
	// The share key of source shared archive
	SourceSharedKey pulumi.StringPtrInput
	// Any tags to assign to the archive
	Tags pulumi.StringArrayInput
	// The name of zone that the archive will be created (e.g. `is1a`, `tk1a`)
	Zone pulumi.StringPtrInput
}

func (ArchiveArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*archiveArgs)(nil)).Elem()
}
