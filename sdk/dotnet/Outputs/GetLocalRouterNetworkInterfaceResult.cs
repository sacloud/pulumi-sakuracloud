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
    public sealed class GetLocalRouterNetworkInterfaceResult
    {
        /// <summary>
        /// The list of IP address assigned to the LocalRouter.
        /// </summary>
        public readonly ImmutableArray<string> IpAddresses;
        /// <summary>
        /// The bit length of the subnet assigned to the LocalRouter.
        /// </summary>
        public readonly int Netmask;
        /// <summary>
        /// The virtual IP address.
        /// </summary>
        public readonly string Vip;
        /// <summary>
        /// The Virtual Router Identifier.
        /// </summary>
        public readonly int Vrid;

        [OutputConstructor]
        private GetLocalRouterNetworkInterfaceResult(
            ImmutableArray<string> ipAddresses,

            int netmask,

            string vip,

            int vrid)
        {
            IpAddresses = ipAddresses;
            Netmask = netmask;
            Vip = vip;
            Vrid = vrid;
        }
    }
}
