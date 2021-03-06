// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Sakuracloud.Inputs
{

    public sealed class DatabaseNetworkInterfaceArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The IP address of the gateway used by Database.
        /// </summary>
        [Input("gateway", required: true)]
        public Input<string> Gateway { get; set; } = null!;

        /// <summary>
        /// The IP address to assign to the Database.
        /// </summary>
        [Input("ipAddress", required: true)]
        public Input<string> IpAddress { get; set; } = null!;

        /// <summary>
        /// The bit length of the subnet to assign to the Database. This must be in the range [`8`-`29`].
        /// </summary>
        [Input("netmask", required: true)]
        public Input<int> Netmask { get; set; } = null!;

        /// <summary>
        /// The number of the listening port. This must be in the range [`1024`-`65535`].
        /// </summary>
        [Input("port")]
        public Input<int>? Port { get; set; }

        [Input("sourceRanges")]
        private InputList<string>? _sourceRanges;

        /// <summary>
        /// The range of source IP addresses that allow to access to the Database via network.
        /// </summary>
        public InputList<string> SourceRanges
        {
            get => _sourceRanges ?? (_sourceRanges = new InputList<string>());
            set => _sourceRanges = value;
        }

        /// <summary>
        /// The id of the switch to which the Database connects.
        /// </summary>
        [Input("switchId", required: true)]
        public Input<string> SwitchId { get; set; } = null!;

        public DatabaseNetworkInterfaceArgs()
        {
        }
    }
}
