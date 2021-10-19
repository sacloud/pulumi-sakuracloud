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
        /// The type of action to be performed when requests matches the rule. This will be one of [`forward`/`redirect`/`fixed`].
        /// </summary>
        public readonly string Action;
        /// <summary>
        /// Content-Type header value for fixed response sent when requests matches the rule. This will be one of [`text/plain`/`text/html`/`application/javascript`/`application/json`].
        /// </summary>
        public readonly string FixedContentType;
        /// <summary>
        /// Content body for fixed response sent when requests matches the rule.
        /// </summary>
        public readonly string FixedMessageBody;
        /// <summary>
        /// HTTP status code for fixed response sent when requests matches the rule. This will be one of [`200`/`403`/`503`].
        /// </summary>
        public readonly string FixedStatusCode;
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
        /// <summary>
        /// The URL to redirect to when the request matches the rule. see https://manual.sakura.ad.jp/cloud/appliance/enhanced-lb/#enhanced-lb-rule for details.
        /// </summary>
        public readonly string RedirectLocation;
        /// <summary>
        /// HTTP status code for redirects sent when requests matches the rule. This will be one of [`301`/`302`].
        /// </summary>
        public readonly string RedirectStatusCode;

        [OutputConstructor]
        private GetProxyLBRuleResult(
            string action,

            string fixedContentType,

            string fixedMessageBody,

            string fixedStatusCode,

            string group,

            string host,

            string path,

            string redirectLocation,

            string redirectStatusCode)
        {
            Action = action;
            FixedContentType = fixedContentType;
            FixedMessageBody = fixedMessageBody;
            FixedStatusCode = fixedStatusCode;
            Group = group;
            Host = host;
            Path = path;
            RedirectLocation = redirectLocation;
            RedirectStatusCode = redirectStatusCode;
        }
    }
}
