// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Provides a SakuraCloud Mobile Gateway resource. This can be used to create, update, and delete Mobile Gateways.
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-sakuracloud/blob/master/website/docs/r/mobile_gateway.html.markdown.
 */
export class MobileGateway extends pulumi.CustomResource {
    /**
     * Get an existing MobileGateway resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
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
     * The description of the resource.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The primary DNS server IP address.
     */
    public readonly dnsServer1!: pulumi.Output<string>;
    /**
     * The secondly DNS server IP address.
     */
    public readonly dnsServer2!: pulumi.Output<string>;
    /**
     * The wait time (seconds) to do graceful shutdown the server connected to the resource.
     */
    public readonly gracefulShutdownTimeout!: pulumi.Output<number | undefined>;
    /**
     * The ID of the icon.
     */
    public readonly iconId!: pulumi.Output<string | undefined>;
    /**
     * The flag of enable/disable connecting from MobileGateway to the Internet.
     */
    public readonly internetConnection!: pulumi.Output<boolean | undefined>;
    /**
     * The name of the resource.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The IP address on private NIC of the Mobile Gateway.
     */
    public readonly privateIpaddress!: pulumi.Output<string | undefined>;
    /**
     * The network mask length on private NIC of the Mobile Gateway.
     */
    public readonly privateNwMaskLen!: pulumi.Output<number | undefined>;
    /**
     * The IP address on public NIC of the Mobile Gateway.
     */
    public /*out*/ readonly publicIpaddress!: pulumi.Output<string>;
    /**
     * The network mask length on public NIC of the Mobile Gateway.
     */
    public /*out*/ readonly publicNwMaskLen!: pulumi.Output<number>;
    /**
     * The ID list of the SIMs connected to the Mobile Gateway.
     */
    public /*out*/ readonly simIds!: pulumi.Output<string[]>;
    public readonly staticRoutes!: pulumi.Output<outputs.MobileGatewayStaticRoute[]>;
    /**
     * The ID of the switch connected to the Mobile Gateway.
     */
    public readonly switchId!: pulumi.Output<string | undefined>;
    /**
     * The tag list of the resources.
     */
    public readonly tags!: pulumi.Output<string[]>;
    /**
     * Traffic control rules. It contains some attributes to Traffic Control.
     */
    public readonly trafficControl!: pulumi.Output<outputs.MobileGatewayTrafficControl | undefined>;
    /**
     * The ID of the zone to which the resource belongs.
     */
    public readonly zone!: pulumi.Output<string>;

