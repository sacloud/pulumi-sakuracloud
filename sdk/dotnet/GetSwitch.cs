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
        public static Task<GetSwitchResult> GetSwitch(GetSwitchArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetSwitchResult>("sakuracloud:index/getSwitch:getSwitch", args ?? InvokeArgs.Empty, options.WithVersion());
    }

    public sealed class GetSwitchArgs : Pulumi.InvokeArgs
    {
        [Input("filter")]
        public Inputs.GetSwitchFilterArgs? Filter { get; set; }

        [Input("zone")]
        public string? Zone { get; set; }

        public GetSwitchArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetSwitchResult
    {
        public readonly string BridgeId;
        public readonly string Description;
        public readonly Outputs.GetSwitchFilterResult? Filter;
        public readonly string IconId;
        public readonly string Name;
        public readonly ImmutableArray<string> ServerIds;
        public readonly ImmutableArray<string> Tags;
        public readonly string Zone;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetSwitchResult(
            string bridgeId,
            string description,
            Outputs.GetSwitchFilterResult? filter,
            string iconId,
            string name,
            ImmutableArray<string> serverIds,
            ImmutableArray<string> tags,
            string zone,
            string id)
        {
            BridgeId = bridgeId;
            Description = description;
            Filter = filter;
            IconId = iconId;
            Name = name;
            ServerIds = serverIds;
            Tags = tags;
            Zone = zone;
            Id = id;
        }
    }

    namespace Inputs
    {

    public sealed class GetSwitchFilterArgs : Pulumi.InvokeArgs
    {
        [Input("conditions")]
        private List<GetSwitchFilterConditionsArgs>? _conditions;
        public List<GetSwitchFilterConditionsArgs> Conditions
        {
            get => _conditions ?? (_conditions = new List<GetSwitchFilterConditionsArgs>());
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

        public GetSwitchFilterArgs()
        {
        }
    }

    public sealed class GetSwitchFilterConditionsArgs : Pulumi.InvokeArgs
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

        public GetSwitchFilterConditionsArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class GetSwitchFilterConditionsResult
    {
        public readonly string Name;
        public readonly ImmutableArray<string> Values;

        [OutputConstructor]
        private GetSwitchFilterConditionsResult(
            string name,
            ImmutableArray<string> values)
        {
            Name = name;
            Values = values;
        }
    }

    [OutputType]
    public sealed class GetSwitchFilterResult
    {
        public readonly ImmutableArray<GetSwitchFilterConditionsResult> Conditions;
        public readonly string? Id;
        public readonly ImmutableArray<string> Names;
        public readonly ImmutableArray<string> Tags;

        [OutputConstructor]
        private GetSwitchFilterResult(
            ImmutableArray<GetSwitchFilterConditionsResult> conditions,
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
    }
}
