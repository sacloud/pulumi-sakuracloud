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
    public sealed class GetSSHKeyFilterResult
    {
        /// <summary>
        /// One or more name/values pairs used for filtering. There are several valid keys, for a full reference, check out finding section in the [SakuraCloud API reference](https://developer.sakura.ad.jp/cloud/api/1.1/).
        /// </summary>
        public readonly ImmutableArray<Outputs.GetSSHKeyFilterConditionResult> Conditions;
        /// <summary>
        /// The resource id on SakuraCloud used for filtering.
        /// </summary>
        public readonly string? Id;
        /// <summary>
        /// The resource names on SakuraCloud used for filtering. If multiple values ​​are specified, they combined as AND condition.
        /// </summary>
        public readonly ImmutableArray<string> Names;

        [OutputConstructor]
        private GetSSHKeyFilterResult(
            ImmutableArray<Outputs.GetSSHKeyFilterConditionResult> conditions,

            string? id,

            ImmutableArray<string> names)
        {
            Conditions = conditions;
            Id = id;
            Names = names;
        }
    }
}
