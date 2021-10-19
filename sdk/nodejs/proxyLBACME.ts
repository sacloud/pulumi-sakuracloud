// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "./types";
import * as utilities from "./utilities";

/**
 * Manages a SakuraCloud ProxyLB ACME Setting.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as sakuracloud from "@pulumi/sakuracloud";
 *
 * const foobarProxyLBACME = new sakuracloud.ProxyLBACME("foobarProxyLBACME", {
 *     proxylbId: sakuracloud_proxylb.foobar.id,
 *     acceptTos: true,
 *     commonName: "www.example.com",
 *     subjectAltNames: ["www1.example.com"],
 *     updateDelaySec: 120,
 * });
 * const foobarProxyLB = sakuracloud.getProxyLB({
 *     filter: {
 *         names: ["foobar"],
 *     },
 * });
 * ```
 */
export class ProxyLBACME extends pulumi.CustomResource {
    /**
     * Get an existing ProxyLBACME resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ProxyLBACMEState, opts?: pulumi.CustomResourceOptions): ProxyLBACME {
        return new ProxyLBACME(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'sakuracloud:index/proxyLBACME:ProxyLBACME';

    /**
     * Returns true if the given object is an instance of ProxyLBACME.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ProxyLBACME {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ProxyLBACME.__pulumiType;
    }

    /**
     * The flag to accept the current Let's Encrypt terms of service(see: https://letsencrypt.org/repository/). This must be set `true` explicitly. Changing this forces a new resource to be created.
     */
    public readonly acceptTos!: pulumi.Output<boolean>;
    /**
     * A list of `certificate` blocks as defined below.
     */
    public /*out*/ readonly certificates!: pulumi.Output<outputs.ProxyLBACMECertificate[]>;
    /**
     * The FQDN used by ACME. This must set resolvable value. Changing this forces a new resource to be created.
     */
    public readonly commonName!: pulumi.Output<string>;
    /**
     * The id of the ProxyLB that set ACME settings to. Changing this forces a new resource to be created.
     */
    public readonly proxylbId!: pulumi.Output<string>;
    /**
     * The Subject alternative names used by ACME. Changing this forces a new resource to be created.
     */
    public readonly subjectAltNames!: pulumi.Output<string[] | undefined>;
    /**
     * The wait time in seconds. This typically used for waiting for a DNS propagation. Changing this forces a new resource to be created.
     */
    public readonly updateDelaySec!: pulumi.Output<number | undefined>;

    /**
     * Create a ProxyLBACME resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ProxyLBACMEArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ProxyLBACMEArgs | ProxyLBACMEState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ProxyLBACMEState | undefined;
            inputs["acceptTos"] = state ? state.acceptTos : undefined;
            inputs["certificates"] = state ? state.certificates : undefined;
            inputs["commonName"] = state ? state.commonName : undefined;
            inputs["proxylbId"] = state ? state.proxylbId : undefined;
            inputs["subjectAltNames"] = state ? state.subjectAltNames : undefined;
            inputs["updateDelaySec"] = state ? state.updateDelaySec : undefined;
        } else {
            const args = argsOrState as ProxyLBACMEArgs | undefined;
            if ((!args || args.acceptTos === undefined) && !opts.urn) {
                throw new Error("Missing required property 'acceptTos'");
            }
            if ((!args || args.commonName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'commonName'");
            }
            if ((!args || args.proxylbId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'proxylbId'");
            }
            inputs["acceptTos"] = args ? args.acceptTos : undefined;
            inputs["commonName"] = args ? args.commonName : undefined;
            inputs["proxylbId"] = args ? args.proxylbId : undefined;
            inputs["subjectAltNames"] = args ? args.subjectAltNames : undefined;
            inputs["updateDelaySec"] = args ? args.updateDelaySec : undefined;
            inputs["certificates"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(ProxyLBACME.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ProxyLBACME resources.
 */
export interface ProxyLBACMEState {
    /**
     * The flag to accept the current Let's Encrypt terms of service(see: https://letsencrypt.org/repository/). This must be set `true` explicitly. Changing this forces a new resource to be created.
     */
    readonly acceptTos?: pulumi.Input<boolean>;
    /**
     * A list of `certificate` blocks as defined below.
     */
    readonly certificates?: pulumi.Input<pulumi.Input<inputs.ProxyLBACMECertificate>[]>;
    /**
     * The FQDN used by ACME. This must set resolvable value. Changing this forces a new resource to be created.
     */
    readonly commonName?: pulumi.Input<string>;
    /**
     * The id of the ProxyLB that set ACME settings to. Changing this forces a new resource to be created.
     */
    readonly proxylbId?: pulumi.Input<string>;
    /**
     * The Subject alternative names used by ACME. Changing this forces a new resource to be created.
     */
    readonly subjectAltNames?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The wait time in seconds. This typically used for waiting for a DNS propagation. Changing this forces a new resource to be created.
     */
    readonly updateDelaySec?: pulumi.Input<number>;
}

/**
 * The set of arguments for constructing a ProxyLBACME resource.
 */
export interface ProxyLBACMEArgs {
    /**
     * The flag to accept the current Let's Encrypt terms of service(see: https://letsencrypt.org/repository/). This must be set `true` explicitly. Changing this forces a new resource to be created.
     */
    readonly acceptTos: pulumi.Input<boolean>;
    /**
     * The FQDN used by ACME. This must set resolvable value. Changing this forces a new resource to be created.
     */
    readonly commonName: pulumi.Input<string>;
    /**
     * The id of the ProxyLB that set ACME settings to. Changing this forces a new resource to be created.
     */
    readonly proxylbId: pulumi.Input<string>;
    /**
     * The Subject alternative names used by ACME. Changing this forces a new resource to be created.
     */
    readonly subjectAltNames?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The wait time in seconds. This typically used for waiting for a DNS propagation. Changing this forces a new resource to be created.
     */
    readonly updateDelaySec?: pulumi.Input<number>;
}
