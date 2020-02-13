// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.SakuraCloud
{
    public partial class Server : Pulumi.CustomResource
    {
        /// <summary>
        /// The id of the CD-ROM to attach to the Server
        /// </summary>
        [Output("cdromId")]
        public Output<string?> CdromId { get; private set; } = null!;

        /// <summary>
        /// The policy of how to allocate virtual CPUs to the server. This must be one of [`standard`/`dedicatedcpu`]
        /// </summary>
        [Output("commitment")]
        public Output<string?> Commitment { get; private set; } = null!;

        /// <summary>
        /// The number of virtual CPUs
        /// </summary>
        [Output("core")]
        public Output<int?> Core { get; private set; } = null!;

        /// <summary>
        /// The description of the Server. The length of this value must be in the range [`1`-`512`]
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        [Output("diskEditParameter")]
        public Output<Outputs.ServerDiskEditParameter?> DiskEditParameter { get; private set; } = null!;

        /// <summary>
        /// A list of disk id connected to the server
        /// </summary>
        [Output("disks")]
        public Output<ImmutableArray<string>> Disks { get; private set; } = null!;

        /// <summary>
        /// A list of IP address of DNS server in the zone
        /// </summary>
        [Output("dnsServers")]
        public Output<ImmutableArray<string>> DnsServers { get; private set; } = null!;

        /// <summary>
        /// The flag to use force shutdown when need to reboot/shutdown while applying
        /// </summary>
        [Output("forceShutdown")]
        public Output<bool?> ForceShutdown { get; private set; } = null!;

        /// <summary>
        /// The IP address of the gateway used by Server
        /// </summary>
        [Output("gateway")]
        public Output<string> Gateway { get; private set; } = null!;

        /// <summary>
        /// The hostname of the Server
        /// </summary>
        [Output("hostname")]
        public Output<string> Hostname { get; private set; } = null!;

        /// <summary>
        /// The icon id to attach to the Server
        /// </summary>
        [Output("iconId")]
        public Output<string?> IconId { get; private set; } = null!;

        /// <summary>
        /// The driver name of network interface. This must be one of [`virtio`/`e1000`]
        /// </summary>
        [Output("interfaceDriver")]
        public Output<string?> InterfaceDriver { get; private set; } = null!;

        /// <summary>
        /// The IP address assigned to the Server
        /// </summary>
        [Output("ipAddress")]
        public Output<string> IpAddress { get; private set; } = null!;

        /// <summary>
        /// The size of memory in GiB
        /// </summary>
        [Output("memory")]
        public Output<int?> Memory { get; private set; } = null!;

        /// <summary>
        /// The name of the Server. The length of this value must be in the range [`1`-`64`]
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The bit length of the subnet assigned to the Server
        /// </summary>
        [Output("netmask")]
        public Output<int> Netmask { get; private set; } = null!;

        /// <summary>
        /// The network address which the `ip_address` belongs
        /// </summary>
        [Output("networkAddress")]
        public Output<string> NetworkAddress { get; private set; } = null!;

        [Output("networkInterfaces")]
        public Output<ImmutableArray<Outputs.ServerNetworkInterfaces>> NetworkInterfaces { get; private set; } = null!;

        /// <summary>
        /// The id of the PrivateHost which the Server is assigned
        /// </summary>
        [Output("privateHostId")]
        public Output<string?> PrivateHostId { get; private set; } = null!;

        /// <summary>
        /// The id of the PrivateHost which the Server is assigned
        /// </summary>
        [Output("privateHostName")]
        public Output<string> PrivateHostName { get; private set; } = null!;

        /// <summary>
        /// Any tags to assign to the Server
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<string>> Tags { get; private set; } = null!;

        /// <summary>
        /// The name of zone that the Server will be created (e.g. `is1a`, `tk1a`)
        /// </summary>
        [Output("zone")]
        public Output<string> Zone { get; private set; } = null!;


        /// <summary>
        /// Create a Server resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Server(string name, ServerArgs? args = null, CustomResourceOptions? options = null)
            : base("sakuracloud:index/server:Server", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private Server(string name, Input<string> id, ServerState? state = null, CustomResourceOptions? options = null)
            : base("sakuracloud:index/server:Server", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Server resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Server Get(string name, Input<string> id, ServerState? state = null, CustomResourceOptions? options = null)
        {
            return new Server(name, id, state, options);
        }
    }

    public sealed class ServerArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The id of the CD-ROM to attach to the Server
        /// </summary>
        [Input("cdromId")]
        public Input<string>? CdromId { get; set; }

        /// <summary>
        /// The policy of how to allocate virtual CPUs to the server. This must be one of [`standard`/`dedicatedcpu`]
        /// </summary>
        [Input("commitment")]
        public Input<string>? Commitment { get; set; }

        /// <summary>
        /// The number of virtual CPUs
        /// </summary>
        [Input("core")]
        public Input<int>? Core { get; set; }

        /// <summary>
        /// The description of the Server. The length of this value must be in the range [`1`-`512`]
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("diskEditParameter")]
        public Input<Inputs.ServerDiskEditParameterArgs>? DiskEditParameter { get; set; }

        [Input("disks")]
        private InputList<string>? _disks;

        /// <summary>
        /// A list of disk id connected to the server
        /// </summary>
        public InputList<string> Disks
        {
            get => _disks ?? (_disks = new InputList<string>());
            set => _disks = value;
        }

        /// <summary>
        /// The flag to use force shutdown when need to reboot/shutdown while applying
        /// </summary>
        [Input("forceShutdown")]
        public Input<bool>? ForceShutdown { get; set; }

        /// <summary>
        /// The icon id to attach to the Server
        /// </summary>
        [Input("iconId")]
        public Input<string>? IconId { get; set; }

        /// <summary>
        /// The driver name of network interface. This must be one of [`virtio`/`e1000`]
        /// </summary>
        [Input("interfaceDriver")]
        public Input<string>? InterfaceDriver { get; set; }

        /// <summary>
        /// The size of memory in GiB
        /// </summary>
        [Input("memory")]
        public Input<int>? Memory { get; set; }

        /// <summary>
        /// The name of the Server. The length of this value must be in the range [`1`-`64`]
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("networkInterfaces")]
        private InputList<Inputs.ServerNetworkInterfacesArgs>? _networkInterfaces;
        public InputList<Inputs.ServerNetworkInterfacesArgs> NetworkInterfaces
        {
            get => _networkInterfaces ?? (_networkInterfaces = new InputList<Inputs.ServerNetworkInterfacesArgs>());
            set => _networkInterfaces = value;
        }

        /// <summary>
        /// The id of the PrivateHost which the Server is assigned
        /// </summary>
        [Input("privateHostId")]
        public Input<string>? PrivateHostId { get; set; }

        [Input("tags")]
        private InputList<string>? _tags;

        /// <summary>
        /// Any tags to assign to the Server
        /// </summary>
        public InputList<string> Tags
        {
            get => _tags ?? (_tags = new InputList<string>());
            set => _tags = value;
        }

        /// <summary>
        /// The name of zone that the Server will be created (e.g. `is1a`, `tk1a`)
        /// </summary>
        [Input("zone")]
        public Input<string>? Zone { get; set; }

        public ServerArgs()
        {
        }
    }

    public sealed class ServerState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The id of the CD-ROM to attach to the Server
        /// </summary>
        [Input("cdromId")]
        public Input<string>? CdromId { get; set; }

        /// <summary>
        /// The policy of how to allocate virtual CPUs to the server. This must be one of [`standard`/`dedicatedcpu`]
        /// </summary>
        [Input("commitment")]
        public Input<string>? Commitment { get; set; }

        /// <summary>
        /// The number of virtual CPUs
        /// </summary>
        [Input("core")]
        public Input<int>? Core { get; set; }

        /// <summary>
        /// The description of the Server. The length of this value must be in the range [`1`-`512`]
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("diskEditParameter")]
        public Input<Inputs.ServerDiskEditParameterGetArgs>? DiskEditParameter { get; set; }

        [Input("disks")]
        private InputList<string>? _disks;

        /// <summary>
        /// A list of disk id connected to the server
        /// </summary>
        public InputList<string> Disks
        {
            get => _disks ?? (_disks = new InputList<string>());
            set => _disks = value;
        }

        [Input("dnsServers")]
        private InputList<string>? _dnsServers;

        /// <summary>
        /// A list of IP address of DNS server in the zone
        /// </summary>
        public InputList<string> DnsServers
        {
            get => _dnsServers ?? (_dnsServers = new InputList<string>());
            set => _dnsServers = value;
        }

        /// <summary>
        /// The flag to use force shutdown when need to reboot/shutdown while applying
        /// </summary>
        [Input("forceShutdown")]
        public Input<bool>? ForceShutdown { get; set; }

        /// <summary>
        /// The IP address of the gateway used by Server
        /// </summary>
        [Input("gateway")]
        public Input<string>? Gateway { get; set; }

        /// <summary>
        /// The hostname of the Server
        /// </summary>
        [Input("hostname")]
        public Input<string>? Hostname { get; set; }

        /// <summary>
        /// The icon id to attach to the Server
        /// </summary>
        [Input("iconId")]
        public Input<string>? IconId { get; set; }

        /// <summary>
        /// The driver name of network interface. This must be one of [`virtio`/`e1000`]
        /// </summary>
        [Input("interfaceDriver")]
        public Input<string>? InterfaceDriver { get; set; }

        /// <summary>
        /// The IP address assigned to the Server
        /// </summary>
        [Input("ipAddress")]
        public Input<string>? IpAddress { get; set; }

        /// <summary>
        /// The size of memory in GiB
        /// </summary>
        [Input("memory")]
        public Input<int>? Memory { get; set; }

        /// <summary>
        /// The name of the Server. The length of this value must be in the range [`1`-`64`]
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The bit length of the subnet assigned to the Server
        /// </summary>
        [Input("netmask")]
        public Input<int>? Netmask { get; set; }

        /// <summary>
        /// The network address which the `ip_address` belongs
        /// </summary>
        [Input("networkAddress")]
        public Input<string>? NetworkAddress { get; set; }

        [Input("networkInterfaces")]
        private InputList<Inputs.ServerNetworkInterfacesGetArgs>? _networkInterfaces;
        public InputList<Inputs.ServerNetworkInterfacesGetArgs> NetworkInterfaces
        {
            get => _networkInterfaces ?? (_networkInterfaces = new InputList<Inputs.ServerNetworkInterfacesGetArgs>());
            set => _networkInterfaces = value;
        }

        /// <summary>
        /// The id of the PrivateHost which the Server is assigned
        /// </summary>
        [Input("privateHostId")]
        public Input<string>? PrivateHostId { get; set; }

        /// <summary>
        /// The id of the PrivateHost which the Server is assigned
        /// </summary>
        [Input("privateHostName")]
        public Input<string>? PrivateHostName { get; set; }

        [Input("tags")]
        private InputList<string>? _tags;

        /// <summary>
        /// Any tags to assign to the Server
        /// </summary>
        public InputList<string> Tags
        {
            get => _tags ?? (_tags = new InputList<string>());
            set => _tags = value;
        }

        /// <summary>
        /// The name of zone that the Server will be created (e.g. `is1a`, `tk1a`)
        /// </summary>
        [Input("zone")]
        public Input<string>? Zone { get; set; }

        public ServerState()
        {
        }
    }

    namespace Inputs
    {

    public sealed class ServerDiskEditParameterArgs : Pulumi.ResourceArgs
    {
        [Input("changePartitionUuid")]
        public Input<bool>? ChangePartitionUuid { get; set; }

        [Input("disablePwAuth")]
        public Input<bool>? DisablePwAuth { get; set; }

        [Input("enableDhcp")]
        public Input<bool>? EnableDhcp { get; set; }

        [Input("gateway")]
        public Input<string>? Gateway { get; set; }

        [Input("hostname")]
        public Input<string>? Hostname { get; set; }

        [Input("ipAddress")]
        public Input<string>? IpAddress { get; set; }

        [Input("netmask")]
        public Input<int>? Netmask { get; set; }

        [Input("noteIds")]
        private InputList<string>? _noteIds;
        public InputList<string> NoteIds
        {
            get => _noteIds ?? (_noteIds = new InputList<string>());
            set => _noteIds = value;
        }

        [Input("password")]
        public Input<string>? Password { get; set; }

        [Input("sshKeyIds")]
        private InputList<string>? _sshKeyIds;
        public InputList<string> SshKeyIds
        {
            get => _sshKeyIds ?? (_sshKeyIds = new InputList<string>());
            set => _sshKeyIds = value;
        }

        public ServerDiskEditParameterArgs()
        {
        }
    }

    public sealed class ServerDiskEditParameterGetArgs : Pulumi.ResourceArgs
    {
        [Input("changePartitionUuid")]
        public Input<bool>? ChangePartitionUuid { get; set; }

        [Input("disablePwAuth")]
        public Input<bool>? DisablePwAuth { get; set; }

        [Input("enableDhcp")]
        public Input<bool>? EnableDhcp { get; set; }

        [Input("gateway")]
        public Input<string>? Gateway { get; set; }

        [Input("hostname")]
        public Input<string>? Hostname { get; set; }

        [Input("ipAddress")]
        public Input<string>? IpAddress { get; set; }

        [Input("netmask")]
        public Input<int>? Netmask { get; set; }

        [Input("noteIds")]
        private InputList<string>? _noteIds;
        public InputList<string> NoteIds
        {
            get => _noteIds ?? (_noteIds = new InputList<string>());
            set => _noteIds = value;
        }

        [Input("password")]
        public Input<string>? Password { get; set; }

        [Input("sshKeyIds")]
        private InputList<string>? _sshKeyIds;
        public InputList<string> SshKeyIds
        {
            get => _sshKeyIds ?? (_sshKeyIds = new InputList<string>());
            set => _sshKeyIds = value;
        }

        public ServerDiskEditParameterGetArgs()
        {
        }
    }

    public sealed class ServerNetworkInterfacesArgs : Pulumi.ResourceArgs
    {
        [Input("macAddress")]
        public Input<string>? MacAddress { get; set; }

        [Input("packetFilterId")]
        public Input<string>? PacketFilterId { get; set; }

        [Input("upstream", required: true)]
        public Input<string> Upstream { get; set; } = null!;

        [Input("userIpAddress")]
        public Input<string>? UserIpAddress { get; set; }

        public ServerNetworkInterfacesArgs()
        {
        }
    }

    public sealed class ServerNetworkInterfacesGetArgs : Pulumi.ResourceArgs
    {
        [Input("macAddress")]
        public Input<string>? MacAddress { get; set; }

        [Input("packetFilterId")]
        public Input<string>? PacketFilterId { get; set; }

        [Input("upstream", required: true)]
        public Input<string> Upstream { get; set; } = null!;

        [Input("userIpAddress")]
        public Input<string>? UserIpAddress { get; set; }

        public ServerNetworkInterfacesGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class ServerDiskEditParameter
    {
        public readonly bool? ChangePartitionUuid;
        public readonly bool? DisablePwAuth;
        public readonly bool? EnableDhcp;
        public readonly string? Gateway;
        public readonly string? Hostname;
        public readonly string? IpAddress;
        public readonly int? Netmask;
        public readonly ImmutableArray<string> NoteIds;
        public readonly string? Password;
        public readonly ImmutableArray<string> SshKeyIds;

        [OutputConstructor]
        private ServerDiskEditParameter(
            bool? changePartitionUuid,
            bool? disablePwAuth,
            bool? enableDhcp,
            string? gateway,
            string? hostname,
            string? ipAddress,
            int? netmask,
            ImmutableArray<string> noteIds,
            string? password,
            ImmutableArray<string> sshKeyIds)
        {
            ChangePartitionUuid = changePartitionUuid;
            DisablePwAuth = disablePwAuth;
            EnableDhcp = enableDhcp;
            Gateway = gateway;
            Hostname = hostname;
            IpAddress = ipAddress;
            Netmask = netmask;
            NoteIds = noteIds;
            Password = password;
            SshKeyIds = sshKeyIds;
        }
    }

    [OutputType]
    public sealed class ServerNetworkInterfaces
    {
        public readonly string MacAddress;
        public readonly string? PacketFilterId;
        public readonly string Upstream;
        public readonly string UserIpAddress;

        [OutputConstructor]
        private ServerNetworkInterfaces(
            string macAddress,
            string? packetFilterId,
            string upstream,
            string userIpAddress)
        {
            MacAddress = macAddress;
            PacketFilterId = packetFilterId;
            Upstream = upstream;
            UserIpAddress = userIpAddress;
        }
    }
    }
}
