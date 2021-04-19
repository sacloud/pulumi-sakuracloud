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
    public sealed class GetDatabaseNetworkInterfaceResult
    {
        /// <summary>
        /// The IP address of the gateway used by Database.
        /// </summary>
        public readonly string Gateway;
        /// <summary>
        /// The IP address assigned to the Database.
        /// </summary>
        public readonly string IpAddress;
        /// <summary>
        /// The bit length of the subnet assigned to the Database.
        /// </summary>
        public readonly int Netmask;
        /// <summary>
        /// The number of the listening port.
        /// </summary>
        public readonly int Port;
        /// <summary>
        /// The range of source IP addresses that allow to access to the Database via network.
        /// </summary>
        public readonly ImmutableArray<string> SourceRanges;
        /// <summary>
        /// The id of the switch connected from the Database.
        /// </summary>
        public readonly string SwitchId;

        [OutputConstructor]
        private GetDatabaseNetworkInterfaceResult(
            string gateway,

            string ipAddress,

            int netmask,

            int port,

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
