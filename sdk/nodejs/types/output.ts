// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";

export interface ContainerRegistryUser {
    name: pulumi.Input<string>;
    password: pulumi.Input<string>;
}

export interface DNSRecord {
    name: pulumi.Input<string>;
    port?: pulumi.Input<number>;
    priority?: pulumi.Input<number>;
    ttl?: pulumi.Input<number>;
    type: pulumi.Input<string>;
    value: pulumi.Input<string>;
    weight?: pulumi.Input<number>;
}

export interface DatabaseBackup {
    time?: pulumi.Input<string>;
    weekdays?: pulumi.Input<pulumi.Input<string>[]>;
}

export interface DatabaseNetworkInterface {
    gateway: pulumi.Input<string>;
    ipAddress: pulumi.Input<string>;
    netmask: pulumi.Input<number>;
    port?: pulumi.Input<number>;
    sourceRanges?: pulumi.Input<pulumi.Input<string>[]>;
    switchId: pulumi.Input<string>;
}

export interface DatabaseReadReplicaNetworkInterface {
    gateway?: pulumi.Input<string>;
    ipAddress: pulumi.Input<string>;
    netmask?: pulumi.Input<number>;
    sourceRanges?: pulumi.Input<pulumi.Input<string>[]>;
    switchId?: pulumi.Input<string>;
}

export interface GSLBHealthCheck {
    delayLoop?: pulumi.Input<number>;
    hostHeader?: pulumi.Input<string>;
    path?: pulumi.Input<string>;
    port?: pulumi.Input<number>;
    protocol: pulumi.Input<string>;
    status?: pulumi.Input<string>;
}

export interface GSLBServer {
    enabled?: pulumi.Input<boolean>;
    ipAddress: pulumi.Input<string>;
    weight?: pulumi.Input<number>;
}

export interface GetArchiveFilter {
    conditions?: outputs.GetArchiveFilterCondition[];
    id?: string;
    names?: string[];
    tags?: string[];
}

export interface GetArchiveFilterCondition {
    name: string;
    values: string[];
}

export interface GetBridgeFilter {
    conditions?: outputs.GetBridgeFilterCondition[];
    id?: string;
    names?: string[];
}

export interface GetBridgeFilterCondition {
    name: string;
    values: string[];
}

export interface GetCDROMFilter {
    conditions?: outputs.GetCDROMFilterCondition[];
    id?: string;
    names?: string[];
    tags?: string[];
}

export interface GetCDROMFilterCondition {
    name: string;
    values: string[];
}

export interface GetContainerRegistryFilter {
    conditions?: outputs.GetContainerRegistryFilterCondition[];
    id?: string;
    names?: string[];
    tags?: string[];
}

export interface GetContainerRegistryFilterCondition {
    name: string;
    values: string[];
}

export interface GetDNSFilter {
    conditions?: outputs.GetDNSFilterCondition[];
    id?: string;
    names?: string[];
    tags?: string[];
}

export interface GetDNSFilterCondition {
    name: string;
    values: string[];
}

export interface GetDNSRecord {
    name: string;
    port: number;
    priority: number;
    ttl: number;
    type: string;
    value: string;
    weight: number;
}

export interface GetDatabaseBackup {
    time: string;
    weekdays: string[];
}

export interface GetDatabaseFilter {
    conditions?: outputs.GetDatabaseFilterCondition[];
    id?: string;
    names?: string[];
    tags?: string[];
}

export interface GetDatabaseFilterCondition {
    name: string;
    values: string[];
}

export interface GetDatabaseNetworkInterface {
    gateway: string;
    ipAddress: string;
    netmask: number;
    port: number;
    sourceRanges: string[];
    switchId: string;
}

export interface GetDiskFilter {
    conditions?: outputs.GetDiskFilterCondition[];
    id?: string;
    names?: string[];
    tags?: string[];
}

