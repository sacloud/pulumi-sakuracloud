// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";

export interface DNSRecord {
    /**
     * The hostname of target Record. If "@" is specified, it indicates own zone.
     */
    name: pulumi.Input<string>;
    /**
     * The port number used when `type` is `SRV`. 
     */
    port?: pulumi.Input<number>;
    /**
     * The priority used when `type` is `MX` or `SRV`.
     */
    priority?: pulumi.Input<number>;
    /**
     * The ttl value of the Record (unit:`second`). 
     */
    ttl?: pulumi.Input<number>;
    /**
     * The Record type.  
     * Valid value is one of the following: [ "A" / "AAAA" / "ALIAS" / "CNAME" / "NS" / "MX" / "TXT" / "SRV" / "CAA" ]
     */
    type: pulumi.Input<string>;
    /**
     * The value of the Record. 
     */
    value: pulumi.Input<string>;
    /**
     * The weight used when `type` is `SRV`.
     */
    weight?: pulumi.Input<number>;
}

export interface GSLBHealthCheck {
    /**
     * Health check access interval (unit:`second`, default:`10`).
     */
    delayLoop?: pulumi.Input<number>;
    /**
     * The value of `Host` header used in http/https health check access.
     */
    hostHeader?: pulumi.Input<string>;
    /**
     * The request path used in http/https health check access.
     */
    path?: pulumi.Input<string>;
    /**
     * Port number used in tcp health check access.
     */
    port?: pulumi.Input<number>;
    /**
     * Protocol used in health check.  
     * Valid value is one of the following: [ "http" / "https" / "ping" / "tcp" ]
     */
    protocol: pulumi.Input<string>;
    /**
     * HTTP status code expected by health check access.
     */
    status?: pulumi.Input<string>;
}

export interface GSLBServer {
    /**
     * The flag for enable/disable the GSLB Server (default:`true`).
     */
    enabled?: pulumi.Input<boolean>;
    /**
     * The IP address of the GSLB Server.
     */
    ipaddress: pulumi.Input<string>;
    /**
     * The weight of GSLB server used when weighting is enabled in the GSLB.
     */
    weight?: pulumi.Input<number>;
}

export interface GetArchiveFilter {
    /**
     * The name of the resource.
     */
    name: string;
    values: string[];
}

export interface GetBridgeFilter {
    /**
     * The name of the resource.
     */
    name: string;
    values: string[];
}

export interface GetCDROMFilter {
    /**
     * The name of the resource.
     */
    name: string;
    values: string[];
}

export interface GetDNSFilter {
    name: string;
    values: string[];
}

export interface GetDatabaseFilter {
    /**
     * The name of the resource.
     */
    name: string;
    values: string[];
}

export interface GetDiskFilter {
    /**
     * The name of the resource.
     */
    name: string;
    values: string[];
}

export interface GetGSLBFilter {
    /**
     * Name of the resource.
     */
    name: string;
    values: string[];
}

export interface GetIconFilter {
    /**
     * The name of the resource.
     */
    name: string;
    values: string[];
}

export interface GetInternetFilter {
    /**
     * The name of the resource.
     */
    name: string;
    values: string[];
}

export interface GetLoadBalancerFilter {
    /**
     * The name of the resource.
     */
    name: string;
    values: string[];
}

export interface GetNFSFilter {
    /**
     * The name of the resource.
     */
    name: string;
    values: string[];
}

export interface GetNoteFilter {
    /**
     * The name of the resource.
     */
    name: string;
    values: string[];
}

export interface GetPacketFilterExpression {
    /**
     * The flag to allow packets. Default value is `true`. 
     */
    allow?: boolean;
    /**
     * The description of the expression.
     */
    description?: string;
    /**
     * The destination port (range).
     */
    destPort?: string;
    /**
     * The target protocol.
     */
    protocol?: string;
    /**
     * The source network address (range).
     */
    sourceNw?: string;
    /**
     * The source port (range).
     */
    sourcePort?: string;
}

export interface GetPacketFilterFilter {
    /**
     * The name of the resource.
     */
    name: string;
    values: string[];
}

export interface GetPrivateHostFilter {
    /**
     * The name of the resource.
     */
    name: string;
    values: string[];
}

export interface GetProxyLBFilter {
    /**
     * Name of the resource.
     */
    name: string;
    values: string[];
}

export interface GetSSHKeyFilter {
    /**
     * The name of the resource.
     */
    name: string;
    values: string[];
}

