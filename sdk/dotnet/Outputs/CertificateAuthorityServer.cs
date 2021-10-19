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
    public sealed class CertificateAuthorityServer
    {
        /// <summary>
        /// The body of the CA's certificate in PEM format.
        /// </summary>
        public readonly string? Certificate;
        /// <summary>
        /// Input for issuing a certificate.
        /// </summary>
        public readonly string? Csr;
        /// <summary>
        /// Flag to suspend/hold the certificate.
        /// </summary>
        public readonly bool? Hold;
        /// <summary>
        /// The id of the certificate.
        /// </summary>
        public readonly string? Id;
        /// <summary>
        /// Current state of the certificate.
        /// </summary>
        public readonly string? IssueState;
        /// <summary>
        /// The date on which the certificate validity period ends, in RFC3339 format.
        /// </summary>
        public readonly string? NotAfter;
        /// <summary>
        /// The date on which the certificate validity period begins, in RFC3339 format.
        /// </summary>
        public readonly string? NotBefore;
        /// <summary>
        /// Input for issuing a certificate.
        /// </summary>
        public readonly string? PublicKey;
        /// <summary>
        /// The body of the CA's certificate in PEM format.
        /// </summary>
        public readonly string? SerialNumber;
        /// <summary>
        /// A `subject` block as defined below.
        /// </summary>
        public readonly Outputs.CertificateAuthorityServerSubject Subject;
        /// <summary>
        /// .
        /// </summary>
        public readonly ImmutableArray<string> SubjectAlternativeNames;
        /// <summary>
        /// The number of hours after initial issuing that the certificate will become invalid.
        /// </summary>
        public readonly int ValidityPeriodHours;

        [OutputConstructor]
        private CertificateAuthorityServer(
            string? certificate,

            string? csr,

            bool? hold,

            string? id,

            string? issueState,

            string? notAfter,

            string? notBefore,

            string? publicKey,

            string? serialNumber,

            Outputs.CertificateAuthorityServerSubject subject,

            ImmutableArray<string> subjectAlternativeNames,

            int validityPeriodHours)
        {
            Certificate = certificate;
            Csr = csr;
            Hold = hold;
            Id = id;
            IssueState = issueState;
            NotAfter = notAfter;
            NotBefore = notBefore;
            PublicKey = publicKey;
            SerialNumber = serialNumber;
            Subject = subject;
            SubjectAlternativeNames = subjectAlternativeNames;
            ValidityPeriodHours = validityPeriodHours;
        }
    }
}
