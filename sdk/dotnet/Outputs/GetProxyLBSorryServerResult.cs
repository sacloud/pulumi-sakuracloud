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
    public sealed class GetProxyLBSorryServerResult
    {
        /// <summary>
        /// The IP address of the SorryServer. This will be used when all servers are down.
        /// </summary>
        public readonly string IpAddress;
        /// <summary>
        /// The number of syslog port.
        /// </summary>
        public readonly int Port;

        [OutputConstructor]
        private GetProxyLBSorryServerResult(
            string ipAddress,

            int port)
        {
            IpAddress = ipAddress;
            Port = port;
        }
    }
}
