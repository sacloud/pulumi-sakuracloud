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
    public sealed class GetProxyLBServerResult
    {
        /// <summary>
        /// The flag to enable as destination of load balancing.
        /// </summary>
        public readonly bool Enabled;
        /// <summary>
        /// The name of load balancing group. This is used when using rule-based load balancing.
        /// </summary>
        public readonly string Group;
        /// <summary>
        /// The IP address of the SorryServer. This will be used when all servers are down.
        /// </summary>
        public readonly string IpAddress;
        /// <summary>
        /// The port number of the SorryServer. This will be used when all servers are down.
        /// </summary>
        public readonly int Port;

        [OutputConstructor]
        private GetProxyLBServerResult(
            bool enabled,

            string group,

            string ipAddress,

            int port)
        {
            Enabled = enabled;
            Group = group;
            IpAddress = ipAddress;
            Port = port;
        }
    }
}
