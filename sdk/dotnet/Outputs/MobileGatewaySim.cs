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
    public sealed class MobileGatewaySim
    {
        /// <summary>
        /// The IP address to assign to the SIM.
        /// </summary>
        public readonly string IpAddress;
        /// <summary>
        /// The id of the Switch connected to the MobileGateway.
        /// </summary>
        public readonly string SimId;

        [OutputConstructor]
        private MobileGatewaySim(
            string ipAddress,

            string simId)
        {
            IpAddress = ipAddress;
            SimId = simId;
        }
    }
}
