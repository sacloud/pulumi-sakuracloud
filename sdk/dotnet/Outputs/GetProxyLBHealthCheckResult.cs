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
    public sealed class GetProxyLBHealthCheckResult
    {
        /// <summary>
        /// The interval in seconds between checks.
        /// </summary>
        public readonly int DelayLoop;
        /// <summary>
        /// The value of host header send when checking by HTTP.
        /// </summary>
        public readonly string HostHeader;
        /// <summary>
        /// The request path that is used as condition of rule-based balancing.
        /// </summary>
        public readonly string Path;
        /// <summary>
        /// The number of syslog port.
        /// </summary>
        public readonly int Port;
        /// <summary>
        /// The protocol used for health checks. This will be one of [`http`/`tcp`].
        /// </summary>
        public readonly string Protocol;

        [OutputConstructor]
        private GetProxyLBHealthCheckResult(
            int delayLoop,

            string hostHeader,

            string path,

            int port,

            string protocol)
        {
            DelayLoop = delayLoop;
            HostHeader = hostHeader;
            Path = path;
            Port = port;
            Protocol = protocol;
        }
    }
}
