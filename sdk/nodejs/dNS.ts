// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

export class DNS extends pulumi.CustomResource {
    /**
     * Get an existing DNS resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DNSState, opts?: pulumi.CustomResourceOptions): DNS {
        return new DNS(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'sakuracloud:index/dNS:DNS';

    /**
     * Returns true if the given object is an instance of DNS.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is DNS {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === DNS.__pulumiType;
    }

    /**
     * The description of the DNS. The length of this value must be in the range [`1`-`512`]
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * A list of IP address of DNS server that manage this zone
     */
    public /*out*/ readonly dnsServers!: pulumi.Output<string[]>;
    /**
     * The icon id to attach to the DNS
     */
    public readonly iconId!: pulumi.Output<string | undefined>;
    public readonly records!: pulumi.Output<outputs.DNSRecord[]>;
    /**
     * Any tags to assign to the DNS
     */
    public readonly tags!: pulumi.Output<string[] | undefined>;
    /**
     * The target zone. (e.g. `example.com`)
     */
    public readonly zone!: pulumi.Output<string>;

    /**
     * Create a DNS resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: DNSArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: DNSArgs | DNSState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as DNSState | undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["dnsServers"] = state ? state.dnsServers : undefined;
            inputs["iconId"] = state ? state.iconId : undefined;
            inputs["records"] = state ? state.records : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["zone"] = state ? state.zone : undefined;
        } else {
            const args = argsOrState as DNSArgs | undefined;
            if (!args || args.zone === undefined) {
                throw new Error("Missing required property 'zone'");
            }
            inputs["description"] = args ? args.description : undefined;
            inputs["iconId"] = args ? args.iconId : undefined;
            inputs["records"] = args ? args.records : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["zone"] = args ? args.zone : undefined;
            inputs["dnsServers"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(DNS.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering DNS resources.
 */
export interface DNSState {
    /**
     * The description of the DNS. The length of this value must be in the range [`1`-`512`]
     */
    readonly description?: pulumi.Input<string>;
    /**
     * A list of IP address of DNS server that manage this zone
     */
    readonly dnsServers?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The icon id to attach to the DNS
     */
    readonly iconId?: pulumi.Input<string>;
    readonly records?: pulumi.Input<pulumi.Input<inputs.DNSRecord>[]>;
    /**
     * Any tags to assign to the DNS
     */
    readonly tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The target zone. (e.g. `example.com`)
     */
    readonly zone?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a DNS resource.
 */
export interface DNSArgs {
    /**
     * The description of the DNS. The length of this value must be in the range [`1`-`512`]
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The icon id to attach to the DNS
     */
    readonly iconId?: pulumi.Input<string>;
    readonly records?: pulumi.Input<pulumi.Input<inputs.DNSRecord>[]>;
    /**
     * Any tags to assign to the DNS
     */
    readonly tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The target zone. (e.g. `example.com`)
     */
    readonly zone: pulumi.Input<string>;
}
