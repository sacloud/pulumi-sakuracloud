// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Manages a SakuraCloud IPv4 PTR.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as sakuracloud from "@pulumi/sakuracloud";
 *
 * const server = new sakuracloud.Server("server", {networkInterfaces: [{
 *     upstream: "shared",
 * }]});
 * const foobar = new sakuracloud.IPv4Ptr("foobar", {
 *     ipAddress: server.ipAddress,
 *     hostname: "www.example.com",
 *     retryMax: 30,
 *     retryInterval: 10,
 * });
 * ```
 */
export class IPv4Ptr extends pulumi.CustomResource {
    /**
     * Get an existing IPv4Ptr resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: IPv4PtrState, opts?: pulumi.CustomResourceOptions): IPv4Ptr {
        return new IPv4Ptr(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'sakuracloud:index/iPv4Ptr:IPv4Ptr';

    /**
     * Returns true if the given object is an instance of IPv4Ptr.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is IPv4Ptr {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === IPv4Ptr.__pulumiType;
    }

    /**
     * The value of the PTR record. This must be FQDN.
     */
    public readonly hostname!: pulumi.Output<string>;
    /**
     * The IP address to which the PTR record is set.
     */
    public readonly ipAddress!: pulumi.Output<string>;
    /**
     * The wait interval(in seconds) for retrying API call used when SakuraCloud API returns any errors. Default:`10`.
     */
    public readonly retryInterval!: pulumi.Output<number | undefined>;
    /**
     * The maximum number of API call retries used when SakuraCloud API returns any errors. Default:`30`.
     */
    public readonly retryMax!: pulumi.Output<number | undefined>;
    /**
     * The name of zone that the IPv4 PTR will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
     */
    public readonly zone!: pulumi.Output<string>;

    /**
     * Create a IPv4Ptr resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: IPv4PtrArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: IPv4PtrArgs | IPv4PtrState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as IPv4PtrState | undefined;
            inputs["hostname"] = state ? state.hostname : undefined;
            inputs["ipAddress"] = state ? state.ipAddress : undefined;
            inputs["retryInterval"] = state ? state.retryInterval : undefined;
            inputs["retryMax"] = state ? state.retryMax : undefined;
            inputs["zone"] = state ? state.zone : undefined;
        } else {
            const args = argsOrState as IPv4PtrArgs | undefined;
            if ((!args || args.hostname === undefined) && !opts.urn) {
                throw new Error("Missing required property 'hostname'");
            }
            if ((!args || args.ipAddress === undefined) && !opts.urn) {
                throw new Error("Missing required property 'ipAddress'");
            }
            inputs["hostname"] = args ? args.hostname : undefined;
            inputs["ipAddress"] = args ? args.ipAddress : undefined;
            inputs["retryInterval"] = args ? args.retryInterval : undefined;
            inputs["retryMax"] = args ? args.retryMax : undefined;
            inputs["zone"] = args ? args.zone : undefined;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(IPv4Ptr.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering IPv4Ptr resources.
 */
export interface IPv4PtrState {
    /**
     * The value of the PTR record. This must be FQDN.
     */
    hostname?: pulumi.Input<string>;
    /**
     * The IP address to which the PTR record is set.
     */
    ipAddress?: pulumi.Input<string>;
    /**
     * The wait interval(in seconds) for retrying API call used when SakuraCloud API returns any errors. Default:`10`.
     */
    retryInterval?: pulumi.Input<number>;
    /**
     * The maximum number of API call retries used when SakuraCloud API returns any errors. Default:`30`.
     */
    retryMax?: pulumi.Input<number>;
    /**
     * The name of zone that the IPv4 PTR will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
     */
    zone?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a IPv4Ptr resource.
 */
export interface IPv4PtrArgs {
    /**
     * The value of the PTR record. This must be FQDN.
     */
    hostname: pulumi.Input<string>;
    /**
     * The IP address to which the PTR record is set.
     */
    ipAddress: pulumi.Input<string>;
    /**
     * The wait interval(in seconds) for retrying API call used when SakuraCloud API returns any errors. Default:`10`.
     */
    retryInterval?: pulumi.Input<number>;
    /**
     * The maximum number of API call retries used when SakuraCloud API returns any errors. Default:`30`.
     */
    retryMax?: pulumi.Input<number>;
    /**
     * The name of zone that the IPv4 PTR will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
     */
    zone?: pulumi.Input<string>;
}