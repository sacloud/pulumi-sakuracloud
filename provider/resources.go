// Copyright 2016-2018, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package provider

import (
	"fmt"
	"path/filepath"
	"unicode"

	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge"
	shim "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfshim"
	shimv2 "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfshim/sdk-v2"
	"github.com/pulumi/pulumi/sdk/v3/go/common/resource"
	"github.com/pulumi/pulumi/sdk/v3/go/common/tokens"
	"github.com/sacloud/pulumi-sakuracloud/provider/pkg/version"
	"github.com/sacloud/terraform-provider-sakuracloud/sakuracloud"
)

// all of the token components used below.
const (
	// packages:
	mainPkg = "sakuracloud"
	// modules:
	mainMod = "index" // the y module
)

// makeMember manufactures a type token for the package and the given module and type.
func makeMember(mod string, mem string) tokens.ModuleMember {
	return tokens.ModuleMember(mainPkg + ":" + mod + ":" + mem)
}

// makeType manufactures a type token for the package and the given module and type.
func makeType(mod string, typ string) tokens.Type {
	return tokens.Type(makeMember(mod, typ))
}

// makeDataSource manufactures a standard resource token given a module and resource name.  It
// automatically uses the main package and names the file by simply lower casing the data source's
// first character.
func makeDataSource(mod string, res string) tokens.ModuleMember {
	fn := string(unicode.ToLower(rune(res[0]))) + res[1:]
	return makeMember(mod+"/"+fn, res)
}

// makeResource manufactures a standard resource token given a module and resource name.  It
// automatically uses the main package and names the file by simply lower casing the resource's
// first character.
func makeResource(mod string, res string) tokens.Type {
	fn := string(unicode.ToLower(rune(res[0]))) + res[1:]
	return makeType(mod+"/"+fn, res)
}

// preConfigureCallback is called before the providerConfigure function of the underlying provider.
// It should validate that the provider can be configured, and provide actionable errors in the case
// it cannot be. Configuration variables can be read from `vars` using the `stringValue` function -
// for example `stringValue(vars, "accessKey")`.
func preConfigureCallback(vars resource.PropertyMap, c shim.ResourceConfig) error {
	return nil
}

// managedByPulumi is a default used for some managed resources, in the absence of something more meaningful.
var managedByPulumi = &tfbridge.DefaultInfo{Value: "Managed by Pulumi"}

