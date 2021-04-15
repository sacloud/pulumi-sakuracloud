// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Sakuracloud.Outputs
{

    [OutputType]
    public sealed class GetLoadBalancerVipServerResult
    {
        /// <summary>
        /// The flag to enable as destination of load balancing.
        /// </summary>
        public readonly bool Enabled;
        /// <summary>
        /// The IP address of the destination server.
        /// </summary>
        public readonly string IpAddress;
        /// <summary>
        /// The path used when checking by HTTP/HTTPS.
        /// </summary>
        public readonly string Path;
        /// <summary>
        /// The protocol used for health checks. This will be one of [`http`/`https`/`tcp`/`ping`].
        /// </summary>
        public readonly string Protocol;
        /// <summary>
        /// The response code to expect when checking by HTTP/HTTPS.
        /// </summary>
        public readonly string Status;

        [OutputConstructor]
        private GetLoadBalancerVipServerResult(
            bool enabled,

            string ipAddress,

            string path,

            string protocol,

            string status)
        {
            Enabled = enabled;
            IpAddress = ipAddress;
            Path = path;
            Protocol = protocol;
            Status = status;
        }
    }
}