export interface GetServerFilter {
    /**
     * The name of the resource.
     */
    name: string;
    values: string[];
}

export interface GetSimpleMonitorFilter {
    name: string;
    values: string[];
}

export interface GetSwitchFilter {
    /**
     * The name of the resource.
     */
    name: string;
    values: string[];
}

export interface GetVPCRouterFilter {
    /**
     * The name of the resource.
     */
    name: string;
    values: string[];
}

export interface LoadBalancerVip {
    /**
     * The interval seconds for health check access.
     */
    delayLoop?: pulumi.Input<number>;
    /**
     * The description of the VIP.
     */
    description?: pulumi.Input<string>;
    /**
     * The port number on which Load Balancer listens.
     */
    port: pulumi.Input<number>;
    /**
     * Real servers. It contains some attributes to Servers.
     */
    servers?: pulumi.Input<pulumi.Input<inputs.LoadBalancerVipServer>[]>;
    /**
     * The hostname or IP address of sorry server.
     */
    sorryServer?: pulumi.Input<string>;
    /**
     * The virtual IP address.
     */
    vip: pulumi.Input<string>;
}

export interface LoadBalancerVipServer {
    /**
     * The request path used in http/https health check access.
     */
    checkPath?: pulumi.Input<string>;
    /**
     * Protocol used in health check.  
     * Valid value is one of the following: [ "http" / "https" / "ping" / "tcp" ]
     */
    checkProtocol: pulumi.Input<string>;
    /**
     * HTTP status code expected by health check access.
     */
    checkStatus?: pulumi.Input<string>;
    /**
     * The flag of enable/disable the Server.
     */
    enabled?: pulumi.Input<boolean>;
    /**
     * The IP address of the Server.
     */
    ipaddress: pulumi.Input<string>;
}

export interface MobileGatewayStaticRoute {
    nextHop: pulumi.Input<string>;
    prefix: pulumi.Input<string>;
}

export interface MobileGatewayTrafficControl {
    /**
     * The flag of enable/disable Auto Traffic Shaping.
     */
    autoTrafficShaping?: pulumi.Input<boolean>;
    /**
     * Traffic bandwidth limit(unit:`Kbps`). 
     */
    bandWidthLimit?: pulumi.Input<number>;
    /**
     * The flag of enable/disable e-mail notification.
     */
    enableEmail?: pulumi.Input<boolean>;
    /**
     * The flag of enable/disable slack notification.
     */
    enableSlack?: pulumi.Input<boolean>;
    /**
     * Traffic quota size (unit:`MB`).  
     */
    quota: pulumi.Input<number>;
    /**
     * The webhook URL of destination of slack notification.
     */
    slackWebhook?: pulumi.Input<string>;
}

export interface PacketFilterExpression {
    /**
     * The flag for allow/deny packets (default:`true`).
     */
    allow?: pulumi.Input<boolean>;
    /**
     * The description of the expression.
     */
    description?: pulumi.Input<string>;
    /**
     * Target destination port.
     * Valid format is one of the following:
     * * Number: `"0"` - `"65535"`
     * * Range: `"xx-yy"`
     * * Range (hex): `"0xPPPP/0xMMMM"`
     */
    destPort?: pulumi.Input<string>;
    /**
     * Protocol used in health check.  
     * Valid value is one of the following: [ "tcp" / "udp" / "icmp" / "fragment" / "ip" ]
     */
    protocol: pulumi.Input<string>;
    /**
     * Target source network IP address or CIDR or range.  
     * Valid format is one of the following:
     * * IP address: `"xxx.xxx.xxx.xxx"`
     * * CIDR: `"xxx.xxx.xxx.xxx/nn"`
     * * Range: `"xxx.xxx.xxx.xxx/yyy.yyy.yyy.yyy"`
     */
    sourceNw?: pulumi.Input<string>;
    /**
     * Target source port.
     * Valid format is one of the following:
     * * Number: `"0"` - `"65535"`
     * * Range: `"xx-yy"`
     * * Range (hex): `"0xPPPP/0xMMMM"`
     */
    sourcePort?: pulumi.Input<string>;
}

export interface ProxyLBACMECertificate {
    /**
     * Additional certificates.
     */
    additionalCertificates?: pulumi.Input<pulumi.Input<inputs.ProxyLBACMECertificateAdditionalCertificate>[]>;
    /**
     * The intermediate certificate.
     */
    intermediateCert?: pulumi.Input<string>;
    /**
     * The private key.
     */
    privateKey?: pulumi.Input<string>;
    /**
     * The server certificate.
     */
    serverCert?: pulumi.Input<string>;
}

