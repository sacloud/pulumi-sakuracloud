// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Sakuracloud.Inputs
{

    public sealed class VPCRouterPublicNetworkInterfaceArgs : Pulumi.ResourceArgs
    {
        [Input("aliases")]
        private InputList<string>? _aliases;

        /// <summary>
        /// A list of ip alias to assign to the VPC Router. This can only be specified if `plan` is not `standard`.
        /// </summary>
        public InputList<string> Aliases
        {
            get => _aliases ?? (_aliases = new InputList<string>());
            set => _aliases = value;
        }

        [Input("ipAddresses")]
        private InputList<string>? _ipAddresses;

        /// <summary>
        /// The list of the IP address to assign to the VPC Router. This is required only one value when `plan` is `standard`, two values otherwise.
        /// </summary>
        public InputList<string> IpAddresses
        {
            get => _ipAddresses ?? (_ipAddresses = new InputList<string>());
            set => _ipAddresses = value;
        }

        /// <summary>
        /// The id of the switch to connect. This is only required when when `plan` is not `standard`.
        /// </summary>
        [Input("switchId")]
        public Input<string>? SwitchId { get; set; }

        /// <summary>
        /// The virtual IP address of the VPC Router. This is only required when `plan` is not `standard`.
        /// </summary>
        [Input("vip")]
        public Input<string>? Vip { get; set; }

        /// <summary>
        /// The Virtual Router Identifier. This is only required when `plan` is not `standard`.
        /// </summary>
        [Input("vrid")]
        public Input<int>? Vrid { get; set; }

        public VPCRouterPublicNetworkInterfaceArgs()
        {
        }
    }
}