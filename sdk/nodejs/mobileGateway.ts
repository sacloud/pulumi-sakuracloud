// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "./types";
import * as utilities from "./utilities";

/**
 * Manages a SakuraCloud Mobile Gateway.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as sakuracloud from "@pulumi/sakuracloud";
 *
 * const zone = sakuracloud.getZone({});
 * const foobarSwitch = new sakuracloud.Switch("foobarSwitch", {});
 * const foobarMobileGateway = new sakuracloud.MobileGateway("foobarMobileGateway", {
 *     internetConnection: true,
 *     dnsServers: zone.then(zone => zone.dnsServers),
 *     privateNetworkInterface: {
 *         switchId: foobarSwitch.id,
 *         ipAddress: "192.168.11.101",
 *         netmask: 24,
 *     },
 *     description: "description",
 *     tags: [
 *         "tag1",
 *         "tag2",
 *     ],
 *     trafficControl: {
 *         quota: 256,
 *         bandWidthLimit: 64,
 *         enableEmail: true,
 *         enableSlack: true,
 *         slackWebhook: "https://hooks.slack.com/services/xxx/xxx/xxx",
 *         autoTrafficShaping: true,
 *     },
 *     staticRoutes: [
 *         {
 *             prefix: "192.168.10.0/24",
 *             nextHop: "192.168.11.1",
 *         },
 *         {
 *             prefix: "192.168.10.0/25",
 *             nextHop: "192.168.11.2",
 *         },
 *         {
 *             prefix: "192.168.10.0/26",
 *             nextHop: "192.168.11.3",
 *         },
 *     ],
 * });
 * ```
 */
export class MobileGateway extends pulumi.CustomResource {
    /**
     * Get an existing MobileGateway resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: MobileGatewayState, opts?: pulumi.CustomResourceOptions): MobileGateway {
        return new MobileGateway(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'sakuracloud:index/mobileGateway:MobileGateway';

    /**
     * Returns true if the given object is an instance of MobileGateway.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is MobileGateway {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === MobileGateway.__pulumiType;
    }

    /**
     * The description of the MobileGateway. The length of this value must be in the range [`1`-`512`].
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * A list of IP address used by each connected devices.
     */
    public readonly dnsServers!: pulumi.Output<string[]>;
    /**
     * The icon id to attach to the MobileGateway.
     */
    public readonly iconId!: pulumi.Output<string | undefined>;
    /**
     * The flag to allow communication between each connected devices.
     */
    public readonly interDeviceCommunication!: pulumi.Output<boolean | undefined>;
    /**
     * The flag to enable connect to the Internet.
     */
    public readonly internetConnection!: pulumi.Output<boolean | undefined>;
    /**
     * The name of the MobileGateway. The length of this value must be in the range [`1`-`64`].
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * An `privateNetworkInterface` block as defined below.
     */
    public readonly privateNetworkInterface!: pulumi.Output<outputs.MobileGatewayPrivateNetworkInterface | undefined>;
    /**
     * The public IP address assigned to the MobileGateway.
     */
    public /*out*/ readonly publicIp!: pulumi.Output<string>;
    /**
     * The bit length of the subnet assigned to the MobileGateway.
     */
    public /*out*/ readonly publicNetmask!: pulumi.Output<number>;
    /**
     * One or more `simRoute` blocks as defined below.
     */
    public readonly simRoutes!: pulumi.Output<outputs.MobileGatewaySimRoute[] | undefined>;
    /**
     * One or more `sim` blocks as defined below.
     */
    public readonly sims!: pulumi.Output<outputs.MobileGatewaySim[] | undefined>;
    /**
     * One or more `staticRoute` blocks as defined below.
     */
    public readonly staticRoutes!: pulumi.Output<outputs.MobileGatewayStaticRoute[] | undefined>;
    /**
     * Any tags to assign to the MobileGateway.
     */
    public readonly tags!: pulumi.Output<string[] | undefined>;
    /**
     * A `trafficControl` block as defined below.
     */
    public readonly trafficControl!: pulumi.Output<outputs.MobileGatewayTrafficControl | undefined>;
    /**
     * The name of zone that the MobileGateway will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
     */
    public readonly zone!: pulumi.Output<string>;

