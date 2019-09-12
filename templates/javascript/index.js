"use strict";
const pulumi = require("@pulumi/pulumi");
const sakuracloud = require("@sacloud/pulumi_sakuracloud");

// Create a SakuraCloud resource (Switch Resource)
const sw = new sakuracloud.Switch("my-switch");

// Export the id of the switch resource
exports.switchId = sw.id;
