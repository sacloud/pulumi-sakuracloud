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
        /// Use this data source to retrieve information about a SakuraCloud Bridge.
        /// 
        /// &gt; This content is derived from https://github.com/sacloud/terraform-provider-sakuracloud/blob/master/website/docs/d/bridge.html.markdown.
        /// </summary>
        public static Task<GetBridgeResult> GetBridge(GetBridgeArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetBridgeResult>("sakuracloud:index/getBridge:getBridge", args, options.WithVersion());
    }

    public sealed class GetBridgeArgs : Pulumi.ResourceArgs
    {
        [Input("filters")]
        private InputList<Inputs.GetBridgeFiltersArgs>? _filters;

        /// <summary>
        /// The map of filter key and value.
        /// </summary>
        public InputList<Inputs.GetBridgeFiltersArgs> Filters
        {
            get => _filters ?? (_filters = new InputList<Inputs.GetBridgeFiltersArgs>());
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

        /// <summary>
        /// The ID of the zone.
        /// </summary>
        [Input("zone")]
        public Input<string>? Zone { get; set; }

        public GetBridgeArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetBridgeResult
    {
        /// <summary>
        /// The description of the resource.
        /// </summary>
        public readonly string Description;
        public readonly ImmutableArray<Outputs.GetBridgeFiltersResult> Filters;
        /// <summary>
        /// The name of the resource.
        /// </summary>
        public readonly string Name;
        public readonly ImmutableArray<string> NameSelectors;
        /// <summary>
        /// The ID list of the switches connected to the bridge.
        /// </summary>
        public readonly ImmutableArray<string> SwitchIds;
        /// <summary>
        /// The ID of the zone to which the resource belongs.
        /// </summary>
        public readonly string Zone;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetBridgeResult(
            string description,
            ImmutableArray<Outputs.GetBridgeFiltersResult> filters,
            string name,
            ImmutableArray<string> nameSelectors,
            ImmutableArray<string> switchIds,
            string zone,
            string id)
        {
            Description = description;
            Filters = filters;
            Name = name;
            NameSelectors = nameSelectors;
            SwitchIds = switchIds;
            Zone = zone;
            Id = id;
        }
    }

    namespace Inputs
    {

    public sealed class GetBridgeFiltersArgs : Pulumi.ResourceArgs
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

        public GetBridgeFiltersArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class GetBridgeFiltersResult
    {
        /// <summary>
        /// The name of the resource.
        /// </summary>
        public readonly string Name;
        public readonly ImmutableArray<string> Values;

        [OutputConstructor]
        private GetBridgeFiltersResult(
            string name,
            ImmutableArray<string> values)
        {
            Name = name;
            Values = values;
        }
    }
    }
}
