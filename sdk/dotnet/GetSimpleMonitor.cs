// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Sakuracloud
{
    public static class GetSimpleMonitor
    {
        /// <summary>
        /// Get information about an existing Simple Monitor.
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Sakuracloud = Pulumi.Sakuracloud;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var foobar = Output.Create(Sakuracloud.GetSimpleMonitor.InvokeAsync(new Sakuracloud.GetSimpleMonitorArgs
        ///         {
        ///             Filter = new Sakuracloud.Inputs.GetSimpleMonitorFilterArgs
        ///             {
        ///                 Names = 
        ///                 {
        ///                     "foobar",
        ///                 },
        ///             },
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetSimpleMonitorResult> InvokeAsync(GetSimpleMonitorArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetSimpleMonitorResult>("sakuracloud:index/getSimpleMonitor:getSimpleMonitor", args ?? new GetSimpleMonitorArgs(), options.WithVersion());
    }


    public sealed class GetSimpleMonitorArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// One or more values used for filtering, as defined below.
        /// </summary>
        [Input("filter")]
        public Inputs.GetSimpleMonitorFilterArgs? Filter { get; set; }

        public GetSimpleMonitorArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetSimpleMonitorResult
    {
        /// <summary>
        /// The interval in seconds between checks.
        /// </summary>
        public readonly int DelayLoop;
        /// <summary>
        /// The description of the SimpleMonitor.
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// The flag to enable monitoring by the simple monitor.
        /// </summary>
        public readonly bool Enabled;
        public readonly Outputs.GetSimpleMonitorFilterResult? Filter;
        /// <summary>
        /// A list of `health_check` blocks as defined below.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetSimpleMonitorHealthCheckResult> HealthChecks;
        /// <summary>
        /// The icon id attached to the SimpleMonitor.
        /// </summary>
        public readonly string IconId;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// The flag to enable notification by email.
        /// </summary>
        public readonly bool NotifyEmailEnabled;
        /// <summary>
        /// The flag to enable HTML format instead of text format.
        /// </summary>
        public readonly bool NotifyEmailHtml;
        /// <summary>
        /// The interval in hours between notification.
        /// </summary>
        public readonly int NotifyInterval;
        /// <summary>
        /// The flag to enable notification by slack/discord.
        /// </summary>
        public readonly bool NotifySlackEnabled;
        /// <summary>
        /// The webhook URL for sending notification by slack/discord.
        /// </summary>
        public readonly string NotifySlackWebhook;
        /// <summary>
        /// Any tags assigned to the SimpleMonitor.
        /// </summary>
        public readonly ImmutableArray<string> Tags;
        /// <summary>
        /// The monitoring target of the simple monitor. This will be IP address or FQDN.
        /// </summary>
        public readonly string Target;

        [OutputConstructor]
        private GetSimpleMonitorResult(
            int delayLoop,

            string description,

            bool enabled,

            Outputs.GetSimpleMonitorFilterResult? filter,

            ImmutableArray<Outputs.GetSimpleMonitorHealthCheckResult> healthChecks,

            string iconId,

            string id,

            bool notifyEmailEnabled,

            bool notifyEmailHtml,

            int notifyInterval,

            bool notifySlackEnabled,

            string notifySlackWebhook,

            ImmutableArray<string> tags,

            string target)
        {
            DelayLoop = delayLoop;
            Description = description;
            Enabled = enabled;
            Filter = filter;
            HealthChecks = healthChecks;
            IconId = iconId;
            Id = id;
            NotifyEmailEnabled = notifyEmailEnabled;
            NotifyEmailHtml = notifyEmailHtml;
            NotifyInterval = notifyInterval;
            NotifySlackEnabled = notifySlackEnabled;
            NotifySlackWebhook = notifySlackWebhook;
            Tags = tags;
            Target = target;
        }
    }
}
