// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "./types";
import * as utilities from "./utilities";

/**
 * Manages a SakuraCloud ProxyLB.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as sakuracloud from "@pulumi/sakuracloud";
 *
 * const foobarServer = new sakuracloud.Server("foobarServer", {networkInterfaces: [{
 *     upstream: "shared",
 * }]});
 * const foobarProxyLB = new sakuracloud.ProxyLB("foobarProxyLB", {
 *     plan: 100,
 *     vipFailover: true,
 *     stickySession: true,
 *     gzip: true,
 *     timeout: 10,
 *     region: "is1",
 *     healthCheck: {
 *         protocol: "http",
 *         delayLoop: 10,
 *         hostHeader: "example.com",
 *         path: "/",
 *     },
 *     sorryServer: {
 *         ipAddress: "192.0.2.1",
 *         port: 80,
 *     },
 *     bindPorts: [{
 *         proxyMode: "http",
 *         port: 80,
 *         responseHeaders: [{
 *             header: "Cache-Control",
 *             value: "public, max-age=10",
 *         }],
 *     }],
 *     servers: [{
 *         ipAddress: foobarServer.ipAddress,
 *         port: 80,
 *         group: "group1",
 *     }],
 *     rules: [{
 *         host: "www.example.com",
 *         path: "/",
 *         group: "group1",
 *     }],
 *     description: "description",
 *     tags: [
 *         "tag1",
 *         "tag2",
 *     ],
 * });
 * ```
 */
export class ProxyLB extends pulumi.CustomResource {
    /**
     * Get an existing ProxyLB resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ProxyLBState, opts?: pulumi.CustomResourceOptions): ProxyLB {
        return new ProxyLB(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'sakuracloud:index/proxyLB:ProxyLB';

    /**
     * Returns true if the given object is an instance of ProxyLB.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ProxyLB {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ProxyLB.__pulumiType;
    }

    /**
     * One or more `bindPort` blocks as defined below.
     */
    public readonly bindPorts!: pulumi.Output<outputs.ProxyLBBindPort[]>;
    /**
     * An `certificate` block as defined below.
     */
    public readonly certificate!: pulumi.Output<outputs.ProxyLBCertificate>;
    /**
     * The description of the ProxyLB. The length of this value must be in the range [`1`-`512`].
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The FQDN for accessing to the ProxyLB. This is typically used as value of CNAME record.
     */
    public /*out*/ readonly fqdn!: pulumi.Output<string>;
    /**
     * The flag to enable gzip compression.
     * ---
     */
    public readonly gzip!: pulumi.Output<boolean | undefined>;
    /**
     * A `healthCheck` block as defined below.
     */
    public readonly healthCheck!: pulumi.Output<outputs.ProxyLBHealthCheck>;
    /**
     * The icon id to attach to the ProxyLB.
     */
    public readonly iconId!: pulumi.Output<string | undefined>;
    /**
     * The name of the ProxyLB. The length of this value must be in the range [`1`-`64`].
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The plan name of the ProxyLB. This must be one of [`100`/`500`/`1000`/`5000`/`10000`/`50000`/`100000`]. Default:`100`.
     */
    public readonly plan!: pulumi.Output<number | undefined>;
    /**
     * A list of CIDR block used by the ProxyLB to access the server.
     */
    public /*out*/ readonly proxyNetworks!: pulumi.Output<string[]>;
    /**
     * The name of region that the proxy LB is in. This must be one of [`tk1`/`is1`/`anycast`]. Changing this forces a new resource to be created. Default:`is1`.
     */
    public readonly region!: pulumi.Output<string | undefined>;
    /**
     * One or more `rule` blocks as defined below.
     */
    public readonly rules!: pulumi.Output<outputs.ProxyLBRule[] | undefined>;
    /**
     * One or more `server` blocks as defined below.
     */
    public readonly servers!: pulumi.Output<outputs.ProxyLBServer[] | undefined>;
    /**
     * A `sorryServer` block as defined below.
     */
    public readonly sorryServer!: pulumi.Output<outputs.ProxyLBSorryServer | undefined>;
    /**
     * The flag to enable sticky session.
     */
    public readonly stickySession!: pulumi.Output<boolean | undefined>;
    /**
     * Any tags to assign to the ProxyLB.
     */
    public readonly tags!: pulumi.Output<string[] | undefined>;
    /**
     * The timeout duration in seconds. Default:`10`.
     */
    public readonly timeout!: pulumi.Output<number | undefined>;
    /**
     * The virtual IP address assigned to the ProxyLB.
     */
    public /*out*/ readonly vip!: pulumi.Output<string>;
    /**
     * The flag to enable VIP fail-over. Changing this forces a new resource to be created.
     */
    public readonly vipFailover!: pulumi.Output<boolean | undefined>;

