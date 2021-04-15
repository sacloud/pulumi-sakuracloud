// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sakuracloud

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Get information about an existing Database.
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
// 		_, err := sakuracloud.LookupDatabase(ctx, &sakuracloud.LookupDatabaseArgs{
// 			Filter: sakuracloud.GetDatabaseFilter{
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
func LookupDatabase(ctx *pulumi.Context, args *LookupDatabaseArgs, opts ...pulumi.InvokeOption) (*LookupDatabaseResult, error) {
	var rv LookupDatabaseResult
	err := ctx.Invoke("sakuracloud:index/getDatabase:getDatabase", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getDatabase.
type LookupDatabaseArgs struct {
	// One or more values used for filtering, as defined below.
	Filter *GetDatabaseFilter `pulumi:"filter"`
	// The name of zone that the Database is in (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
	Zone *string `pulumi:"zone"`
}

// A collection of values returned by getDatabase.
type LookupDatabaseResult struct {
	// A list of `backup` blocks as defined below.
	Backups []GetDatabaseBackup `pulumi:"backups"`
	// The type of the database. This will be one of [`mariadb`/`postgres`].
	DatabaseType string `pulumi:"databaseType"`
	// The description of the Database.
	Description string             `pulumi:"description"`
	Filter      *GetDatabaseFilter `pulumi:"filter"`
	// The icon id attached to the Database.
	IconId string `pulumi:"iconId"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// The name of the Database.
	Name string `pulumi:"name"`
	// A list of `networkInterface` blocks as defined below.
	NetworkInterfaces []GetDatabaseNetworkInterface `pulumi:"networkInterfaces"`
	// The map for setting RDBMS-specific parameters. Valid keys can be found with the `usacloud database list-parameters` command.
	Parameters map[string]string `pulumi:"parameters"`
	// The password of default user on the database.
	Password string `pulumi:"password"`
	// The plan name of the Database. This will be one of [`10g`/`30g`/`90g`/`240g`/`500g`/`1t`].
	Plan string `pulumi:"plan"`
	// The password of user that processing a replication.
	ReplicaPassword string `pulumi:"replicaPassword"`
	// The name of user that processing a replication.
	ReplicaUser string `pulumi:"replicaUser"`
	// Any tags assigned to the Database.
	Tags []string `pulumi:"tags"`
	// The name of default user on the database.
	Username string `pulumi:"username"`
	Zone     string `pulumi:"zone"`
}
