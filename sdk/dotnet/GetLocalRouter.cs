// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.SakuraCloud
{
    public static partial class Invokes
    {
        public static Task<GetLocalRouterResult> GetLocalRouter(GetLocalRouterArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetLocalRouterResult>("sakuracloud:index/getLocalRouter:getLocalRouter", args ?? InvokeArgs.Empty, options.WithVersion());
    }

    public sealed class GetLocalRouterArgs : Pulumi.InvokeArgs
    {
        [Input("filter")]
        public Inputs.GetLocalRouterFilterArgs? Filter { get; set; }

        public GetLocalRouterArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetLocalRouterResult
    {
        public readonly string Description;
        public readonly Outputs.GetLocalRouterFilterResult? Filter;
        public readonly string IconId;
        public readonly string Name;
        public readonly ImmutableArray<Outputs.GetLocalRouterNetworkInterfacesResult> NetworkInterfaces;
        public readonly ImmutableArray<Outputs.GetLocalRouterPeersResult> Peers;
        public readonly ImmutableArray<string> SecretKeys;
        public readonly ImmutableArray<Outputs.GetLocalRouterStaticRoutesResult> StaticRoutes;
        public readonly ImmutableArray<Outputs.GetLocalRouterSwitchesResult> Switches;
        public readonly ImmutableArray<string> Tags;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetLocalRouterResult(
            string description,
            Outputs.GetLocalRouterFilterResult? filter,
            string iconId,
            string name,
            ImmutableArray<Outputs.GetLocalRouterNetworkInterfacesResult> networkInterfaces,
            ImmutableArray<Outputs.GetLocalRouterPeersResult> peers,
            ImmutableArray<string> secretKeys,
            ImmutableArray<Outputs.GetLocalRouterStaticRoutesResult> staticRoutes,
            ImmutableArray<Outputs.GetLocalRouterSwitchesResult> switches,
            ImmutableArray<string> tags,
            string id)
        {
            Description = description;
            Filter = filter;
            IconId = iconId;
            Name = name;
            NetworkInterfaces = networkInterfaces;
            Peers = peers;
            SecretKeys = secretKeys;
            StaticRoutes = staticRoutes;
            Switches = switches;
            Tags = tags;
            Id = id;
        }
    }

    namespace Inputs
    {

    public sealed class GetLocalRouterFilterArgs : Pulumi.InvokeArgs
    {
        [Input("conditions")]
        private List<GetLocalRouterFilterConditionsArgs>? _conditions;
        public List<GetLocalRouterFilterConditionsArgs> Conditions
        {
            get => _conditions ?? (_conditions = new List<GetLocalRouterFilterConditionsArgs>());
            set => _conditions = value;
        }

        [Input("id")]
        public string? Id { get; set; }

        [Input("names")]
        private List<string>? _names;
        public List<string> Names
        {
            get => _names ?? (_names = new List<string>());
            set => _names = value;
        }

        [Input("tags")]
        private List<string>? _tags;
        public List<string> Tags
        {
            get => _tags ?? (_tags = new List<string>());
            set => _tags = value;
        }

        public GetLocalRouterFilterArgs()
        {
        }
    }

    public sealed class GetLocalRouterFilterConditionsArgs : Pulumi.InvokeArgs
    {
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        [Input("values", required: true)]
        private List<string>? _values;
        public List<string> Values
        {
            get => _values ?? (_values = new List<string>());
            set => _values = value;
        }

        public GetLocalRouterFilterConditionsArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class GetLocalRouterFilterConditionsResult
    {
        public readonly string Name;
        public readonly ImmutableArray<string> Values;

        [OutputConstructor]
        private GetLocalRouterFilterConditionsResult(
            string name,
            ImmutableArray<string> values)
        {
            Name = name;
            Values = values;
        }
    }

    [OutputType]
    public sealed class GetLocalRouterFilterResult
    {
        public readonly ImmutableArray<GetLocalRouterFilterConditionsResult> Conditions;
        public readonly string? Id;
        public readonly ImmutableArray<string> Names;
        public readonly ImmutableArray<string> Tags;

        [OutputConstructor]
        private GetLocalRouterFilterResult(
            ImmutableArray<GetLocalRouterFilterConditionsResult> conditions,
            string? id,
            ImmutableArray<string> names,
            ImmutableArray<string> tags)
        {
            Conditions = conditions;
            Id = id;
            Names = names;
            Tags = tags;
        }
    }

    [OutputType]
    public sealed class GetLocalRouterNetworkInterfacesResult
    {
        public readonly ImmutableArray<string> IpAddresses;
        public readonly int Netmask;
        public readonly string Vip;
        public readonly int Vrid;

        [OutputConstructor]
        private GetLocalRouterNetworkInterfacesResult(
            ImmutableArray<string> ipAddresses,
            int netmask,
            string vip,
            int vrid)
        {
            IpAddresses = ipAddresses;
            Netmask = netmask;
            Vip = vip;
            Vrid = vrid;
        }
    }

    [OutputType]
    public sealed class GetLocalRouterPeersResult
    {
        public readonly string Description;
        public readonly bool Enabled;
        public readonly string PeerId;
        public readonly string SecretKey;

        [OutputConstructor]
        private GetLocalRouterPeersResult(
            string description,
            bool enabled,
            string peerId,
            string secretKey)
        {
            Description = description;
            Enabled = enabled;
            PeerId = peerId;
            SecretKey = secretKey;
        }
    }

    [OutputType]
    public sealed class GetLocalRouterStaticRoutesResult
    {
        public readonly string NextHop;
        public readonly string Prefix;

        [OutputConstructor]
        private GetLocalRouterStaticRoutesResult(
            string nextHop,
            string prefix)
        {
            NextHop = nextHop;
            Prefix = prefix;
        }
    }

    [OutputType]
    public sealed class GetLocalRouterSwitchesResult
    {
        public readonly string Category;
        public readonly string Code;
        public readonly string ZoneId;

        [OutputConstructor]
        private GetLocalRouterSwitchesResult(
            string category,
            string code,
            string zoneId)
        {
            Category = category;
            Code = code;
            ZoneId = zoneId;
        }
    }
    }
}