// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

export class Server extends pulumi.CustomResource {
    /**
     * Get an existing Server resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ServerState, opts?: pulumi.CustomResourceOptions): Server {
        return new Server(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'sakuracloud:index/server:Server';

    /**
     * Returns true if the given object is an instance of Server.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Server {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Server.__pulumiType;
    }

    /**
     * The id of the CD-ROM to attach to the Server
     */
    public readonly cdromId!: pulumi.Output<string | undefined>;
    /**
     * The policy of how to allocate virtual CPUs to the server. This must be one of [`standard`/`dedicatedcpu`]
     */
    public readonly commitment!: pulumi.Output<string | undefined>;
    /**
     * The number of virtual CPUs
     */
    public readonly core!: pulumi.Output<number | undefined>;
    /**
     * The description of the Server. The length of this value must be in the range [`1`-`512`]
     */
    public readonly description!: pulumi.Output<string | undefined>;
    public readonly diskEditParameter!: pulumi.Output<outputs.ServerDiskEditParameter | undefined>;
    /**
     * A list of disk id connected to the server
     */
    public readonly disks!: pulumi.Output<string[] | undefined>;
    /**
     * A list of IP address of DNS server in the zone
     */
    public /*out*/ readonly dnsServers!: pulumi.Output<string[]>;
    /**
     * The flag to use force shutdown when need to reboot/shutdown while applying
     */
    public readonly forceShutdown!: pulumi.Output<boolean | undefined>;
    /**
     * The IP address of the gateway used by Server
     */
    public /*out*/ readonly gateway!: pulumi.Output<string>;
    /**
     * The hostname of the Server
     */
    public /*out*/ readonly hostname!: pulumi.Output<string>;
    /**
     * The icon id to attach to the Server
     */
    public readonly iconId!: pulumi.Output<string | undefined>;
    /**
     * The driver name of network interface. This must be one of [`virtio`/`e1000`]
     */
    public readonly interfaceDriver!: pulumi.Output<string | undefined>;
    /**
     * The IP address assigned to the Server
     */
    public /*out*/ readonly ipAddress!: pulumi.Output<string>;
    /**
     * The size of memory in GiB
     */
    public readonly memory!: pulumi.Output<number | undefined>;
    /**
     * The name of the Server. The length of this value must be in the range [`1`-`64`]
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The bit length of the subnet assigned to the Server
     */
    public /*out*/ readonly netmask!: pulumi.Output<number>;
    /**
     * The network address which the `ip_address` belongs
     */
    public /*out*/ readonly networkAddress!: pulumi.Output<string>;
    public readonly networkInterfaces!: pulumi.Output<outputs.ServerNetworkInterface[] | undefined>;
    /**
     * The id of the PrivateHost which the Server is assigned
     */
    public readonly privateHostId!: pulumi.Output<string | undefined>;
    /**
     * The id of the PrivateHost which the Server is assigned
     */
    public /*out*/ readonly privateHostName!: pulumi.Output<string>;
    /**
     * Any tags to assign to the Server
     */
    public readonly tags!: pulumi.Output<string[] | undefined>;
    /**
     * The name of zone that the Server will be created (e.g. `is1a`, `tk1a`)
     */
    public readonly zone!: pulumi.Output<string>;

