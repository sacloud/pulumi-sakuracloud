module github.com/sacloud/pulumi-sakuracloud

go 1.13

require (
	github.com/gliderlabs/ssh v0.1.3 // indirect
	github.com/hashicorp/terraform-plugin-sdk v1.7.0
	github.com/pkg/errors v0.8.1
	github.com/pulumi/pulumi v1.10.2-0.20200211223422-2b59d1405d72
	github.com/pulumi/pulumi-terraform-bridge v1.8.0
	github.com/sacloud/terraform-provider-sakuracloud v1.21.2-0.20200424040529-e988d9661c54
	github.com/stretchr/testify v1.4.1-0.20191106224347-f1bd0923b832
	github.com/xanzy/ssh-agent v0.2.1 // indirect
)

replace github.com/Azure/go-autorest => github.com/Azure/go-autorest v12.4.3+incompatible