export interface ProxyLBACMECertificateAdditionalCertificate {
    /**
     * The intermediate certificate.
     */
    intermediateCert?: pulumi.Input<string>;
    /**
     * The private key.
     */
    privateKey?: pulumi.Input<string>;
    /**
     * The server certificate.
     */
    serverCert?: pulumi.Input<string>;
}

export interface ProxyLBBindPort {
    /**
     * Port number.
     */
    port?: pulumi.Input<number>;
    /**
     * Proxy protocol.  
     * Valid value is one of the following: [ "http" / "https"]
     */
    proxyMode: pulumi.Input<string>;
    /**
     * The flag for enable to redirect to https.
     */
    redirectToHttps?: pulumi.Input<boolean>;
    /**
     * Additional response headers. It contains some attributes to Response Header.  
     */
    responseHeaders?: pulumi.Input<pulumi.Input<inputs.ProxyLBBindPortResponseHeader>[]>;
    /**
     * The flag for enable to support HTTP/2.
     */
    supportHttp2?: pulumi.Input<boolean>;
}

export interface ProxyLBBindPortResponseHeader {
    /**
     * The key of additional header.  
     */
    header: pulumi.Input<string>;
    /**
     * The value of additional header.  
     */
    value: pulumi.Input<string>;
}

export interface ProxyLBCertificate {
    /**
     * Additional certificates.
     */
    additionalCertificates?: pulumi.Input<pulumi.Input<inputs.ProxyLBCertificateAdditionalCertificate>[]>;
    /**
     * The intermediate certificate.
     */
    intermediateCert?: pulumi.Input<string>;
    /**
     * The private key.
     */
    privateKey?: pulumi.Input<string>;
    /**
     * The server certificate.
     */
    serverCert?: pulumi.Input<string>;
}

export interface ProxyLBCertificateAdditionalCertificate {
    /**
     * The intermediate certificate.
     */
    intermediateCert?: pulumi.Input<string>;
    /**
     * The private key.
     */
    privateKey: pulumi.Input<string>;
    /**
     * The server certificate.
     */
    serverCert: pulumi.Input<string>;
}

export interface ProxyLBHealthCheck {
    /**
     * Health check access interval (unit:`second`, default:`10`).
     */
    delayLoop?: pulumi.Input<number>;
    /**
     * The value of `Host` header used in http/https health check access.
     */
    hostHeader?: pulumi.Input<string>;
    /**
     * The request path used in http health check access.
     */
    path?: pulumi.Input<string>;
    /**
     * Protocol used in health check.  
     * Valid value is one of the following: [ "http" / "tcp" ]
     */
    protocol: pulumi.Input<string>;
}

export interface ProxyLBServer {
    /**
     * The flag for enable/disable the Real-Server (default:`true`).
     */
    enabled?: pulumi.Input<boolean>;
    /**
     * The IP address of the Real-Server.
     */
    ipaddress: pulumi.Input<string>;
    /**
     * Port number.
     */
    port: pulumi.Input<number>;
}

export interface ProxyLBSorryServer {
    /**
     * The IP address of the Real-Server.
     */
    ipaddress: pulumi.Input<string>;
    /**
     * Port number.
     */
    port?: pulumi.Input<number>;
}

export interface SimpleMonitorHealthCheck {
    /**
     * The community name used in snmp health check.
     */
    community?: pulumi.Input<string>;
    /**
     * Health check access interval (unit:`second`). 
     */
    delayLoop?: pulumi.Input<number>;
    /**
     * The expect value used in dns/snmp health check.
     */
    excepctedData?: pulumi.Input<string>;
    /**
     * The value of `Host` header used in http/https health check access.
     */
    hostHeader?: pulumi.Input<string>;
    /**
     * The OID used in snmp health check.
     */
    oid?: pulumi.Input<string>;
    /**
     * The Basic Auth Password request path used in http/https health check access.
     */
    password?: pulumi.Input<string>;
    /**
     * The request path used in http/https health check access.
     */
    path?: pulumi.Input<string>;
    /**
     * Port number used in health check access.
     */
    port?: pulumi.Input<number>;
    /**
     * Protocol used in health check.  
     * Valid value is one of the following: [ "http" / "https" / "ping" / "tcp" / "dns" / "ssh" / "smtp" / "pop3" / "snmp" / "sslcertificate" ]
     */
    protocol: pulumi.Input<string>;
    /**
     * The QName value used in dns health check access.
     */
    qname?: pulumi.Input<string>;
    /**
     * The number of remaining days used in ssh-certificate check.
     */
    remainingDays?: pulumi.Input<number>;
    /**
     * The flag of enable/disable SNI.
     */
    sni?: pulumi.Input<boolean>;
    /**
     * SNMP cersion used in snmp health check.
     */
    snmpVersion?: pulumi.Input<string>;
    /**
     * HTTP status code expected by health check access.
     */
    status?: pulumi.Input<string>;
    /**
     * The Basic Auth Username used in http/https health check access.
     */
    username?: pulumi.Input<string>;
}

