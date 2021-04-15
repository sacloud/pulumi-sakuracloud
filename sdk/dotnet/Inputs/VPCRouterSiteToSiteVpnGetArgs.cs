// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Sakuracloud.Inputs
{

    public sealed class VPCRouterSiteToSiteVpnGetArgs : Pulumi.ResourceArgs
    {
        [Input("localPrefixes", required: true)]
        private InputList<string>? _localPrefixes;

        /// <summary>
        /// A list of CIDR block of the network under the VPC Router.
        /// </summary>
        public InputList<string> LocalPrefixes
        {
            get => _localPrefixes ?? (_localPrefixes = new InputList<string>());
            set => _localPrefixes = value;
        }

        /// <summary>
        /// The IP address of the opposing appliance connected to the VPC Router.
        /// </summary>
        [Input("peer", required: true)]
        public Input<string> Peer { get; set; } = null!;

        /// <summary>
        /// The pre shared secret for the VPN. The length of this value must be in the range [`0`-`40`].
        /// </summary>
        [Input("preSharedSecret", required: true)]
        public Input<string> PreSharedSecret { get; set; } = null!;

        /// <summary>
        /// The id of the opposing appliance connected to the VPC Router. This is typically set same as value of `peer`.
        /// </summary>
        [Input("remoteId", required: true)]
        public Input<string> RemoteId { get; set; } = null!;

        [Input("routes", required: true)]
        private InputList<string>? _routes;

        /// <summary>
        /// A list of CIDR block of VPN connected networks.
        /// </summary>
        public InputList<string> Routes
        {
            get => _routes ?? (_routes = new InputList<string>());
            set => _routes = value;
        }

        public VPCRouterSiteToSiteVpnGetArgs()
        {
        }
    }
}
