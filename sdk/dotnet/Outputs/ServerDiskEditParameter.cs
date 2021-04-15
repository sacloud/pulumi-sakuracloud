// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Sakuracloud.Outputs
{

    [OutputType]
    public sealed class ServerDiskEditParameter
    {
        /// <summary>
        /// The flag to change partition uuid.
        /// </summary>
        public readonly bool? ChangePartitionUuid;
        /// <summary>
        /// The flag to disable password authentication.
        /// </summary>
        public readonly bool? DisablePwAuth;
        /// <summary>
        /// The flag to enable DHCP client.
        /// </summary>
        public readonly bool? EnableDhcp;
        /// <summary>
        /// The gateway address used by the Server.
        /// </summary>
        public readonly string? Gateway;
        /// <summary>
        /// The hostname of the Server. The length of this value must be in the range [`1`-`64`].
        /// </summary>
        public readonly string? Hostname;
        /// <summary>
        /// The IP address to assign to the Server.
        /// </summary>
        public readonly string? IpAddress;
        /// <summary>
        /// The bit length of the subnet to assign to the Server.
        /// </summary>
        public readonly int? Netmask;
        /// <summary>
        /// A list of the Note id.  
        /// Note: **The `note_ids` will be removed in a future version. Please use the `note` instead**
        /// </summary>
        public readonly ImmutableArray<string> NoteIds;
        /// <summary>
        /// A list of the `note` block as defined below.
        /// </summary>
        public readonly ImmutableArray<Outputs.ServerDiskEditParameterNote> Notes;
        /// <summary>
        /// The password of default user. The length of this value must be in the range [`8`-`64`].
        /// </summary>
        public readonly string? Password;
        /// <summary>
        /// A list of the SSHKey id.
        /// </summary>
        public readonly ImmutableArray<string> SshKeyIds;
        /// <summary>
        /// A list of the SSHKey text.
        /// </summary>
        public readonly ImmutableArray<string> SshKeys;

        [OutputConstructor]
        private ServerDiskEditParameter(
            bool? changePartitionUuid,

            bool? disablePwAuth,

            bool? enableDhcp,

            string? gateway,

            string? hostname,

            string? ipAddress,

            int? netmask,

            ImmutableArray<string> noteIds,

            ImmutableArray<Outputs.ServerDiskEditParameterNote> notes,

            string? password,

            ImmutableArray<string> sshKeyIds,

            ImmutableArray<string> sshKeys)
        {
            ChangePartitionUuid = changePartitionUuid;
            DisablePwAuth = disablePwAuth;
            EnableDhcp = enableDhcp;
            Gateway = gateway;
            Hostname = hostname;
            IpAddress = ipAddress;
            Netmask = netmask;
            NoteIds = noteIds;
            Notes = notes;
            Password = password;
            SshKeyIds = sshKeyIds;
            SshKeys = sshKeys;
        }
    }
}