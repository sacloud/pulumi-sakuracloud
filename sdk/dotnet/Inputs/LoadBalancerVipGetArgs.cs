// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Sakuracloud.Inputs
{

    public sealed class LoadBalancerVipGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The interval in seconds between checks. This must be in the range [`10`-`2147483647`].
        /// </summary>
        [Input("delayLoop")]
        public Input<int>? DelayLoop { get; set; }

        /// <summary>
        /// The description of the VIP. The length of this value must be in the range [`1`-`512`].
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The target port number for load-balancing. This must be in the range [`1`-`65535`].
        /// </summary>
        [Input("port", required: true)]
        public Input<int> Port { get; set; } = null!;

        [Input("servers")]
        private InputList<Inputs.LoadBalancerVipServerGetArgs>? _servers;

        /// <summary>
        /// One or more `server` blocks as defined below.
        /// </summary>
        public InputList<Inputs.LoadBalancerVipServerGetArgs> Servers
        {
            get => _servers ?? (_servers = new InputList<Inputs.LoadBalancerVipServerGetArgs>());
            set => _servers = value;
        }

        /// <summary>
        /// The IP address of the SorryServer. This will be used when all servers under this VIP are down.
        /// </summary>
        [Input("sorryServer")]
        public Input<string>? SorryServer { get; set; }

        /// <summary>
        /// The virtual IP address.
        /// </summary>
        [Input("vip", required: true)]
        public Input<string> Vip { get; set; } = null!;

        public LoadBalancerVipGetArgs()
        {
        }
    }
}