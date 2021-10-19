package main

import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/sacloud/pulumi-sakuracloud/sdk/go/sakuracloud"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		sw, err := sakuracloud.NewSwitch(ctx, "from-pulumi-with-go", &sakuracloud.SwitchArgs{
			Name:        "from-pulumi-with-go",
			Description: "this resource was created by pulumi",
			Tags:        []string{"tag1", "tag2"},
		})
		if err != nil {
			return err
		}
		ctx.Export("swith-id", sw.ID())
		return nil
	})
}
