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
    public sealed class VPCRouterDhcpServer
    {
        /// <summary>
        /// A list of IP address of DNS server to assign to DHCP client.
        /// </summary>
        public readonly ImmutableArray<string> DnsServers;
        /// <summary>
        /// The index of the network interface on which to enable the DHCP service. This must be in the range [`1`-`7`].
        /// </summary>
        public readonly int InterfaceIndex;
        /// <summary>
        /// The start value of IP address range to assign to DHCP client.
        /// </summary>
        public readonly string RangeStart;
        /// <summary>
        /// The end value of IP address range to assign to DHCP client.
        /// </summary>
        public readonly string RangeStop;

        [OutputConstructor]
        private VPCRouterDhcpServer(
            ImmutableArray<string> dnsServers,

            int interfaceIndex,

            string rangeStart,

            string rangeStop)
        {
            DnsServers = dnsServers;
            InterfaceIndex = interfaceIndex;
            RangeStart = rangeStart;
            RangeStop = rangeStop;
        }
    }
}