import * as sakuracloud from "@sacloud/pulumi_sakuracloud";

const centOSArchive = sakuracloud.getArchive({osType: "centos"});

const disk = new sakuracloud.Disk("pulumi-example", {
    name: "pulumi-example",
    sourceArchiveId: centOSArchive.id,
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
