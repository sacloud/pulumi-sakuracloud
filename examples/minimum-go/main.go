package main

import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/sacloud/pulumi-sakuracloud/sdk/go/sakuracloud"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		sw, err := sakuracloud.NewSwitch(ctx, "from-pulumi-with-go", &sakuracloud.SwitchArgs{
			Name:        pulumi.StringPtr("from-pulumi-with-go"),
			Description: pulumi.StringPtr("this resource was created by pulumi"),
			Tags:        pulumi.ToStringArray([]string{"tag1", "tag2"}),
		})
		if err != nil {
			return err
		}
		ctx.Export("swith-id", sw.ID())
		return nil
	})
}
