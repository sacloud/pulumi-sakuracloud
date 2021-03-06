// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Sakuracloud
{
    public static class GetSSHKey
    {
        /// <summary>
        /// Get information about an existing SSH Key.
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Sakuracloud = Pulumi.Sakuracloud;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var foobar = Output.Create(Sakuracloud.GetSSHKey.InvokeAsync(new Sakuracloud.GetSSHKeyArgs
        ///         {
        ///             Filter = new Sakuracloud.Inputs.GetSSHKeyFilterArgs
        ///             {
        ///                 Names = 
        ///                 {
        ///                     "foobar",
        ///                 },
        ///             },
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetSSHKeyResult> InvokeAsync(GetSSHKeyArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetSSHKeyResult>("sakuracloud:index/getSSHKey:getSSHKey", args ?? new GetSSHKeyArgs(), options.WithVersion());
    }


    public sealed class GetSSHKeyArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// One or more values used for filtering, as defined below.
        /// </summary>
        [Input("filter")]
        public Inputs.GetSSHKeyFilterArgs? Filter { get; set; }

        public GetSSHKeyArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetSSHKeyResult
    {
        /// <summary>
        /// The description of the SSHKey.
        /// </summary>
        public readonly string Description;
        public readonly Outputs.GetSSHKeyFilterResult? Filter;
        /// <summary>
        /// The fingerprint of public key.
        /// </summary>
        public readonly string Fingerprint;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// The name of the SSHKey.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// The value of public key.
        /// </summary>
        public readonly string PublicKey;

        [OutputConstructor]
        private GetSSHKeyResult(
            string description,

            Outputs.GetSSHKeyFilterResult? filter,

            string fingerprint,

            string id,

            string name,

            string publicKey)
        {
            Description = description;
            Filter = filter;
            Fingerprint = fingerprint;
            Id = id;
            Name = name;
            PublicKey = publicKey;
        }
    }
}
