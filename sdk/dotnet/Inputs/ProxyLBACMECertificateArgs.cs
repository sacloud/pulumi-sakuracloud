// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Sakuracloud.Inputs
{

    public sealed class ProxyLBACMECertificateArgs : Pulumi.ResourceArgs
    {
        [Input("additionalCertificates")]
        private InputList<Inputs.ProxyLBACMECertificateAdditionalCertificateArgs>? _additionalCertificates;

        /// <summary>
        /// A list of `additional_certificate` blocks as defined below.
        /// </summary>
        public InputList<Inputs.ProxyLBACMECertificateAdditionalCertificateArgs> AdditionalCertificates
        {
            get => _additionalCertificates ?? (_additionalCertificates = new InputList<Inputs.ProxyLBACMECertificateAdditionalCertificateArgs>());
            set => _additionalCertificates = value;
        }

        /// <summary>
        /// The intermediate certificate for a server.
        /// </summary>
        [Input("intermediateCert")]
        public Input<string>? IntermediateCert { get; set; }

        /// <summary>
        /// The private key for a server.
        /// </summary>
        [Input("privateKey")]
        public Input<string>? PrivateKey { get; set; }

        /// <summary>
        /// The certificate for a server.
        /// </summary>
        [Input("serverCert")]
        public Input<string>? ServerCert { get; set; }

        public ProxyLBACMECertificateArgs()
        {
        }
    }
}