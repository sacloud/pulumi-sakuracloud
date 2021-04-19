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
    public sealed class DatabaseReadReplicaNetworkInterface
    {
        /// <summary>
        /// The IP address of the gateway used by read-replica database. If `gateway` isn't specified, it will be set to the same value of the master database.
        /// </summary>
        public readonly string? Gateway;
        /// <summary>
        /// The IP address to assign to the read-replica database.
        /// </summary>
        public readonly string IpAddress;
        /// <summary>
        /// The bit length of the subnet to assign to the read-replica database. This must be in the range [`8`-`29`]. If `netmask` isn't specified, it will be set to the same value of the master database.
        /// </summary>
        public readonly int? Netmask;
        /// <summary>
        /// The range of source IP addresses that allow to access to the read-replica database via network.
        /// </summary>
        public readonly ImmutableArray<string> SourceRanges;
        /// <summary>
        /// The id of the switch to which the read-replica database connects. If `switch_id` isn't specified, it will be set to the same value of the master database.
        /// </summary>
        public readonly string? SwitchId;

        [OutputConstructor]
        private DatabaseReadReplicaNetworkInterface(
            string? gateway,

            string ipAddress,

            int? netmask,

            ImmutableArray<string> sourceRanges,

            string? switchId)
        {
            Gateway = gateway;
            IpAddress = ipAddress;
            Netmask = netmask;
            SourceRanges = sourceRanges;
            SwitchId = switchId;
        }
    }
}
