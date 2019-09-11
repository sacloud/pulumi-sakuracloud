import * as sakuracloud from "@sacloud/pulumi_sakuracloud";

const sw = new sakuracloud.Switch("from-pulumi-ts", {
   name: "from-pulumi-ts",
   description: "this resource was created by pulumi-sakuracloud with typescript",
   tags: ["tag1", "tag2"],
});

// Export the connection string for the storage account
export const switchID = sw.id;
