// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package sakuracloud

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

func LookupSimpleMonitor(ctx *pulumi.Context, args *LookupSimpleMonitorArgs, opts ...pulumi.InvokeOption) (*LookupSimpleMonitorResult, error) {
	var rv LookupSimpleMonitorResult
	err := ctx.Invoke("sakuracloud:index/getSimpleMonitor:getSimpleMonitor", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getSimpleMonitor.
type LookupSimpleMonitorArgs struct {
	Filter *GetSimpleMonitorFilter `pulumi:"filter"`
}


// A collection of values returned by getSimpleMonitor.
type LookupSimpleMonitorResult struct {
	DelayLoop int `pulumi:"delayLoop"`
	Description string `pulumi:"description"`
	Enabled bool `pulumi:"enabled"`
	Filter *GetSimpleMonitorFilter `pulumi:"filter"`
	HealthChecks []GetSimpleMonitorHealthCheck `pulumi:"healthChecks"`
	IconId string `pulumi:"iconId"`
	// id is the provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	NotifyEmailEnabled bool `pulumi:"notifyEmailEnabled"`
	NotifyEmailHtml bool `pulumi:"notifyEmailHtml"`
	NotifyInterval int `pulumi:"notifyInterval"`
	NotifySlackEnabled bool `pulumi:"notifySlackEnabled"`
	NotifySlackWebhook string `pulumi:"notifySlackWebhook"`
	Tags []string `pulumi:"tags"`
	Target string `pulumi:"target"`
}