export interface GetDiskFilterCondition {
    name: string;
    values: string[];
}

export interface GetGSLBFilter {
    conditions?: outputs.GetGSLBFilterCondition[];
    id?: string;
    names?: string[];
    tags?: string[];
}

export interface GetGSLBFilterCondition {
    name: string;
    values: string[];
}

export interface GetGSLBHealthCheck {
    delayLoop: number;
    hostHeader: string;
    path: string;
    port: number;
    protocol: string;
    status: string;
}

export interface GetGSLBServer {
    enabled: boolean;
    ipAddress: string;
    weight: number;
}

export interface GetIconFilter {
    conditions?: outputs.GetIconFilterCondition[];
    id?: string;
    names?: string[];
    tags?: string[];
}

export interface GetIconFilterCondition {
    name: string;
    values: string[];
}

export interface GetInternetFilter {
    conditions?: outputs.GetInternetFilterCondition[];
    id?: string;
    names?: string[];
    tags?: string[];
}

export interface GetInternetFilterCondition {
    name: string;
    values: string[];
}

export interface GetLoadBalancerFilter {
    conditions?: outputs.GetLoadBalancerFilterCondition[];
    id?: string;
    names?: string[];
    tags?: string[];
}

export interface GetLoadBalancerFilterCondition {
    name: string;
    values: string[];
}

export interface GetLoadBalancerNetworkInterface {
    gateway: string;
    ipAddresses: string[];
    netmask: number;
    switchId: string;
    vrid: number;
}

export interface GetLoadBalancerVip {
    delayLoop: number;
    description: string;
    port: number;
    servers: outputs.GetLoadBalancerVipServer[];
    sorryServer: string;
    vip: string;
}

export interface GetLoadBalancerVipServer {
    enabled: boolean;
    ipAddress: string;
    path: string;
    protocol: string;
    status: string;
}

export interface GetLocalRouterFilter {
    conditions?: outputs.GetLocalRouterFilterCondition[];
    id?: string;
    names?: string[];
    tags?: string[];
}

export interface GetLocalRouterFilterCondition {
    name: string;
    values: string[];
}

export interface GetLocalRouterNetworkInterface {
    ipAddresses: string[];
    netmask: number;
    vip: string;
    vrid: number;
}

export interface GetLocalRouterPeer {
    description: string;
    enabled: boolean;
    peerId: string;
    secretKey: string;
}

export interface GetLocalRouterStaticRoute {
    nextHop: string;
    prefix: string;
}

export interface GetLocalRouterSwitch {
    category: string;
    code: string;
    zoneId: string;
}

export interface GetNFSFilter {
    conditions?: outputs.GetNFSFilterCondition[];
    id?: string;
    names?: string[];
    tags?: string[];
}

export interface GetNFSFilterCondition {
    name: string;
    values: string[];
}

export interface GetNFSNetworkInterface {
    gateway: string;
    ipAddress: string;
    netmask: number;
    switchId: string;
}

export interface GetNoteFilter {
    conditions?: outputs.GetNoteFilterCondition[];
    id?: string;
    names?: string[];
    tags?: string[];
}

export interface GetNoteFilterCondition {
    name: string;
    values: string[];
}

export interface GetPacketFilterExpression {
    allow: boolean;
    description: string;
    destinationPort: string;
    protocol: string;
    sourceNetwork: string;
    sourcePort: string;
}

export interface GetPacketFilterFilter {
    conditions?: outputs.GetPacketFilterFilterCondition[];
    id?: string;
    names?: string[];
}

export interface GetPacketFilterFilterCondition {
    name: string;
    values: string[];
}

export interface GetPrivateHostFilter {
    conditions?: outputs.GetPrivateHostFilterCondition[];
    id?: string;
    names?: string[];
    tags?: string[];
}

export interface GetPrivateHostFilterCondition {
    name: string;
    values: string[];
}

