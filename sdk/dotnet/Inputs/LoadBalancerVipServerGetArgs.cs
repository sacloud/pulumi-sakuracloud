// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Sakuracloud.Inputs
{

    public sealed class LoadBalancerVipServerGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The flag to enable as destination of load balancing.
        /// </summary>
        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        /// <summary>
        /// The IP address of the destination server.
        /// </summary>
        [Input("ipAddress", required: true)]
        public Input<string> IpAddress { get; set; } = null!;

        /// <summary>
        /// The path used when checking by HTTP/HTTPS.
        /// </summary>
        [Input("path")]
        public Input<string>? Path { get; set; }

        /// <summary>
        /// The protocol used for health checks. This must be one of [`http`/`https`/`tcp`/`ping`].
        /// </summary>
        [Input("protocol", required: true)]
        public Input<string> Protocol { get; set; } = null!;

        /// <summary>
        /// The response code to expect when checking by HTTP/HTTPS.
        /// </summary>
        [Input("status")]
        public Input<string>? Status { get; set; }

        public LoadBalancerVipServerGetArgs()
        {
        }
    }
}