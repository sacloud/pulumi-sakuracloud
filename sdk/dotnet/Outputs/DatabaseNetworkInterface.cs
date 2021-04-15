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
    public sealed class DatabaseNetworkInterface
    {
        /// <summary>
        /// The IP address of the gateway used by Database.
        /// </summary>
        public readonly string Gateway;
        /// <summary>
        /// The IP address to assign to the Database.
        /// </summary>
        public readonly string IpAddress;
        /// <summary>
        /// The bit length of the subnet to assign to the Database. This must be in the range [`8`-`29`].
        /// </summary>
        public readonly int Netmask;
        /// <summary>
        /// The number of the listening port. This must be in the range [`1024`-`65535`].
        /// </summary>
        public readonly int? Port;
        /// <summary>
        /// The range of source IP addresses that allow to access to the Database via network.
        /// </summary>
        public readonly ImmutableArray<string> SourceRanges;
        /// <summary>
        /// The id of the switch to which the Database connects.
        /// </summary>
        public readonly string SwitchId;

        [OutputConstructor]
        private DatabaseNetworkInterface(
            string gateway,

            string ipAddress,

            int netmask,

            int? port,

            ImmutableArray<string> sourceRanges,

            string switchId)
        {
            Gateway = gateway;
            IpAddress = ipAddress;
            Netmask = netmask;
            Port = port;
            SourceRanges = sourceRanges;
            SwitchId = switchId;
        }
    }
}