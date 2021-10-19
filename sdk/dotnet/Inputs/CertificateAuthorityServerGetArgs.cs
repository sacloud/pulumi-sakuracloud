// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Sakuracloud.Inputs
{

    public sealed class CertificateAuthorityServerGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The body of the CA's certificate in PEM format.
        /// </summary>
        [Input("certificate")]
        public Input<string>? Certificate { get; set; }

        /// <summary>
        /// Input for issuing a certificate.
        /// </summary>
        [Input("csr")]
        public Input<string>? Csr { get; set; }

        /// <summary>
        /// Flag to suspend/hold the certificate.
        /// </summary>
        [Input("hold")]
        public Input<bool>? Hold { get; set; }

        /// <summary>
        /// The id of the certificate.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// Current state of the certificate.
        /// </summary>
        [Input("issueState")]
        public Input<string>? IssueState { get; set; }

        /// <summary>
        /// The date on which the certificate validity period ends, in RFC3339 format.
        /// </summary>
        [Input("notAfter")]
        public Input<string>? NotAfter { get; set; }

        /// <summary>
        /// The date on which the certificate validity period begins, in RFC3339 format.
        /// </summary>
        [Input("notBefore")]
        public Input<string>? NotBefore { get; set; }

        /// <summary>
        /// Input for issuing a certificate.
        /// </summary>
        [Input("publicKey")]
        public Input<string>? PublicKey { get; set; }

        /// <summary>
        /// The body of the CA's certificate in PEM format.
        /// </summary>
        [Input("serialNumber")]
        public Input<string>? SerialNumber { get; set; }

        /// <summary>
        /// A `subject` block as defined below.
        /// </summary>
        [Input("subject", required: true)]
        public Input<Inputs.CertificateAuthorityServerSubjectGetArgs> Subject { get; set; } = null!;

        [Input("subjectAlternativeNames")]
        private InputList<string>? _subjectAlternativeNames;

        /// <summary>
        /// .
        /// </summary>
        public InputList<string> SubjectAlternativeNames
        {
            get => _subjectAlternativeNames ?? (_subjectAlternativeNames = new InputList<string>());
            set => _subjectAlternativeNames = value;
        }

        /// <summary>
        /// The number of hours after initial issuing that the certificate will become invalid.
        /// </summary>
        [Input("validityPeriodHours", required: true)]
        public Input<int> ValidityPeriodHours { get; set; } = null!;

        public CertificateAuthorityServerGetArgs()
        {
        }
    }
}