export interface GetProxyLBBindPort {
    port: number;
    proxyMode: string;
    redirectToHttps: boolean;
    responseHeaders: outputs.GetProxyLBBindPortResponseHeader[];
    supportHttp2: boolean;
}

export interface GetProxyLBBindPortResponseHeader {
    header: string;
    value: string;
}

export interface GetProxyLBCertificate {
    additionalCertificates: outputs.GetProxyLBCertificateAdditionalCertificate[];
    intermediateCert: string;
    privateKey: string;
    serverCert: string;
}

export interface GetProxyLBCertificateAdditionalCertificate {
    intermediateCert: string;
    privateKey: string;
    serverCert: string;
}

export interface GetProxyLBFilter {
    conditions?: outputs.GetProxyLBFilterCondition[];
    id?: string;
    names?: string[];
    tags?: string[];
}

export interface GetProxyLBFilterCondition {
    name: string;
    values: string[];
}

export interface GetProxyLBHealthCheck {
    delayLoop: number;
    hostHeader: string;
    path: string;
    port: number;
    protocol: string;
}

export interface GetProxyLBRule {
    group: string;
    host: string;
    path: string;
}

export interface GetProxyLBServer {
    enabled: boolean;
    group: string;
    ipAddress: string;
    port: number;
}

export interface GetProxyLBSorryServer {
    ipAddress: string;
    port: number;
}

export interface GetSSHKeyFilter {
    conditions?: outputs.GetSSHKeyFilterCondition[];
    id?: string;
    names?: string[];
}

export interface GetSSHKeyFilterCondition {
    name: string;
    values: string[];
}

export interface GetServerFilter {
    conditions?: outputs.GetServerFilterCondition[];
    id?: string;
    names?: string[];
    tags?: string[];
}

export interface GetServerFilterCondition {
    name: string;
    values: string[];
}

export interface GetServerNetworkInterface {
    macAddress: string;
    packetFilterId: string;
    upstream: string;
    userIpAddress: string;
}

export interface GetSimpleMonitorFilter {
    conditions?: outputs.GetSimpleMonitorFilterCondition[];
    id?: string;
    names?: string[];
    tags?: string[];
}

export interface GetSimpleMonitorFilterCondition {
    name: string;
    values: string[];
}

export interface GetSimpleMonitorHealthCheck {
    community: string;
    excepctedData: string;
    hostHeader: string;
    oid: string;
    password: string;
    path: string;
    port: number;
    protocol: string;
    qname: string;
    remainingDays: number;
    sni: boolean;
    snmpVersion: string;
    status: number;
    username: string;
}

export interface GetSwitchFilter {
    conditions?: outputs.GetSwitchFilterCondition[];
    id?: string;
    names?: string[];
    tags?: string[];
}

export interface GetSwitchFilterCondition {
    name: string;
    values: string[];
}

export interface GetVPCRouterDhcpServer {
    dnsServers: string[];
    interfaceIndex: number;
    rangeStart: string;
    rangeStop: string;
}

export interface GetVPCRouterDhcpStaticMapping {
    ipAddress: string;
    macAddress: string;
}

export interface GetVPCRouterFilter {
    conditions?: outputs.GetVPCRouterFilterCondition[];
    id?: string;
    names?: string[];
    tags?: string[];
}

export interface GetVPCRouterFilterCondition {
    name: string;
    values: string[];
}

export interface GetVPCRouterFirewall {
    direction: string;
    expressions: outputs.GetVPCRouterFirewallExpression[];
    interfaceIndex: number;
}

export interface GetVPCRouterFirewallExpression {
    allow: boolean;
    description: string;
    destinationNetwork: string;
    destinationPort: string;
    logging: boolean;
    protocol: string;
    sourceNetwork: string;
    sourcePort: string;
}

export interface GetVPCRouterL2tp {
    preSharedSecret: string;
    rangeStart: string;
    rangeStop: string;
}

