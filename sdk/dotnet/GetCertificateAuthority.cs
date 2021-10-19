// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Sakuracloud
{
    public static class GetCertificateAuthority
    {
        /// <summary>
        /// Get information about an existing sakuracloud_certificate_authority.
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Sakuracloud = Pulumi.Sakuracloud;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var foobar = Output.Create(Sakuracloud.GetCertificateAuthority.InvokeAsync(new Sakuracloud.GetCertificateAuthorityArgs
        ///         {
        ///             Filter = new Sakuracloud.Inputs.GetCertificateAuthorityFilterArgs
        ///             {
        ///                 Names = 
        ///                 {
        ///                     "foobar",
        ///                 },
        ///             },
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetCertificateAuthorityResult> InvokeAsync(GetCertificateAuthorityArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetCertificateAuthorityResult>("sakuracloud:index/getCertificateAuthority:getCertificateAuthority", args ?? new GetCertificateAuthorityArgs(), options.WithVersion());
    }


    public sealed class GetCertificateAuthorityArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// One or more values used for filtering, as defined below.
        /// </summary>
        [Input("filter")]
        public Inputs.GetCertificateAuthorityFilterArgs? Filter { get; set; }

        public GetCertificateAuthorityArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetCertificateAuthorityResult
    {
        /// <summary>
        /// The body of the CA's certificate in PEM format.
        /// </summary>
        public readonly string Certificate;
        /// <summary>
        /// A list of `client` blocks as defined below.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetCertificateAuthorityClientResult> Clients;
        /// <summary>
        /// The URL of the CRL.
        /// </summary>
        public readonly string CrlUrl;
        /// <summary>
        /// The description of the CertificateAuthority.
        /// </summary>
        public readonly string Description;
        public readonly Outputs.GetCertificateAuthorityFilterResult? Filter;
        /// <summary>
        /// The icon id attached to the CertificateAuthority.
        /// </summary>
        public readonly string IconId;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// The name of the CertificateAuthority.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// The date on which the certificate validity period ends, in RFC3339 format.
        /// </summary>
        public readonly string NotAfter;
        /// <summary>
        /// The date on which the certificate validity period begins, in RFC3339 format.
        /// </summary>
        public readonly string NotBefore;
        /// <summary>
        /// The body of the CA's certificate in PEM format.
        /// </summary>
        public readonly string SerialNumber;
        /// <summary>
        /// A list of `server` blocks as defined below.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetCertificateAuthorityServerResult> Servers;
        /// <summary>
        /// .
        /// </summary>
        public readonly string SubjectString;
        /// <summary>
        /// Any tags assigned to the CertificateAuthority.
        /// </summary>
        public readonly ImmutableArray<string> Tags;

        [OutputConstructor]
        private GetCertificateAuthorityResult(
            string certificate,

            ImmutableArray<Outputs.GetCertificateAuthorityClientResult> clients,

            string crlUrl,

            string description,

            Outputs.GetCertificateAuthorityFilterResult? filter,

            string iconId,

            string id,

            string name,

            string notAfter,

            string notBefore,

            string serialNumber,

            ImmutableArray<Outputs.GetCertificateAuthorityServerResult> servers,

            string subjectString,

            ImmutableArray<string> tags)
        {
            Certificate = certificate;
            Clients = clients;
            CrlUrl = crlUrl;
            Description = description;
            Filter = filter;
            IconId = iconId;
            Id = id;
            Name = name;
            NotAfter = notAfter;
            NotBefore = notBefore;
            SerialNumber = serialNumber;
            Servers = servers;
            SubjectString = subjectString;
            Tags = tags;
        }
    }
}