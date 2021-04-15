// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Sakuracloud
{
    public static class GetWebAccel
    {
        /// <summary>
        /// Get information about an existing sakuracloud_webaccel.
        /// </summary>
        public static Task<GetWebAccelResult> InvokeAsync(GetWebAccelArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetWebAccelResult>("sakuracloud:index/getWebAccel:getWebAccel", args ?? new GetWebAccelArgs(), options.WithVersion());
    }


    public sealed class GetWebAccelArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// .
        /// </summary>
        [Input("domain")]
        public string? Domain { get; set; }

        /// <summary>
        /// .
        /// </summary>
        [Input("name")]
        public string? Name { get; set; }

        public GetWebAccelArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetWebAccelResult
    {
        /// <summary>
        /// .
        /// </summary>
        public readonly string CnameRecordValue;
        public readonly string Domain;
        /// <summary>
        /// .
        /// </summary>
        public readonly string DomainType;
        /// <summary>
        /// .
        /// </summary>
        public readonly bool HasCertificate;
        /// <summary>
        /// .
        /// </summary>
        public readonly string HostHeader;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string Name;
        /// <summary>
        /// .
        /// </summary>
        public readonly string Origin;
        /// <summary>
        /// .
        /// </summary>
        public readonly string SiteId;
        /// <summary>
        /// .
        /// </summary>
        public readonly string Status;
        /// <summary>
        /// .
        /// </summary>
        public readonly string Subdomain;
        /// <summary>
        /// .
        /// </summary>
        public readonly string TxtRecordValue;

        [OutputConstructor]
        private GetWebAccelResult(
            string cnameRecordValue,

            string domain,

            string domainType,

            bool hasCertificate,

            string hostHeader,

            string id,

            string name,

            string origin,

            string siteId,

            string status,

            string subdomain,

            string txtRecordValue)
        {
            CnameRecordValue = cnameRecordValue;
            Domain = domain;
            DomainType = domainType;
            HasCertificate = hasCertificate;
            HostHeader = hostHeader;
            Id = id;
            Name = name;
            Origin = origin;
            SiteId = siteId;
            Status = status;
            Subdomain = subdomain;
            TxtRecordValue = txtRecordValue;
        }
    }
}