module github.com/sacloud/pulumi-sakuracloud

go 1.12

replace (
	github.com/Nvveen/Gotty => github.com/ijc25/Gotty v0.0.0-20170406111628-a8b993ba6abd
	github.com/golang/glog => github.com/pulumi/glog v0.0.0-20180820174630-7eaa6ffb71e4
)

require (
	github.com/hashicorp/terraform v0.12.7
	github.com/pkg/errors v0.8.1
	github.com/pulumi/pulumi v0.17.28-0.20190731182900-6804d640fc7c
	github.com/pulumi/pulumi-terraform v0.18.4-0.20190906215050-e93c61b800df
	github.com/sacloud/terraform-provider-sakuracloud v1.16.3
	github.com/stretchr/testify v1.3.1-0.20190311161405-34c6fa2dc709
)
