// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Provides a SakuraCloud Archive resource. This can be used to create, update, and delete Archives.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as sakuracloud from "@pulumi/sakuracloud";
 * 
 * // Create a new Archive
 * const foobar = new sakuracloud.Archive("foobar", {
 *     archiveFile: "your/archive/file.raw",
 *     description: "description",
 *     file: [{}],
 *     hash: "",
 *     md5: [{}],
 *     size: 20,
 *     tags: [
 *         "foo",
 *         "bar",
 *     ],
 *     "your/archive/file.raw": [{}],
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-sakuracloud/blob/master/website/docs/r/archive.html.markdown.
 */
export class Archive extends pulumi.CustomResource {
    /**
     * Get an existing Archive resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
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
     * Archive file to upload (format:`raw`).
     */
    public readonly archiveFile!: pulumi.Output<string>;
    /**
     * The description of the resource.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * MD5 hash value of the archive file.
     */
    public readonly hash!: pulumi.Output<string>;
    /**
     * The ID of the icon.
     */
    public readonly iconId!: pulumi.Output<string | undefined>;
    /**
     * The name of the resource.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The size of the resource (unit:`GB`).   
     * Valid value is one of the following: [ 20 (default) / 40 / 60 / 80 / 100 / 250 / 500 / 750 / 1024 ]
     */
    public readonly size!: pulumi.Output<number | undefined>;
    /**
     * The tag list of the resources.
     */
    public readonly tags!: pulumi.Output<string[]>;
    /**
     * The ID of the zone to which the resource belongs.
     */
    public readonly zone!: pulumi.Output<string>;

    /**
     * Create a Archive resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ArchiveArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ArchiveArgs | ArchiveState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as ArchiveState | undefined;
            inputs["archiveFile"] = state ? state.archiveFile : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["hash"] = state ? state.hash : undefined;
            inputs["iconId"] = state ? state.iconId : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["size"] = state ? state.size : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["zone"] = state ? state.zone : undefined;
        } else {
            const args = argsOrState as ArchiveArgs | undefined;
            if (!args || args.archiveFile === undefined) {
                throw new Error("Missing required property 'archiveFile'");
            }
            inputs["archiveFile"] = args ? args.archiveFile : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["hash"] = args ? args.hash : undefined;
            inputs["iconId"] = args ? args.iconId : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["size"] = args ? args.size : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["zone"] = args ? args.zone : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Archive.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Archive resources.
 */
export interface ArchiveState {
    /**
     * Archive file to upload (format:`raw`).
     */
    readonly archiveFile?: pulumi.Input<string>;
    /**
     * The description of the resource.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * MD5 hash value of the archive file.
     */
    readonly hash?: pulumi.Input<string>;
    /**
     * The ID of the icon.
     */
    readonly iconId?: pulumi.Input<string>;
    /**
     * The name of the resource.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The size of the resource (unit:`GB`).   
     * Valid value is one of the following: [ 20 (default) / 40 / 60 / 80 / 100 / 250 / 500 / 750 / 1024 ]
     */
    readonly size?: pulumi.Input<number>;
    /**
     * The tag list of the resources.
     */
    readonly tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The ID of the zone to which the resource belongs.
     */
    readonly zone?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Archive resource.
 */
export interface ArchiveArgs {
    /**
     * Archive file to upload (format:`raw`).
     */
    readonly archiveFile: pulumi.Input<string>;
    /**
     * The description of the resource.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * MD5 hash value of the archive file.
     */
    readonly hash?: pulumi.Input<string>;
    /**
     * The ID of the icon.
     */
    readonly iconId?: pulumi.Input<string>;
    /**
     * The name of the resource.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The size of the resource (unit:`GB`).   
     * Valid value is one of the following: [ 20 (default) / 40 / 60 / 80 / 100 / 250 / 500 / 750 / 1024 ]
     */
    readonly size?: pulumi.Input<number>;
    /**
     * The tag list of the resources.
     */
    readonly tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The ID of the zone to which the resource belongs.
     */
    readonly zone?: pulumi.Input<string>;
}
