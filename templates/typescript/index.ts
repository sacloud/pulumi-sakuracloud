import * as pulumi from "@pulumi/pulumi";
import * as sakuracloud from "@sacloud/pulumi_sakuracloud";

// Create a SakuraCloud resource (Switch)
const sw = new sakuracloud.Switch("my-switch");

// Export the ID of the switch
export const switchId = sw.id;
