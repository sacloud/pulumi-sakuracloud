// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Sakuracloud.Inputs
{

    public sealed class LocalRouterNetworkInterfaceGetArgs : Pulumi.ResourceArgs
    {
        [Input("ipAddresses", required: true)]
        private InputList<string>? _ipAddresses;

        /// <summary>
        /// A list of IP address to assign to the LocalRouter.
        /// </summary>
        public InputList<string> IpAddresses
        {
            get => _ipAddresses ?? (_ipAddresses = new InputList<string>());
            set => _ipAddresses = value;
        }

        /// <summary>
        /// The bit length of the subnet assigned to the LocalRouter. This must be in the range [`8`-`29`].
        /// </summary>
        [Input("netmask", required: true)]
        public Input<int> Netmask { get; set; } = null!;

        /// <summary>
        /// The virtual IP address.
        /// </summary>
        [Input("vip", required: true)]
        public Input<string> Vip { get; set; } = null!;

        /// <summary>
        /// The Virtual Router Identifier.
        /// </summary>
        [Input("vrid", required: true)]
        public Input<int> Vrid { get; set; } = null!;

        public LocalRouterNetworkInterfaceGetArgs()
        {
        }
    }
}
