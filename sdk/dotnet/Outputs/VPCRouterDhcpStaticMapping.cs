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
    public sealed class VPCRouterDhcpStaticMapping
    {
        /// <summary>
        /// The static IP address to assign to DHCP client.
        /// </summary>
        public readonly string IpAddress;
        /// <summary>
        /// The source MAC address of static mapping.
        /// </summary>
        public readonly string MacAddress;

        [OutputConstructor]
        private VPCRouterDhcpStaticMapping(
            string ipAddress,

            string macAddress)
        {
            IpAddress = ipAddress;
            MacAddress = macAddress;
        }
    }
}