export interface VPCRouterDhcpServer {
    /**
     * (Required) DNS server list to be assigned by DHCP.  
     */
    dnsServers?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * (Required) Start IP address of address range to be assigned by PPTP.
     */
    rangeStart: pulumi.Input<string>;
    /**
     * (Required) End IP address of address range to be assigned by PPTP.
     */
    rangeStop: pulumi.Input<string>;
    /**
     * (Required) The NIC index of VPC Router running DHCP Server.
     */
    vpcRouterInterfaceIndex: pulumi.Input<number>;
}

export interface VPCRouterDhcpStaticMapping {
    /**
     * (Required) The MAC address to be the key of the mapping. 
     */
    ipaddress: pulumi.Input<string>;
    /**
     * (Required) The IP address mapped by MAC address.
     */
    macaddress: pulumi.Input<string>;
}

export interface VPCRouterFirewall {
    /**
     * (Required) Direction of filtering packets.  
     * Valid value is one of the following: [ "send" / "receive" ]
     */
    direction: pulumi.Input<string>;
    /**
     * (Required) Filtering rules. It contains some attributes to Expressions.
     */
    expressions: pulumi.Input<pulumi.Input<inputs.VPCRouterFirewallExpression>[]>;
    /**
     * (Required) The NIC index of VPC Router running DHCP Server.
     */
    vpcRouterInterfaceIndex?: pulumi.Input<number>;
}

export interface VPCRouterFirewallExpression {
    /**
     * (Required) The flag for allow/deny packets.
     */
    allow: pulumi.Input<boolean>;
    /**
     * The description of the resource.
     */
    description?: pulumi.Input<string>;
    /**
     * (Required) Target destination network IP address or CIDR or range.  
     * Valid format is one of the following:
     * * IP address: `"xxx.xxx.xxx.xxx"`
     * * CIDR: `"xxx.xxx.xxx.xxx/nn"`
     * * Range: `"xxx.xxx.xxx.xxx/yyy.yyy.yyy.yyy"`
     */
    destNw: pulumi.Input<string>;
    /**
     * (Required) Target destination port.
     * Valid format is one of the following:
     * * Number: `"0"` - `"65535"`
     * * Range: `"xx-yy"`
     * * Range (hex): `"0xPPPP/0xMMMM"`
     */
    destPort: pulumi.Input<string>;
    /**
     * (Required) The flag for enable/disable logging.
     */
    logging?: pulumi.Input<boolean>;
    /**
     * (Required) Protocol used in health check.  
     * Valid value is one of the following: [ "tcp" / "udp" / "icmp" / "ip" ]
     */
    protocol: pulumi.Input<string>;
    /**
     * (Required) Target source network IP address or CIDR or range.  
     * Valid format is one of the following:
     * * IP address: `"xxx.xxx.xxx.xxx"`
     * * CIDR: `"xxx.xxx.xxx.xxx/nn"`
     * * Range: `"xxx.xxx.xxx.xxx/yyy.yyy.yyy.yyy"`
     */
    sourceNw: pulumi.Input<string>;
    /**
     * (Required) Target source port.
     * Valid format is one of the following:
     * * Number: `"0"` - `"65535"`
     * * Range: `"xx-yy"`
     * * Range (hex): `"0xPPPP/0xMMMM"`
     */
    sourcePort: pulumi.Input<string>;
}

export interface VPCRouterInterface {
    /**
     * (Required) The MAC address to be the key of the mapping. 
     */
    ipaddresses: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * (Optional) Network mask length of the VPC Router Interface.
     */
    nwMaskLen: pulumi.Input<number>;
    /**
     * The ID of the switch connected to the VPC Router. Used when plan is `premium` or `highspec`.
     */
    switchId: pulumi.Input<string>;
    /**
     * The Virtual IP address of the VPC Router. Used when plan is `premium` or `highspec`.
     */
    vip?: pulumi.Input<string>;
}

