// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package sakuracloud

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

type SimpleMonitor struct {
	pulumi.CustomResourceState

	// The interval in seconds between checks. This must be in the range [`60`-`3600`]
	DelayLoop pulumi.IntPtrOutput `pulumi:"delayLoop"`
	// The description of the SimpleMonitor. The length of this value must be in the range [`1`-`512`]
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The flag to enable monitoring by the simple monitor
	Enabled     pulumi.BoolPtrOutput           `pulumi:"enabled"`
	HealthCheck SimpleMonitorHealthCheckOutput `pulumi:"healthCheck"`
	// The icon id to attach to the SimpleMonitor
	IconId pulumi.StringPtrOutput `pulumi:"iconId"`
	// The flag to enable notification by email
	NotifyEmailEnabled pulumi.BoolPtrOutput `pulumi:"notifyEmailEnabled"`
	// The flag to enable HTML format instead of text format
	NotifyEmailHtml pulumi.BoolPtrOutput `pulumi:"notifyEmailHtml"`
	// The interval in hours between notification. This must be in the range [`1`-`72`]
	NotifyInterval pulumi.IntPtrOutput `pulumi:"notifyInterval"`
	// The flag to enable notification by slack/discord
	NotifySlackEnabled pulumi.BoolPtrOutput `pulumi:"notifySlackEnabled"`
	// The webhook URL for sending notification by slack/discord
	NotifySlackWebhook pulumi.StringPtrOutput `pulumi:"notifySlackWebhook"`
	// Any tags to assign to the SimpleMonitor
	Tags pulumi.StringArrayOutput `pulumi:"tags"`
	// The monitoring target of the simple monitor. This must be IP address or FQDN
	Target pulumi.StringOutput `pulumi:"target"`
}

