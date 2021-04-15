// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sakuracloud

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
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
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := sakuracloud.LookupESME(ctx, &sakuracloud.LookupESMEArgs{
// 			Filter: sakuracloud.GetESMEFilter{
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