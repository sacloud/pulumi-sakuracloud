// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package sakuracloud

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

func LookupVPCRouter(ctx *pulumi.Context, args *LookupVPCRouterArgs, opts ...pulumi.InvokeOption) (*LookupVPCRouterResult, error) {
	var rv LookupVPCRouterResult
	err := ctx.Invoke("sakuracloud:index/getVPCRouter:getVPCRouter", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getVPCRouter.
type LookupVPCRouterArgs struct {
	Filter *GetVPCRouterFilter `pulumi:"filter"`
	Zone *string `pulumi:"zone"`
}


// A collection of values returned by getVPCRouter.
type LookupVPCRouterResult struct {
	Description string `pulumi:"description"`
	DhcpServers []GetVPCRouterDhcpServer `pulumi:"dhcpServers"`
	DhcpStaticMappings []GetVPCRouterDhcpStaticMapping `pulumi:"dhcpStaticMappings"`
	Filter *GetVPCRouterFilter `pulumi:"filter"`
	Firewalls []GetVPCRouterFirewall `pulumi:"firewalls"`
	IconId string `pulumi:"iconId"`
	// id is the provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	InternetConnection bool `pulumi:"internetConnection"`
	L2tps []GetVPCRouterL2tp `pulumi:"l2tps"`
	Name string `pulumi:"name"`
	Plan string `pulumi:"plan"`
	PortForwardings []GetVPCRouterPortForwarding `pulumi:"portForwardings"`
	Pptps []GetVPCRouterPptp `pulumi:"pptps"`
	PrivateNetworkInterfaces []GetVPCRouterPrivateNetworkInterface `pulumi:"privateNetworkInterfaces"`
	PublicIp string `pulumi:"publicIp"`
	PublicNetmask int `pulumi:"publicNetmask"`
	PublicNetworkInterfaces []GetVPCRouterPublicNetworkInterface `pulumi:"publicNetworkInterfaces"`
	SiteToSiteVpns []GetVPCRouterSiteToSiteVpn `pulumi:"siteToSiteVpns"`
	StaticNats []GetVPCRouterStaticNat `pulumi:"staticNats"`
	StaticRoutes []GetVPCRouterStaticRoute `pulumi:"staticRoutes"`
	SyslogHost string `pulumi:"syslogHost"`
	Tags []string `pulumi:"tags"`
	Users []GetVPCRouterUser `pulumi:"users"`
	Zone string `pulumi:"zone"`
}

