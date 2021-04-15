// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Sakuracloud.Inputs
{

    public sealed class VPCRouterL2tpArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The pre shared secret for the VPN. The length of this value must be in the range [`0`-`40`].
        /// </summary>
        [Input("preSharedSecret", required: true)]
        public Input<string> PreSharedSecret { get; set; } = null!;

        /// <summary>
        /// The start value of IP address range to assign to DHCP client.
        /// </summary>
        [Input("rangeStart", required: true)]
        public Input<string> RangeStart { get; set; } = null!;

        /// <summary>
        /// The end value of IP address range to assign to DHCP client.
        /// </summary>
        [Input("rangeStop", required: true)]
        public Input<string> RangeStop { get; set; } = null!;

        public VPCRouterL2tpArgs()
        {
        }
    }
}
