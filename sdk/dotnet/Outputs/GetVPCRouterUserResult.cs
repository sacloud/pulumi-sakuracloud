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
    public sealed class GetVPCRouterUserResult
    {
        /// <summary>
        /// The name of the target field. This value is case-sensitive.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// The password used to authenticate remote access.
        /// </summary>
        public readonly string Password;

        [OutputConstructor]
        private GetVPCRouterUserResult(
            string name,

            string password)
        {
            Name = name;
            Password = password;
        }
    }
}