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
    public sealed class GetSimpleMonitorHealthCheckResult
    {
        /// <summary>
        /// The SNMP community string used when checking by SNMP.
        /// </summary>
        public readonly string Community;
        /// <summary>
        /// The string that should be included in the response body when checking for HTTP/HTTPS.
        /// </summary>
        public readonly string ContainsString;
        /// <summary>
        /// The expected value used when checking by DNS.
        /// </summary>
        public readonly string ExcepctedData;
        /// <summary>
        /// The value of host header send when checking by HTTP/HTTPS.
        /// </summary>
        public readonly string HostHeader;
        /// <summary>
        /// The flag to enable HTTP/2 when checking by HTTPS.
        /// </summary>
        public readonly bool Http2;
        /// <summary>
        /// The SNMP OID used when checking by SNMP.
        /// </summary>
        public readonly string Oid;
        /// <summary>
        /// The password for basic auth used when checking by HTTP/HTTPS.
        /// </summary>
        public readonly string Password;
        /// <summary>
        /// The path used when checking by HTTP/HTTPS.
        /// </summary>
        public readonly string Path;
        /// <summary>
        /// The target port number.
        /// </summary>
        public readonly int Port;
        /// <summary>
        /// The protocol used for health checks. This will be one of [`http`/`https`/`ping`/`tcp`/`dns`/`ssh`/`smtp`/`pop3`/`snmp`/`sslcertificate`].
        /// </summary>
        public readonly string Protocol;
        /// <summary>
        /// The FQDN used when checking by DNS.
        /// </summary>
        public readonly string Qname;
        /// <summary>
        /// The number of remaining days until certificate expiration used when checking SSL certificates.
        /// </summary>
        public readonly int RemainingDays;
        /// <summary>
        /// The flag to enable SNI when checking by HTTP/HTTPS.
        /// </summary>
        public readonly bool Sni;
        /// <summary>
        /// The SNMP version used when checking by SNMP.
        /// </summary>
        public readonly string SnmpVersion;
        /// <summary>
        /// The response-code to expect when checking by HTTP/HTTPS.
        /// </summary>
        public readonly int Status;
        /// <summary>
        /// The user name for basic auth used when checking by HTTP/HTTPS.
        /// </summary>
        public readonly string Username;

        [OutputConstructor]
        private GetSimpleMonitorHealthCheckResult(
            string community,

            string containsString,

            string excepctedData,

            string hostHeader,

            bool http2,

            string oid,

            string password,

            string path,

            int port,

            string protocol,

            string qname,

            int remainingDays,

            bool sni,

            string snmpVersion,

            int status,

            string username)
        {
            Community = community;
            ContainsString = containsString;
            ExcepctedData = excepctedData;
            HostHeader = hostHeader;
            Http2 = http2;
            Oid = oid;
            Password = password;
            Path = path;
            Port = port;
            Protocol = protocol;
            Qname = qname;
            RemainingDays = remainingDays;
            Sni = sni;
            SnmpVersion = snmpVersion;
            Status = status;
            Username = username;
        }
    }
}
