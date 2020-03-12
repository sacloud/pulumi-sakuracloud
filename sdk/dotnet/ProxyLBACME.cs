// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.SakuraCloud
{
    public partial class ProxyLBACME : Pulumi.CustomResource
    {
        /// <summary>
        /// The flag to accept the current Let's Encrypt terms of service(see: https://letsencrypt.org/repository/).
        /// This must be set `true` explicitly
        /// </summary>
        [Output("acceptTos")]
        public Output<bool> AcceptTos { get; private set; } = null!;

        [Output("certificates")]
        public Output<ImmutableArray<Outputs.ProxyLBACMECertificates>> Certificates { get; private set; } = null!;

        /// <summary>
        /// The FQDN used by ACME. This must set resolvable value
        /// </summary>
        [Output("commonName")]
        public Output<string> CommonName { get; private set; } = null!;

        /// <summary>
        /// The id of the ProxyLB that set ACME settings to
        /// </summary>
        [Output("proxylbId")]
        public Output<string> ProxylbId { get; private set; } = null!;

        /// <summary>
        /// The wait time in seconds. This typically used for waiting for a DNS propagation
        /// </summary>
        [Output("updateDelaySec")]
        public Output<int?> UpdateDelaySec { get; private set; } = null!;


        /// <summary>
        /// Create a ProxyLBACME resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ProxyLBACME(string name, ProxyLBACMEArgs args, CustomResourceOptions? options = null)
            : base("sakuracloud:index/proxyLBACME:ProxyLBACME", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private ProxyLBACME(string name, Input<string> id, ProxyLBACMEState? state = null, CustomResourceOptions? options = null)
            : base("sakuracloud:index/proxyLBACME:ProxyLBACME", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing ProxyLBACME resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ProxyLBACME Get(string name, Input<string> id, ProxyLBACMEState? state = null, CustomResourceOptions? options = null)
        {
            return new ProxyLBACME(name, id, state, options);
        }
    }

    public sealed class ProxyLBACMEArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The flag to accept the current Let's Encrypt terms of service(see: https://letsencrypt.org/repository/).
        /// This must be set `true` explicitly
        /// </summary>
        [Input("acceptTos", required: true)]
        public Input<bool> AcceptTos { get; set; } = null!;

        /// <summary>
        /// The FQDN used by ACME. This must set resolvable value
        /// </summary>
        [Input("commonName", required: true)]
        public Input<string> CommonName { get; set; } = null!;

        /// <summary>
        /// The id of the ProxyLB that set ACME settings to
        /// </summary>
        [Input("proxylbId", required: true)]
        public Input<string> ProxylbId { get; set; } = null!;

        /// <summary>
        /// The wait time in seconds. This typically used for waiting for a DNS propagation
        /// </summary>
        [Input("updateDelaySec")]
        public Input<int>? UpdateDelaySec { get; set; }

        public ProxyLBACMEArgs()
        {
        }
    }

    public sealed class ProxyLBACMEState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The flag to accept the current Let's Encrypt terms of service(see: https://letsencrypt.org/repository/).
        /// This must be set `true` explicitly
        /// </summary>
        [Input("acceptTos")]
        public Input<bool>? AcceptTos { get; set; }

        [Input("certificates")]
        private InputList<Inputs.ProxyLBACMECertificatesGetArgs>? _certificates;
        public InputList<Inputs.ProxyLBACMECertificatesGetArgs> Certificates
        {
            get => _certificates ?? (_certificates = new InputList<Inputs.ProxyLBACMECertificatesGetArgs>());
            set => _certificates = value;
        }

        /// <summary>
        /// The FQDN used by ACME. This must set resolvable value
        /// </summary>
        [Input("commonName")]
        public Input<string>? CommonName { get; set; }

        /// <summary>
        /// The id of the ProxyLB that set ACME settings to
        /// </summary>
        [Input("proxylbId")]
        public Input<string>? ProxylbId { get; set; }

        /// <summary>
        /// The wait time in seconds. This typically used for waiting for a DNS propagation
        /// </summary>
        [Input("updateDelaySec")]
        public Input<int>? UpdateDelaySec { get; set; }

        public ProxyLBACMEState()
        {
        }
    }

    namespace Inputs
    {

    public sealed class ProxyLBACMECertificatesAdditionalCertificatesGetArgs : Pulumi.ResourceArgs
    {
        [Input("intermediateCert")]
        public Input<string>? IntermediateCert { get; set; }

        [Input("privateKey")]
        public Input<string>? PrivateKey { get; set; }

        [Input("serverCert")]
        public Input<string>? ServerCert { get; set; }

        public ProxyLBACMECertificatesAdditionalCertificatesGetArgs()
        {
        }
    }

    public sealed class ProxyLBACMECertificatesGetArgs : Pulumi.ResourceArgs
    {
        [Input("additionalCertificates")]
        private InputList<ProxyLBACMECertificatesAdditionalCertificatesGetArgs>? _additionalCertificates;
        public InputList<ProxyLBACMECertificatesAdditionalCertificatesGetArgs> AdditionalCertificates
        {
            get => _additionalCertificates ?? (_additionalCertificates = new InputList<ProxyLBACMECertificatesAdditionalCertificatesGetArgs>());
            set => _additionalCertificates = value;
        }

        [Input("intermediateCert")]
        public Input<string>? IntermediateCert { get; set; }

        [Input("privateKey")]
        public Input<string>? PrivateKey { get; set; }

        [Input("serverCert")]
        public Input<string>? ServerCert { get; set; }

        public ProxyLBACMECertificatesGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class ProxyLBACMECertificates
    {
        public readonly ImmutableArray<ProxyLBACMECertificatesAdditionalCertificates> AdditionalCertificates;
        public readonly string IntermediateCert;
        public readonly string PrivateKey;
        public readonly string ServerCert;

        [OutputConstructor]
        private ProxyLBACMECertificates(
            ImmutableArray<ProxyLBACMECertificatesAdditionalCertificates> additionalCertificates,
            string intermediateCert,
            string privateKey,
            string serverCert)
        {
            AdditionalCertificates = additionalCertificates;
            IntermediateCert = intermediateCert;
            PrivateKey = privateKey;
            ServerCert = serverCert;
        }
    }

    [OutputType]
    public sealed class ProxyLBACMECertificatesAdditionalCertificates
    {
        public readonly string IntermediateCert;
        public readonly string PrivateKey;
        public readonly string ServerCert;

        [OutputConstructor]
        private ProxyLBACMECertificatesAdditionalCertificates(
            string intermediateCert,
            string privateKey,
            string serverCert)
        {
            IntermediateCert = intermediateCert;
            PrivateKey = privateKey;
            ServerCert = serverCert;
        }
    }
    }
}
