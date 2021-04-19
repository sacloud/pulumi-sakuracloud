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
    public sealed class ServerDiskEditParameterNote
    {
        /// <summary>
        /// The id of the API key to be injected into the Note/StartupScript when editing the disk.
        /// </summary>
        public readonly string? ApiKeyId;
        /// <summary>
        /// The id of the Note/StartupScript.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// The value of the variable that be injected into the Note/StartupScript when editing the disk.
        /// </summary>
        public readonly ImmutableDictionary<string, string>? Variables;

        [OutputConstructor]
        private ServerDiskEditParameterNote(
            string? apiKeyId,

            string id,

            ImmutableDictionary<string, string>? variables)
        {
            ApiKeyId = apiKeyId;
            Id = id;
            Variables = variables;
        }
    }
}