    /**
     * Create a MobileGateway resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: MobileGatewayArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: MobileGatewayArgs | MobileGatewayState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as MobileGatewayState | undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["dnsServers"] = state ? state.dnsServers : undefined;
            inputs["iconId"] = state ? state.iconId : undefined;
            inputs["interDeviceCommunication"] = state ? state.interDeviceCommunication : undefined;
            inputs["internetConnection"] = state ? state.internetConnection : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["privateNetworkInterface"] = state ? state.privateNetworkInterface : undefined;
            inputs["publicIp"] = state ? state.publicIp : undefined;
            inputs["publicNetmask"] = state ? state.publicNetmask : undefined;
            inputs["simRoutes"] = state ? state.simRoutes : undefined;
            inputs["sims"] = state ? state.sims : undefined;
            inputs["staticRoutes"] = state ? state.staticRoutes : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["trafficControl"] = state ? state.trafficControl : undefined;
            inputs["zone"] = state ? state.zone : undefined;
        } else {
            const args = argsOrState as MobileGatewayArgs | undefined;
            if ((!args || args.dnsServers === undefined) && !opts.urn) {
                throw new Error("Missing required property 'dnsServers'");
            }
            inputs["description"] = args ? args.description : undefined;
            inputs["dnsServers"] = args ? args.dnsServers : undefined;
            inputs["iconId"] = args ? args.iconId : undefined;
            inputs["interDeviceCommunication"] = args ? args.interDeviceCommunication : undefined;
            inputs["internetConnection"] = args ? args.internetConnection : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["privateNetworkInterface"] = args ? args.privateNetworkInterface : undefined;
            inputs["simRoutes"] = args ? args.simRoutes : undefined;
            inputs["sims"] = args ? args.sims : undefined;
            inputs["staticRoutes"] = args ? args.staticRoutes : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["trafficControl"] = args ? args.trafficControl : undefined;
            inputs["zone"] = args ? args.zone : undefined;
            inputs["publicIp"] = undefined /*out*/;
            inputs["publicNetmask"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(MobileGateway.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering MobileGateway resources.
 */
export interface MobileGatewayState {
    /**
     * The description of the MobileGateway. The length of this value must be in the range [`1`-`512`].
     */
    description?: pulumi.Input<string>;
    /**
     * A list of IP address used by each connected devices.
     */
    dnsServers?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The icon id to attach to the MobileGateway.
     */
    iconId?: pulumi.Input<string>;
    /**
     * The flag to allow communication between each connected devices.
     */
    interDeviceCommunication?: pulumi.Input<boolean>;
    /**
     * The flag to enable connect to the Internet.
     */
    internetConnection?: pulumi.Input<boolean>;
    /**
     * The name of the MobileGateway. The length of this value must be in the range [`1`-`64`].
     */
    name?: pulumi.Input<string>;
    /**
     * An `privateNetworkInterface` block as defined below.
     */
    privateNetworkInterface?: pulumi.Input<inputs.MobileGatewayPrivateNetworkInterface>;
    /**
     * The public IP address assigned to the MobileGateway.
     */
    publicIp?: pulumi.Input<string>;
    /**
     * The bit length of the subnet assigned to the MobileGateway.
     */
    publicNetmask?: pulumi.Input<number>;
    /**
     * One or more `simRoute` blocks as defined below.
     */
    simRoutes?: pulumi.Input<pulumi.Input<inputs.MobileGatewaySimRoute>[]>;
    /**
     * One or more `sim` blocks as defined below.
     */
    sims?: pulumi.Input<pulumi.Input<inputs.MobileGatewaySim>[]>;
    /**
     * One or more `staticRoute` blocks as defined below.
     */
    staticRoutes?: pulumi.Input<pulumi.Input<inputs.MobileGatewayStaticRoute>[]>;
    /**
     * Any tags to assign to the MobileGateway.
     */
    tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * A `trafficControl` block as defined below.
     */
    trafficControl?: pulumi.Input<inputs.MobileGatewayTrafficControl>;
    /**
     * The name of zone that the MobileGateway will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
     */
    zone?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a MobileGateway resource.
 */
export interface MobileGatewayArgs {
    /**
     * The description of the MobileGateway. The length of this value must be in the range [`1`-`512`].
     */
    description?: pulumi.Input<string>;
    /**
     * A list of IP address used by each connected devices.
     */
    dnsServers: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The icon id to attach to the MobileGateway.
     */
    iconId?: pulumi.Input<string>;
    /**
     * The flag to allow communication between each connected devices.
     */
    interDeviceCommunication?: pulumi.Input<boolean>;
    /**
     * The flag to enable connect to the Internet.
     */
    internetConnection?: pulumi.Input<boolean>;
    /**
     * The name of the MobileGateway. The length of this value must be in the range [`1`-`64`].
     */
    name?: pulumi.Input<string>;
    /**
     * An `privateNetworkInterface` block as defined below.
     */
    privateNetworkInterface?: pulumi.Input<inputs.MobileGatewayPrivateNetworkInterface>;
    /**
     * One or more `simRoute` blocks as defined below.
     */
    simRoutes?: pulumi.Input<pulumi.Input<inputs.MobileGatewaySimRoute>[]>;
    /**
     * One or more `sim` blocks as defined below.
     */
    sims?: pulumi.Input<pulumi.Input<inputs.MobileGatewaySim>[]>;
    /**
     * One or more `staticRoute` blocks as defined below.
     */
    staticRoutes?: pulumi.Input<pulumi.Input<inputs.MobileGatewayStaticRoute>[]>;
    /**
     * Any tags to assign to the MobileGateway.
     */
    tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * A `trafficControl` block as defined below.
     */
    trafficControl?: pulumi.Input<inputs.MobileGatewayTrafficControl>;
    /**
     * The name of zone that the MobileGateway will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
     */
    zone?: pulumi.Input<string>;
}
