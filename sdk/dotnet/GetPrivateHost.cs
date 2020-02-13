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
        public static Task<GetPrivateHostResult> GetPrivateHost(GetPrivateHostArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetPrivateHostResult>("sakuracloud:index/getPrivateHost:getPrivateHost", args ?? InvokeArgs.Empty, options.WithVersion());
    }

    public sealed class GetPrivateHostArgs : Pulumi.InvokeArgs
    {
        [Input("filter")]
        public Inputs.GetPrivateHostFilterArgs? Filter { get; set; }

        [Input("zone")]
        public string? Zone { get; set; }

        public GetPrivateHostArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetPrivateHostResult
    {
        public readonly int AssignedCore;
        public readonly int AssignedMemory;
        public readonly string Class;
        public readonly string Description;
        public readonly Outputs.GetPrivateHostFilterResult? Filter;
        public readonly string Hostname;
        public readonly string IconId;
        public readonly string Name;
        public readonly ImmutableArray<string> Tags;
        public readonly string Zone;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetPrivateHostResult(
            int assignedCore,
            int assignedMemory,
            string @class,
            string description,
            Outputs.GetPrivateHostFilterResult? filter,
            string hostname,
            string iconId,
            string name,
            ImmutableArray<string> tags,
            string zone,
            string id)
        {
            AssignedCore = assignedCore;
            AssignedMemory = assignedMemory;
            Class = @class;
            Description = description;
            Filter = filter;
            Hostname = hostname;
            IconId = iconId;
            Name = name;
            Tags = tags;
            Zone = zone;
            Id = id;
        }
    }

    namespace Inputs
    {

    public sealed class GetPrivateHostFilterArgs : Pulumi.InvokeArgs
    {
        [Input("conditions")]
        private List<GetPrivateHostFilterConditionsArgs>? _conditions;
        public List<GetPrivateHostFilterConditionsArgs> Conditions
        {
            get => _conditions ?? (_conditions = new List<GetPrivateHostFilterConditionsArgs>());
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

        public GetPrivateHostFilterArgs()
        {
        }
    }

    public sealed class GetPrivateHostFilterConditionsArgs : Pulumi.InvokeArgs
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

        public GetPrivateHostFilterConditionsArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class GetPrivateHostFilterConditionsResult
    {
        public readonly string Name;
        public readonly ImmutableArray<string> Values;

        [OutputConstructor]
        private GetPrivateHostFilterConditionsResult(
            string name,
            ImmutableArray<string> values)
        {
            Name = name;
            Values = values;
        }
    }

    [OutputType]
    public sealed class GetPrivateHostFilterResult
    {
        public readonly ImmutableArray<GetPrivateHostFilterConditionsResult> Conditions;
        public readonly string? Id;
        public readonly ImmutableArray<string> Names;
        public readonly ImmutableArray<string> Tags;

        [OutputConstructor]
        private GetPrivateHostFilterResult(
            ImmutableArray<GetPrivateHostFilterConditionsResult> conditions,
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
