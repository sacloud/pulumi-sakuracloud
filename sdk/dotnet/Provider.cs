// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.SakuraCloud
{
    /// <summary>
    /// The provider type for the sakuracloud package. By default, resources use package-wide configuration
    /// settings, however an explicit `Provider` instance may be created and passed during resource
    /// construction to achieve fine-grained programmatic control over provider settings. See the
    /// [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.
    /// 
    /// &gt; This content is derived from https://github.com/sacloud/terraform-provider-sakuracloud/blob/master/website/docs/index.html.markdown.
    /// </summary>
    public partial class Provider : Pulumi.ProviderResource
    {
        /// <summary>
        /// Create a Provider resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Provider(string name, ProviderArgs? args = null, ResourceOptions? options = null)
            : base("sakuracloud", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private static ResourceOptions MakeResourceOptions(ResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new ResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = ResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
    }

    public sealed class ProviderArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The value of AcceptLanguage header used when calling SakuraCloud API. It can also be sourced from the
        /// `SAKURACLOUD_ACCEPT_LANGUAGE` environment variables, or via a shared credentials file if `profile` is
        /// specified
        /// </summary>
        [Input("acceptLanguage")]
        public Input<string>? AcceptLanguage { get; set; }

        /// <summary>
        /// The maximum number of SakuraCloud API calls per second. It can also be sourced from the
        /// `SAKURACLOUD_RATE_LIMIT` environment variables, or via a shared credentials file if `profile` is specified.
        /// Default:`%!s(int=10)`
        /// </summary>
        [Input("apiRequestRateLimit", json: true)]
        public Input<int>? ApiRequestRateLimit { get; set; }

        /// <summary>
        /// The timeout seconds for each SakuraCloud API call. It can also be sourced from the
        /// `SAKURACLOUD_API_REQUEST_TIMEOUT` environment variables, or via a shared credentials file if `profile` is
        /// specified. Default:`%!s(int=300)`
        /// </summary>
        [Input("apiRequestTimeout", json: true)]
        public Input<int>? ApiRequestTimeout { get; set; }

        /// <summary>
        /// The root URL of SakuraCloud API. It can also be sourced from the `SAKURACLOUD_API_ROOT_URL` environment
        /// variables, or via a shared credentials file if `profile` is specified.
        /// Default:`https://secure.sakura.ad.jp/cloud/zone`
        /// </summary>
        [Input("apiRootUrl")]
        public Input<string>? ApiRootUrl { get; set; }

        /// <summary>
        /// The flag to enable fake of SakuraCloud API call. It is for debugging or developping the provider. It can
        /// also be sourced from the `FAKE_MODE` environment variables, or via a shared credentials file if `profile` is
        /// specified
        /// </summary>
        [Input("fakeMode")]
        public Input<string>? FakeMode { get; set; }

        /// <summary>
        /// The file path used by SakuraCloud API fake driver for storing fake data. It is for debugging or developping
        /// the provider. It can also be sourced from the `FAKE_STORE_PATH` environment variables, or via a shared
        /// credentials file if `profile` is specified
        /// </summary>
        [Input("fakeStorePath")]
        public Input<string>? FakeStorePath { get; set; }

        /// <summary>
        /// The profile name of your SakuraCloud account. Default:`default`
        /// </summary>
        [Input("profile")]
        public Input<string>? Profile { get; set; }

        /// <summary>
        /// The maximum number of API call retries used when SakuraCloud API returns status code `423` or `503`. It can
        /// also be sourced from the `SAKURACLOUD_RETRY_MAX` environment variables, or via a shared credentials file if
        /// `profile` is specified. Default:`100`
        /// </summary>
        [Input("retryMax", json: true)]
        public Input<int>? RetryMax { get; set; }

        /// <summary>
        /// The maximum wait interval(in seconds) for retrying API call used when SakuraCloud API returns status code
        /// `423` or `503`. It can also be sourced from the `SAKURACLOUD_RETRY_WAIT_MAX` environment variables, or via a
        /// shared credentials file if `profile` is specified
        /// </summary>
        [Input("retryWaitMax", json: true)]
        public Input<int>? RetryWaitMax { get; set; }

        /// <summary>
        /// The minimum wait interval(in seconds) for retrying API call used when SakuraCloud API returns status code
        /// `423` or `503`. It can also be sourced from the `SAKURACLOUD_RETRY_WAIT_MIN` environment variables, or via a
        /// shared credentials file if `profile` is specified
        /// </summary>
        [Input("retryWaitMin", json: true)]
        public Input<int>? RetryWaitMin { get; set; }

        /// <summary>
        /// The API secret of your SakuraCloud account. It must be provided, but it can also be sourced from the
        /// `SAKURACLOUD_ACCESS_TOKEN_SECRET` environment variables, or via a shared credentials file if `profile` is
        /// specified
        /// </summary>
        [Input("secret")]
        public Input<string>? Secret { get; set; }

        /// <summary>
        /// The API token of your SakuraCloud account. It must be provided, but it can also be sourced from the
        /// `SAKURACLOUD_ACCESS_TOKEN` environment variables, or via a shared credentials file if `profile` is specified
        /// </summary>
        [Input("token")]
        public Input<string>? Token { get; set; }

        /// <summary>
        /// The flag to enable output trace log. It can also be sourced from the `SAKURACLOUD_TRACE` environment
        /// variables, or via a shared credentials file if `profile` is specified
        /// </summary>
        [Input("trace")]
        public Input<string>? Trace { get; set; }

        /// <summary>
        /// The name of zone to use as default. It must be provided, but it can also be sourced from the
        /// `SAKURACLOUD_ZONE` environment variables, or via a shared credentials file if `profile` is specified
        /// </summary>
        [Input("zone")]
        public Input<string>? Zone { get; set; }

        [Input("zones", json: true)]
        private InputList<string>? _zones;

        /// <summary>
        /// A list of available SakuraCloud zone name. It can also be sourced via a shared credentials file if `profile`
        /// is specified. Default:[`is1a`, `is1b`, `tk1a`, `tk1v`]
        /// </summary>
        public InputList<string> Zones
        {
            get => _zones ?? (_zones = new InputList<string>());
            set => _zones = value;
        }

        public ProviderArgs()
        {
            Profile = Utilities.GetEnv("SAKURACLOUD_PROFILE") ?? "default";
            Secret = Utilities.GetEnv("SAKURACLOUD_ACCESS_TOKEN_SECRET") ?? "";
            Token = Utilities.GetEnv("SAKURACLOUD_ACCESS_TOKEN") ?? "";
            Zone = Utilities.GetEnv("SAKURACLOUD_ZONE") ?? "is1b";
        }
    }
}
