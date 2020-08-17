// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.SakuraCloud
{
    public partial class ProxyLB : Pulumi.CustomResource
    {
        [Output("bindPorts")]
        public Output<ImmutableArray<Outputs.ProxyLBBindPorts>> BindPorts { get; private set; } = null!;

        [Output("certificate")]
        public Output<Outputs.ProxyLBCertificate> Certificate { get; private set; } = null!;

        /// <summary>
        /// The description of the ProxyLB. The length of this value must be in the range [`1`-`512`]
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// The FQDN for accessing to the ProxyLB. This is typically used as value of CNAME record
        /// </summary>
        [Output("fqdn")]
        public Output<string> Fqdn { get; private set; } = null!;

        [Output("healthCheck")]
        public Output<Outputs.ProxyLBHealthCheck> HealthCheck { get; private set; } = null!;

        /// <summary>
        /// The icon id to attach to the ProxyLB
        /// </summary>
        [Output("iconId")]
        public Output<string?> IconId { get; private set; } = null!;

        /// <summary>
        /// The name of the ProxyLB. The length of this value must be in the range [`1`-`64`]
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The plan name of the ProxyLB. This must be one of [`100`/`500`/`1000`/`5000`/`10000`/`50000`/`100000`]
        /// </summary>
        [Output("plan")]
        public Output<int?> Plan { get; private set; } = null!;

        /// <summary>
        /// A list of CIDR block used by the ProxyLB to access the server
        /// </summary>
        [Output("proxyNetworks")]
        public Output<ImmutableArray<string>> ProxyNetworks { get; private set; } = null!;

        /// <summary>
        /// The name of region that the proxy LB is in. This must be one of [`tk1`/`is1`/`anycast`]
        /// </summary>
        [Output("region")]
        public Output<string?> Region { get; private set; } = null!;

        [Output("rules")]
        public Output<ImmutableArray<Outputs.ProxyLBRules>> Rules { get; private set; } = null!;

        [Output("servers")]
        public Output<ImmutableArray<Outputs.ProxyLBServers>> Servers { get; private set; } = null!;

        [Output("sorryServer")]
        public Output<Outputs.ProxyLBSorryServer?> SorryServer { get; private set; } = null!;

        /// <summary>
        /// The flag to enable sticky session
        /// </summary>
        [Output("stickySession")]
        public Output<bool?> StickySession { get; private set; } = null!;

        /// <summary>
        /// Any tags to assign to the ProxyLB
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<string>> Tags { get; private set; } = null!;

        /// <summary>
        /// The timeout duration in seconds
        /// </summary>
        [Output("timeout")]
        public Output<int?> Timeout { get; private set; } = null!;

        /// <summary>
        /// The virtual IP address assigned to the ProxyLB
        /// </summary>
        [Output("vip")]
        public Output<string> Vip { get; private set; } = null!;

        /// <summary>
        /// The flag to enable VIP fail-over
        /// </summary>
        [Output("vipFailover")]
        public Output<bool?> VipFailover { get; private set; } = null!;


        /// <summary>
        /// Create a ProxyLB resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ProxyLB(string name, ProxyLBArgs args, CustomResourceOptions? options = null)
            : base("sakuracloud:index/proxyLB:ProxyLB", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private ProxyLB(string name, Input<string> id, ProxyLBState? state = null, CustomResourceOptions? options = null)
            : base("sakuracloud:index/proxyLB:ProxyLB", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing ProxyLB resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ProxyLB Get(string name, Input<string> id, ProxyLBState? state = null, CustomResourceOptions? options = null)
        {
            return new ProxyLB(name, id, state, options);
        }
    }

    public sealed class ProxyLBArgs : Pulumi.ResourceArgs
    {
        [Input("bindPorts", required: true)]
        private InputList<Inputs.ProxyLBBindPortsArgs>? _bindPorts;
        public InputList<Inputs.ProxyLBBindPortsArgs> BindPorts
        {
            get => _bindPorts ?? (_bindPorts = new InputList<Inputs.ProxyLBBindPortsArgs>());
            set => _bindPorts = value;
        }

        [Input("certificate")]
        public Input<Inputs.ProxyLBCertificateArgs>? Certificate { get; set; }

        /// <summary>
        /// The description of the ProxyLB. The length of this value must be in the range [`1`-`512`]
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("healthCheck", required: true)]
        public Input<Inputs.ProxyLBHealthCheckArgs> HealthCheck { get; set; } = null!;

        /// <summary>
        /// The icon id to attach to the ProxyLB
        /// </summary>
        [Input("iconId")]
        public Input<string>? IconId { get; set; }

        /// <summary>
        /// The name of the ProxyLB. The length of this value must be in the range [`1`-`64`]
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The plan name of the ProxyLB. This must be one of [`100`/`500`/`1000`/`5000`/`10000`/`50000`/`100000`]
        /// </summary>
        [Input("plan")]
        public Input<int>? Plan { get; set; }

        /// <summary>
        /// The name of region that the proxy LB is in. This must be one of [`tk1`/`is1`/`anycast`]
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        [Input("rules")]
        private InputList<Inputs.ProxyLBRulesArgs>? _rules;
        public InputList<Inputs.ProxyLBRulesArgs> Rules
        {
            get => _rules ?? (_rules = new InputList<Inputs.ProxyLBRulesArgs>());
            set => _rules = value;
        }

        [Input("servers")]
        private InputList<Inputs.ProxyLBServersArgs>? _servers;
        public InputList<Inputs.ProxyLBServersArgs> Servers
        {
            get => _servers ?? (_servers = new InputList<Inputs.ProxyLBServersArgs>());
            set => _servers = value;
        }

        [Input("sorryServer")]
        public Input<Inputs.ProxyLBSorryServerArgs>? SorryServer { get; set; }

        /// <summary>
        /// The flag to enable sticky session
        /// </summary>
        [Input("stickySession")]
        public Input<bool>? StickySession { get; set; }

        [Input("tags")]
        private InputList<string>? _tags;

        /// <summary>
        /// Any tags to assign to the ProxyLB
        /// </summary>
        public InputList<string> Tags
        {
            get => _tags ?? (_tags = new InputList<string>());
            set => _tags = value;
        }

        /// <summary>
        /// The timeout duration in seconds
        /// </summary>
        [Input("timeout")]
        public Input<int>? Timeout { get; set; }

        /// <summary>
        /// The flag to enable VIP fail-over
        /// </summary>
        [Input("vipFailover")]
        public Input<bool>? VipFailover { get; set; }

        public ProxyLBArgs()
        {
        }
    }

    public sealed class ProxyLBState : Pulumi.ResourceArgs
    {
        [Input("bindPorts")]
        private InputList<Inputs.ProxyLBBindPortsGetArgs>? _bindPorts;
        public InputList<Inputs.ProxyLBBindPortsGetArgs> BindPorts
        {
            get => _bindPorts ?? (_bindPorts = new InputList<Inputs.ProxyLBBindPortsGetArgs>());
            set => _bindPorts = value;
        }

        [Input("certificate")]
        public Input<Inputs.ProxyLBCertificateGetArgs>? Certificate { get; set; }

        /// <summary>
        /// The description of the ProxyLB. The length of this value must be in the range [`1`-`512`]
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The FQDN for accessing to the ProxyLB. This is typically used as value of CNAME record
        /// </summary>
        [Input("fqdn")]
        public Input<string>? Fqdn { get; set; }

        [Input("healthCheck")]
        public Input<Inputs.ProxyLBHealthCheckGetArgs>? HealthCheck { get; set; }

        /// <summary>
        /// The icon id to attach to the ProxyLB
        /// </summary>
        [Input("iconId")]
        public Input<string>? IconId { get; set; }

        /// <summary>
        /// The name of the ProxyLB. The length of this value must be in the range [`1`-`64`]
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The plan name of the ProxyLB. This must be one of [`100`/`500`/`1000`/`5000`/`10000`/`50000`/`100000`]
        /// </summary>
        [Input("plan")]
        public Input<int>? Plan { get; set; }

        [Input("proxyNetworks")]
        private InputList<string>? _proxyNetworks;

        /// <summary>
        /// A list of CIDR block used by the ProxyLB to access the server
        /// </summary>
        public InputList<string> ProxyNetworks
        {
            get => _proxyNetworks ?? (_proxyNetworks = new InputList<string>());
            set => _proxyNetworks = value;
        }

        /// <summary>
        /// The name of region that the proxy LB is in. This must be one of [`tk1`/`is1`/`anycast`]
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        [Input("rules")]
        private InputList<Inputs.ProxyLBRulesGetArgs>? _rules;
        public InputList<Inputs.ProxyLBRulesGetArgs> Rules
        {
            get => _rules ?? (_rules = new InputList<Inputs.ProxyLBRulesGetArgs>());
            set => _rules = value;
        }

        [Input("servers")]
        private InputList<Inputs.ProxyLBServersGetArgs>? _servers;
        public InputList<Inputs.ProxyLBServersGetArgs> Servers
        {
            get => _servers ?? (_servers = new InputList<Inputs.ProxyLBServersGetArgs>());
            set => _servers = value;
        }

        [Input("sorryServer")]
        public Input<Inputs.ProxyLBSorryServerGetArgs>? SorryServer { get; set; }

        /// <summary>
        /// The flag to enable sticky session
        /// </summary>
        [Input("stickySession")]
        public Input<bool>? StickySession { get; set; }

        [Input("tags")]
        private InputList<string>? _tags;

        /// <summary>
        /// Any tags to assign to the ProxyLB
        /// </summary>
        public InputList<string> Tags
        {
            get => _tags ?? (_tags = new InputList<string>());
            set => _tags = value;
        }

        /// <summary>
        /// The timeout duration in seconds
        /// </summary>
        [Input("timeout")]
        public Input<int>? Timeout { get; set; }

        /// <summary>
        /// The virtual IP address assigned to the ProxyLB
        /// </summary>
        [Input("vip")]
        public Input<string>? Vip { get; set; }

        /// <summary>
        /// The flag to enable VIP fail-over
        /// </summary>
        [Input("vipFailover")]
        public Input<bool>? VipFailover { get; set; }

        public ProxyLBState()
        {
        }
    }

    namespace Inputs
    {

    public sealed class ProxyLBBindPortsArgs : Pulumi.ResourceArgs
    {
        [Input("port")]
        public Input<int>? Port { get; set; }

        [Input("proxyMode", required: true)]
        public Input<string> ProxyMode { get; set; } = null!;

        [Input("redirectToHttps")]
        public Input<bool>? RedirectToHttps { get; set; }

        [Input("responseHeaders")]
        private InputList<ProxyLBBindPortsResponseHeadersArgs>? _responseHeaders;
        public InputList<ProxyLBBindPortsResponseHeadersArgs> ResponseHeaders
        {
            get => _responseHeaders ?? (_responseHeaders = new InputList<ProxyLBBindPortsResponseHeadersArgs>());
            set => _responseHeaders = value;
        }

        [Input("supportHttp2")]
        public Input<bool>? SupportHttp2 { get; set; }

        public ProxyLBBindPortsArgs()
        {
        }
    }

    public sealed class ProxyLBBindPortsGetArgs : Pulumi.ResourceArgs
    {
        [Input("port")]
        public Input<int>? Port { get; set; }

        [Input("proxyMode", required: true)]
        public Input<string> ProxyMode { get; set; } = null!;

        [Input("redirectToHttps")]
        public Input<bool>? RedirectToHttps { get; set; }

        [Input("responseHeaders")]
        private InputList<ProxyLBBindPortsResponseHeadersGetArgs>? _responseHeaders;
        public InputList<ProxyLBBindPortsResponseHeadersGetArgs> ResponseHeaders
        {
            get => _responseHeaders ?? (_responseHeaders = new InputList<ProxyLBBindPortsResponseHeadersGetArgs>());
            set => _responseHeaders = value;
        }

        [Input("supportHttp2")]
        public Input<bool>? SupportHttp2 { get; set; }

        public ProxyLBBindPortsGetArgs()
        {
        }
    }

    public sealed class ProxyLBBindPortsResponseHeadersArgs : Pulumi.ResourceArgs
    {
        [Input("header", required: true)]
        public Input<string> Header { get; set; } = null!;

        [Input("value", required: true)]
        public Input<string> Value { get; set; } = null!;

        public ProxyLBBindPortsResponseHeadersArgs()
        {
        }
    }

    public sealed class ProxyLBBindPortsResponseHeadersGetArgs : Pulumi.ResourceArgs
    {
        [Input("header", required: true)]
        public Input<string> Header { get; set; } = null!;

        [Input("value", required: true)]
        public Input<string> Value { get; set; } = null!;

        public ProxyLBBindPortsResponseHeadersGetArgs()
        {
        }
    }

    public sealed class ProxyLBCertificateAdditionalCertificatesArgs : Pulumi.ResourceArgs
    {
        [Input("intermediateCert")]
        public Input<string>? IntermediateCert { get; set; }

        [Input("privateKey", required: true)]
        public Input<string> PrivateKey { get; set; } = null!;

        [Input("serverCert", required: true)]
        public Input<string> ServerCert { get; set; } = null!;

        public ProxyLBCertificateAdditionalCertificatesArgs()
        {
        }
    }

    public sealed class ProxyLBCertificateAdditionalCertificatesGetArgs : Pulumi.ResourceArgs
    {
        [Input("intermediateCert")]
        public Input<string>? IntermediateCert { get; set; }

        [Input("privateKey", required: true)]
        public Input<string> PrivateKey { get; set; } = null!;

        [Input("serverCert", required: true)]
        public Input<string> ServerCert { get; set; } = null!;

        public ProxyLBCertificateAdditionalCertificatesGetArgs()
        {
        }
    }

    public sealed class ProxyLBCertificateArgs : Pulumi.ResourceArgs
    {
        [Input("additionalCertificates")]
        private InputList<ProxyLBCertificateAdditionalCertificatesArgs>? _additionalCertificates;
        public InputList<ProxyLBCertificateAdditionalCertificatesArgs> AdditionalCertificates
        {
            get => _additionalCertificates ?? (_additionalCertificates = new InputList<ProxyLBCertificateAdditionalCertificatesArgs>());
            set => _additionalCertificates = value;
        }

        [Input("intermediateCert")]
        public Input<string>? IntermediateCert { get; set; }

        [Input("privateKey")]
        public Input<string>? PrivateKey { get; set; }

        [Input("serverCert")]
        public Input<string>? ServerCert { get; set; }

        public ProxyLBCertificateArgs()
        {
        }
    }

    public sealed class ProxyLBCertificateGetArgs : Pulumi.ResourceArgs
    {
        [Input("additionalCertificates")]
        private InputList<ProxyLBCertificateAdditionalCertificatesGetArgs>? _additionalCertificates;
        public InputList<ProxyLBCertificateAdditionalCertificatesGetArgs> AdditionalCertificates
        {
            get => _additionalCertificates ?? (_additionalCertificates = new InputList<ProxyLBCertificateAdditionalCertificatesGetArgs>());
            set => _additionalCertificates = value;
        }

        [Input("intermediateCert")]
        public Input<string>? IntermediateCert { get; set; }

        [Input("privateKey")]
        public Input<string>? PrivateKey { get; set; }

        [Input("serverCert")]
        public Input<string>? ServerCert { get; set; }

        public ProxyLBCertificateGetArgs()
        {
        }
    }

    public sealed class ProxyLBHealthCheckArgs : Pulumi.ResourceArgs
    {
        [Input("delayLoop")]
        public Input<int>? DelayLoop { get; set; }

        [Input("hostHeader")]
        public Input<string>? HostHeader { get; set; }

        [Input("path")]
        public Input<string>? Path { get; set; }

        [Input("port")]
        public Input<int>? Port { get; set; }

        [Input("protocol", required: true)]
        public Input<string> Protocol { get; set; } = null!;

        public ProxyLBHealthCheckArgs()
        {
        }
    }

    public sealed class ProxyLBHealthCheckGetArgs : Pulumi.ResourceArgs
    {
        [Input("delayLoop")]
        public Input<int>? DelayLoop { get; set; }

        [Input("hostHeader")]
        public Input<string>? HostHeader { get; set; }

        [Input("path")]
        public Input<string>? Path { get; set; }

        [Input("port")]
        public Input<int>? Port { get; set; }

        [Input("protocol", required: true)]
        public Input<string> Protocol { get; set; } = null!;

        public ProxyLBHealthCheckGetArgs()
        {
        }
    }

    public sealed class ProxyLBRulesArgs : Pulumi.ResourceArgs
    {
        [Input("group")]
        public Input<string>? Group { get; set; }

        [Input("host")]
        public Input<string>? Host { get; set; }

        [Input("path")]
        public Input<string>? Path { get; set; }

        public ProxyLBRulesArgs()
        {
        }
    }

    public sealed class ProxyLBRulesGetArgs : Pulumi.ResourceArgs
    {
        [Input("group")]
        public Input<string>? Group { get; set; }

        [Input("host")]
        public Input<string>? Host { get; set; }

        [Input("path")]
        public Input<string>? Path { get; set; }

        public ProxyLBRulesGetArgs()
        {
        }
    }

    public sealed class ProxyLBServersArgs : Pulumi.ResourceArgs
    {
        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        [Input("group")]
        public Input<string>? Group { get; set; }

        [Input("ipAddress", required: true)]
        public Input<string> IpAddress { get; set; } = null!;

        [Input("port", required: true)]
        public Input<int> Port { get; set; } = null!;

        public ProxyLBServersArgs()
        {
        }
    }

    public sealed class ProxyLBServersGetArgs : Pulumi.ResourceArgs
    {
        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        [Input("group")]
        public Input<string>? Group { get; set; }

        [Input("ipAddress", required: true)]
        public Input<string> IpAddress { get; set; } = null!;

        [Input("port", required: true)]
        public Input<int> Port { get; set; } = null!;

        public ProxyLBServersGetArgs()
        {
        }
    }

    public sealed class ProxyLBSorryServerArgs : Pulumi.ResourceArgs
    {
        [Input("ipAddress", required: true)]
        public Input<string> IpAddress { get; set; } = null!;

        [Input("port")]
        public Input<int>? Port { get; set; }

        public ProxyLBSorryServerArgs()
        {
        }
    }

    public sealed class ProxyLBSorryServerGetArgs : Pulumi.ResourceArgs
    {
        [Input("ipAddress", required: true)]
        public Input<string> IpAddress { get; set; } = null!;

        [Input("port")]
        public Input<int>? Port { get; set; }

        public ProxyLBSorryServerGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class ProxyLBBindPorts
    {
        public readonly int? Port;
        public readonly string ProxyMode;
        public readonly bool? RedirectToHttps;
        public readonly ImmutableArray<ProxyLBBindPortsResponseHeaders> ResponseHeaders;
        public readonly bool? SupportHttp2;

        [OutputConstructor]
        private ProxyLBBindPorts(
            int? port,
            string proxyMode,
            bool? redirectToHttps,
            ImmutableArray<ProxyLBBindPortsResponseHeaders> responseHeaders,
            bool? supportHttp2)
        {
            Port = port;
            ProxyMode = proxyMode;
            RedirectToHttps = redirectToHttps;
            ResponseHeaders = responseHeaders;
            SupportHttp2 = supportHttp2;
        }
    }

    [OutputType]
    public sealed class ProxyLBBindPortsResponseHeaders
    {
        public readonly string Header;
        public readonly string Value;

        [OutputConstructor]
        private ProxyLBBindPortsResponseHeaders(
            string header,
            string value)
        {
            Header = header;
            Value = value;
        }
    }

    [OutputType]
    public sealed class ProxyLBCertificate
    {
        public readonly ImmutableArray<ProxyLBCertificateAdditionalCertificates> AdditionalCertificates;
        public readonly string IntermediateCert;
        public readonly string PrivateKey;
        public readonly string ServerCert;

        [OutputConstructor]
        private ProxyLBCertificate(
            ImmutableArray<ProxyLBCertificateAdditionalCertificates> additionalCertificates,
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
    public sealed class ProxyLBCertificateAdditionalCertificates
    {
        public readonly string? IntermediateCert;
        public readonly string PrivateKey;
        public readonly string ServerCert;

        [OutputConstructor]
        private ProxyLBCertificateAdditionalCertificates(
            string? intermediateCert,
            string privateKey,
            string serverCert)
        {
            IntermediateCert = intermediateCert;
            PrivateKey = privateKey;
            ServerCert = serverCert;
        }
    }

    [OutputType]
    public sealed class ProxyLBHealthCheck
    {
        public readonly int? DelayLoop;
        public readonly string? HostHeader;
        public readonly string? Path;
        public readonly int? Port;
        public readonly string Protocol;

        [OutputConstructor]
        private ProxyLBHealthCheck(
            int? delayLoop,
            string? hostHeader,
            string? path,
            int? port,
            string protocol)
        {
            DelayLoop = delayLoop;
            HostHeader = hostHeader;
            Path = path;
            Port = port;
            Protocol = protocol;
        }
    }

    [OutputType]
    public sealed class ProxyLBRules
    {
        public readonly string? Group;
        public readonly string? Host;
        public readonly string? Path;

        [OutputConstructor]
        private ProxyLBRules(
            string? group,
            string? host,
            string? path)
        {
            Group = group;
            Host = host;
            Path = path;
        }
    }

    [OutputType]
    public sealed class ProxyLBServers
    {
        public readonly bool? Enabled;
        public readonly string? Group;
        public readonly string IpAddress;
        public readonly int Port;

        [OutputConstructor]
        private ProxyLBServers(
            bool? enabled,
            string? group,
            string ipAddress,
            int port)
        {
            Enabled = enabled;
            Group = group;
            IpAddress = ipAddress;
            Port = port;
        }
    }

    [OutputType]
    public sealed class ProxyLBSorryServer
    {
        public readonly string IpAddress;
        public readonly int? Port;

        [OutputConstructor]
        private ProxyLBSorryServer(
            string ipAddress,
            int? port)
        {
            IpAddress = ipAddress;
            Port = port;
        }
    }
    }
}
