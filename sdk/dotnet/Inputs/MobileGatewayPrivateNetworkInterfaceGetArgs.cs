// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Sakuracloud.Inputs
{

    public sealed class MobileGatewayPrivateNetworkInterfaceGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The IP address to assign to the MobileGateway.
        /// </summary>
        [Input("ipAddress", required: true)]
        public Input<string> IpAddress { get; set; } = null!;

        /// <summary>
        /// The bit length of the subnet to assign to the MobileGateway. This must be in the range [`8`-`29`].
        /// </summary>
        [Input("netmask", required: true)]
        public Input<int> Netmask { get; set; } = null!;

        /// <summary>
        /// The id of the switch to which the MobileGateway connects.
        /// </summary>
        [Input("switchId", required: true)]
        public Input<string> SwitchId { get; set; } = null!;

        public MobileGatewayPrivateNetworkInterfaceGetArgs()
        {
        }
    }
}