    /**
     * Create a Server resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: ServerArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ServerArgs | ServerState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as ServerState | undefined;
            inputs["cdromId"] = state ? state.cdromId : undefined;
            inputs["commitment"] = state ? state.commitment : undefined;
            inputs["core"] = state ? state.core : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["diskEditParameter"] = state ? state.diskEditParameter : undefined;
            inputs["disks"] = state ? state.disks : undefined;
            inputs["dnsServers"] = state ? state.dnsServers : undefined;
            inputs["forceShutdown"] = state ? state.forceShutdown : undefined;
            inputs["gateway"] = state ? state.gateway : undefined;
            inputs["hostname"] = state ? state.hostname : undefined;
            inputs["iconId"] = state ? state.iconId : undefined;
            inputs["interfaceDriver"] = state ? state.interfaceDriver : undefined;
            inputs["ipAddress"] = state ? state.ipAddress : undefined;
            inputs["memory"] = state ? state.memory : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["netmask"] = state ? state.netmask : undefined;
            inputs["networkAddress"] = state ? state.networkAddress : undefined;
            inputs["networkInterfaces"] = state ? state.networkInterfaces : undefined;
            inputs["privateHostId"] = state ? state.privateHostId : undefined;
            inputs["privateHostName"] = state ? state.privateHostName : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["zone"] = state ? state.zone : undefined;
        } else {
            const args = argsOrState as ServerArgs | undefined;
            inputs["cdromId"] = args ? args.cdromId : undefined;
            inputs["commitment"] = args ? args.commitment : undefined;
            inputs["core"] = args ? args.core : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["diskEditParameter"] = args ? args.diskEditParameter : undefined;
            inputs["disks"] = args ? args.disks : undefined;
            inputs["forceShutdown"] = args ? args.forceShutdown : undefined;
            inputs["iconId"] = args ? args.iconId : undefined;
            inputs["interfaceDriver"] = args ? args.interfaceDriver : undefined;
            inputs["memory"] = args ? args.memory : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["networkInterfaces"] = args ? args.networkInterfaces : undefined;
            inputs["privateHostId"] = args ? args.privateHostId : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["zone"] = args ? args.zone : undefined;
            inputs["dnsServers"] = undefined /*out*/;
            inputs["gateway"] = undefined /*out*/;
            inputs["hostname"] = undefined /*out*/;
            inputs["ipAddress"] = undefined /*out*/;
            inputs["netmask"] = undefined /*out*/;
            inputs["networkAddress"] = undefined /*out*/;
            inputs["privateHostName"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Server.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Server resources.
 */
export interface ServerState {
    /**
     * The id of the CD-ROM to attach to the Server
     */
    readonly cdromId?: pulumi.Input<string>;
    /**
     * The policy of how to allocate virtual CPUs to the server. This must be one of [`standard`/`dedicatedcpu`]
     */
    readonly commitment?: pulumi.Input<string>;
    /**
     * The number of virtual CPUs
     */
    readonly core?: pulumi.Input<number>;
    /**
     * The description of the Server. The length of this value must be in the range [`1`-`512`]
     */
    readonly description?: pulumi.Input<string>;
    readonly diskEditParameter?: pulumi.Input<inputs.ServerDiskEditParameter>;
    /**
     * A list of disk id connected to the server
     */
    readonly disks?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * A list of IP address of DNS server in the zone
     */
    readonly dnsServers?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The flag to use force shutdown when need to reboot/shutdown while applying
     */
    readonly forceShutdown?: pulumi.Input<boolean>;
    /**
     * The IP address of the gateway used by Server
     */
    readonly gateway?: pulumi.Input<string>;
    /**
     * The hostname of the Server
     */
    readonly hostname?: pulumi.Input<string>;
    /**
     * The icon id to attach to the Server
     */
    readonly iconId?: pulumi.Input<string>;
    /**
     * The driver name of network interface. This must be one of [`virtio`/`e1000`]
     */
    readonly interfaceDriver?: pulumi.Input<string>;
    /**
     * The IP address assigned to the Server
     */
    readonly ipAddress?: pulumi.Input<string>;
    /**
     * The size of memory in GiB
     */
    readonly memory?: pulumi.Input<number>;
    /**
     * The name of the Server. The length of this value must be in the range [`1`-`64`]
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The bit length of the subnet assigned to the Server
     */
    readonly netmask?: pulumi.Input<number>;
    /**
     * The network address which the `ip_address` belongs
     */
    readonly networkAddress?: pulumi.Input<string>;
    readonly networkInterfaces?: pulumi.Input<pulumi.Input<inputs.ServerNetworkInterface>[]>;
    /**
     * The id of the PrivateHost which the Server is assigned
     */
    readonly privateHostId?: pulumi.Input<string>;
    /**
     * The id of the PrivateHost which the Server is assigned
     */
    readonly privateHostName?: pulumi.Input<string>;
    /**
     * Any tags to assign to the Server
     */
    readonly tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The name of zone that the Server will be created (e.g. `is1a`, `tk1a`)
     */
    readonly zone?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Server resource.
 */
export interface ServerArgs {
    /**
     * The id of the CD-ROM to attach to the Server
     */
    readonly cdromId?: pulumi.Input<string>;
    /**
     * The policy of how to allocate virtual CPUs to the server. This must be one of [`standard`/`dedicatedcpu`]
     */
    readonly commitment?: pulumi.Input<string>;
    /**
     * The number of virtual CPUs
     */
    readonly core?: pulumi.Input<number>;
    /**
     * The description of the Server. The length of this value must be in the range [`1`-`512`]
     */
    readonly description?: pulumi.Input<string>;
    readonly diskEditParameter?: pulumi.Input<inputs.ServerDiskEditParameter>;
    /**
     * A list of disk id connected to the server
     */
    readonly disks?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The flag to use force shutdown when need to reboot/shutdown while applying
     */
    readonly forceShutdown?: pulumi.Input<boolean>;
    /**
     * The icon id to attach to the Server
     */
    readonly iconId?: pulumi.Input<string>;
    /**
     * The driver name of network interface. This must be one of [`virtio`/`e1000`]
     */
    readonly interfaceDriver?: pulumi.Input<string>;
    /**
     * The size of memory in GiB
     */
    readonly memory?: pulumi.Input<number>;
    /**
     * The name of the Server. The length of this value must be in the range [`1`-`64`]
     */
    readonly name?: pulumi.Input<string>;
    readonly networkInterfaces?: pulumi.Input<pulumi.Input<inputs.ServerNetworkInterface>[]>;
    /**
     * The id of the PrivateHost which the Server is assigned
     */
    readonly privateHostId?: pulumi.Input<string>;
    /**
     * Any tags to assign to the Server
     */
    readonly tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The name of zone that the Server will be created (e.g. `is1a`, `tk1a`)
     */
    readonly zone?: pulumi.Input<string>;
}
