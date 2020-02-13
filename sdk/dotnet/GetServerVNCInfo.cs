// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.SakuraCloud
{
    public static partial class Invokes
    {
        public static Task<GetServerVNCInfoResult> GetServerVNCInfo(GetServerVNCInfoArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetServerVNCInfoResult>("sakuracloud:index/getServerVNCInfo:getServerVNCInfo", args ?? InvokeArgs.Empty, options.WithVersion());
    }

    public sealed class GetServerVNCInfoArgs : Pulumi.InvokeArgs
    {
        [Input("serverId", required: true)]
        public string ServerId { get; set; } = null!;

        [Input("zone")]
        public string? Zone { get; set; }

        public GetServerVNCInfoArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetServerVNCInfoResult
    {
        public readonly string Host;
        public readonly string Password;
        public readonly int Port;
        public readonly string ServerId;
        public readonly string Zone;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetServerVNCInfoResult(
            string host,
            string password,
            int port,
            string serverId,
            string zone,
            string id)
        {
            Host = host;
            Password = password;
            Port = port;
            ServerId = serverId;
            Zone = zone;
            Id = id;
        }
    }
}