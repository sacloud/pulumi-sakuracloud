// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "./types";
import * as utilities from "./utilities";

/**
 * Manages a SakuraCloud Container Registry.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as sakuracloud from "@pulumi/sakuracloud";
 *
 * const config = new pulumi.Config();
 * const users = config.getObject("users") || [
 *     {
 *         name: "user1",
 *         password: "password1",
 *         permission: "all",
 *     },
 *     {
 *         name: "user2",
 *         password: "password2",
 *         permission: "readwrite",
 *     },
 * ];
 * const foobar = new sakuracloud.ContainerRegistry("foobar", {
 *     subdomainLabel: "your-subdomain-label",
 *     accessLevel: "readwrite",
 *     description: "description",
 *     tags: [
 *         "tag1",
 *         "tag2",
 *     ],
 *     dynamic: [{
 *         forEach: users,
 *         content: [{
 *             name: user.value.name,
 *             password: user.value.password,
 *             permission: user.value.permission,
 *         }],
 *     }],
 * });
 * ```
 */
export class ContainerRegistry extends pulumi.CustomResource {
    /**
     * Get an existing ContainerRegistry resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ContainerRegistryState, opts?: pulumi.CustomResourceOptions): ContainerRegistry {
        return new ContainerRegistry(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'sakuracloud:index/containerRegistry:ContainerRegistry';

    /**
     * Returns true if the given object is an instance of ContainerRegistry.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ContainerRegistry {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ContainerRegistry.__pulumiType;
    }

    /**
     * The level of access that allow to users. This must be one of [`readwrite`/`readonly`/`none`].
     */
    public readonly accessLevel!: pulumi.Output<string>;
    /**
     * The description of the Container Registry. The length of this value must be in the range [`1`-`512`].
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The FQDN for accessing the Container Registry. FQDN is built from `subdomainLabel` + `.sakuracr.jp`.
     */
    public /*out*/ readonly fqdn!: pulumi.Output<string>;
    /**
     * The icon id to attach to the Container Registry.
     */
    public readonly iconId!: pulumi.Output<string | undefined>;
    /**
     * The name of the Container Registry. The length of this value must be in the range [`1`-`64`].
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The label at the lowest of the FQDN used when be accessed from users. The length of this value must be in the range [`1`-`64`]. Changing this forces a new resource to be created.
     */
    public readonly subdomainLabel!: pulumi.Output<string>;
    /**
     * Any tags to assign to the Container Registry.
     */
    public readonly tags!: pulumi.Output<string[] | undefined>;
    /**
     * One or more `user` blocks as defined below.
     */
    public readonly users!: pulumi.Output<outputs.ContainerRegistryUser[] | undefined>;
    /**
     * The alias for accessing the container registry.
     */
    public readonly virtualDomain!: pulumi.Output<string | undefined>;

    /**
     * Create a ContainerRegistry resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ContainerRegistryArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ContainerRegistryArgs | ContainerRegistryState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ContainerRegistryState | undefined;
            inputs["accessLevel"] = state ? state.accessLevel : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["fqdn"] = state ? state.fqdn : undefined;
            inputs["iconId"] = state ? state.iconId : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["subdomainLabel"] = state ? state.subdomainLabel : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["users"] = state ? state.users : undefined;
            inputs["virtualDomain"] = state ? state.virtualDomain : undefined;
        } else {
            const args = argsOrState as ContainerRegistryArgs | undefined;
            if ((!args || args.accessLevel === undefined) && !opts.urn) {
                throw new Error("Missing required property 'accessLevel'");
            }
            if ((!args || args.subdomainLabel === undefined) && !opts.urn) {
                throw new Error("Missing required property 'subdomainLabel'");
            }
            inputs["accessLevel"] = args ? args.accessLevel : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["iconId"] = args ? args.iconId : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["subdomainLabel"] = args ? args.subdomainLabel : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["users"] = args ? args.users : undefined;
            inputs["virtualDomain"] = args ? args.virtualDomain : undefined;
            inputs["fqdn"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(ContainerRegistry.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ContainerRegistry resources.
 */
export interface ContainerRegistryState {
    /**
     * The level of access that allow to users. This must be one of [`readwrite`/`readonly`/`none`].
     */
    accessLevel?: pulumi.Input<string>;
    /**
     * The description of the Container Registry. The length of this value must be in the range [`1`-`512`].
     */
    description?: pulumi.Input<string>;
    /**
     * The FQDN for accessing the Container Registry. FQDN is built from `subdomainLabel` + `.sakuracr.jp`.
     */
    fqdn?: pulumi.Input<string>;
    /**
     * The icon id to attach to the Container Registry.
     */
    iconId?: pulumi.Input<string>;
    /**
     * The name of the Container Registry. The length of this value must be in the range [`1`-`64`].
     */
    name?: pulumi.Input<string>;
    /**
     * The label at the lowest of the FQDN used when be accessed from users. The length of this value must be in the range [`1`-`64`]. Changing this forces a new resource to be created.
     */
    subdomainLabel?: pulumi.Input<string>;
    /**
     * Any tags to assign to the Container Registry.
     */
    tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * One or more `user` blocks as defined below.
     */
    users?: pulumi.Input<pulumi.Input<inputs.ContainerRegistryUser>[]>;
    /**
     * The alias for accessing the container registry.
     */
    virtualDomain?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a ContainerRegistry resource.
 */
export interface ContainerRegistryArgs {
    /**
     * The level of access that allow to users. This must be one of [`readwrite`/`readonly`/`none`].
     */
    accessLevel: pulumi.Input<string>;
    /**
     * The description of the Container Registry. The length of this value must be in the range [`1`-`512`].
     */
    description?: pulumi.Input<string>;
    /**
     * The icon id to attach to the Container Registry.
     */
    iconId?: pulumi.Input<string>;
    /**
     * The name of the Container Registry. The length of this value must be in the range [`1`-`64`].
     */
    name?: pulumi.Input<string>;
    /**
     * The label at the lowest of the FQDN used when be accessed from users. The length of this value must be in the range [`1`-`64`]. Changing this forces a new resource to be created.
     */
    subdomainLabel: pulumi.Input<string>;
    /**
     * Any tags to assign to the Container Registry.
     */
    tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * One or more `user` blocks as defined below.
     */
    users?: pulumi.Input<pulumi.Input<inputs.ContainerRegistryUser>[]>;
    /**
     * The alias for accessing the container registry.
     */
    virtualDomain?: pulumi.Input<string>;
}
