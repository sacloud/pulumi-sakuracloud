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
    public sealed class ProxyLBSorryServer
    {
        /// <summary>
        /// The IP address of the SorryServer. This will be used when all servers are down.
        /// </summary>
        public readonly string IpAddress;
        /// <summary>
        /// The port number of the SorryServer. This will be used when all servers are down.
        /// </summary>
        public readonly int? Port;

        [OutputConstructor]
        private ProxyLBSorryServer(
            string ipAddress,

            int? port)
        {
            IpAddress = ipAddress;
            Port = port;
        }
    }
}