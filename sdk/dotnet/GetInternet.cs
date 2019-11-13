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
        /// Use this data source to retrieve information about a SakuraCloud Internet (Switch+Router).
        /// 
        /// &gt; This content is derived from https://github.com/sacloud/terraform-provider-sakuracloud/blob/master/website/docs/d/internet.html.markdown.
        /// </summary>
        public static Task<GetInternetResult> GetInternet(GetInternetArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetInternetResult>("sakuracloud:index/getInternet:getInternet", args, options.WithVersion());
    }

    public sealed class GetInternetArgs : Pulumi.ResourceArgs
    {
        [Input("filters")]
        private InputList<Inputs.GetInternetFiltersArgs>? _filters;

        /// <summary>
        /// The map of filter key and value.
        /// </summary>
        public InputList<Inputs.GetInternetFiltersArgs> Filters
        {
            get => _filters ?? (_filters = new InputList<Inputs.GetInternetFiltersArgs>());
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

        public GetInternetArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetInternetResult
    {
        /// <summary>
        /// Bandwidth of outbound traffic.
        /// </summary>
        public readonly int BandWidth;
        /// <summary>
        /// The description of the resource.
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// The ipv6 enabled flag.
        /// </summary>
        public readonly bool EnableIpv6;
        public readonly ImmutableArray<Outputs.GetInternetFiltersResult> Filters;
        /// <summary>
        /// The network gateway address of the switch.
        /// </summary>
        public readonly string Gateway;
        /// <summary>
        /// The ID of the icon of the resource.
        /// </summary>
        public readonly string IconId;
        /// <summary>
        /// Global IP address list.
        /// </summary>
        public readonly ImmutableArray<string> Ipaddresses;
        /// <summary>
        /// The ipv6 network address.
        /// </summary>
        public readonly string Ipv6NwAddress;
        /// <summary>
        /// Address prefix of ipv6 network.
        /// </summary>
        public readonly string Ipv6Prefix;
        /// <summary>
        /// Address prefix length of ipv6 network.
        /// </summary>
        public readonly int Ipv6PrefixLen;
        /// <summary>
        /// Max global IP address.
        /// </summary>
        public readonly string MaxIpaddress;
        /// <summary>
        /// Min global IP address.
        /// </summary>
        public readonly string MinIpaddress;
        /// <summary>
        /// The name of the resource.
        /// </summary>
        public readonly string Name;
        public readonly ImmutableArray<string> NameSelectors;
        /// <summary>
        /// The network address.
        /// </summary>
        public readonly string NwAddress;
        /// <summary>
        /// Network mask length.
        /// </summary>
        public readonly int NwMaskLen;
        /// <summary>
        /// The ID list of the servers connected to the switch.
        /// </summary>
        public readonly ImmutableArray<string> ServerIds;
        /// <summary>
        /// The ID of the switch.
        /// </summary>
        public readonly string SwitchId;
        public readonly ImmutableArray<string> TagSelectors;
        /// <summary>
        /// The tag list of the resources.
        /// </summary>
        public readonly ImmutableArray<string> Tags;
        /// <summary>
        /// The ID of the zone to which the resource belongs.
        /// </summary>
        public readonly string Zone;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetInternetResult(
            int bandWidth,
            string description,
            bool enableIpv6,
            ImmutableArray<Outputs.GetInternetFiltersResult> filters,
            string gateway,
            string iconId,
            ImmutableArray<string> ipaddresses,
            string ipv6NwAddress,
            string ipv6Prefix,
            int ipv6PrefixLen,
            string maxIpaddress,
            string minIpaddress,
            string name,
            ImmutableArray<string> nameSelectors,
            string nwAddress,
            int nwMaskLen,
            ImmutableArray<string> serverIds,
            string switchId,
            ImmutableArray<string> tagSelectors,
            ImmutableArray<string> tags,
            string zone,
            string id)
        {
            BandWidth = bandWidth;
            Description = description;
            EnableIpv6 = enableIpv6;
            Filters = filters;
            Gateway = gateway;
            IconId = iconId;
            Ipaddresses = ipaddresses;
            Ipv6NwAddress = ipv6NwAddress;
            Ipv6Prefix = ipv6Prefix;
            Ipv6PrefixLen = ipv6PrefixLen;
            MaxIpaddress = maxIpaddress;
            MinIpaddress = minIpaddress;
            Name = name;
            NameSelectors = nameSelectors;
            NwAddress = nwAddress;
            NwMaskLen = nwMaskLen;
            ServerIds = serverIds;
            SwitchId = switchId;
            TagSelectors = tagSelectors;
            Tags = tags;
            Zone = zone;
            Id = id;
        }
    }

    namespace Inputs
    {

    public sealed class GetInternetFiltersArgs : Pulumi.ResourceArgs
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

        public GetInternetFiltersArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class GetInternetFiltersResult
    {
        /// <summary>
        /// The name of the resource.
        /// </summary>
        public readonly string Name;
        public readonly ImmutableArray<string> Values;

        [OutputConstructor]
        private GetInternetFiltersResult(
            string name,
            ImmutableArray<string> values)
        {
            Name = name;
            Values = values;
        }
    }
    }
}
