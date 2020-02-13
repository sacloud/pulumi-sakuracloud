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
        public static Task<GetPacketFilterResult> GetPacketFilter(GetPacketFilterArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetPacketFilterResult>("sakuracloud:index/getPacketFilter:getPacketFilter", args ?? InvokeArgs.Empty, options.WithVersion());
    }

    public sealed class GetPacketFilterArgs : Pulumi.InvokeArgs
    {
        [Input("filter")]
        public Inputs.GetPacketFilterFilterArgs? Filter { get; set; }

        [Input("zone")]
        public string? Zone { get; set; }

        public GetPacketFilterArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetPacketFilterResult
    {
        public readonly string Description;
        public readonly ImmutableArray<Outputs.GetPacketFilterExpressionsResult> Expressions;
        public readonly Outputs.GetPacketFilterFilterResult? Filter;
        public readonly string Name;
        public readonly string Zone;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetPacketFilterResult(
            string description,
            ImmutableArray<Outputs.GetPacketFilterExpressionsResult> expressions,
            Outputs.GetPacketFilterFilterResult? filter,
            string name,
            string zone,
            string id)
        {
            Description = description;
            Expressions = expressions;
            Filter = filter;
            Name = name;
            Zone = zone;
            Id = id;
        }
    }

    namespace Inputs
    {

    public sealed class GetPacketFilterFilterArgs : Pulumi.InvokeArgs
    {
        [Input("conditions")]
        private List<GetPacketFilterFilterConditionsArgs>? _conditions;
        public List<GetPacketFilterFilterConditionsArgs> Conditions
        {
            get => _conditions ?? (_conditions = new List<GetPacketFilterFilterConditionsArgs>());
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

        public GetPacketFilterFilterArgs()
        {
        }
    }

    public sealed class GetPacketFilterFilterConditionsArgs : Pulumi.InvokeArgs
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

        public GetPacketFilterFilterConditionsArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class GetPacketFilterExpressionsResult
    {
        public readonly bool Allow;
        public readonly string Description;
        public readonly string DestinationPort;
        public readonly string Protocol;
        public readonly string SourceNetwork;
        public readonly string SourcePort;

        [OutputConstructor]
        private GetPacketFilterExpressionsResult(
            bool allow,
            string description,
            string destinationPort,
            string protocol,
            string sourceNetwork,
            string sourcePort)
        {
            Allow = allow;
            Description = description;
            DestinationPort = destinationPort;
            Protocol = protocol;
            SourceNetwork = sourceNetwork;
            SourcePort = sourcePort;
        }
    }

    [OutputType]
    public sealed class GetPacketFilterFilterConditionsResult
    {
        public readonly string Name;
        public readonly ImmutableArray<string> Values;

        [OutputConstructor]
        private GetPacketFilterFilterConditionsResult(
            string name,
            ImmutableArray<string> values)
        {
            Name = name;
            Values = values;
        }
    }

    [OutputType]
    public sealed class GetPacketFilterFilterResult
    {
        public readonly ImmutableArray<GetPacketFilterFilterConditionsResult> Conditions;
        public readonly string? Id;
        public readonly ImmutableArray<string> Names;

        [OutputConstructor]
        private GetPacketFilterFilterResult(
            ImmutableArray<GetPacketFilterFilterConditionsResult> conditions,
            string? id,
            ImmutableArray<string> names)
        {
            Conditions = conditions;
            Id = id;
            Names = names;
        }
    }
    }
}
