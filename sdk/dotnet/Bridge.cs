// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Sakuracloud
{
    /// <summary>
    /// Manages a SakuraCloud Bridge.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Sakuracloud = Pulumi.Sakuracloud;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var foobar = new Sakuracloud.Bridge("foobar", new Sakuracloud.BridgeArgs
    ///         {
    ///             Description = "description",
    ///         });
    ///         var is1a = new Sakuracloud.Switch("is1a", new Sakuracloud.SwitchArgs
    ///         {
    ///             Description = "description",
    ///             BridgeId = foobar.Id,
    ///             Zone = "is1a",
    ///         });
    ///         var is1b = new Sakuracloud.Switch("is1b", new Sakuracloud.SwitchArgs
    ///         {
    ///             Description = "description",
    ///             BridgeId = foobar.Id,
    ///             Zone = "is1b",
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// </summary>
    [SakuracloudResourceType("sakuracloud:index/bridge:Bridge")]
    public partial class Bridge : Pulumi.CustomResource
    {
        /// <summary>
        /// The description of the Bridge. The length of this value must be in the range [`1`-`512`].
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// The name of the Bridge. The length of this value must be in the range [`1`-`64`].
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The name of zone that the Bridge will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        /// </summary>
        [Output("zone")]
        public Output<string> Zone { get; private set; } = null!;


        /// <summary>
        /// Create a Bridge resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Bridge(string name, BridgeArgs? args = null, CustomResourceOptions? options = null)
            : base("sakuracloud:index/bridge:Bridge", name, args ?? new BridgeArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Bridge(string name, Input<string> id, BridgeState? state = null, CustomResourceOptions? options = null)
            : base("sakuracloud:index/bridge:Bridge", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Bridge resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Bridge Get(string name, Input<string> id, BridgeState? state = null, CustomResourceOptions? options = null)
        {
            return new Bridge(name, id, state, options);
        }
    }

    public sealed class BridgeArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The description of the Bridge. The length of this value must be in the range [`1`-`512`].
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The name of the Bridge. The length of this value must be in the range [`1`-`64`].
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The name of zone that the Bridge will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        /// </summary>
        [Input("zone")]
        public Input<string>? Zone { get; set; }

        public BridgeArgs()
        {
        }
    }

    public sealed class BridgeState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The description of the Bridge. The length of this value must be in the range [`1`-`512`].
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The name of the Bridge. The length of this value must be in the range [`1`-`64`].
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The name of zone that the Bridge will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        /// </summary>
        [Input("zone")]
        public Input<string>? Zone { get; set; }

        public BridgeState()
        {
        }
    }
}
