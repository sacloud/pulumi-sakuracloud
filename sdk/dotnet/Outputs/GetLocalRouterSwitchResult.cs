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
    public sealed class GetLocalRouterSwitchResult
    {
        /// <summary>
        /// The category name of connected services (e.g. `cloud`, `vps`).
        /// </summary>
        public readonly string Category;
        /// <summary>
        /// The resource ID of the Switch.
        /// </summary>
        public readonly string Code;
        /// <summary>
        /// The id of the Zone.
        /// </summary>
        public readonly string ZoneId;

        [OutputConstructor]
        private GetLocalRouterSwitchResult(
            string category,

            string code,

            string zoneId)
        {
            Category = category;
            Code = code;
            ZoneId = zoneId;
        }
    }
}
