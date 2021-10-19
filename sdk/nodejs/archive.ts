// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Manages a SakuraCloud Archive.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as sakuracloud from "@pulumi/sakuracloud";
 *
 * // from archive/disk
 * const from_archive_or_disk = new sakuracloud.Archive("from-archive-or-disk", {
 *     description: "description",
 *     sourceArchiveId: "1.23456789012e+11",
 *     sourceArchiveZone: "tk1a",
 *     tags: [
 *         "tag1",
 *         "tag2",
 *     ],
 * });
 * // from shared archive
 * const from_shared_archive = new sakuracloud.Archive("from-shared-archive", {
 *     description: "description",
 *     sourceSharedKey: "is1a:123456789012:xxx",
 *     tags: [
 *         "tag1",
 *         "tag2",
 *     ],
 * });
 * // from local file
 * const foobar = new sakuracloud.Archive("foobar", {
 *     archiveFile: "test/dummy.raw",
 *     description: "description",
 *     size: 20,
 *     tags: [
 *         "tag1",
 *         "tag2",
 *     ],
 * });
 * ```
 */
export class Archive extends pulumi.CustomResource {
    /**
     * Get an existing Archive resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ArchiveState, opts?: pulumi.CustomResourceOptions): Archive {
        return new Archive(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'sakuracloud:index/archive:Archive';

    /**
     * Returns true if the given object is an instance of Archive.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Archive {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Archive.__pulumiType;
    }

    /**
     * The file path to upload to the SakuraCloud.
     */
    public readonly archiveFile!: pulumi.Output<string | undefined>;
    /**
     * The description of the archive. The length of this value must be in the range [`1`-`512`].
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The md5 checksum calculated from the base64 encoded file body. Changing this forces a new resource to be created.
     */
    public readonly hash!: pulumi.Output<string>;
    /**
     * The icon id to attach to the archive.
     */
    public readonly iconId!: pulumi.Output<string | undefined>;
    /**
     * The name of the archive. The length of this value must be in the range [`1`-`64`].
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The size of archive in GiB. This must be one of [`20`/`40`/`60`/`80`/`100`/`250`/`500`/`750`/`1024`]. Changing this forces a new resource to be created. Default:`20`.
     */
    public readonly size!: pulumi.Output<number>;
    /**
     * The id of the source archive. This conflicts with [`sourceDiskId`]. Changing this forces a new resource to be created.
     */
    public readonly sourceArchiveId!: pulumi.Output<string | undefined>;
    /**
     * The share key of source shared archive. Changing this forces a new resource to be created.
     */
    public readonly sourceArchiveZone!: pulumi.Output<string | undefined>;
    /**
     * The id of the source disk. This conflicts with [`sourceArchiveId`]. Changing this forces a new resource to be created.
     */
    public readonly sourceDiskId!: pulumi.Output<string | undefined>;
    /**
     * The share key of source shared archive. Changing this forces a new resource to be created.
     */
    public readonly sourceSharedKey!: pulumi.Output<string | undefined>;
    /**
     * Any tags to assign to the archive.
     */
    public readonly tags!: pulumi.Output<string[] | undefined>;
    /**
     * The name of zone that the archive will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
     */
    public readonly zone!: pulumi.Output<string>;

    /**
     * Create a Archive resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: ArchiveArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ArchiveArgs | ArchiveState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ArchiveState | undefined;
            inputs["archiveFile"] = state ? state.archiveFile : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["hash"] = state ? state.hash : undefined;
            inputs["iconId"] = state ? state.iconId : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["size"] = state ? state.size : undefined;
            inputs["sourceArchiveId"] = state ? state.sourceArchiveId : undefined;
            inputs["sourceArchiveZone"] = state ? state.sourceArchiveZone : undefined;
            inputs["sourceDiskId"] = state ? state.sourceDiskId : undefined;
            inputs["sourceSharedKey"] = state ? state.sourceSharedKey : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["zone"] = state ? state.zone : undefined;
        } else {
            const args = argsOrState as ArchiveArgs | undefined;
            inputs["archiveFile"] = args ? args.archiveFile : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["hash"] = args ? args.hash : undefined;
            inputs["iconId"] = args ? args.iconId : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["size"] = args ? args.size : undefined;
            inputs["sourceArchiveId"] = args ? args.sourceArchiveId : undefined;
            inputs["sourceArchiveZone"] = args ? args.sourceArchiveZone : undefined;
            inputs["sourceDiskId"] = args ? args.sourceDiskId : undefined;
            inputs["sourceSharedKey"] = args ? args.sourceSharedKey : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["zone"] = args ? args.zone : undefined;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(Archive.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Archive resources.
 */
export interface ArchiveState {
    /**
     * The file path to upload to the SakuraCloud.
     */
    archiveFile?: pulumi.Input<string>;
    /**
     * The description of the archive. The length of this value must be in the range [`1`-`512`].
     */
    description?: pulumi.Input<string>;
    /**
     * The md5 checksum calculated from the base64 encoded file body. Changing this forces a new resource to be created.
     */
    hash?: pulumi.Input<string>;
    /**
     * The icon id to attach to the archive.
     */
    iconId?: pulumi.Input<string>;
    /**
     * The name of the archive. The length of this value must be in the range [`1`-`64`].
     */
    name?: pulumi.Input<string>;
    /**
     * The size of archive in GiB. This must be one of [`20`/`40`/`60`/`80`/`100`/`250`/`500`/`750`/`1024`]. Changing this forces a new resource to be created. Default:`20`.
     */
    size?: pulumi.Input<number>;
    /**
     * The id of the source archive. This conflicts with [`sourceDiskId`]. Changing this forces a new resource to be created.
     */
    sourceArchiveId?: pulumi.Input<string>;
    /**
     * The share key of source shared archive. Changing this forces a new resource to be created.
     */
    sourceArchiveZone?: pulumi.Input<string>;
    /**
     * The id of the source disk. This conflicts with [`sourceArchiveId`]. Changing this forces a new resource to be created.
     */
    sourceDiskId?: pulumi.Input<string>;
    /**
     * The share key of source shared archive. Changing this forces a new resource to be created.
     */
    sourceSharedKey?: pulumi.Input<string>;
    /**
     * Any tags to assign to the archive.
     */
    tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The name of zone that the archive will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
     */
    zone?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Archive resource.
 */
export interface ArchiveArgs {
    /**
     * The file path to upload to the SakuraCloud.
     */
    archiveFile?: pulumi.Input<string>;
    /**
     * The description of the archive. The length of this value must be in the range [`1`-`512`].
     */
    description?: pulumi.Input<string>;
    /**
     * The md5 checksum calculated from the base64 encoded file body. Changing this forces a new resource to be created.
     */
    hash?: pulumi.Input<string>;
    /**
     * The icon id to attach to the archive.
     */
    iconId?: pulumi.Input<string>;
    /**
     * The name of the archive. The length of this value must be in the range [`1`-`64`].
     */
    name?: pulumi.Input<string>;
    /**
     * The size of archive in GiB. This must be one of [`20`/`40`/`60`/`80`/`100`/`250`/`500`/`750`/`1024`]. Changing this forces a new resource to be created. Default:`20`.
     */
    size?: pulumi.Input<number>;
    /**
     * The id of the source archive. This conflicts with [`sourceDiskId`]. Changing this forces a new resource to be created.
     */
    sourceArchiveId?: pulumi.Input<string>;
    /**
     * The share key of source shared archive. Changing this forces a new resource to be created.
     */
    sourceArchiveZone?: pulumi.Input<string>;
    /**
     * The id of the source disk. This conflicts with [`sourceArchiveId`]. Changing this forces a new resource to be created.
     */
    sourceDiskId?: pulumi.Input<string>;
    /**
     * The share key of source shared archive. Changing this forces a new resource to be created.
     */
    sourceSharedKey?: pulumi.Input<string>;
    /**
     * Any tags to assign to the archive.
     */
    tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The name of zone that the archive will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
     */
    zone?: pulumi.Input<string>;
}
