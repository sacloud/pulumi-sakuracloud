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
    /// Manages a SakuraCloud Switch.
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
    ///         var foobar = new Sakuracloud.Switch("foobar", new Sakuracloud.SwitchArgs
    ///         {
    ///             Description = "description",
    ///             Tags = 
    ///             {
    ///                 "tag1",
    ///                 "tag2",
    ///             },
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// </summary>
    [SakuracloudResourceType("sakuracloud:index/switch:Switch")]
    public partial class Switch : Pulumi.CustomResource
    {
        /// <summary>
        /// The bridge id attached to the Switch.
        /// </summary>
        [Output("bridgeId")]
        public Output<string?> BridgeId { get; private set; } = null!;

        /// <summary>
        /// The description of the Switch. The length of this value must be in the range [`1`-`512`].
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// The icon id to attach to the Switch.
        /// </summary>
        [Output("iconId")]
        public Output<string?> IconId { get; private set; } = null!;

        /// <summary>
        /// The name of the Switch. The length of this value must be in the range [`1`-`64`].
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// A list of server id connected to the switch.
        /// </summary>
        [Output("serverIds")]
        public Output<ImmutableArray<string>> ServerIds { get; private set; } = null!;

        /// <summary>
        /// Any tags to assign to the Switch.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<string>> Tags { get; private set; } = null!;

        /// <summary>
        /// The name of zone that the Switch will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        /// </summary>
        [Output("zone")]
        public Output<string> Zone { get; private set; } = null!;


        /// <summary>
        /// Create a Switch resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Switch(string name, SwitchArgs? args = null, CustomResourceOptions? options = null)
            : base("sakuracloud:index/switch:Switch", name, args ?? new SwitchArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Switch(string name, Input<string> id, SwitchState? state = null, CustomResourceOptions? options = null)
            : base("sakuracloud:index/switch:Switch", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Switch resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Switch Get(string name, Input<string> id, SwitchState? state = null, CustomResourceOptions? options = null)
        {
            return new Switch(name, id, state, options);
        }
    }

    public sealed class SwitchArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The bridge id attached to the Switch.
        /// </summary>
        [Input("bridgeId")]
        public Input<string>? BridgeId { get; set; }

        /// <summary>
        /// The description of the Switch. The length of this value must be in the range [`1`-`512`].
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The icon id to attach to the Switch.
        /// </summary>
        [Input("iconId")]
        public Input<string>? IconId { get; set; }

        /// <summary>
        /// The name of the Switch. The length of this value must be in the range [`1`-`64`].
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("tags")]
        private InputList<string>? _tags;

        /// <summary>
        /// Any tags to assign to the Switch.
        /// </summary>
        public InputList<string> Tags
        {
            get => _tags ?? (_tags = new InputList<string>());
            set => _tags = value;
        }

        /// <summary>
        /// The name of zone that the Switch will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        /// </summary>
        [Input("zone")]
        public Input<string>? Zone { get; set; }

        public SwitchArgs()
        {
        }
    }

    public sealed class SwitchState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The bridge id attached to the Switch.
        /// </summary>
        [Input("bridgeId")]
        public Input<string>? BridgeId { get; set; }

        /// <summary>
        /// The description of the Switch. The length of this value must be in the range [`1`-`512`].
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The icon id to attach to the Switch.
        /// </summary>
        [Input("iconId")]
        public Input<string>? IconId { get; set; }

        /// <summary>
        /// The name of the Switch. The length of this value must be in the range [`1`-`64`].
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("serverIds")]
        private InputList<string>? _serverIds;

        /// <summary>
        /// A list of server id connected to the switch.
        /// </summary>
        public InputList<string> ServerIds
        {
            get => _serverIds ?? (_serverIds = new InputList<string>());
            set => _serverIds = value;
        }

        [Input("tags")]
        private InputList<string>? _tags;

        /// <summary>
        /// Any tags to assign to the Switch.
        /// </summary>
        public InputList<string> Tags
        {
            get => _tags ?? (_tags = new InputList<string>());
            set => _tags = value;
        }

        /// <summary>
        /// The name of zone that the Switch will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        /// </summary>
        [Input("zone")]
        public Input<string>? Zone { get; set; }

        public SwitchState()
        {
        }
    }
}
