// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sakuracloud

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Get information about an existing Simple Monitor.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-sakuracloud/sdk/go/sakuracloud"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := sakuracloud.LookupSimpleMonitor(ctx, &GetSimpleMonitorArgs{
// 			Filter: GetSimpleMonitorFilter{
// 				Names: []string{
// 					"foobar",
// 				},
// 			},
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
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
	// One or more values used for filtering, as defined below.
	Filter *GetSimpleMonitorFilter `pulumi:"filter"`
}

// A collection of values returned by getSimpleMonitor.
type LookupSimpleMonitorResult struct {
	// The interval in seconds between checks.
	DelayLoop int `pulumi:"delayLoop"`
	// The description of the SimpleMonitor.
	Description string `pulumi:"description"`
	// The flag to enable monitoring by the simple monitor.
	Enabled bool                    `pulumi:"enabled"`
	Filter  *GetSimpleMonitorFilter `pulumi:"filter"`
	// A list of `healthCheck` blocks as defined below.
	HealthChecks []GetSimpleMonitorHealthCheck `pulumi:"healthChecks"`
	// The icon id attached to the SimpleMonitor.
	IconId string `pulumi:"iconId"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// The flag to enable notification by email.
	NotifyEmailEnabled bool `pulumi:"notifyEmailEnabled"`
	// The flag to enable HTML format instead of text format.
	NotifyEmailHtml bool `pulumi:"notifyEmailHtml"`
	// The interval in hours between notification.
	NotifyInterval int `pulumi:"notifyInterval"`
	// The flag to enable notification by slack/discord.
	NotifySlackEnabled bool `pulumi:"notifySlackEnabled"`
	// The webhook URL for sending notification by slack/discord.
	NotifySlackWebhook string `pulumi:"notifySlackWebhook"`
	// Any tags assigned to the SimpleMonitor.
	Tags []string `pulumi:"tags"`
	// The monitoring target of the simple monitor. This will be IP address or FQDN.
	Target string `pulumi:"target"`
	// The timeout in seconds for monitoring.
	Timeout int `pulumi:"timeout"`
}

func LookupSimpleMonitorOutput(ctx *pulumi.Context, args LookupSimpleMonitorOutputArgs, opts ...pulumi.InvokeOption) LookupSimpleMonitorResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupSimpleMonitorResult, error) {
			args := v.(LookupSimpleMonitorArgs)
			r, err := LookupSimpleMonitor(ctx, &args, opts...)
			return *r, err
		}).(LookupSimpleMonitorResultOutput)
}

// A collection of arguments for invoking getSimpleMonitor.
type LookupSimpleMonitorOutputArgs struct {
	// One or more values used for filtering, as defined below.
	Filter GetSimpleMonitorFilterPtrInput `pulumi:"filter"`
}

func (LookupSimpleMonitorOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupSimpleMonitorArgs)(nil)).Elem()
}

// A collection of values returned by getSimpleMonitor.
type LookupSimpleMonitorResultOutput struct{ *pulumi.OutputState }

func (LookupSimpleMonitorResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupSimpleMonitorResult)(nil)).Elem()
}

func (o LookupSimpleMonitorResultOutput) ToLookupSimpleMonitorResultOutput() LookupSimpleMonitorResultOutput {
	return o
}

func (o LookupSimpleMonitorResultOutput) ToLookupSimpleMonitorResultOutputWithContext(ctx context.Context) LookupSimpleMonitorResultOutput {
	return o
}

// The interval in seconds between checks.
func (o LookupSimpleMonitorResultOutput) DelayLoop() pulumi.IntOutput {
	return o.ApplyT(func(v LookupSimpleMonitorResult) int { return v.DelayLoop }).(pulumi.IntOutput)
}

// The description of the SimpleMonitor.
func (o LookupSimpleMonitorResultOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v LookupSimpleMonitorResult) string { return v.Description }).(pulumi.StringOutput)
}

// The flag to enable monitoring by the simple monitor.
func (o LookupSimpleMonitorResultOutput) Enabled() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupSimpleMonitorResult) bool { return v.Enabled }).(pulumi.BoolOutput)
}

func (o LookupSimpleMonitorResultOutput) Filter() GetSimpleMonitorFilterPtrOutput {
	return o.ApplyT(func(v LookupSimpleMonitorResult) *GetSimpleMonitorFilter { return v.Filter }).(GetSimpleMonitorFilterPtrOutput)
}

// A list of `healthCheck` blocks as defined below.
func (o LookupSimpleMonitorResultOutput) HealthChecks() GetSimpleMonitorHealthCheckArrayOutput {
	return o.ApplyT(func(v LookupSimpleMonitorResult) []GetSimpleMonitorHealthCheck { return v.HealthChecks }).(GetSimpleMonitorHealthCheckArrayOutput)
}

// The icon id attached to the SimpleMonitor.
func (o LookupSimpleMonitorResultOutput) IconId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupSimpleMonitorResult) string { return v.IconId }).(pulumi.StringOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o LookupSimpleMonitorResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupSimpleMonitorResult) string { return v.Id }).(pulumi.StringOutput)
}

// The flag to enable notification by email.
func (o LookupSimpleMonitorResultOutput) NotifyEmailEnabled() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupSimpleMonitorResult) bool { return v.NotifyEmailEnabled }).(pulumi.BoolOutput)
}

// The flag to enable HTML format instead of text format.
func (o LookupSimpleMonitorResultOutput) NotifyEmailHtml() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupSimpleMonitorResult) bool { return v.NotifyEmailHtml }).(pulumi.BoolOutput)
}

// The interval in hours between notification.
func (o LookupSimpleMonitorResultOutput) NotifyInterval() pulumi.IntOutput {
	return o.ApplyT(func(v LookupSimpleMonitorResult) int { return v.NotifyInterval }).(pulumi.IntOutput)
}

// The flag to enable notification by slack/discord.
func (o LookupSimpleMonitorResultOutput) NotifySlackEnabled() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupSimpleMonitorResult) bool { return v.NotifySlackEnabled }).(pulumi.BoolOutput)
}

// The webhook URL for sending notification by slack/discord.
func (o LookupSimpleMonitorResultOutput) NotifySlackWebhook() pulumi.StringOutput {
	return o.ApplyT(func(v LookupSimpleMonitorResult) string { return v.NotifySlackWebhook }).(pulumi.StringOutput)
}

// Any tags assigned to the SimpleMonitor.
func (o LookupSimpleMonitorResultOutput) Tags() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupSimpleMonitorResult) []string { return v.Tags }).(pulumi.StringArrayOutput)
}

// The monitoring target of the simple monitor. This will be IP address or FQDN.
func (o LookupSimpleMonitorResultOutput) Target() pulumi.StringOutput {
	return o.ApplyT(func(v LookupSimpleMonitorResult) string { return v.Target }).(pulumi.StringOutput)
}

// The timeout in seconds for monitoring.
func (o LookupSimpleMonitorResultOutput) Timeout() pulumi.IntOutput {
	return o.ApplyT(func(v LookupSimpleMonitorResult) int { return v.Timeout }).(pulumi.IntOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupSimpleMonitorResultOutput{})
}
