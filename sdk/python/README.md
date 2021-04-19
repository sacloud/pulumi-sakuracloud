# Pulumi Provider for SakuraCloud

## Compatibility with Pulumi

- Pulumi v3.x ->  0.6+ (Unreleased)
- Pulumi v2.x ->  0.5  (Unreleased)
- Pulumi v1.x -> ~0.4


## Installing

### pulumi plugin

    $ pulumi plugin install resource sakuracloud 0.5.0 --server https://github.com/sacloud/pulumi-sakuracloud/releases/download/0.5.0

### SDK

This package is available in many languages in the standard packaging formats.

### Node.js (Java/TypeScript)

To use from JavaScript or TypeScript in Node.js, install using either `npm`:

    $ npm install @sacloud/pulumi_sakuracloud

or `yarn`:

    $ yarn add @sacloud/pulumi_sakuracloud

### Python

To use from Python, install using `pip`:

    $ pip install pulumi_sakuracloud

### Go

To use from Go, use `go get` to grab the latest version of the library

    $ go get github.com/sacloud/pulumi-sakuracloud/sdk/go/...
    
### .NET core(C#, VB.NET, and F#) **Preview**

To use from .NET core, use `dotnet` to grab the latest version of the library

    $ dotnet add package Pulumi.Sakuracloud

## Configuration

The following configuration points are available for the `sakuracloud` provider:

- `sakuracloud:token` (environment: `SAKURACLOUD_ACCESS_TOKEN`) - the API token for `sakuracloud`
- `sakuracloud:secret` (environment: `SAKURACLOUD_ACCESS_TOKEN_SECRET`) - the API secret for `sakuracloud`
- `sakuracloud:zone` (environment: `SAKURACLOUD_ZONE`) - the default zone in which to deploy resources


## Development

### Add dependencies

In order to properly build the sdks, the following tools are expected:
- `pulumictl` (See the project's README for installation instructions: https://github.com/pulumi/pulumictl)

In the root of the repository, run:

- `GO111MODULE=on go get github.com/pulumi/pulumi-terraform@master`
- `(cd provider && go get github.com/sacloud/terraform-provider-sakuracloud)`
- `(cd provider && go mod download)`

### Build the provider:

- `make build_sdks`
