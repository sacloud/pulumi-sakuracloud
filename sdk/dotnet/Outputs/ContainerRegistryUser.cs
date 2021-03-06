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
    public sealed class ContainerRegistryUser
    {
        /// <summary>
        /// The user name used to authenticate remote access.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// The password used to authenticate remote access.
        /// </summary>
        public readonly string Password;
        /// <summary>
        /// The level of access that allow to the user. This must be one of [`all`/`readwrite`/`readonly`].
        /// </summary>
        public readonly string Permission;

        [OutputConstructor]
        private ContainerRegistryUser(
            string name,

            string password,

            string permission)
        {
            Name = name;
            Password = password;
            Permission = permission;
        }
    }
}
