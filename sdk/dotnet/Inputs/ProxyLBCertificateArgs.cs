// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Sakuracloud.Inputs
{

    public sealed class ProxyLBCertificateArgs : Pulumi.ResourceArgs
    {
        [Input("additionalCertificates")]
        private InputList<Inputs.ProxyLBCertificateAdditionalCertificateArgs>? _additionalCertificates;

        /// <summary>
        /// One or more `additional_certificate` blocks as defined below.
        /// </summary>
        public InputList<Inputs.ProxyLBCertificateAdditionalCertificateArgs> AdditionalCertificates
        {
            get => _additionalCertificates ?? (_additionalCertificates = new InputList<Inputs.ProxyLBCertificateAdditionalCertificateArgs>());
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

        public ProxyLBCertificateArgs()
        {
        }
    }
}