export interface GetVPCRouterPortForwarding {
    description: string;
    privateIp: string;
    privatePort: number;
    protocol: string;
    publicPort: number;
}

export interface GetVPCRouterPptp {
    rangeStart: string;
    rangeStop: string;
}

export interface GetVPCRouterPrivateNetworkInterface {
    index: number;
    ipAddresses: string[];
    netmask: number;
    switchId: string;
    vip: string;
}

export interface GetVPCRouterPublicNetworkInterface {
    aliases: string[];
    ipAddresses: string[];
    switchId: string;
    vip: string;
    vrid: number;
}

export interface GetVPCRouterSiteToSiteVpn {
    localPrefixes: string[];
    peer: string;
    preSharedSecret: string;
    remoteId: string;
    routes: string[];
}

export interface GetVPCRouterStaticNat {
    description: string;
    privateIp: string;
    publicIp: string;
}

export interface GetVPCRouterStaticRoute {
    nextHop: string;
    prefix: string;
}

export interface GetVPCRouterUser {
    name: string;
    password: string;
}

export interface LoadBalancerNetworkInterface {
    gateway?: pulumi.Input<string>;
    ipAddresses: pulumi.Input<pulumi.Input<string>[]>;
    netmask: pulumi.Input<number>;
    switchId: pulumi.Input<string>;
    vrid: pulumi.Input<number>;
}

export interface LoadBalancerVip {
    delayLoop?: pulumi.Input<number>;
    description?: pulumi.Input<string>;
    port: pulumi.Input<number>;
    servers?: pulumi.Input<pulumi.Input<outputs.LoadBalancerVipServer>[]>;
    sorryServer?: pulumi.Input<string>;
    vip: pulumi.Input<string>;
}

export interface LoadBalancerVipServer {
    enabled?: pulumi.Input<boolean>;
    ipAddress: pulumi.Input<string>;
    path?: pulumi.Input<string>;
    protocol: pulumi.Input<string>;
    status?: pulumi.Input<string>;
}

export interface LocalRouterNetworkInterface {
    ipAddresses: pulumi.Input<pulumi.Input<string>[]>;
    netmask: pulumi.Input<number>;
    vip: pulumi.Input<string>;
    vrid: pulumi.Input<number>;
}

export interface LocalRouterPeer {
    description?: pulumi.Input<string>;
    enabled?: pulumi.Input<boolean>;
    peerId: pulumi.Input<string>;
    secretKey: pulumi.Input<string>;
}

export interface LocalRouterStaticRoute {
    nextHop: pulumi.Input<string>;
    prefix: pulumi.Input<string>;
}

export interface LocalRouterSwitch {
    category?: pulumi.Input<string>;
    code: pulumi.Input<string>;
    zoneId: pulumi.Input<string>;
}

export interface MobileGatewayPrivateNetworkInterface {
    ipAddress: pulumi.Input<string>;
    netmask: pulumi.Input<number>;
    switchId: pulumi.Input<string>;
}

export interface MobileGatewaySim {
    ipAddress: pulumi.Input<string>;
    simId: pulumi.Input<string>;
}

export interface MobileGatewaySimRoute {
    prefix: pulumi.Input<string>;
    simId: pulumi.Input<string>;
}

export interface MobileGatewayStaticRoute {
    nextHop: pulumi.Input<string>;
    prefix: pulumi.Input<string>;
}

export interface MobileGatewayTrafficControl {
    autoTrafficShaping?: pulumi.Input<boolean>;
    bandWidthLimit?: pulumi.Input<number>;
    enableEmail?: pulumi.Input<boolean>;
    enableSlack?: pulumi.Input<boolean>;
    quota: pulumi.Input<number>;
    slackWebhook?: pulumi.Input<string>;
}

export interface NFSNetworkInterface {
    gateway?: pulumi.Input<string>;
    ipAddress: pulumi.Input<string>;
    netmask: pulumi.Input<number>;
    switchId: pulumi.Input<string>;
}