// Provider returns additional overlaid schema and metadata associated with the provider..
func Provider() tfbridge.ProviderInfo {
	// Instantiate the Terraform provider
	p := shimv2.NewProvider(sakuracloud.Provider())

	// Create a Pulumi provider mapping
	prov := tfbridge.ProviderInfo{
		P:                    p,
		Name:                 "sakuracloud",
		Description:          "A Pulumi package for creating and managing SakuraCloud resources.",
		Keywords:             []string{"pulumi", "sakuracloud"},
		License:              "Apache-2.0",
		Homepage:             "https://github.com/sacloud/pulumi-sakuracloud",
		Repository:           "https://github.com/sacloud/pulumi-sakuracloud",
		GitHubOrg:            "sacloud",
		PreConfigureCallback: preConfigureCallback,
		Config: map[string]*tfbridge.SchemaInfo{
			"token": {
				Default: &tfbridge.DefaultInfo{
					Value:   "",
					EnvVars: []string{"SAKURACLOUD_ACCESS_TOKEN"},
				},
			},
			"secret": {
				Default: &tfbridge.DefaultInfo{
					Value:   "",
					EnvVars: []string{"SAKURACLOUD_ACCESS_TOKEN_SECRET"},
				},
			},
			"profile": {
				Default: &tfbridge.DefaultInfo{
					Value:   "default",
					EnvVars: []string{"SAKURACLOUD_PROFILE"},
				},
			},
			"zone": {
				Default: &tfbridge.DefaultInfo{
					Value:   "is1b",
					EnvVars: []string{"SAKURACLOUD_ZONE"},
				},
			},
		},
		Resources: map[string]*tfbridge.ResourceInfo{
			// Map each resource in the Terraform provider to a Pulumi type. Two examples
			// are below - the single line form is the common case. The multi-line form is
			// needed only if you wish to override types or other default options.
			//
			// "aws_iam_role": {Tok: makeResource(mainMod, "IamRole")}
			//
			// "aws_acm_certificate": {
			// 	Tok: makeResource(mainMod, "Certificate"),
			// 	Fields: map[string]*tfbridge.SchemaInfo{
			// 		"tags": {Type: makeType(mainPkg, "Tags")},
			// 	},
			// },
			"sakuracloud_auto_backup":           {Tok: makeResource(mainMod, "AutoBackup")},
			"sakuracloud_archive":               {Tok: makeResource(mainMod, "Archive")},
			"sakuracloud_archive_share":         {Tok: makeResource(mainMod, "ArchiveShare")},
			"sakuracloud_bridge":                {Tok: makeResource(mainMod, "Bridge")},
			"sakuracloud_cdrom":                 {Tok: makeResource(mainMod, "CDROM")},
			"sakuracloud_certificate_authority": {Tok: makeResource(mainMod, "CertificateAuthority")},
			"sakuracloud_container_registry":    {Tok: makeResource(mainMod, "ContainerRegistry")},
			"sakuracloud_enhanced_db":           {Tok: makeResource(mainMod, "EnhancedDB")},
			"sakuracloud_database":              {Tok: makeResource(mainMod, "Database")},
			"sakuracloud_database_read_replica": {Tok: makeResource(mainMod, "DatabaseReadReplica")},
			"sakuracloud_disk":                  {Tok: makeResource(mainMod, "Disk")},
			"sakuracloud_dns":                   {Tok: makeResource(mainMod, "DNS")},
			"sakuracloud_dns_record":            {Tok: makeResource(mainMod, "DNSRecord")},
			"sakuracloud_esme":                  {Tok: makeResource(mainMod, "ESME")},
			"sakuracloud_gslb":                  {Tok: makeResource(mainMod, "GSLB")},
			"sakuracloud_icon":                  {Tok: makeResource(mainMod, "Icon")},
			"sakuracloud_internet":              {Tok: makeResource(mainMod, "Internet")},
			"sakuracloud_ipv4_ptr":              {Tok: makeResource(mainMod, "IPv4Ptr")},
			"sakuracloud_load_balancer":         {Tok: makeResource(mainMod, "LoadBalancer")},
			"sakuracloud_local_router":          {Tok: makeResource(mainMod, "LocalRouter")},
			"sakuracloud_mobile_gateway":        {Tok: makeResource(mainMod, "MobileGateway")},
			"sakuracloud_nfs":                   {Tok: makeResource(mainMod, "NFS")},
			"sakuracloud_note":                  {Tok: makeResource(mainMod, "Note")},
			"sakuracloud_packet_filter":         {Tok: makeResource(mainMod, "PacketFilter")},
			"sakuracloud_packet_filter_rules":   {Tok: makeResource(mainMod, "PacketFilterRule")},
			"sakuracloud_private_host":          {Tok: makeResource(mainMod, "PrivateHost")},
			"sakuracloud_proxylb":               {Tok: makeResource(mainMod, "ProxyLB")},
			"sakuracloud_proxylb_acme":          {Tok: makeResource(mainMod, "ProxyLBACME")},
			"sakuracloud_server":                {Tok: makeResource(mainMod, "Server")},
			"sakuracloud_sim":                   {Tok: makeResource(mainMod, "SIM")},
			"sakuracloud_simple_monitor":        {Tok: makeResource(mainMod, "SimpleMonitor")},
			"sakuracloud_ssh_key":               {Tok: makeResource(mainMod, "SSHKey")},
			"sakuracloud_ssh_key_gen":           {Tok: makeResource(mainMod, "SSHKeyGen")},
			"sakuracloud_subnet":                {Tok: makeResource(mainMod, "Subnet")},
			"sakuracloud_switch":                {Tok: makeResource(mainMod, "Switch")},
			"sakuracloud_vpc_router":            {Tok: makeResource(mainMod, "VPCRouter")},
			"sakuracloud_webaccel_certificate":  {Tok: makeResource(mainMod, "WebAccelCertificate")},
		},
		DataSources: map[string]*tfbridge.DataSourceInfo{
			// Map each resource in the Terraform provider to a Pulumi function. An example
			// is below.
			// "aws_ami": {Tok: makeDataSource(mainMod, "getAmi")},
			"sakuracloud_archive":               {Tok: makeDataSource(mainMod, "getArchive")},
			"sakuracloud_bridge":                {Tok: makeDataSource(mainMod, "getBridge")},
			"sakuracloud_cdrom":                 {Tok: makeDataSource(mainMod, "getCDROM")},
			"sakuracloud_certificate_authority": {Tok: makeDataSource(mainMod, "getCertificateAuthority")},
			"sakuracloud_container_registry":    {Tok: makeDataSource(mainMod, "getContainerRegistry")},
			"sakuracloud_enhanced_db":           {Tok: makeDataSource(mainMod, "getEnhancedDB")},
			"sakuracloud_database":              {Tok: makeDataSource(mainMod, "getDatabase")},
			"sakuracloud_disk":                  {Tok: makeDataSource(mainMod, "getDisk")},
			"sakuracloud_dns":                   {Tok: makeDataSource(mainMod, "getDNS")},
			"sakuracloud_esme":                  {Tok: makeDataSource(mainMod, "getESME")},
			"sakuracloud_gslb":                  {Tok: makeDataSource(mainMod, "getGSLB")},
			"sakuracloud_icon":                  {Tok: makeDataSource(mainMod, "getIcon")},
			"sakuracloud_internet":              {Tok: makeDataSource(mainMod, "getInternet")},
			"sakuracloud_load_balancer":         {Tok: makeDataSource(mainMod, "getLoadBalancer")},
			"sakuracloud_local_router":          {Tok: makeDataSource(mainMod, "getLocalRouter")},
			"sakuracloud_nfs":                   {Tok: makeDataSource(mainMod, "getNFS")},
			"sakuracloud_note":                  {Tok: makeDataSource(mainMod, "getNote")},
			"sakuracloud_packet_filter":         {Tok: makeDataSource(mainMod, "getPacketFilter")},
			"sakuracloud_private_host":          {Tok: makeDataSource(mainMod, "getPrivateHost")},
			"sakuracloud_proxylb":               {Tok: makeDataSource(mainMod, "getProxyLB")},
			"sakuracloud_server":                {Tok: makeDataSource(mainMod, "getServer")},
			"sakuracloud_server_vnc_info":       {Tok: makeDataSource(mainMod, "getServerVNCInfo")},
			"sakuracloud_simple_monitor":        {Tok: makeDataSource(mainMod, "getSimpleMonitor")},
			"sakuracloud_ssh_key":               {Tok: makeDataSource(mainMod, "getSSHKey")},
			"sakuracloud_subnet":                {Tok: makeDataSource(mainMod, "getSubnet")},
			"sakuracloud_switch":                {Tok: makeDataSource(mainMod, "getSwitch")},
			"sakuracloud_vpc_router":            {Tok: makeDataSource(mainMod, "getVPCRouter")},
			"sakuracloud_webaccel":              {Tok: makeDataSource(mainMod, "getWebAccel")},
			"sakuracloud_zone":                  {Tok: makeDataSource(mainMod, "getZone")},
		},
		JavaScript: &tfbridge.JavaScriptInfo{
			// List any npm dependencies and their versions
			Dependencies: map[string]string{
				"@pulumi/pulumi": "^3.0.0",
				"mime":           "^2.0.0",
			},
			DevDependencies: map[string]string{
				"@types/node": "^10.0.0", // so we can access strongly typed node definitions.
				"@types/mime": "^2.0.0",
			},
			// See the documentation for tfbridge.OverlayInfo for how to lay out this
			// section, or refer to the AWS provider. Delete this section if there are
			// no overlay files.
			//Overlay: &tfbridge.OverlayInfo{},
		},
		Python: &tfbridge.PythonInfo{
			// List any Python dependencies and their version ranges
			Requires: map[string]string{
				"pulumi": ">=3.0.0,<4.0.0",
			},
		},
		Golang: &tfbridge.GolangInfo{
			ImportBasePath: filepath.Join(
				fmt.Sprintf("github.com/sacloud/pulumi-%[1]s/sdk/", mainPkg),
				tfbridge.GetModuleMajorVersion(version.Version),
				"go",
				mainPkg,
			),
			GenerateResourceContainerTypes: true,
		},
		CSharp: &tfbridge.CSharpInfo{
			PackageReferences: map[string]string{
				"Pulumi": "3.*",
			},
		},
	}

	prov.SetAutonaming(255, "-")

	return prov
}
