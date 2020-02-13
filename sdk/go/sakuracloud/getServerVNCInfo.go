// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package sakuracloud

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

func GetServerVNCInfo(ctx *pulumi.Context, args *GetServerVNCInfoArgs, opts ...pulumi.InvokeOption) (*GetServerVNCInfoResult, error) {
	var rv GetServerVNCInfoResult
	err := ctx.Invoke("sakuracloud:index/getServerVNCInfo:getServerVNCInfo", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getServerVNCInfo.
type GetServerVNCInfoArgs struct {
	ServerId string `pulumi:"serverId"`
	Zone *string `pulumi:"zone"`
}


// A collection of values returned by getServerVNCInfo.
type GetServerVNCInfoResult struct {
	Host string `pulumi:"host"`
	// id is the provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	Password string `pulumi:"password"`
	Port int `pulumi:"port"`
	ServerId string `pulumi:"serverId"`
	Zone string `pulumi:"zone"`
}