export interface PacketFilterExpression {
    allow?: pulumi.Input<boolean>;
    description?: pulumi.Input<string>;
    destinationPort?: pulumi.Input<string>;
    protocol: pulumi.Input<string>;
    sourceNetwork?: pulumi.Input<string>;
    sourcePort?: pulumi.Input<string>;
}

export interface PacketFilterRuleExpression {
    allow?: pulumi.Input<boolean>;
    description?: pulumi.Input<string>;
    destinationPort?: pulumi.Input<string>;
    protocol: pulumi.Input<string>;
    sourceNetwork?: pulumi.Input<string>;
    sourcePort?: pulumi.Input<string>;
}

export interface ProxyLBACMECertificate {
    additionalCertificates?: pulumi.Input<pulumi.Input<outputs.ProxyLBACMECertificateAdditionalCertificate>[]>;
    intermediateCert?: pulumi.Input<string>;
    privateKey?: pulumi.Input<string>;
    serverCert?: pulumi.Input<string>;
}

export interface ProxyLBACMECertificateAdditionalCertificate {
    intermediateCert?: pulumi.Input<string>;
    privateKey?: pulumi.Input<string>;
    serverCert?: pulumi.Input<string>;
}

export interface ProxyLBBindPort {
    port?: pulumi.Input<number>;
    proxyMode: pulumi.Input<string>;
    redirectToHttps?: pulumi.Input<boolean>;
    responseHeaders?: pulumi.Input<pulumi.Input<outputs.ProxyLBBindPortResponseHeader>[]>;
    supportHttp2?: pulumi.Input<boolean>;
}

export interface ProxyLBBindPortResponseHeader {
    header: pulumi.Input<string>;
    value: pulumi.Input<string>;
}

export interface ProxyLBCertificate {
    additionalCertificates?: pulumi.Input<pulumi.Input<outputs.ProxyLBCertificateAdditionalCertificate>[]>;
    intermediateCert?: pulumi.Input<string>;
    privateKey?: pulumi.Input<string>;
    serverCert?: pulumi.Input<string>;
}

export interface ProxyLBCertificateAdditionalCertificate {
    intermediateCert?: pulumi.Input<string>;
    privateKey: pulumi.Input<string>;
    serverCert: pulumi.Input<string>;
}

export interface ProxyLBHealthCheck {
    delayLoop?: pulumi.Input<number>;
    hostHeader?: pulumi.Input<string>;
    path?: pulumi.Input<string>;
    port?: pulumi.Input<number>;
    protocol: pulumi.Input<string>;
}

export interface ProxyLBRule {
    group?: pulumi.Input<string>;
    host?: pulumi.Input<string>;
    path?: pulumi.Input<string>;
}

export interface ProxyLBServer {
    enabled?: pulumi.Input<boolean>;
    group?: pulumi.Input<string>;
    ipAddress: pulumi.Input<string>;
    port: pulumi.Input<number>;
}

export interface ProxyLBSorryServer {
    ipAddress: pulumi.Input<string>;
    port?: pulumi.Input<number>;
}

export interface ServerDiskEditParameter {
    changePartitionUuid?: pulumi.Input<boolean>;
    disablePwAuth?: pulumi.Input<boolean>;
    enableDhcp?: pulumi.Input<boolean>;
    gateway?: pulumi.Input<string>;
    hostname?: pulumi.Input<string>;
    ipAddress?: pulumi.Input<string>;
    netmask?: pulumi.Input<number>;
    noteIds?: pulumi.Input<pulumi.Input<string>[]>;
    password?: pulumi.Input<string>;
    sshKeyIds?: pulumi.Input<pulumi.Input<string>[]>;
}

export interface ServerNetworkInterface {
    macAddress?: pulumi.Input<string>;
    packetFilterId?: pulumi.Input<string>;
    upstream: pulumi.Input<string>;
    userIpAddress?: pulumi.Input<string>;
}

