# Pulumi Provider for SakuraCloud

## Compatibility with Pulumi

- Pulumi v3.x ->  0.6+ 
- Pulumi v2.x ->  0.5  
- Pulumi v1.x -> ~0.4

## Installing

### pulumi plugin

    $ pulumi plugin install resource sakuracloud 0.6.1 --server https://github.com/sacloud/pulumi-sakuracloud/releases/download/0.6.1

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

    $ go get github.com/sacloud/pulumi-sakuracloud/sdk
    
### .NET core(C#, VB.NET, and F#)

To use from .NET core, use `dotnet` to grab the latest version of the library

    $ dotnet add package Pulumi.Sakuracloud

## Configuration

The following configuration points are available for the `sakuracloud` provider:

- `sakuracloud:token` (environment: `SAKURACLOUD_ACCESS_TOKEN`) - the API token for `sakuracloud`
- `sakuracloud:secret` (environment: `SAKURACLOUD_ACCESS_TOKEN_SECRET`) - the API secret for `sakuracloud`
- `sakuracloud:zone` (environment: `SAKURACLOUD_ZONE`) - the default zone in which to deploy resources
