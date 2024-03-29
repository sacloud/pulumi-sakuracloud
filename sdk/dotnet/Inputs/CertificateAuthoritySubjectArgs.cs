// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Sakuracloud.Inputs
{

    public sealed class CertificateAuthoritySubjectArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// .
        /// </summary>
        [Input("commonName", required: true)]
        public Input<string> CommonName { get; set; } = null!;

        /// <summary>
        /// .
        /// </summary>
        [Input("country", required: true)]
        public Input<string> Country { get; set; } = null!;

        /// <summary>
        /// .
        /// </summary>
        [Input("organization", required: true)]
        public Input<string> Organization { get; set; } = null!;

        [Input("organizationUnits")]
        private InputList<string>? _organizationUnits;

        /// <summary>
        /// .
        /// </summary>
        public InputList<string> OrganizationUnits
        {
            get => _organizationUnits ?? (_organizationUnits = new InputList<string>());
            set => _organizationUnits = value;
        }

        public CertificateAuthoritySubjectArgs()
        {
        }
    }
}
