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
        public static Task<GetLoadBalancerResult> GetLoadBalancer(GetLoadBalancerArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetLoadBalancerResult>("sakuracloud:index/getLoadBalancer:getLoadBalancer", args ?? InvokeArgs.Empty, options.WithVersion());
    }

    public sealed class GetLoadBalancerArgs : Pulumi.InvokeArgs
    {
        [Input("filter")]
        public Inputs.GetLoadBalancerFilterArgs? Filter { get; set; }

        [Input("zone")]
        public string? Zone { get; set; }

        public GetLoadBalancerArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetLoadBalancerResult
    {
        public readonly string Description;
        public readonly Outputs.GetLoadBalancerFilterResult? Filter;
        public readonly string IconId;
        public readonly string Name;
        public readonly ImmutableArray<Outputs.GetLoadBalancerNetworkInterfacesResult> NetworkInterfaces;
        public readonly string Plan;
        public readonly ImmutableArray<string> Tags;
        public readonly ImmutableArray<Outputs.GetLoadBalancerVipsResult> Vips;
        public readonly string Zone;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetLoadBalancerResult(
            string description,
            Outputs.GetLoadBalancerFilterResult? filter,
            string iconId,
            string name,
            ImmutableArray<Outputs.GetLoadBalancerNetworkInterfacesResult> networkInterfaces,
            string plan,
            ImmutableArray<string> tags,
            ImmutableArray<Outputs.GetLoadBalancerVipsResult> vips,
            string zone,
            string id)
        {
            Description = description;
            Filter = filter;
            IconId = iconId;
            Name = name;
            NetworkInterfaces = networkInterfaces;
            Plan = plan;
            Tags = tags;
            Vips = vips;
            Zone = zone;
            Id = id;
        }
    }

    namespace Inputs
    {

    public sealed class GetLoadBalancerFilterArgs : Pulumi.InvokeArgs
    {
        [Input("conditions")]
        private List<GetLoadBalancerFilterConditionsArgs>? _conditions;
        public List<GetLoadBalancerFilterConditionsArgs> Conditions
        {
            get => _conditions ?? (_conditions = new List<GetLoadBalancerFilterConditionsArgs>());
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

        public GetLoadBalancerFilterArgs()
        {
        }
    }

    public sealed class GetLoadBalancerFilterConditionsArgs : Pulumi.InvokeArgs
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

        public GetLoadBalancerFilterConditionsArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class GetLoadBalancerFilterConditionsResult
    {
        public readonly string Name;
        public readonly ImmutableArray<string> Values;

        [OutputConstructor]
        private GetLoadBalancerFilterConditionsResult(
            string name,
            ImmutableArray<string> values)
        {
            Name = name;
            Values = values;
        }
    }

    [OutputType]
    public sealed class GetLoadBalancerFilterResult
    {
        public readonly ImmutableArray<GetLoadBalancerFilterConditionsResult> Conditions;
        public readonly string? Id;
        public readonly ImmutableArray<string> Names;
        public readonly ImmutableArray<string> Tags;

        [OutputConstructor]
        private GetLoadBalancerFilterResult(
            ImmutableArray<GetLoadBalancerFilterConditionsResult> conditions,
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
    public sealed class GetLoadBalancerNetworkInterfacesResult
    {
        public readonly string Gateway;
        public readonly ImmutableArray<string> IpAddresses;
        public readonly int Netmask;
        public readonly string SwitchId;
        public readonly int Vrid;

        [OutputConstructor]
        private GetLoadBalancerNetworkInterfacesResult(
            string gateway,
            ImmutableArray<string> ipAddresses,
            int netmask,
            string switchId,
            int vrid)
        {
            Gateway = gateway;
            IpAddresses = ipAddresses;
            Netmask = netmask;
            SwitchId = switchId;
            Vrid = vrid;
        }
    }

    [OutputType]
    public sealed class GetLoadBalancerVipsResult
    {
        public readonly int DelayLoop;
        public readonly string Description;
        public readonly int Port;
        public readonly ImmutableArray<GetLoadBalancerVipsServersResult> Servers;
        public readonly string SorryServer;
        public readonly string Vip;

        [OutputConstructor]
        private GetLoadBalancerVipsResult(
            int delayLoop,
            string description,
            int port,
            ImmutableArray<GetLoadBalancerVipsServersResult> servers,
            string sorryServer,
            string vip)
        {
            DelayLoop = delayLoop;
            Description = description;
            Port = port;
            Servers = servers;
            SorryServer = sorryServer;
            Vip = vip;
        }
    }

    [OutputType]
    public sealed class GetLoadBalancerVipsServersResult
    {
        public readonly bool Enabled;
        public readonly string IpAddress;
        public readonly string Path;
        public readonly string Protocol;
        public readonly string Status;

        [OutputConstructor]
        private GetLoadBalancerVipsServersResult(
            bool enabled,
            string ipAddress,
            string path,
            string protocol,
            string status)
        {
            Enabled = enabled;
            IpAddress = ipAddress;
            Path = path;
            Protocol = protocol;
            Status = status;
        }
    }
    }
}
