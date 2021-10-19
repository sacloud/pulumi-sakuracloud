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
    public sealed class GetCertificateAuthorityFilterConditionResult
    {
        /// <summary>
        /// The name of the target field. This value is case-sensitive.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// The values of the condition. If multiple values ​​are specified, they combined as AND condition.
        /// </summary>
        public readonly ImmutableArray<string> Values;

        [OutputConstructor]
        private GetCertificateAuthorityFilterConditionResult(
            string name,

            ImmutableArray<string> values)
        {
            Name = name;
            Values = values;
        }
    }
}
