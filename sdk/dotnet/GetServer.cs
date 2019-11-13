// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Sakuracloud
{
    public static partial class Invokes
    {
        /// <summary>
        /// Use this data source to retrieve information about a SakuraCloud Server.
        /// 
        /// &gt; This content is derived from https://github.com/sacloud/terraform-provider-sakuracloud/blob/master/website/docs/d/server.html.markdown.
        /// </summary>
        public static Task<GetServerResult> GetServer(GetServerArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetServerResult>("sakuracloud:index/getServer:getServer", args, options.WithVersion());
    }

    public sealed class GetServerArgs : Pulumi.ResourceArgs
    {
        [Input("filters")]
        private InputList<Inputs.GetServerFiltersArgs>? _filters;

        /// <summary>
        /// The map of filter key and value.
        /// </summary>
        public InputList<Inputs.GetServerFiltersArgs> Filters
        {
            get => _filters ?? (_filters = new InputList<Inputs.GetServerFiltersArgs>());
            set => _filters = value;
        }

        [Input("nameSelectors")]
        private InputList<string>? _nameSelectors;

        /// <summary>
        /// The list of names to filtering.
        /// </summary>
        public InputList<string> NameSelectors
        {
            get => _nameSelectors ?? (_nameSelectors = new InputList<string>());
            set => _nameSelectors = value;
        }

        [Input("tagSelectors")]
        private InputList<string>? _tagSelectors;

        /// <summary>
        /// The list of tags to filtering.
        /// </summary>
        public InputList<string> TagSelectors
        {
            get => _tagSelectors ?? (_tagSelectors = new InputList<string>());
            set => _tagSelectors = value;
        }

        /// <summary>
        /// The ID of the zone.
        /// </summary>
        [Input("zone")]
        public Input<string>? Zone { get; set; }

        public GetServerArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetServerResult
    {
        /// <summary>
        /// The display IP address list of the NICs (excluding primary NIC) of Server.  
        /// </summary>
        public readonly ImmutableArray<string> AdditionalDisplayIpaddresses;
        /// <summary>
        /// The ID list of the Switches connected to NICs (excluding primary NIC) of Server.
        /// </summary>
        public readonly ImmutableArray<string> AdditionalNics;
        /// <summary>
        /// The ID of the CD-ROM inserted to Server.
        /// </summary>
        public readonly string CdromId;
        /// <summary>
        /// The plan of assignment of CPU to VM.
        /// </summary>
        public readonly string Commitment;
        /// <summary>
        /// The number of cores.
        /// </summary>
        public readonly int Core;
        /// <summary>
        /// The description of the resource.
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// The ID list of the Disks connected to Server.
        /// </summary>
        public readonly ImmutableArray<string> Disks;
        /// <summary>
        /// The IP address of NIC for display.
        /// </summary>
        public readonly string DisplayIpaddress;
        /// <summary>
        /// List of default DNS servers for the zone to which the Server belongs.
        /// </summary>
        public readonly ImmutableArray<string> DnsServers;
        public readonly ImmutableArray<Outputs.GetServerFiltersResult> Filters;
        /// <summary>
        /// Default gateway address of the Server.	 
        /// </summary>
        public readonly string Gateway;
        /// <summary>
        /// The ID of the icon of the resource.
        /// </summary>
        public readonly string IconId;
        /// <summary>
        /// The name of network interface driver.
        /// </summary>
        public readonly string InterfaceDriver;
        /// <summary>
        /// The IP address of primary NIC.
        /// </summary>
        public readonly string Ipaddress;
        /// <summary>
        /// The MAC address list of NICs connected to Server.
        /// </summary>
        public readonly ImmutableArray<string> Macaddresses;
        /// <summary>
        /// The size of memory (unit:`GB`).
        /// </summary>
        public readonly int Memory;
        /// <summary>
        /// The name of the resource.
        /// </summary>
        public readonly string Name;
        public readonly ImmutableArray<string> NameSelectors;
        /// <summary>
        /// The primary NIC's connection destination.
        /// </summary>
        public readonly string Nic;
        /// <summary>
        /// The network address of the Server.
        /// </summary>
        public readonly string NwAddress;
        /// <summary>
        /// Network mask length of the Server.
        /// </summary>
        public readonly string NwMaskLen;
        /// <summary>
        /// The ID list of the Packet Filter connected to Server.
        /// </summary>
        public readonly ImmutableArray<string> PacketFilterIds;
        /// <summary>
        /// The ID of the Private Host to which the Server belongs.
        /// </summary>
        public readonly string PrivateHostId;
        /// <summary>
        /// The name of the Private Host to which the Server belongs.
        /// </summary>
        public readonly string PrivateHostName;
        public readonly ImmutableArray<string> TagSelectors;
        /// <summary>
        /// The tag list of the resources.
        /// </summary>
        public readonly ImmutableArray<string> Tags;
        /// <summary>
        /// The hostname of VNC server.
        /// </summary>
        public readonly string VncHost;
        /// <summary>
        /// The password of VNC server.
        /// </summary>
        public readonly string VncPassword;
        /// <summary>
        /// The port number of VNC server.
        /// </summary>
        public readonly int VncPort;
        /// <summary>
        /// The ID of the zone to which the resource belongs.
        /// </summary>
        public readonly string Zone;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetServerResult(
            ImmutableArray<string> additionalDisplayIpaddresses,
            ImmutableArray<string> additionalNics,
            string cdromId,
            string commitment,
            int core,
            string description,
            ImmutableArray<string> disks,
            string displayIpaddress,
            ImmutableArray<string> dnsServers,
            ImmutableArray<Outputs.GetServerFiltersResult> filters,
            string gateway,
            string iconId,
            string interfaceDriver,
            string ipaddress,
            ImmutableArray<string> macaddresses,
            int memory,
            string name,
            ImmutableArray<string> nameSelectors,
            string nic,
            string nwAddress,
            string nwMaskLen,
            ImmutableArray<string> packetFilterIds,
            string privateHostId,
            string privateHostName,
            ImmutableArray<string> tagSelectors,
            ImmutableArray<string> tags,
            string vncHost,
            string vncPassword,
            int vncPort,
            string zone,
            string id)
        {
            AdditionalDisplayIpaddresses = additionalDisplayIpaddresses;
            AdditionalNics = additionalNics;
            CdromId = cdromId;
            Commitment = commitment;
            Core = core;
            Description = description;
            Disks = disks;
            DisplayIpaddress = displayIpaddress;
            DnsServers = dnsServers;
            Filters = filters;
            Gateway = gateway;
            IconId = iconId;
            InterfaceDriver = interfaceDriver;
            Ipaddress = ipaddress;
            Macaddresses = macaddresses;
            Memory = memory;
            Name = name;
            NameSelectors = nameSelectors;
            Nic = nic;
            NwAddress = nwAddress;
            NwMaskLen = nwMaskLen;
            PacketFilterIds = packetFilterIds;
            PrivateHostId = privateHostId;
            PrivateHostName = privateHostName;
            TagSelectors = tagSelectors;
            Tags = tags;
            VncHost = vncHost;
            VncPassword = vncPassword;
            VncPort = vncPort;
            Zone = zone;
            Id = id;
        }
    }

    namespace Inputs
    {

    public sealed class GetServerFiltersArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the resource.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        [Input("values", required: true)]
        private InputList<string>? _values;
        public InputList<string> Values
        {
            get => _values ?? (_values = new InputList<string>());
            set => _values = value;
        }

        public GetServerFiltersArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class GetServerFiltersResult
    {
        /// <summary>
        /// The name of the resource.
        /// </summary>
        public readonly string Name;
        public readonly ImmutableArray<string> Values;

        [OutputConstructor]
        private GetServerFiltersResult(
            string name,
            ImmutableArray<string> values)
        {
            Name = name;
            Values = values;
        }
    }
    }
}