    /**
     * Create a ProxyLB resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ProxyLBArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ProxyLBArgs | ProxyLBState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ProxyLBState | undefined;
            inputs["bindPorts"] = state ? state.bindPorts : undefined;
            inputs["certificate"] = state ? state.certificate : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["fqdn"] = state ? state.fqdn : undefined;
            inputs["gzip"] = state ? state.gzip : undefined;
            inputs["healthCheck"] = state ? state.healthCheck : undefined;
            inputs["iconId"] = state ? state.iconId : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["plan"] = state ? state.plan : undefined;
            inputs["proxyNetworks"] = state ? state.proxyNetworks : undefined;
            inputs["region"] = state ? state.region : undefined;
            inputs["rules"] = state ? state.rules : undefined;
            inputs["servers"] = state ? state.servers : undefined;
            inputs["sorryServer"] = state ? state.sorryServer : undefined;
            inputs["stickySession"] = state ? state.stickySession : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["timeout"] = state ? state.timeout : undefined;
            inputs["vip"] = state ? state.vip : undefined;
            inputs["vipFailover"] = state ? state.vipFailover : undefined;
        } else {
            const args = argsOrState as ProxyLBArgs | undefined;
            if ((!args || args.bindPorts === undefined) && !opts.urn) {
                throw new Error("Missing required property 'bindPorts'");
            }
            if ((!args || args.healthCheck === undefined) && !opts.urn) {
                throw new Error("Missing required property 'healthCheck'");
            }
            inputs["bindPorts"] = args ? args.bindPorts : undefined;
            inputs["certificate"] = args ? args.certificate : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["gzip"] = args ? args.gzip : undefined;
            inputs["healthCheck"] = args ? args.healthCheck : undefined;
            inputs["iconId"] = args ? args.iconId : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["plan"] = args ? args.plan : undefined;
            inputs["region"] = args ? args.region : undefined;
            inputs["rules"] = args ? args.rules : undefined;
            inputs["servers"] = args ? args.servers : undefined;
            inputs["sorryServer"] = args ? args.sorryServer : undefined;
            inputs["stickySession"] = args ? args.stickySession : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["timeout"] = args ? args.timeout : undefined;
            inputs["vipFailover"] = args ? args.vipFailover : undefined;
            inputs["fqdn"] = undefined /*out*/;
            inputs["proxyNetworks"] = undefined /*out*/;
            inputs["vip"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(ProxyLB.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ProxyLB resources.
 */
export interface ProxyLBState {
    /**
     * One or more `bindPort` blocks as defined below.
     */
    readonly bindPorts?: pulumi.Input<pulumi.Input<inputs.ProxyLBBindPort>[]>;
    /**
     * An `certificate` block as defined below.
     */
    readonly certificate?: pulumi.Input<inputs.ProxyLBCertificate>;
    /**
     * The description of the ProxyLB. The length of this value must be in the range [`1`-`512`].
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The FQDN for accessing to the ProxyLB. This is typically used as value of CNAME record.
     */
    readonly fqdn?: pulumi.Input<string>;
    /**
     * The flag to enable gzip compression.
     * ---
     */
    readonly gzip?: pulumi.Input<boolean>;
    /**
     * A `healthCheck` block as defined below.
     */
    readonly healthCheck?: pulumi.Input<inputs.ProxyLBHealthCheck>;
    /**
     * The icon id to attach to the ProxyLB.
     */
    readonly iconId?: pulumi.Input<string>;
    /**
     * The name of the ProxyLB. The length of this value must be in the range [`1`-`64`].
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The plan name of the ProxyLB. This must be one of [`100`/`500`/`1000`/`5000`/`10000`/`50000`/`100000`]. Default:`100`.
     */
    readonly plan?: pulumi.Input<number>;
    /**
     * A list of CIDR block used by the ProxyLB to access the server.
     */
    readonly proxyNetworks?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The name of region that the proxy LB is in. This must be one of [`tk1`/`is1`/`anycast`]. Changing this forces a new resource to be created. Default:`is1`.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * One or more `rule` blocks as defined below.
     */
    readonly rules?: pulumi.Input<pulumi.Input<inputs.ProxyLBRule>[]>;
    /**
     * One or more `server` blocks as defined below.
     */
    readonly servers?: pulumi.Input<pulumi.Input<inputs.ProxyLBServer>[]>;
    /**
     * A `sorryServer` block as defined below.
     */
    readonly sorryServer?: pulumi.Input<inputs.ProxyLBSorryServer>;
    /**
     * The flag to enable sticky session.
     */
    readonly stickySession?: pulumi.Input<boolean>;
    /**
     * Any tags to assign to the ProxyLB.
     */
    readonly tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The timeout duration in seconds. Default:`10`.
     */
    readonly timeout?: pulumi.Input<number>;
    /**
     * The virtual IP address assigned to the ProxyLB.
     */
    readonly vip?: pulumi.Input<string>;
    /**
     * The flag to enable VIP fail-over. Changing this forces a new resource to be created.
     */
    readonly vipFailover?: pulumi.Input<boolean>;
}

/**
 * The set of arguments for constructing a ProxyLB resource.
 */
export interface ProxyLBArgs {
    /**
     * One or more `bindPort` blocks as defined below.
     */
    readonly bindPorts: pulumi.Input<pulumi.Input<inputs.ProxyLBBindPort>[]>;
    /**
     * An `certificate` block as defined below.
     */
    readonly certificate?: pulumi.Input<inputs.ProxyLBCertificate>;
    /**
     * The description of the ProxyLB. The length of this value must be in the range [`1`-`512`].
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The flag to enable gzip compression.
     * ---
     */
    readonly gzip?: pulumi.Input<boolean>;
    /**
     * A `healthCheck` block as defined below.
     */
    readonly healthCheck: pulumi.Input<inputs.ProxyLBHealthCheck>;
    /**
     * The icon id to attach to the ProxyLB.
     */
    readonly iconId?: pulumi.Input<string>;
    /**
     * The name of the ProxyLB. The length of this value must be in the range [`1`-`64`].
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The plan name of the ProxyLB. This must be one of [`100`/`500`/`1000`/`5000`/`10000`/`50000`/`100000`]. Default:`100`.
     */
    readonly plan?: pulumi.Input<number>;
    /**
     * The name of region that the proxy LB is in. This must be one of [`tk1`/`is1`/`anycast`]. Changing this forces a new resource to be created. Default:`is1`.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * One or more `rule` blocks as defined below.
     */
    readonly rules?: pulumi.Input<pulumi.Input<inputs.ProxyLBRule>[]>;
    /**
     * One or more `server` blocks as defined below.
     */
    readonly servers?: pulumi.Input<pulumi.Input<inputs.ProxyLBServer>[]>;
    /**
     * A `sorryServer` block as defined below.
     */
    readonly sorryServer?: pulumi.Input<inputs.ProxyLBSorryServer>;
    /**
     * The flag to enable sticky session.
     */
    readonly stickySession?: pulumi.Input<boolean>;
    /**
     * Any tags to assign to the ProxyLB.
     */
    readonly tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The timeout duration in seconds. Default:`10`.
     */
    readonly timeout?: pulumi.Input<number>;
    /**
     * The flag to enable VIP fail-over. Changing this forces a new resource to be created.
     */
    readonly vipFailover?: pulumi.Input<boolean>;
}
