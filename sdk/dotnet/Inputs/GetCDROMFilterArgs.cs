// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Sakuracloud.Inputs
{

    public sealed class GetCDROMFilterArgs : Pulumi.InvokeArgs
    {
        [Input("conditions")]
        private List<Inputs.GetCDROMFilterConditionArgs>? _conditions;

        /// <summary>
        /// One or more name/values pairs used for filtering. There are several valid keys, for a full reference, check out finding section in the [SakuraCloud API reference](https://developer.sakura.ad.jp/cloud/api/1.1/).
        /// </summary>
        public List<Inputs.GetCDROMFilterConditionArgs> Conditions
        {
            get => _conditions ?? (_conditions = new List<Inputs.GetCDROMFilterConditionArgs>());
            set => _conditions = value;
        }

        /// <summary>
        /// The resource id on SakuraCloud used for filtering.
        /// </summary>
        [Input("id")]
        public string? Id { get; set; }

        [Input("names")]
        private List<string>? _names;

        /// <summary>
        /// The resource names on SakuraCloud used for filtering. If multiple values ​​are specified, they combined as AND condition.
        /// </summary>
        public List<string> Names
        {
            get => _names ?? (_names = new List<string>());
            set => _names = value;
        }

        [Input("tags")]
        private List<string>? _tags;

        /// <summary>
        /// The resource tags on SakuraCloud used for filtering. If multiple values ​​are specified, they combined as AND condition.
        /// </summary>
        public List<string> Tags
        {
            get => _tags ?? (_tags = new List<string>());
            set => _tags = value;
        }

        public GetCDROMFilterArgs()
        {
        }
    }
}
