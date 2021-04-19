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
    public sealed class GetSimpleMonitorFilterResult
    {
        /// <summary>
        /// One or more name/values pairs used for filtering. There are several valid keys, for a full reference, check out finding section in the [SakuraCloud API reference](https://developer.sakura.ad.jp/cloud/api/1.1/).
        /// </summary>
        public readonly ImmutableArray<Outputs.GetSimpleMonitorFilterConditionResult> Conditions;
        /// <summary>
        /// The resource id on SakuraCloud used for filtering.
        /// </summary>
        public readonly string? Id;
        /// <summary>
        /// The resource names on SakuraCloud used for filtering. If multiple values ​​are specified, they combined as AND condition.
        /// </summary>
        public readonly ImmutableArray<string> Names;
        /// <summary>
        /// The resource tags on SakuraCloud used for filtering. If multiple values ​​are specified, they combined as AND condition.
        /// </summary>
        public readonly ImmutableArray<string> Tags;

        [OutputConstructor]
        private GetSimpleMonitorFilterResult(
            ImmutableArray<Outputs.GetSimpleMonitorFilterConditionResult> conditions,

            string? id,

            ImmutableArray<string> names,

            ImmutableArray<string> tags)
        {
            Conditions = conditions;
            Id = id;
            Names = names;
            Tags = tags;
        }
    }
}