    /**
     * Create a MobileGateway resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: MobileGatewayArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: MobileGatewayArgs | MobileGatewayState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as MobileGatewayState | undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["dnsServer1"] = state ? state.dnsServer1 : undefined;
            inputs["dnsServer2"] = state ? state.dnsServer2 : undefined;
            inputs["gracefulShutdownTimeout"] = state ? state.gracefulShutdownTimeout : undefined;
            inputs["iconId"] = state ? state.iconId : undefined;
            inputs["internetConnection"] = state ? state.internetConnection : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["privateIpaddress"] = state ? state.privateIpaddress : undefined;
            inputs["privateNwMaskLen"] = state ? state.privateNwMaskLen : undefined;
            inputs["publicIpaddress"] = state ? state.publicIpaddress : undefined;
            inputs["publicNwMaskLen"] = state ? state.publicNwMaskLen : undefined;
            inputs["simIds"] = state ? state.simIds : undefined;
            inputs["staticRoutes"] = state ? state.staticRoutes : undefined;
            inputs["switchId"] = state ? state.switchId : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["trafficControl"] = state ? state.trafficControl : undefined;
            inputs["zone"] = state ? state.zone : undefined;
        } else {
            const args = argsOrState as MobileGatewayArgs | undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["dnsServer1"] = args ? args.dnsServer1 : undefined;
            inputs["dnsServer2"] = args ? args.dnsServer2 : undefined;
            inputs["gracefulShutdownTimeout"] = args ? args.gracefulShutdownTimeout : undefined;
            inputs["iconId"] = args ? args.iconId : undefined;
            inputs["internetConnection"] = args ? args.internetConnection : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["privateIpaddress"] = args ? args.privateIpaddress : undefined;
            inputs["privateNwMaskLen"] = args ? args.privateNwMaskLen : undefined;
            inputs["staticRoutes"] = args ? args.staticRoutes : undefined;
            inputs["switchId"] = args ? args.switchId : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["trafficControl"] = args ? args.trafficControl : undefined;
            inputs["zone"] = args ? args.zone : undefined;
            inputs["publicIpaddress"] = undefined /*out*/;
            inputs["publicNwMaskLen"] = undefined /*out*/;
            inputs["simIds"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(MobileGateway.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering MobileGateway resources.
 */
export interface MobileGatewayState {
    /**
     * The description of the resource.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The primary DNS server IP address.
     */
    readonly dnsServer1?: pulumi.Input<string>;
    /**
     * The secondly DNS server IP address.
     */
    readonly dnsServer2?: pulumi.Input<string>;
    /**
     * The wait time (seconds) to do graceful shutdown the server connected to the resource.
     */
    readonly gracefulShutdownTimeout?: pulumi.Input<number>;
    /**
     * The ID of the icon.
     */
    readonly iconId?: pulumi.Input<string>;
    /**
     * The flag of enable/disable connecting from MobileGateway to the Internet.
     */
    readonly internetConnection?: pulumi.Input<boolean>;
    /**
     * The name of the resource.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The IP address on private NIC of the Mobile Gateway.
     */
    readonly privateIpaddress?: pulumi.Input<string>;
    /**
     * The network mask length on private NIC of the Mobile Gateway.
     */
    readonly privateNwMaskLen?: pulumi.Input<number>;
    /**
     * The IP address on public NIC of the Mobile Gateway.
     */
    readonly publicIpaddress?: pulumi.Input<string>;
    /**
     * The network mask length on public NIC of the Mobile Gateway.
     */
    readonly publicNwMaskLen?: pulumi.Input<number>;
    /**
     * The ID list of the SIMs connected to the Mobile Gateway.
     */
    readonly simIds?: pulumi.Input<pulumi.Input<string>[]>;
    readonly staticRoutes?: pulumi.Input<pulumi.Input<inputs.MobileGatewayStaticRoute>[]>;
    /**
     * The ID of the switch connected to the Mobile Gateway.
     */
    readonly switchId?: pulumi.Input<string>;
    /**
     * The tag list of the resources.
     */
    readonly tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Traffic control rules. It contains some attributes to Traffic Control.
     */
    readonly trafficControl?: pulumi.Input<inputs.MobileGatewayTrafficControl>;
    /**
     * The ID of the zone to which the resource belongs.
     */
    readonly zone?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a MobileGateway resource.
 */
export interface MobileGatewayArgs {
    /**
     * The description of the resource.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The primary DNS server IP address.
     */
    readonly dnsServer1?: pulumi.Input<string>;
    /**
     * The secondly DNS server IP address.
     */
    readonly dnsServer2?: pulumi.Input<string>;
    /**
     * The wait time (seconds) to do graceful shutdown the server connected to the resource.
     */
    readonly gracefulShutdownTimeout?: pulumi.Input<number>;
    /**
     * The ID of the icon.
     */
    readonly iconId?: pulumi.Input<string>;
    /**
     * The flag of enable/disable connecting from MobileGateway to the Internet.
     */
    readonly internetConnection?: pulumi.Input<boolean>;
    /**
     * The name of the resource.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The IP address on private NIC of the Mobile Gateway.
     */
    readonly privateIpaddress?: pulumi.Input<string>;
    /**
     * The network mask length on private NIC of the Mobile Gateway.
     */
    readonly privateNwMaskLen?: pulumi.Input<number>;
    readonly staticRoutes?: pulumi.Input<pulumi.Input<inputs.MobileGatewayStaticRoute>[]>;
    /**
     * The ID of the switch connected to the Mobile Gateway.
     */
    readonly switchId?: pulumi.Input<string>;
    /**
     * The tag list of the resources.
     */
    readonly tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Traffic control rules. It contains some attributes to Traffic Control.
     */
    readonly trafficControl?: pulumi.Input<inputs.MobileGatewayTrafficControl>;
    /**
     * The ID of the zone to which the resource belongs.
     */
    readonly zone?: pulumi.Input<string>;
}