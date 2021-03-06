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
    public sealed class VPCRouterStaticNat
    {
        /// <summary>
        /// The description of the static nat. The length of this value must be in the range [`0`-`512`].
        /// </summary>
        public readonly string? Description;
        /// <summary>
        /// The private IP address used for the static NAT.
        /// </summary>
        public readonly string PrivateIp;
        /// <summary>
        /// The public IP address used for the static NAT.
        /// </summary>
        public readonly string PublicIp;

        [OutputConstructor]
        private VPCRouterStaticNat(
            string? description,

            string privateIp,

            string publicIp)
        {
            Description = description;
            PrivateIp = privateIp;
            PublicIp = publicIp;
        }
    }
}