export interface SimpleMonitorHealthCheck {
    community?: pulumi.Input<string>;
    excepctedData?: pulumi.Input<string>;
    hostHeader?: pulumi.Input<string>;
    oid?: pulumi.Input<string>;
    password?: pulumi.Input<string>;
    path?: pulumi.Input<string>;
    port?: pulumi.Input<number>;
    protocol: pulumi.Input<string>;
    qname?: pulumi.Input<string>;
    remainingDays?: pulumi.Input<number>;
    sni?: pulumi.Input<boolean>;
    snmpVersion?: pulumi.Input<string>;
    status?: pulumi.Input<number>;
    username?: pulumi.Input<string>;
}

export interface VPCRouterDhcpServer {
    dnsServers?: pulumi.Input<pulumi.Input<string>[]>;
    interfaceIndex: pulumi.Input<number>;
    rangeStart: pulumi.Input<string>;
    rangeStop: pulumi.Input<string>;
}

export interface VPCRouterDhcpStaticMapping {
    ipAddress: pulumi.Input<string>;
    macAddress: pulumi.Input<string>;
}

export interface VPCRouterFirewall {
    direction: pulumi.Input<string>;
    expressions: pulumi.Input<pulumi.Input<outputs.VPCRouterFirewallExpression>[]>;
    interfaceIndex?: pulumi.Input<number>;
}

export interface VPCRouterFirewallExpression {
    allow: pulumi.Input<boolean>;
    description?: pulumi.Input<string>;
    destinationNetwork?: pulumi.Input<string>;
    destinationPort?: pulumi.Input<string>;
    logging?: pulumi.Input<boolean>;
    protocol: pulumi.Input<string>;
    sourceNetwork?: pulumi.Input<string>;
    sourcePort?: pulumi.Input<string>;
}

export interface VPCRouterL2tp {
    preSharedSecret: pulumi.Input<string>;
    rangeStart: pulumi.Input<string>;
    rangeStop: pulumi.Input<string>;
}

export interface VPCRouterPortForwarding {
    description?: pulumi.Input<string>;
    privateIp: pulumi.Input<string>;
    privatePort: pulumi.Input<number>;
    protocol: pulumi.Input<string>;
    publicPort: pulumi.Input<number>;
}

export interface VPCRouterPptp {
    rangeStart: pulumi.Input<string>;
    rangeStop: pulumi.Input<string>;
}

export interface VPCRouterPrivateNetworkInterface {
    index: pulumi.Input<number>;
    ipAddresses: pulumi.Input<pulumi.Input<string>[]>;
    netmask: pulumi.Input<number>;
    switchId: pulumi.Input<string>;
    vip?: pulumi.Input<string>;
}

export interface VPCRouterPublicNetworkInterface {
    aliases?: pulumi.Input<pulumi.Input<string>[]>;
    ipAddresses?: pulumi.Input<pulumi.Input<string>[]>;
    switchId?: pulumi.Input<string>;
    vip?: pulumi.Input<string>;
    vrid?: pulumi.Input<number>;
}

export interface VPCRouterSiteToSiteVpn {
    localPrefixes: pulumi.Input<pulumi.Input<string>[]>;
    peer: pulumi.Input<string>;
    preSharedSecret: pulumi.Input<string>;
    remoteId: pulumi.Input<string>;
    routes: pulumi.Input<pulumi.Input<string>[]>;
}

export interface VPCRouterStaticNat {
    description?: pulumi.Input<string>;
    privateIp: pulumi.Input<string>;
    publicIp: pulumi.Input<string>;
}

export interface VPCRouterStaticRoute {
    nextHop: pulumi.Input<string>;
    prefix: pulumi.Input<string>;
}

export interface VPCRouterUser {
    name: pulumi.Input<string>;
    password: pulumi.Input<string>;
}
