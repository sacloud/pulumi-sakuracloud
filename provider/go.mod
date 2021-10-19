module github.com/sacloud/pulumi-sakuracloud/provider

go 1.16

require (
	github.com/hashicorp/terraform-plugin-sdk v1.9.1 // indirect
	github.com/pulumi/pulumi-terraform-bridge/v3 v3.9.0
	github.com/pulumi/pulumi/pkg/v3 v3.15.0 // indirect
	github.com/pulumi/pulumi/sdk/v3 v3.15.0
	github.com/sacloud/terraform-provider-sakuracloud v1.21.2-0.20211018023032-6c12edc62816
)

replace (
	github.com/hashicorp/go-getter v1.5.0 => github.com/hashicorp/go-getter v1.4.0
	github.com/hashicorp/terraform-plugin-sdk/v2 => github.com/pulumi/terraform-plugin-sdk/v2 v2.0.0-20210629210550-59d24255d71f
)
