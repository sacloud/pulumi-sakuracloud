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
    public sealed class VPCRouterWireGuardPeer
    {
        /// <summary>
        /// The IP address for peer.
        /// </summary>
        public readonly string IpAddress;
        /// <summary>
        /// the of the peer.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// the public key of the WireGuard client.
        /// </summary>
        public readonly string PublicKey;

        [OutputConstructor]
        private VPCRouterWireGuardPeer(
            string ipAddress,

            string name,

            string publicKey)
        {
            IpAddress = ipAddress;
            Name = name;
            PublicKey = publicKey;
        }
    }
}
