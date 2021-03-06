// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Sakuracloud.Inputs
{

    public sealed class LocalRouterPeerGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The description of the LocalRouter. The length of this value must be in the range [`1`-`512`].
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The flag to enable the LocalRouter.
        /// </summary>
        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        /// <summary>
        /// The ID of the peer LocalRouter.
        /// </summary>
        [Input("peerId", required: true)]
        public Input<string> PeerId { get; set; } = null!;

        /// <summary>
        /// The secret key of the peer LocalRouter.
        /// </summary>
        [Input("secretKey", required: true)]
        public Input<string> SecretKey { get; set; } = null!;

        public LocalRouterPeerGetArgs()
        {
        }
    }
}
