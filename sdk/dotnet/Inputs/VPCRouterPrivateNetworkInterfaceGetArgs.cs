// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Sakuracloud.Inputs
{

    public sealed class VPCRouterPrivateNetworkInterfaceGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The index of the network interface. This must be in the range [`1`-`7`].
        /// </summary>
        [Input("index", required: true)]
        public Input<int> Index { get; set; } = null!;

        [Input("ipAddresses", required: true)]
        private InputList<string>? _ipAddresses;

        /// <summary>
        /// A list of ip address to assign to the network interface. This is required only one value when `plan` is `standard`, two values otherwise.
        /// </summary>
        public InputList<string> IpAddresses
        {
            get => _ipAddresses ?? (_ipAddresses = new InputList<string>());
            set => _ipAddresses = value;
        }

        /// <summary>
        /// The bit length of the subnet to assign to the network interface.
        /// </summary>
        [Input("netmask", required: true)]
        public Input<int> Netmask { get; set; } = null!;

        /// <summary>
        /// The id of the connected switch.
        /// </summary>
        [Input("switchId", required: true)]
        public Input<string> SwitchId { get; set; } = null!;

        /// <summary>
        /// The virtual IP address to assign to the network interface. This is only required when `plan` is not `standard`.
        /// </summary>
        [Input("vip")]
        public Input<string>? Vip { get; set; }

        public VPCRouterPrivateNetworkInterfaceGetArgs()
        {
        }
    }
}
