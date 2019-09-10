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

package sakuracloud

import (
	"unicode"

	"github.com/hashicorp/terraform/helper/schema"
	"github.com/hashicorp/terraform/terraform"
	"github.com/pulumi/pulumi-terraform/pkg/tfbridge"
	"github.com/pulumi/pulumi/pkg/resource"
	"github.com/pulumi/pulumi/pkg/tokens"
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

// boolRef returns a reference to the bool argument.
func boolRef(b bool) *bool {
	return &b
}

// stringValue gets a string value from a property map if present, else ""
func stringValue(vars resource.PropertyMap, prop resource.PropertyKey) string {
	val, ok := vars[prop]
	if ok && val.IsString() {
		return val.StringValue()
	}
	return ""
}

// preConfigureCallback is called before the providerConfigure function of the underlying provider.
// It should validate that the provider can be configured, and provide actionable errors in the case
// it cannot be. Configuration variables can be read from `vars` using the `stringValue` function -
// for example `stringValue(vars, "accessKey")`.
func preConfigureCallback(vars resource.PropertyMap, c *terraform.ResourceConfig) error {
	return nil
}

// managedByPulumi is a default used for some managed resources, in the absence of something more meaningful.
var managedByPulumi = &tfbridge.DefaultInfo{Value: "Managed by Pulumi"}

// Provider returns additional overlaid schema and metadata associated with the provider..
func Provider() tfbridge.ProviderInfo {
	// Instantiate the Terraform provider
	p := sakuracloud.Provider().(*schema.Provider)

	// Create a Pulumi provider mapping
	prov := tfbridge.ProviderInfo{
		P:           p,
		Name:        "sakuracloud",
		Description: "A Pulumi package for creating and managing SakuraCloud resources.",
		Keywords:    []string{"pulumi", "sakuracloud"},
		License:     "Apache-2.0",
		Homepage:    "https://github.com/sacloud/pulumi-sakuracloud",
		Repository:  "https://github.com/sacloud/pulumi-sakuracloud",
		GitHubOrg:   "sacloud",
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
			"zone": {
				Default: &tfbridge.DefaultInfo{
					Value:   "is1b",
					EnvVars: []string{"SAKURACLOUD_ZONE"},
				},
			},
		},
		PreConfigureCallback: preConfigureCallback,
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
			"sakuracloud_archive":                     {Tok: makeResource(mainMod, "Archive")},
			"sakuracloud_auto_backup":                 {Tok: makeResource(mainMod, "AutoBackup")},
			"sakuracloud_bridge":                      {Tok: makeResource(mainMod, "Bridge")},
			"sakuracloud_bucket_object":               {Tok: makeResource(mainMod, "BucketObject")},
			"sakuracloud_cdrom":                       {Tok: makeResource(mainMod, "CDROM")},
			"sakuracloud_database":                    {Tok: makeResource(mainMod, "Database")},
			"sakuracloud_database_read_replica":       {Tok: makeResource(mainMod, "DatabaseReadReplica")},
			"sakuracloud_disk":                        {Tok: makeResource(mainMod, "Disk")},
			"sakuracloud_dns":                         {Tok: makeResource(mainMod, "DNS")},
			"sakuracloud_dns_record":                  {Tok: makeResource(mainMod, "DNSRecord")},
			"sakuracloud_gslb":                        {Tok: makeResource(mainMod, "GSLB")},
			"sakuracloud_gslb_server":                 {Tok: makeResource(mainMod, "GSLBServer")},
			"sakuracloud_icon":                        {Tok: makeResource(mainMod, "Icon")},
			"sakuracloud_internet":                    {Tok: makeResource(mainMod, "Internet")},
			"sakuracloud_ipv4_ptr":                    {Tok: makeResource(mainMod, "IPv4Ptr")},
			"sakuracloud_load_balancer":               {Tok: makeResource(mainMod, "LoadBalancer")},
			"sakuracloud_mobile_gateway":              {Tok: makeResource(mainMod, "MobileGateway")},
			"sakuracloud_mobile_gateway_sim_route":    {Tok: makeResource(mainMod, "MobileGatewaySIMRoute")},
			"sakuracloud_mobile_gateway_static_route": {Tok: makeResource(mainMod, "MobileGatewayStaticRoute")},
			"sakuracloud_nfs":                         {Tok: makeResource(mainMod, "NFS")},
			"sakuracloud_note":                        {Tok: makeResource(mainMod, "Note")},
			"sakuracloud_packet_filter":               {Tok: makeResource(mainMod, "PacketFilter")},
			"sakuracloud_packet_filter_rule":          {Tok: makeResource(mainMod, "PacketFilterRule")},
			"sakuracloud_private_host":                {Tok: makeResource(mainMod, "PrivateHost")},
			"sakuracloud_proxylb":                     {Tok: makeResource(mainMod, "ProxyLB")},
			"sakuracloud_proxylb_acme":                {Tok: makeResource(mainMod, "ProxyLBACME")},
			"sakuracloud_server":                      {Tok: makeResource(mainMod, "Server")},
			"sakuracloud_sim":                         {Tok: makeResource(mainMod, "SIM")},
			"sakuracloud_simple_monitor":              {Tok: makeResource(mainMod, "SimpleMonitor")},
			"sakuracloud_ssh_key":                     {Tok: makeResource(mainMod, "SSHKey")},
			"sakuracloud_ssh_key_gen":                 {Tok: makeResource(mainMod, "SSHKeyGen")},
			"sakuracloud_subnet":                      {Tok: makeResource(mainMod, "Subnet")},
			"sakuracloud_switch":                      {Tok: makeResource(mainMod, "Switch")},
			"sakuracloud_vpc_router":                  {Tok: makeResource(mainMod, "VPCRouter")},
		},
		DataSources: map[string]*tfbridge.DataSourceInfo{
			// Map each resource in the Terraform provider to a Pulumi function. An example
			// is below.
			// "aws_ami": {Tok: makeDataSource(mainMod, "getAmi")},
			"sakuracloud_archive":        {Tok: makeDataSource(mainMod, "getArchive")},
			"sakuracloud_bridge":         {Tok: makeDataSource(mainMod, "getBridge")},
			"sakuracloud_bucket_object":  {Tok: makeDataSource(mainMod, "getBucketObject")},
			"sakuracloud_cdrom":          {Tok: makeDataSource(mainMod, "getCDROM")},
			"sakuracloud_database":       {Tok: makeDataSource(mainMod, "getDatabase")},
			"sakuracloud_disk":           {Tok: makeDataSource(mainMod, "getDisk")},
			"sakuracloud_dns":            {Tok: makeDataSource(mainMod, "getDNS")},
			"sakuracloud_gslb":           {Tok: makeDataSource(mainMod, "getGSLB")},
			"sakuracloud_icon":           {Tok: makeDataSource(mainMod, "getIcon")},
			"sakuracloud_internet":       {Tok: makeDataSource(mainMod, "getInternet")},
			"sakuracloud_load_balancer":  {Tok: makeDataSource(mainMod, "getLoadBalancer")},
			"sakuracloud_nfs":            {Tok: makeDataSource(mainMod, "getNFS")},
			"sakuracloud_note":           {Tok: makeDataSource(mainMod, "getNote")},
			"sakuracloud_packet_filter":  {Tok: makeDataSource(mainMod, "getPacketFilter")},
			"sakuracloud_private_host":   {Tok: makeDataSource(mainMod, "getPrivateHost")},
			"sakuracloud_proxylb":        {Tok: makeDataSource(mainMod, "getProxyLB")},
			"sakuracloud_server":         {Tok: makeDataSource(mainMod, "getServer")},
			"sakuracloud_simple_monitor": {Tok: makeDataSource(mainMod, "getSimpleMonitor")},
			"sakuracloud_ssh_key":        {Tok: makeDataSource(mainMod, "getSSHKey")},
			"sakuracloud_subnet":         {Tok: makeDataSource(mainMod, "getSubnet")},
			"sakuracloud_switch":         {Tok: makeDataSource(mainMod, "getSwitch")},
			"sakuracloud_vpc_router":     {Tok: makeDataSource(mainMod, "getVPCRouter")},
			"sakuracloud_zone":           {Tok: makeDataSource(mainMod, "getZone")},
		},
		JavaScript: &tfbridge.JavaScriptInfo{
			// List any npm dependencies and their versions
			Dependencies: map[string]string{
				"@pulumi/pulumi": "latest",
			},
			DevDependencies: map[string]string{
				"@types/node": "^8.0.25", // so we can access strongly typed node definitions.
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
				"pulumi": ">=1.0.0,<2.0.0",
			},
		},
	}

	// For all resources with name properties, we will add an auto-name property.  Make sure to skip those that
	// already have a name mapping entry, since those may have custom overrides set above (e.g., for length).
	const nameProperty = "name"
	for resname, res := range prov.Resources {
		if schema := p.ResourcesMap[resname]; schema != nil {
			// Only apply auto-name to input properties (Optional || Required) named `name`
			if tfs, has := schema.Schema[nameProperty]; has && (tfs.Optional || tfs.Required) {
				if _, hasfield := res.Fields[nameProperty]; !hasfield {
					if res.Fields == nil {
						res.Fields = make(map[string]*tfbridge.SchemaInfo)
					}
					res.Fields[nameProperty] = tfbridge.AutoName(nameProperty, 255)
				}
			}
		}
	}

	return prov
}