export interface VPCRouterL2tp {
    /**
     * The pre shared secret for IPSec.
     */
    preSharedSecret: pulumi.Input<string>;
    /**
     * (Required) Start IP address of address range to be assigned by PPTP.
     */
    rangeStart: pulumi.Input<string>;
    /**
     * (Required) End IP address of address range to be assigned by PPTP.
     */
    rangeStop: pulumi.Input<string>;
}

export interface VPCRouterPortForwarding {
    /**
     * The description of the resource.
     */
    description?: pulumi.Input<string>;
    /**
     * (Required) The global port of the Port Forwarding.
     */
    globalPort: pulumi.Input<number>;
    /**
     * (Required) The private IP address of the Static NAT.
     */
    privateAddress: pulumi.Input<string>;
    /**
     * (Required) The destination port number of the Port Forwarding.
     */
    privatePort: pulumi.Input<number>;
    /**
     * (Required) Protocol used in health check.  
     * Valid value is one of the following: [ "tcp" / "udp" / "icmp" / "ip" ]
     */
    protocol: pulumi.Input<string>;
}

export interface VPCRouterPptp {
    /**
     * (Required) Start IP address of address range to be assigned by PPTP.
     */
    rangeStart: pulumi.Input<string>;
    /**
     * (Required) End IP address of address range to be assigned by PPTP.
     */
    rangeStop: pulumi.Input<string>;
}

export interface VPCRouterSiteToSiteVpn {
    /**
     * ESP authentication protocol.
     */
    espAuthenticationProtocol?: pulumi.Input<string>;
    /**
     * ESP DH group.
     */
    espDhGroup?: pulumi.Input<string>;
    /**
     * ESP encryption protocol.
     */
    espEncryptionProtocol?: pulumi.Input<string>;
    /**
     * ESP lifetime.
     */
    espLifetime?: pulumi.Input<string>;
    /**
     * ESP mode.
     */
    espMode?: pulumi.Input<string>;
    /**
     * ESP perfect forward secrecy.
     */
    espPerfectForwardSecrecy?: pulumi.Input<string>;
    /**
     * IKE authentication protocol.
     */
    ikeAuthenticationProtocol?: pulumi.Input<string>;
    /**
     * IKE encryption protocol.
     */
    ikeEncryptionProtocol?: pulumi.Input<string>;
    /**
     * IKE lifetime.
     */
    ikeLifetime?: pulumi.Input<string>;
    /**
     * IKE mode.
     */
    ikeMode?: pulumi.Input<string>;
    /**
     * IKE perfect forward secrecy.
     */
    ikePerfectForwardSecrecy?: pulumi.Input<string>;
    /**
     * IKE pre shared secret.
     */
    ikePreSharedSecret?: pulumi.Input<string>;
    /**
     * The local prefix.
     */
    localPrefixes: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The peer IP address.
     */
    peer: pulumi.Input<string>;
    /**
     * Peer ID.
     */
    peerId?: pulumi.Input<string>;
    /**
     * Peer inside networks.
     */
    peerInsideNetworks?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Peer outsite ipaddress.
     */
    peerOutsideIpaddress?: pulumi.Input<string>;
    /**
     * The pre shared secret for IPSec.
     */
    preSharedSecret: pulumi.Input<string>;
    /**
     * The IPSec ID of target.
     */
    remoteId: pulumi.Input<string>;
    /**
     * The routing prefix.
     */
    routes: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * VPC Router inside networks.
     */
    vpcRouterInsideNetworks?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * VPC Router outside IP address.
     */
    vpcRouterOutsideIpaddress?: pulumi.Input<string>;
}

export interface VPCRouterStaticNat {
    /**
     * The description of the resource.
     */
    description?: pulumi.Input<string>;
    /**
     * (Required) The global IP address of the Static NAT.
     */
    globalAddress: pulumi.Input<string>;
    /**
     * (Required) The private IP address of the Static NAT.
     */
    privateAddress: pulumi.Input<string>;
}

export interface VPCRouterStaticRoute {
    /**
     * (Required) The next hop IP address of the Static Route.
     */
    nextHop: pulumi.Input<string>;
    /**
     * (Required) The prefix of the Static Route.
     */
    prefix: pulumi.Input<string>;
}

export interface VPCRouterUser {
    /**
     * The name of the resource.
     */
    name: pulumi.Input<string>;
    /**
     * (Required) The password.
     */
    password: pulumi.Input<string>;
}
