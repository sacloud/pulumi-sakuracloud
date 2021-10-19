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
    public sealed class GetVPCRouterWireGuardResult
    {
        /// <summary>
        /// The IP address for peer.
        /// </summary>
        public readonly string IpAddress;
        /// <summary>
        /// A list of `peer` blocks as defined below.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetVPCRouterWireGuardPeerResult> Peers;
        /// <summary>
        /// the public key of the WireGuard client.
        /// </summary>
        public readonly string PublicKey;

        [OutputConstructor]
        private GetVPCRouterWireGuardResult(
            string ipAddress,

            ImmutableArray<Outputs.GetVPCRouterWireGuardPeerResult> peers,

            string publicKey)
        {
            IpAddress = ipAddress;
            Peers = peers;
            PublicKey = publicKey;
        }
    }
}
