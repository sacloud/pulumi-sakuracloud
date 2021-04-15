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
    public sealed class VPCRouterL2tp
    {
        /// <summary>
        /// The pre shared secret for the VPN. The length of this value must be in the range [`0`-`40`].
        /// </summary>
        public readonly string PreSharedSecret;
        /// <summary>
        /// The start value of IP address range to assign to DHCP client.
        /// </summary>
        public readonly string RangeStart;
        /// <summary>
        /// The end value of IP address range to assign to DHCP client.
        /// </summary>
        public readonly string RangeStop;

        [OutputConstructor]
        private VPCRouterL2tp(
            string preSharedSecret,

            string rangeStart,

            string rangeStop)
        {
            PreSharedSecret = preSharedSecret;
            RangeStart = rangeStart;
            RangeStop = rangeStop;
        }
    }
}