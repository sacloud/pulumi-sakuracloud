// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sakuracloud

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Get information about an existing Note.
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
// 		_, err := sakuracloud.LookupNote(ctx, &sakuracloud.LookupNoteArgs{
// 			Filter: sakuracloud.GetNoteFilter{
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
func LookupNote(ctx *pulumi.Context, args *LookupNoteArgs, opts ...pulumi.InvokeOption) (*LookupNoteResult, error) {
	var rv LookupNoteResult
	err := ctx.Invoke("sakuracloud:index/getNote:getNote", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getNote.
type LookupNoteArgs struct {
	// One or more values used for filtering, as defined below.
	Filter *GetNoteFilter `pulumi:"filter"`
}

// A collection of values returned by getNote.
type LookupNoteResult struct {
	// The class of the Note. This will be one of [`shell`/`yamlCloudConfig`].
	Class string `pulumi:"class"`
	// The content of the Note.
	Content string `pulumi:"content"`
	// The description of the Note.
	Description string         `pulumi:"description"`
	Filter      *GetNoteFilter `pulumi:"filter"`
	// The icon id attached to the Note.
	IconId string `pulumi:"iconId"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// The name of the Note.
	Name string `pulumi:"name"`
	// Any tags assigned to the Note.
	Tags []string `pulumi:"tags"`
}
