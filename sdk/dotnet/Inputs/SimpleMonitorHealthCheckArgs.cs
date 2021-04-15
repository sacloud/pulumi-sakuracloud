// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Sakuracloud.Inputs
{

    public sealed class SimpleMonitorHealthCheckArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The SNMP community string used when checking by SNMP.
        /// </summary>
        [Input("community")]
        public Input<string>? Community { get; set; }

        /// <summary>
        /// The string that should be included in the response body when checking for HTTP/HTTPS.
        /// </summary>
        [Input("containsString")]
        public Input<string>? ContainsString { get; set; }

        /// <summary>
        /// The expected value used when checking by DNS.
        /// </summary>
        [Input("excepctedData")]
        public Input<string>? ExcepctedData { get; set; }

        /// <summary>
        /// The value of host header send when checking by HTTP/HTTPS.
        /// </summary>
        [Input("hostHeader")]
        public Input<string>? HostHeader { get; set; }

        /// <summary>
        /// The flag to enable HTTP/2 when checking by HTTPS.
        /// </summary>
        [Input("http2")]
        public Input<bool>? Http2 { get; set; }

        /// <summary>
        /// The SNMP OID used when checking by SNMP.
        /// </summary>
        [Input("oid")]
        public Input<string>? Oid { get; set; }

        /// <summary>
        /// The password for basic auth used when checking by HTTP/HTTPS.
        /// </summary>
        [Input("password")]
        public Input<string>? Password { get; set; }

        /// <summary>
        /// The path used when checking by HTTP/HTTPS.
        /// </summary>
        [Input("path")]
        public Input<string>? Path { get; set; }

        /// <summary>
        /// The target port number.
        /// </summary>
        [Input("port")]
        public Input<int>? Port { get; set; }

        /// <summary>
        /// The protocol used for health checks. This must be one of [`http`/`https`/`ping`/`tcp`/`dns`/`ssh`/`smtp`/`pop3`/`snmp`/`sslcertificate`].
        /// </summary>
        [Input("protocol", required: true)]
        public Input<string> Protocol { get; set; } = null!;

        /// <summary>
        /// The FQDN used when checking by DNS.
        /// </summary>
        [Input("qname")]
        public Input<string>? Qname { get; set; }

        /// <summary>
        /// The number of remaining days until certificate expiration used when checking SSL certificates. This must be in the range [`1`-`9999`].
        /// </summary>
        [Input("remainingDays")]
        public Input<int>? RemainingDays { get; set; }

        /// <summary>
        /// The flag to enable SNI when checking by HTTP/HTTPS.
        /// </summary>
        [Input("sni")]
        public Input<bool>? Sni { get; set; }

        /// <summary>
        /// The SNMP version used when checking by SNMP. This must be one of `1`/`2c`.
        /// </summary>
        [Input("snmpVersion")]
        public Input<string>? SnmpVersion { get; set; }

        /// <summary>
        /// The response-code to expect when checking by HTTP/HTTPS.
        /// </summary>
        [Input("status")]
        public Input<int>? Status { get; set; }

        /// <summary>
        /// The user name for basic auth used when checking by HTTP/HTTPS.
        /// </summary>
        [Input("username")]
        public Input<string>? Username { get; set; }

        public SimpleMonitorHealthCheckArgs()
        {
        }
    }
}