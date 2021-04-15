// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Sakuracloud.Inputs
{

    public sealed class ServerNetworkInterfaceArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The MAC address.
        /// </summary>
        [Input("macAddress")]
        public Input<string>? MacAddress { get; set; }

        /// <summary>
        /// The id of the packet filter to attach to the network interface.
        /// </summary>
        [Input("packetFilterId")]
        public Input<string>? PacketFilterId { get; set; }

        /// <summary>
        /// The upstream type or upstream switch id. This must be one of [`shared`/`disconnect`/`&lt;switch id&gt;`].
        /// </summary>
        [Input("upstream", required: true)]
        public Input<string> Upstream { get; set; } = null!;

        /// <summary>
        /// The IP address for only display. This value doesn't affect actual NIC settings.
        /// </summary>
        [Input("userIpAddress")]
        public Input<string>? UserIpAddress { get; set; }

        public ServerNetworkInterfaceArgs()
        {
        }
    }
}