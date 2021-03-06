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
    public sealed class ProxyLBBindPort
    {
        /// <summary>
        /// The number of listening port.
        /// </summary>
        public readonly int? Port;
        /// <summary>
        /// The proxy mode. This must be one of [`http`/`https`/`tcp`].
        /// </summary>
        public readonly string ProxyMode;
        /// <summary>
        /// The flag to enable redirection from http to https. This flag is used only when `proxy_mode` is `http`.
        /// </summary>
        public readonly bool? RedirectToHttps;
        /// <summary>
        /// One or more `response_header` blocks as defined below.
        /// </summary>
        public readonly ImmutableArray<Outputs.ProxyLBBindPortResponseHeader> ResponseHeaders;
        /// <summary>
        /// The flag to enable HTTP/2. This flag is used only when `proxy_mode` is `https`.
        /// </summary>
        public readonly bool? SupportHttp2;

        [OutputConstructor]
        private ProxyLBBindPort(
            int? port,

            string proxyMode,

            bool? redirectToHttps,

            ImmutableArray<Outputs.ProxyLBBindPortResponseHeader> responseHeaders,

            bool? supportHttp2)
        {
            Port = port;
            ProxyMode = proxyMode;
            RedirectToHttps = redirectToHttps;
            ResponseHeaders = responseHeaders;
            SupportHttp2 = supportHttp2;
        }
    }
}
