// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Sakuracloud
{
    /// <summary>
    /// Provides a SakuraCloud GSLB Server resource. This can be used to create and delete GSLB Servers.
    /// 
    /// ## Import (not supported)
    /// 
    /// Import of GSLB Server is not supported.
    /// 
    /// &gt; This content is derived from https://github.com/sacloud/terraform-provider-sakuracloud/blob/master/website/docs/r/gslb_server.html.markdown.
    /// </summary>
    public partial class GSLBServer : Pulumi.CustomResource
    {
        /// <summary>
        /// The flag for enable/disable the GSLB Server (default:`true`).
        /// </summary>
        [Output("enabled")]
        public Output<bool?> Enabled { get; private set; } = null!;

        /// <summary>
        /// The ID of the GSLB to which the GSLB Server belongs.
        /// </summary>
        [Output("gslbId")]
        public Output<string> GslbId { get; private set; } = null!;

        /// <summary>
        /// The IP address of the GSLB Server.
        /// </summary>
        [Output("ipaddress")]
        public Output<string> Ipaddress { get; private set; } = null!;

        /// <summary>
        /// The weight of GSLB server used when weighting is enabled in the GSLB.
        /// </summary>
        [Output("weight")]
        public Output<int?> Weight { get; private set; } = null!;


        /// <summary>
        /// Create a GSLBServer resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public GSLBServer(string name, GSLBServerArgs args, CustomResourceOptions? options = null)
            : base("sakuracloud:index/gSLBServer:GSLBServer", name, args, MakeResourceOptions(options, ""))
        {
        }

        private GSLBServer(string name, Input<string> id, GSLBServerState? state = null, CustomResourceOptions? options = null)
            : base("sakuracloud:index/gSLBServer:GSLBServer", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing GSLBServer resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static GSLBServer Get(string name, Input<string> id, GSLBServerState? state = null, CustomResourceOptions? options = null)
        {
            return new GSLBServer(name, id, state, options);
        }
    }

    public sealed class GSLBServerArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The flag for enable/disable the GSLB Server (default:`true`).
        /// </summary>
        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        /// <summary>
        /// The ID of the GSLB to which the GSLB Server belongs.
        /// </summary>
        [Input("gslbId", required: true)]
        public Input<string> GslbId { get; set; } = null!;

        /// <summary>
        /// The IP address of the GSLB Server.
        /// </summary>
        [Input("ipaddress", required: true)]
        public Input<string> Ipaddress { get; set; } = null!;

        /// <summary>
        /// The weight of GSLB server used when weighting is enabled in the GSLB.
        /// </summary>
        [Input("weight")]
        public Input<int>? Weight { get; set; }

        public GSLBServerArgs()
        {
        }
    }

    public sealed class GSLBServerState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The flag for enable/disable the GSLB Server (default:`true`).
        /// </summary>
        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        /// <summary>
        /// The ID of the GSLB to which the GSLB Server belongs.
        /// </summary>
        [Input("gslbId")]
        public Input<string>? GslbId { get; set; }

        /// <summary>
        /// The IP address of the GSLB Server.
        /// </summary>
        [Input("ipaddress")]
        public Input<string>? Ipaddress { get; set; }

        /// <summary>
        /// The weight of GSLB server used when weighting is enabled in the GSLB.
        /// </summary>
        [Input("weight")]
        public Input<int>? Weight { get; set; }

        public GSLBServerState()
        {
        }
    }
}