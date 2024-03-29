// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sakuracloud

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Get information about an existing ESME.
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
// 		_, err := sakuracloud.LookupESME(ctx, &GetESMEArgs{
// 			Filter: GetESMEFilter{
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
func LookupESME(ctx *pulumi.Context, args *LookupESMEArgs, opts ...pulumi.InvokeOption) (*LookupESMEResult, error) {
	var rv LookupESMEResult
	err := ctx.Invoke("sakuracloud:index/getESME:getESME", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getESME.
type LookupESMEArgs struct {
	// One or more values used for filtering, as defined below.
	Filter *GetESMEFilter `pulumi:"filter"`
}

// A collection of values returned by getESME.
type LookupESMEResult struct {
	// The description of the ESME.
	Description string         `pulumi:"description"`
	Filter      *GetESMEFilter `pulumi:"filter"`
	// The icon id attached to the ESME.
	IconId string `pulumi:"iconId"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// The name of the ESME.
	Name string `pulumi:"name"`
	// The API URL for send SMS with generated OTP.
	SendMessageWithGeneratedOtpApiUrl string `pulumi:"sendMessageWithGeneratedOtpApiUrl"`
	// The API URL for send SMS with inputted OTP.
	SendMessageWithInputtedOtpApiUrl string `pulumi:"sendMessageWithInputtedOtpApiUrl"`
	// Any tags assigned to the ESME.
	Tags []string `pulumi:"tags"`
}

func LookupESMEOutput(ctx *pulumi.Context, args LookupESMEOutputArgs, opts ...pulumi.InvokeOption) LookupESMEResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupESMEResult, error) {
			args := v.(LookupESMEArgs)
			r, err := LookupESME(ctx, &args, opts...)
			return *r, err
		}).(LookupESMEResultOutput)
}

// A collection of arguments for invoking getESME.
type LookupESMEOutputArgs struct {
	// One or more values used for filtering, as defined below.
	Filter GetESMEFilterPtrInput `pulumi:"filter"`
}

func (LookupESMEOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupESMEArgs)(nil)).Elem()
}

// A collection of values returned by getESME.
type LookupESMEResultOutput struct{ *pulumi.OutputState }

func (LookupESMEResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupESMEResult)(nil)).Elem()
}

func (o LookupESMEResultOutput) ToLookupESMEResultOutput() LookupESMEResultOutput {
	return o
}

func (o LookupESMEResultOutput) ToLookupESMEResultOutputWithContext(ctx context.Context) LookupESMEResultOutput {
	return o
}

// The description of the ESME.
func (o LookupESMEResultOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v LookupESMEResult) string { return v.Description }).(pulumi.StringOutput)
}

func (o LookupESMEResultOutput) Filter() GetESMEFilterPtrOutput {
	return o.ApplyT(func(v LookupESMEResult) *GetESMEFilter { return v.Filter }).(GetESMEFilterPtrOutput)
}

// The icon id attached to the ESME.
func (o LookupESMEResultOutput) IconId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupESMEResult) string { return v.IconId }).(pulumi.StringOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o LookupESMEResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupESMEResult) string { return v.Id }).(pulumi.StringOutput)
}

// The name of the ESME.
func (o LookupESMEResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupESMEResult) string { return v.Name }).(pulumi.StringOutput)
}

// The API URL for send SMS with generated OTP.
func (o LookupESMEResultOutput) SendMessageWithGeneratedOtpApiUrl() pulumi.StringOutput {
	return o.ApplyT(func(v LookupESMEResult) string { return v.SendMessageWithGeneratedOtpApiUrl }).(pulumi.StringOutput)
}

// The API URL for send SMS with inputted OTP.
func (o LookupESMEResultOutput) SendMessageWithInputtedOtpApiUrl() pulumi.StringOutput {
	return o.ApplyT(func(v LookupESMEResult) string { return v.SendMessageWithInputtedOtpApiUrl }).(pulumi.StringOutput)
}

// Any tags assigned to the ESME.
func (o LookupESMEResultOutput) Tags() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupESMEResult) []string { return v.Tags }).(pulumi.StringArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupESMEResultOutput{})
}
