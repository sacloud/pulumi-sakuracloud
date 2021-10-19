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
    public sealed class VPCRouterWireGuard
    {
        /// <summary>
        /// The IP address for WireGuard server. This must be formatted with xxx.xxx.xxx.xxx/nn.
        /// </summary>
        public readonly string IpAddress;
        /// <summary>
        /// One or more `peer` blocks as defined below.
        /// </summary>
        public readonly ImmutableArray<Outputs.VPCRouterWireGuardPeer> Peers;
        /// <summary>
        /// the public key of the WireGuard client.
        /// </summary>
        public readonly string? PublicKey;

        [OutputConstructor]
        private VPCRouterWireGuard(
            string ipAddress,

            ImmutableArray<Outputs.VPCRouterWireGuardPeer> peers,

            string? publicKey)
        {
            IpAddress = ipAddress;
            Peers = peers;
            PublicKey = publicKey;
        }
    }
}