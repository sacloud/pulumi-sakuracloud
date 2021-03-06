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
    public sealed class GetDNSRecordResult
    {
        /// <summary>
        /// The name of the target field. This value is case-sensitive.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// The number of port.
        /// </summary>
        public readonly int Port;
        /// <summary>
        /// The priority of target DNS Record.
        /// </summary>
        public readonly int Priority;
        /// <summary>
        /// The number of the TTL.
        /// </summary>
        public readonly int Ttl;
        /// <summary>
        /// The type of DNS Record. This will be one of [`A`/`AAAA`/`ALIAS`/`CNAME`/`NS`/`MX`/`TXT`/`SRV`/`CAA`/`PTR`].
        /// </summary>
        public readonly string Type;
        /// <summary>
        /// The value of the DNS Record.
        /// </summary>
        public readonly string Value;
        /// <summary>
        /// The weight of target DNS Record.
        /// </summary>
        public readonly int Weight;

        [OutputConstructor]
        private GetDNSRecordResult(
            string name,

            int port,

            int priority,

            int ttl,

            string type,

            string value,

            int weight)
        {
            Name = name;
            Port = port;
            Priority = priority;
            Ttl = ttl;
            Type = type;
            Value = value;
            Weight = weight;
        }
    }
}
