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
    /// Manages a SakuraCloud Simple Monitor.
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
    ///         var foobar = new Sakuracloud.SimpleMonitor("foobar", new Sakuracloud.SimpleMonitorArgs
    ///         {
    ///             DelayLoop = 60,
    ///             Description = "description",
    ///             HealthCheck = new Sakuracloud.Inputs.SimpleMonitorHealthCheckArgs
    ///             {
    ///                 ContainsString = "ok",
    ///                 HostHeader = "example.com",
    ///                 Http2 = true,
    ///                 Path = "/",
    ///                 Port = 443,
    ///                 Protocol = "https",
    ///                 Sni = true,
    ///                 Status = 200,
    ///             },
    ///             NotifyEmailEnabled = true,
    ///             NotifyEmailHtml = true,
    ///             NotifySlackEnabled = true,
    ///             NotifySlackWebhook = "https://hooks.slack.com/services/xxx/xxx/xxx",
    ///             Tags = 
    ///             {
    ///                 "tag1",
    ///                 "tag2",
    ///             },
    ///             Target = "www.example.com",
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// </summary>
    [SakuracloudResourceType("sakuracloud:index/simpleMonitor:SimpleMonitor")]
    public partial class SimpleMonitor : Pulumi.CustomResource
    {
        /// <summary>
        /// The interval in seconds between checks. This must be in the range [`60`-`3600`]. Default:`60`.
        /// </summary>
        [Output("delayLoop")]
        public Output<int?> DelayLoop { get; private set; } = null!;

        /// <summary>
        /// The description of the SimpleMonitor. The length of this value must be in the range [`1`-`512`].
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// The flag to enable monitoring by the simple monitor. Default:`true`.
        /// </summary>
        [Output("enabled")]
        public Output<bool?> Enabled { get; private set; } = null!;

        /// <summary>
        /// A `health_check` block as defined below.
        /// </summary>
        [Output("healthCheck")]
        public Output<Outputs.SimpleMonitorHealthCheck> HealthCheck { get; private set; } = null!;

        /// <summary>
        /// The icon id to attach to the SimpleMonitor.
        /// </summary>
        [Output("iconId")]
        public Output<string?> IconId { get; private set; } = null!;

        /// <summary>
        /// The flag to enable notification by email. Default:`true`.
        /// </summary>
        [Output("notifyEmailEnabled")]
        public Output<bool?> NotifyEmailEnabled { get; private set; } = null!;

        /// <summary>
        /// The flag to enable HTML format instead of text format.
        /// </summary>
        [Output("notifyEmailHtml")]
        public Output<bool?> NotifyEmailHtml { get; private set; } = null!;

        /// <summary>
        /// The interval in hours between notification. This must be in the range [`1`-`72`]. Default:`2`.
        /// </summary>
        [Output("notifyInterval")]
        public Output<int?> NotifyInterval { get; private set; } = null!;

        /// <summary>
        /// The flag to enable notification by slack/discord.
        /// </summary>
        [Output("notifySlackEnabled")]
        public Output<bool?> NotifySlackEnabled { get; private set; } = null!;

        /// <summary>
        /// The webhook URL for sending notification by slack/discord.
        /// </summary>
        [Output("notifySlackWebhook")]
        public Output<string?> NotifySlackWebhook { get; private set; } = null!;

        /// <summary>
        /// Any tags to assign to the SimpleMonitor.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<string>> Tags { get; private set; } = null!;

        /// <summary>
        /// The monitoring target of the simple monitor. This must be IP address or FQDN. Changing this forces a new resource to be created.
        /// </summary>
        [Output("target")]
        public Output<string> Target { get; private set; } = null!;


        /// <summary>
        /// Create a SimpleMonitor resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public SimpleMonitor(string name, SimpleMonitorArgs args, CustomResourceOptions? options = null)
            : base("sakuracloud:index/simpleMonitor:SimpleMonitor", name, args ?? new SimpleMonitorArgs(), MakeResourceOptions(options, ""))
        {
        }

        private SimpleMonitor(string name, Input<string> id, SimpleMonitorState? state = null, CustomResourceOptions? options = null)
            : base("sakuracloud:index/simpleMonitor:SimpleMonitor", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing SimpleMonitor resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static SimpleMonitor Get(string name, Input<string> id, SimpleMonitorState? state = null, CustomResourceOptions? options = null)
        {
            return new SimpleMonitor(name, id, state, options);
        }
    }

    public sealed class SimpleMonitorArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The interval in seconds between checks. This must be in the range [`60`-`3600`]. Default:`60`.
        /// </summary>
        [Input("delayLoop")]
        public Input<int>? DelayLoop { get; set; }

        /// <summary>
        /// The description of the SimpleMonitor. The length of this value must be in the range [`1`-`512`].
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The flag to enable monitoring by the simple monitor. Default:`true`.
        /// </summary>
        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        /// <summary>
        /// A `health_check` block as defined below.
        /// </summary>
        [Input("healthCheck", required: true)]
        public Input<Inputs.SimpleMonitorHealthCheckArgs> HealthCheck { get; set; } = null!;

        /// <summary>
        /// The icon id to attach to the SimpleMonitor.
        /// </summary>
        [Input("iconId")]
        public Input<string>? IconId { get; set; }

        /// <summary>
        /// The flag to enable notification by email. Default:`true`.
        /// </summary>
        [Input("notifyEmailEnabled")]
        public Input<bool>? NotifyEmailEnabled { get; set; }

        /// <summary>
        /// The flag to enable HTML format instead of text format.
        /// </summary>
        [Input("notifyEmailHtml")]
        public Input<bool>? NotifyEmailHtml { get; set; }

        /// <summary>
        /// The interval in hours between notification. This must be in the range [`1`-`72`]. Default:`2`.
        /// </summary>
        [Input("notifyInterval")]
        public Input<int>? NotifyInterval { get; set; }

        /// <summary>
        /// The flag to enable notification by slack/discord.
        /// </summary>
        [Input("notifySlackEnabled")]
        public Input<bool>? NotifySlackEnabled { get; set; }

        /// <summary>
        /// The webhook URL for sending notification by slack/discord.
        /// </summary>
        [Input("notifySlackWebhook")]
        public Input<string>? NotifySlackWebhook { get; set; }

        [Input("tags")]
        private InputList<string>? _tags;

        /// <summary>
        /// Any tags to assign to the SimpleMonitor.
        /// </summary>
        public InputList<string> Tags
        {
            get => _tags ?? (_tags = new InputList<string>());
            set => _tags = value;
        }

        /// <summary>
        /// The monitoring target of the simple monitor. This must be IP address or FQDN. Changing this forces a new resource to be created.
        /// </summary>
        [Input("target", required: true)]
        public Input<string> Target { get; set; } = null!;

        public SimpleMonitorArgs()
        {
        }
    }

    public sealed class SimpleMonitorState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The interval in seconds between checks. This must be in the range [`60`-`3600`]. Default:`60`.
        /// </summary>
        [Input("delayLoop")]
        public Input<int>? DelayLoop { get; set; }

        /// <summary>
        /// The description of the SimpleMonitor. The length of this value must be in the range [`1`-`512`].
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The flag to enable monitoring by the simple monitor. Default:`true`.
        /// </summary>
        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        /// <summary>
        /// A `health_check` block as defined below.
        /// </summary>
        [Input("healthCheck")]
        public Input<Inputs.SimpleMonitorHealthCheckGetArgs>? HealthCheck { get; set; }

        /// <summary>
        /// The icon id to attach to the SimpleMonitor.
        /// </summary>
        [Input("iconId")]
        public Input<string>? IconId { get; set; }

        /// <summary>
        /// The flag to enable notification by email. Default:`true`.
        /// </summary>
        [Input("notifyEmailEnabled")]
        public Input<bool>? NotifyEmailEnabled { get; set; }

        /// <summary>
        /// The flag to enable HTML format instead of text format.
        /// </summary>
        [Input("notifyEmailHtml")]
        public Input<bool>? NotifyEmailHtml { get; set; }

        /// <summary>
        /// The interval in hours between notification. This must be in the range [`1`-`72`]. Default:`2`.
        /// </summary>
        [Input("notifyInterval")]
        public Input<int>? NotifyInterval { get; set; }

        /// <summary>
        /// The flag to enable notification by slack/discord.
        /// </summary>
        [Input("notifySlackEnabled")]
        public Input<bool>? NotifySlackEnabled { get; set; }

        /// <summary>
        /// The webhook URL for sending notification by slack/discord.
        /// </summary>
        [Input("notifySlackWebhook")]
        public Input<string>? NotifySlackWebhook { get; set; }

        [Input("tags")]
        private InputList<string>? _tags;

        /// <summary>
        /// Any tags to assign to the SimpleMonitor.
        /// </summary>
        public InputList<string> Tags
        {
            get => _tags ?? (_tags = new InputList<string>());
            set => _tags = value;
        }

        /// <summary>
        /// The monitoring target of the simple monitor. This must be IP address or FQDN. Changing this forces a new resource to be created.
        /// </summary>
        [Input("target")]
        public Input<string>? Target { get; set; }

        public SimpleMonitorState()
        {
        }
    }
}
