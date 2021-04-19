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
    public sealed class GetProxyLBRuleResult
    {
        /// <summary>
        /// The name of load balancing group. This is used when using rule-based load balancing.
        /// </summary>
        public readonly string Group;
        /// <summary>
        /// The value of HTTP host header that is used as condition of rule-based balancing.
        /// </summary>
        public readonly string Host;
        /// <summary>
        /// The request path that is used as condition of rule-based balancing.
        /// </summary>
        public readonly string Path;

        [OutputConstructor]
        private GetProxyLBRuleResult(
            string group,

            string host,

            string path)
        {
            Group = group;
            Host = host;
            Path = path;
        }
    }
}
