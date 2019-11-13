// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Sakuracloud
{
    /// <summary>
    /// Provides a SakuraCloud Mobile Gateway SIM Route resource. This can be used to create, update, and delete Mobile Gateway SIM Routes.
    /// 
    /// ## Import (not supported)
    /// 
    /// Import of Mobile Gateway SIM Route is not supported.
    /// 
    /// &gt; This content is derived from https://github.com/sacloud/terraform-provider-sakuracloud/blob/master/website/docs/r/mobile_gateway_sim_route.html.markdown.
    /// </summary>
    public partial class MobileGatewaySIMRoute : Pulumi.CustomResource
    {
        /// <summary>
        /// The ID of the Mobile Gateway to set SIM Route.
        /// </summary>
        [Output("mobileGatewayId")]
        public Output<string> MobileGatewayId { get; private set; } = null!;

        /// <summary>
        /// The routing prefix (format:`CIDR`).
        /// </summary>
        [Output("prefix")]
        public Output<string> Prefix { get; private set; } = null!;

        /// <summary>
        /// The ID of the routing destination SIM.
        /// </summary>
        [Output("simId")]
        public Output<string> SimId { get; private set; } = null!;

        /// <summary>
        /// The ID of the zone to which the resource belongs.
        /// </summary>
        [Output("zone")]
        public Output<string> Zone { get; private set; } = null!;


        /// <summary>
        /// Create a MobileGatewaySIMRoute resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public MobileGatewaySIMRoute(string name, MobileGatewaySIMRouteArgs args, CustomResourceOptions? options = null)
            : base("sakuracloud:index/mobileGatewaySIMRoute:MobileGatewaySIMRoute", name, args, MakeResourceOptions(options, ""))
        {
        }

        private MobileGatewaySIMRoute(string name, Input<string> id, MobileGatewaySIMRouteState? state = null, CustomResourceOptions? options = null)
            : base("sakuracloud:index/mobileGatewaySIMRoute:MobileGatewaySIMRoute", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing MobileGatewaySIMRoute resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static MobileGatewaySIMRoute Get(string name, Input<string> id, MobileGatewaySIMRouteState? state = null, CustomResourceOptions? options = null)
        {
            return new MobileGatewaySIMRoute(name, id, state, options);
        }
    }

    public sealed class MobileGatewaySIMRouteArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of the Mobile Gateway to set SIM Route.
        /// </summary>
        [Input("mobileGatewayId", required: true)]
        public Input<string> MobileGatewayId { get; set; } = null!;

        /// <summary>
        /// The routing prefix (format:`CIDR`).
        /// </summary>
        [Input("prefix", required: true)]
        public Input<string> Prefix { get; set; } = null!;

        /// <summary>
        /// The ID of the routing destination SIM.
        /// </summary>
        [Input("simId", required: true)]
        public Input<string> SimId { get; set; } = null!;

        /// <summary>
        /// The ID of the zone to which the resource belongs.
        /// </summary>
        [Input("zone")]
        public Input<string>? Zone { get; set; }

        public MobileGatewaySIMRouteArgs()
        {
        }
    }

    public sealed class MobileGatewaySIMRouteState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of the Mobile Gateway to set SIM Route.
        /// </summary>
        [Input("mobileGatewayId")]
        public Input<string>? MobileGatewayId { get; set; }

        /// <summary>
        /// The routing prefix (format:`CIDR`).
        /// </summary>
        [Input("prefix")]
        public Input<string>? Prefix { get; set; }

        /// <summary>
        /// The ID of the routing destination SIM.
        /// </summary>
        [Input("simId")]
        public Input<string>? SimId { get; set; }

        /// <summary>
        /// The ID of the zone to which the resource belongs.
        /// </summary>
        [Input("zone")]
        public Input<string>? Zone { get; set; }

        public MobileGatewaySIMRouteState()
        {
        }
    }
}