// NewSimpleMonitor registers a new resource with the given unique name, arguments, and options.
func NewSimpleMonitor(ctx *pulumi.Context,
	name string, args *SimpleMonitorArgs, opts ...pulumi.ResourceOption) (*SimpleMonitor, error) {
	if args == nil || args.HealthCheck == nil {
		return nil, errors.New("missing required argument 'HealthCheck'")
	}
	if args == nil || args.Target == nil {
		return nil, errors.New("missing required argument 'Target'")
	}
	if args == nil {
		args = &SimpleMonitorArgs{}
	}
	var resource SimpleMonitor
	err := ctx.RegisterResource("sakuracloud:index/simpleMonitor:SimpleMonitor", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSimpleMonitor gets an existing SimpleMonitor resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSimpleMonitor(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SimpleMonitorState, opts ...pulumi.ResourceOption) (*SimpleMonitor, error) {
	var resource SimpleMonitor
	err := ctx.ReadResource("sakuracloud:index/simpleMonitor:SimpleMonitor", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering SimpleMonitor resources.
type simpleMonitorState struct {
	// The interval in seconds between checks. This must be in the range [`60`-`3600`]
	DelayLoop *int `pulumi:"delayLoop"`
	// The description of the SimpleMonitor. The length of this value must be in the range [`1`-`512`]
	Description *string `pulumi:"description"`
	// The flag to enable monitoring by the simple monitor
	Enabled     *bool                     `pulumi:"enabled"`
	HealthCheck *SimpleMonitorHealthCheck `pulumi:"healthCheck"`
	// The icon id to attach to the SimpleMonitor
	IconId *string `pulumi:"iconId"`
	// The flag to enable notification by email
	NotifyEmailEnabled *bool `pulumi:"notifyEmailEnabled"`
	// The flag to enable HTML format instead of text format
	NotifyEmailHtml *bool `pulumi:"notifyEmailHtml"`
	// The interval in hours between notification. This must be in the range [`1`-`72`]
	NotifyInterval *int `pulumi:"notifyInterval"`
	// The flag to enable notification by slack/discord
	NotifySlackEnabled *bool `pulumi:"notifySlackEnabled"`
	// The webhook URL for sending notification by slack/discord
	NotifySlackWebhook *string `pulumi:"notifySlackWebhook"`
	// Any tags to assign to the SimpleMonitor
	Tags []string `pulumi:"tags"`
	// The monitoring target of the simple monitor. This must be IP address or FQDN
	Target *string `pulumi:"target"`
}

type SimpleMonitorState struct {
	// The interval in seconds between checks. This must be in the range [`60`-`3600`]
	DelayLoop pulumi.IntPtrInput
	// The description of the SimpleMonitor. The length of this value must be in the range [`1`-`512`]
	Description pulumi.StringPtrInput
	// The flag to enable monitoring by the simple monitor
	Enabled     pulumi.BoolPtrInput
	HealthCheck SimpleMonitorHealthCheckPtrInput
	// The icon id to attach to the SimpleMonitor
	IconId pulumi.StringPtrInput
	// The flag to enable notification by email
	NotifyEmailEnabled pulumi.BoolPtrInput
	// The flag to enable HTML format instead of text format
	NotifyEmailHtml pulumi.BoolPtrInput
	// The interval in hours between notification. This must be in the range [`1`-`72`]
	NotifyInterval pulumi.IntPtrInput
	// The flag to enable notification by slack/discord
	NotifySlackEnabled pulumi.BoolPtrInput
	// The webhook URL for sending notification by slack/discord
	NotifySlackWebhook pulumi.StringPtrInput
	// Any tags to assign to the SimpleMonitor
	Tags pulumi.StringArrayInput
	// The monitoring target of the simple monitor. This must be IP address or FQDN
	Target pulumi.StringPtrInput
}

func (SimpleMonitorState) ElementType() reflect.Type {
	return reflect.TypeOf((*simpleMonitorState)(nil)).Elem()
}

type simpleMonitorArgs struct {
	// The interval in seconds between checks. This must be in the range [`60`-`3600`]
	DelayLoop *int `pulumi:"delayLoop"`
	// The description of the SimpleMonitor. The length of this value must be in the range [`1`-`512`]
	Description *string `pulumi:"description"`
	// The flag to enable monitoring by the simple monitor
	Enabled     *bool                    `pulumi:"enabled"`
	HealthCheck SimpleMonitorHealthCheck `pulumi:"healthCheck"`
	// The icon id to attach to the SimpleMonitor
	IconId *string `pulumi:"iconId"`
	// The flag to enable notification by email
	NotifyEmailEnabled *bool `pulumi:"notifyEmailEnabled"`
	// The flag to enable HTML format instead of text format
	NotifyEmailHtml *bool `pulumi:"notifyEmailHtml"`
	// The interval in hours between notification. This must be in the range [`1`-`72`]
	NotifyInterval *int `pulumi:"notifyInterval"`
	// The flag to enable notification by slack/discord
	NotifySlackEnabled *bool `pulumi:"notifySlackEnabled"`
	// The webhook URL for sending notification by slack/discord
	NotifySlackWebhook *string `pulumi:"notifySlackWebhook"`
	// Any tags to assign to the SimpleMonitor
	Tags []string `pulumi:"tags"`
	// The monitoring target of the simple monitor. This must be IP address or FQDN
	Target string `pulumi:"target"`
}

// The set of arguments for constructing a SimpleMonitor resource.
type SimpleMonitorArgs struct {
	// The interval in seconds between checks. This must be in the range [`60`-`3600`]
	DelayLoop pulumi.IntPtrInput
	// The description of the SimpleMonitor. The length of this value must be in the range [`1`-`512`]
	Description pulumi.StringPtrInput
	// The flag to enable monitoring by the simple monitor
	Enabled     pulumi.BoolPtrInput
	HealthCheck SimpleMonitorHealthCheckInput
	// The icon id to attach to the SimpleMonitor
	IconId pulumi.StringPtrInput
	// The flag to enable notification by email
	NotifyEmailEnabled pulumi.BoolPtrInput
	// The flag to enable HTML format instead of text format
	NotifyEmailHtml pulumi.BoolPtrInput
	// The interval in hours between notification. This must be in the range [`1`-`72`]
	NotifyInterval pulumi.IntPtrInput
	// The flag to enable notification by slack/discord
	NotifySlackEnabled pulumi.BoolPtrInput
	// The webhook URL for sending notification by slack/discord
	NotifySlackWebhook pulumi.StringPtrInput
	// Any tags to assign to the SimpleMonitor
	Tags pulumi.StringArrayInput
	// The monitoring target of the simple monitor. This must be IP address or FQDN
	Target pulumi.StringInput
}

func (SimpleMonitorArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*simpleMonitorArgs)(nil)).Elem()
}
