// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Sakuracloud.Inputs
{

    public sealed class ServerDiskEditParameterNoteGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The id of the API key to be injected into the Note/StartupScript when editing the disk.
        /// </summary>
        [Input("apiKeyId")]
        public Input<string>? ApiKeyId { get; set; }

        /// <summary>
        /// The id of the Note/StartupScript.
        /// </summary>
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        [Input("variables")]
        private InputMap<string>? _variables;

        /// <summary>
        /// The value of the variable that be injected into the Note/StartupScript when editing the disk.
        /// </summary>
        public InputMap<string> Variables
        {
            get => _variables ?? (_variables = new InputMap<string>());
            set => _variables = value;
        }

        public ServerDiskEditParameterNoteGetArgs()
        {
        }
    }
}
