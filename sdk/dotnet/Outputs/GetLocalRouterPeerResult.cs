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
    public sealed class GetLocalRouterPeerResult
    {
        /// <summary>
        /// The description of the LocalRouter.
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// The flag to enable the LocalRouter.
        /// </summary>
        public readonly bool Enabled;
        /// <summary>
        /// The ID of the peer LocalRouter.
        /// </summary>
        public readonly string PeerId;
        /// <summary>
        /// The secret key of the peer LocalRouter.
        /// </summary>
        public readonly string SecretKey;

        [OutputConstructor]
        private GetLocalRouterPeerResult(
            string description,

            bool enabled,

            string peerId,

            string secretKey)
        {
            Description = description;
            Enabled = enabled;
            PeerId = peerId;
            SecretKey = secretKey;
        }
    }
}