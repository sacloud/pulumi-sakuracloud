// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Sakuracloud
{
    public static partial class Invokes
    {
        /// <summary>
        /// Use this data source to retrieve information about a SakuraCloud ProxyLB.
        /// 
        /// &gt; This content is derived from https://github.com/sacloud/terraform-provider-sakuracloud/blob/master/website/docs/d/proxylb.html.markdown.
        /// </summary>
        public static Task<GetProxyLBResult> GetProxyLB(GetProxyLBArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetProxyLBResult>("sakuracloud:index/getProxyLB:getProxyLB", args, options.WithVersion());
    }

    public sealed class GetProxyLBArgs : Pulumi.ResourceArgs
    {
        [Input("filters")]
        private InputList<Inputs.GetProxyLBFiltersArgs>? _filters;

        /// <summary>
        /// The map of filter key and value.
        /// </summary>
        public InputList<Inputs.GetProxyLBFiltersArgs> Filters
        {
            get => _filters ?? (_filters = new InputList<Inputs.GetProxyLBFiltersArgs>());
            set => _filters = value;
        }

        [Input("nameSelectors")]
        private InputList<string>? _nameSelectors;

        /// <summary>
        /// The list of names to filtering.
        /// </summary>
        public InputList<string> NameSelectors
        {
            get => _nameSelectors ?? (_nameSelectors = new InputList<string>());
            set => _nameSelectors = value;
        }

        [Input("tagSelectors")]
        private InputList<string>? _tagSelectors;

        /// <summary>
        /// The list of tags to filtering.
        /// </summary>
        public InputList<string> TagSelectors
        {
            get => _tagSelectors ?? (_tagSelectors = new InputList<string>());
            set => _tagSelectors = value;
        }

        public GetProxyLBArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetProxyLBResult
    {
        /// <summary>
        /// The external listen ports. It contains some attributes to Bind Ports.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetProxyLBBindPortsResult> BindPorts;
        /// <summary>
        /// Certificate used to terminate SSL/TSL. It contains some attributes to Certificate.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetProxyLBCertificatesResult> Certificates;
        /// <summary>
        /// The description of the resource.
        /// </summary>
        public readonly string Description;
        public readonly ImmutableArray<Outputs.GetProxyLBFiltersResult> Filters;
        public readonly string Fqdn;
        /// <summary>
        /// The health check rules. It contains some attributes to Health Check.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetProxyLBHealthChecksResult> HealthChecks;
        /// <summary>
        /// The ID of the icon.
        /// </summary>
        public readonly string IconId;
        /// <summary>
        /// Name of the resource.
        /// </summary>
        public readonly string Name;
        public readonly ImmutableArray<string> NameSelectors;
        /// <summary>
        /// The plan of the resource.
        /// </summary>
        public readonly int Plan;
        public readonly ImmutableArray<string> ProxyNetworks;
        /// <summary>
        /// Real servers. It contains some attributes to Servers.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetProxyLBServersResult> Servers;
        /// <summary>
        /// The pair of IPAddress and port number of sorry-server.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetProxyLBSorryServersResult> SorryServers;
        /// <summary>
        /// The flag of enable Sticky-Session.  
        /// </summary>
        public readonly bool StickySession;
        public readonly ImmutableArray<string> TagSelectors;
        /// <summary>
        /// The tag list of the resources.
        /// </summary>
        public readonly ImmutableArray<string> Tags;
        /// <summary>
        /// Timeout seconds. 
        /// </summary>
        public readonly int Timeout;
        public readonly string Vip;
        /// <summary>
        /// The flag of enable VIP Fail-Over.  
        /// </summary>
        public readonly bool VipFailover;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetProxyLBResult(
            ImmutableArray<Outputs.GetProxyLBBindPortsResult> bindPorts,
            ImmutableArray<Outputs.GetProxyLBCertificatesResult> certificates,
            string description,
            ImmutableArray<Outputs.GetProxyLBFiltersResult> filters,
            string fqdn,
            ImmutableArray<Outputs.GetProxyLBHealthChecksResult> healthChecks,
            string iconId,
            string name,
            ImmutableArray<string> nameSelectors,
            int plan,
            ImmutableArray<string> proxyNetworks,
            ImmutableArray<Outputs.GetProxyLBServersResult> servers,
            ImmutableArray<Outputs.GetProxyLBSorryServersResult> sorryServers,
            bool stickySession,
            ImmutableArray<string> tagSelectors,
            ImmutableArray<string> tags,
            int timeout,
            string vip,
            bool vipFailover,
            string id)
        {
            BindPorts = bindPorts;
            Certificates = certificates;
            Description = description;
            Filters = filters;
            Fqdn = fqdn;
            HealthChecks = healthChecks;
            IconId = iconId;
            Name = name;
            NameSelectors = nameSelectors;
            Plan = plan;
            ProxyNetworks = proxyNetworks;
            Servers = servers;
            SorryServers = sorryServers;
            StickySession = stickySession;
            TagSelectors = tagSelectors;
            Tags = tags;
            Timeout = timeout;
            Vip = vip;
            VipFailover = vipFailover;
            Id = id;
        }
    }

    namespace Inputs
    {

    public sealed class GetProxyLBFiltersArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Name of the resource.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        [Input("values", required: true)]
        private InputList<string>? _values;
        public InputList<string> Values
        {
            get => _values ?? (_values = new InputList<string>());
            set => _values = value;
        }

        public GetProxyLBFiltersArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class GetProxyLBBindPortsResponseHeadersResult
    {
        /// <summary>
        /// The key of additional header.  
        /// </summary>
        public readonly string Header;
        /// <summary>
        /// The value of additional header.  
        /// </summary>
        public readonly string Value;

        [OutputConstructor]
        private GetProxyLBBindPortsResponseHeadersResult(
            string header,
            string value)
        {
            Header = header;
            Value = value;
        }
    }

    [OutputType]
    public sealed class GetProxyLBBindPortsResult
    {
        /// <summary>
        /// Port number.
        /// </summary>
        public readonly int Port;
        /// <summary>
        /// Proxy protocol.  
        /// </summary>
        public readonly string ProxyMode;
        /// <summary>
        /// The flag for enable to redirect to https.
        /// </summary>
        public readonly bool RedirectToHttps;
        /// <summary>
        /// Additional response headers. It contains some attributes to Response Header.  
        /// </summary>
        public readonly ImmutableArray<GetProxyLBBindPortsResponseHeadersResult> ResponseHeaders;
        /// <summary>
        /// The flag for enable to support HTTP/2.
        /// </summary>
        public readonly bool SupportHttp2;

        [OutputConstructor]
        private GetProxyLBBindPortsResult(
            int port,
            string proxyMode,
            bool redirectToHttps,
            ImmutableArray<GetProxyLBBindPortsResponseHeadersResult> responseHeaders,
            bool supportHttp2)
        {
            Port = port;
            ProxyMode = proxyMode;
            RedirectToHttps = redirectToHttps;
            ResponseHeaders = responseHeaders;
            SupportHttp2 = supportHttp2;
        }
    }

    [OutputType]
    public sealed class GetProxyLBCertificatesAdditionalCertificatesResult
    {
        /// <summary>
        /// The intermediate certificate.
        /// </summary>
        public readonly string IntermediateCert;
        /// <summary>
        /// The private key.
        /// </summary>
        public readonly string PrivateKey;
        /// <summary>
        /// The server certificate.
        /// </summary>
        public readonly string ServerCert;

        [OutputConstructor]
        private GetProxyLBCertificatesAdditionalCertificatesResult(
            string intermediateCert,
            string privateKey,
            string serverCert)
        {
            IntermediateCert = intermediateCert;
            PrivateKey = privateKey;
            ServerCert = serverCert;
        }
    }

    [OutputType]
    public sealed class GetProxyLBCertificatesResult
    {
        /// <summary>
        /// The additional certificates.
        /// </summary>
        public readonly ImmutableArray<GetProxyLBCertificatesAdditionalCertificatesResult> AdditionalCertificates;
        /// <summary>
        /// The intermediate certificate.
        /// </summary>
        public readonly string IntermediateCert;
        /// <summary>
        /// The private key.
        /// </summary>
        public readonly string PrivateKey;
        /// <summary>
        /// The server certificate.
        /// </summary>
        public readonly string ServerCert;

        [OutputConstructor]
        private GetProxyLBCertificatesResult(
            ImmutableArray<GetProxyLBCertificatesAdditionalCertificatesResult> additionalCertificates,
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
    public sealed class GetProxyLBFiltersResult
    {
        /// <summary>
        /// Name of the resource.
        /// </summary>
        public readonly string Name;
        public readonly ImmutableArray<string> Values;

        [OutputConstructor]
        private GetProxyLBFiltersResult(
            string name,
            ImmutableArray<string> values)
        {
            Name = name;
            Values = values;
        }
    }

    [OutputType]
    public sealed class GetProxyLBHealthChecksResult
    {
        /// <summary>
        /// Health check access interval (unit:`second`, default:`10`).
        /// </summary>
        public readonly int DelayLoop;
        /// <summary>
        /// The value of `Host` header used in http/https health check access.
        /// </summary>
        public readonly string HostHeader;
        /// <summary>
        /// The request path used in http health check access.
        /// </summary>
        public readonly string Path;
        /// <summary>
        /// Port number.
        /// </summary>
        public readonly int Port;
        /// <summary>
        /// Protocol used in health check.  
        /// </summary>
        public readonly string Protocol;

        [OutputConstructor]
        private GetProxyLBHealthChecksResult(
            int delayLoop,
            string hostHeader,
            string path,
            int port,
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
    public sealed class GetProxyLBServersResult
    {
        /// <summary>
        /// The flag for enable/disable the Real-Server (default:`true`).
        /// </summary>
        public readonly bool Enabled;
        /// <summary>
        /// The IP address of the Real-Server.
        /// </summary>
        public readonly string Ipaddress;
        /// <summary>
        /// Port number.
        /// </summary>
        public readonly int Port;

        [OutputConstructor]
        private GetProxyLBServersResult(
            bool enabled,
            string ipaddress,
            int port)
        {
            Enabled = enabled;
            Ipaddress = ipaddress;
            Port = port;
        }
    }

    [OutputType]
    public sealed class GetProxyLBSorryServersResult
    {
        /// <summary>
        /// The IP address of the Real-Server.
        /// </summary>
        public readonly string Ipaddress;
        /// <summary>
        /// Port number.
        /// </summary>
        public readonly int Port;

        [OutputConstructor]
        private GetProxyLBSorryServersResult(
            string ipaddress,
            int port)
        {
            Ipaddress = ipaddress;
            Port = port;
        }
    }
    }
}
