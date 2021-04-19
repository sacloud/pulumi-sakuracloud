// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Sakuracloud.Inputs
{

    public sealed class ProxyLBSorryServerGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The IP address of the SorryServer. This will be used when all servers are down.
        /// </summary>
        [Input("ipAddress", required: true)]
        public Input<string> IpAddress { get; set; } = null!;

        /// <summary>
        /// The port number of the SorryServer. This will be used when all servers are down.
        /// </summary>
        [Input("port")]
        public Input<int>? Port { get; set; }

        public ProxyLBSorryServerGetArgs()
        {
        }
    }
}
