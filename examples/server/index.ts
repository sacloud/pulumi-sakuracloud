import * as pulumi from "@pulumi/pulumi";
import * as sakuracloud from "@sacloud/pulumi_sakuracloud";
import Constants from "@sacloud/constants"

const ubuntuArchive = pulumi.output(sakuracloud.getArchive({osType: Constants.Archive.OSTypes.Ubuntu}));

const disk = new sakuracloud.Disk("pulumi-example", {
    name: "pulumi-example",
    sourceArchiveId: ubuntuArchive.id,
});

const server = new sakuracloud.Server("pulumi-example", {
    name: "pulumi-example",
    disks: [disk.id],

    networkInterfaces: [{
        upstream: "shared",
    }],

    diskEditParameter: {
        password: "YourPassword01",
    },
});

// Export the created resource' IDs
export const serverID = server.id;
export const diskID = disk.id;
