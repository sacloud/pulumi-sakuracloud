// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Immutable;

namespace Pulumi.Sakuracloud
{
    public static class Config
    {
        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Design", "IDE1006", Justification = 
        "Double underscore prefix used to avoid conflicts with variable names.")]
        private sealed class __Value<T>
        {
            private readonly Func<T> _getter;
            private T _value = default!;
            private bool _set;

            public __Value(Func<T> getter)
            {
                _getter = getter;
            }

            public T Get() => _set ? _value : _getter();

            public void Set(T value)
            {
                _value = value;
                _set = true;
            }
        }

        private static readonly Pulumi.Config __config = new Pulumi.Config("sakuracloud");

        private static readonly __Value<string?> _acceptLanguage = new __Value<string?>(() => __config.Get("acceptLanguage"));
        /// <summary>
        /// The value of AcceptLanguage header used when calling SakuraCloud API. It can also be sourced from the
        /// `SAKURACLOUD_ACCEPT_LANGUAGE` environment variables, or via a shared credentials file if `profile` is specified
        /// </summary>
        public static string? AcceptLanguage
        {
            get => _acceptLanguage.Get();
            set => _acceptLanguage.Set(value);
        }

        private static readonly __Value<int?> _apiRequestRateLimit = new __Value<int?>(() => __config.GetInt32("apiRequestRateLimit"));
        /// <summary>
        /// The maximum number of SakuraCloud API calls per second. It can also be sourced from the `SAKURACLOUD_RATE_LIMIT`
        /// environment variables, or via a shared credentials file if `profile` is specified. Default:`10`
        /// </summary>
        public static int? ApiRequestRateLimit
        {
            get => _apiRequestRateLimit.Get();
            set => _apiRequestRateLimit.Set(value);
        }

        private static readonly __Value<int?> _apiRequestTimeout = new __Value<int?>(() => __config.GetInt32("apiRequestTimeout"));
        /// <summary>
        /// The timeout seconds for each SakuraCloud API call. It can also be sourced from the `SAKURACLOUD_API_REQUEST_TIMEOUT`
        /// environment variables, or via a shared credentials file if `profile` is specified. Default:`300`
        /// </summary>
        public static int? ApiRequestTimeout
        {
            get => _apiRequestTimeout.Get();
            set => _apiRequestTimeout.Set(value);
        }

        private static readonly __Value<string?> _apiRootUrl = new __Value<string?>(() => __config.Get("apiRootUrl"));
        /// <summary>
        /// The root URL of SakuraCloud API. It can also be sourced from the `SAKURACLOUD_API_ROOT_URL` environment variables, or
        /// via a shared credentials file if `profile` is specified. Default:`https://secure.sakura.ad.jp/cloud/zone`
        /// </summary>
        public static string? ApiRootUrl
        {
            get => _apiRootUrl.Get();
            set => _apiRootUrl.Set(value);
        }

        private static readonly __Value<string?> _defaultZone = new __Value<string?>(() => __config.Get("defaultZone"));
        /// <summary>
        /// The name of zone to use as default for global resources. It must be provided, but it can also be sourced from the
        /// `SAKURACLOUD_DEFAULT_ZONE` environment variables, or via a shared credentials file if `profile` is specified
        /// </summary>
        public static string? DefaultZone
        {
            get => _defaultZone.Get();
            set => _defaultZone.Set(value);
        }

        private static readonly __Value<string?> _fakeMode = new __Value<string?>(() => __config.Get("fakeMode"));
        /// <summary>
        /// The flag to enable fake of SakuraCloud API call. It is for debugging or developping the provider. It can also be sourced
        /// from the `FAKE_MODE` environment variables, or via a shared credentials file if `profile` is specified
        /// </summary>
        public static string? FakeMode
        {
            get => _fakeMode.Get();
            set => _fakeMode.Set(value);
        }

        private static readonly __Value<string?> _fakeStorePath = new __Value<string?>(() => __config.Get("fakeStorePath"));
        /// <summary>
        /// The file path used by SakuraCloud API fake driver for storing fake data. It is for debugging or developping the
        /// provider. It can also be sourced from the `FAKE_STORE_PATH` environment variables, or via a shared credentials file if
        /// `profile` is specified
        /// </summary>
        public static string? FakeStorePath
        {
            get => _fakeStorePath.Get();
            set => _fakeStorePath.Set(value);
        }

        private static readonly __Value<string?> _profile = new __Value<string?>(() => __config.Get("profile") ?? Utilities.GetEnv("SAKURACLOUD_PROFILE") ?? "default");
        /// <summary>
        /// The profile name of your SakuraCloud account. Default:`default`
        /// </summary>
        public static string? Profile
        {
            get => _profile.Get();
            set => _profile.Set(value);
        }

        private static readonly __Value<int?> _retryMax = new __Value<int?>(() => __config.GetInt32("retryMax"));
        /// <summary>
        /// The maximum number of API call retries used when SakuraCloud API returns status code `423` or `503`. It can also be
        /// sourced from the `SAKURACLOUD_RETRY_MAX` environment variables, or via a shared credentials file if `profile` is
        /// specified. Default:`100`
        /// </summary>
        public static int? RetryMax
        {
            get => _retryMax.Get();
            set => _retryMax.Set(value);
        }

        private static readonly __Value<int?> _retryWaitMax = new __Value<int?>(() => __config.GetInt32("retryWaitMax"));
        /// <summary>
        /// The maximum wait interval(in seconds) for retrying API call used when SakuraCloud API returns status code `423` or
        /// `503`. It can also be sourced from the `SAKURACLOUD_RETRY_WAIT_MAX` environment variables, or via a shared credentials
        /// file if `profile` is specified
        /// </summary>
        public static int? RetryWaitMax
        {
            get => _retryWaitMax.Get();
            set => _retryWaitMax.Set(value);
        }

        private static readonly __Value<int?> _retryWaitMin = new __Value<int?>(() => __config.GetInt32("retryWaitMin"));
        /// <summary>
        /// The minimum wait interval(in seconds) for retrying API call used when SakuraCloud API returns status code `423` or
        /// `503`. It can also be sourced from the `SAKURACLOUD_RETRY_WAIT_MIN` environment variables, or via a shared credentials
        /// file if `profile` is specified
        /// </summary>
        public static int? RetryWaitMin
        {
            get => _retryWaitMin.Get();
            set => _retryWaitMin.Set(value);
        }

        private static readonly __Value<string?> _secret = new __Value<string?>(() => __config.Get("secret") ?? Utilities.GetEnv("SAKURACLOUD_ACCESS_TOKEN_SECRET") ?? "");
        /// <summary>
        /// The API secret of your SakuraCloud account. It must be provided, but it can also be sourced from the
        /// `SAKURACLOUD_ACCESS_TOKEN_SECRET` environment variables, or via a shared credentials file if `profile` is specified
        /// </summary>
        public static string? Secret
        {
            get => _secret.Get();
            set => _secret.Set(value);
        }

        private static readonly __Value<string?> _token = new __Value<string?>(() => __config.Get("token") ?? Utilities.GetEnv("SAKURACLOUD_ACCESS_TOKEN") ?? "");
        /// <summary>
        /// The API token of your SakuraCloud account. It must be provided, but it can also be sourced from the
        /// `SAKURACLOUD_ACCESS_TOKEN` environment variables, or via a shared credentials file if `profile` is specified
        /// </summary>
        public static string? Token
        {
            get => _token.Get();
            set => _token.Set(value);
        }

        private static readonly __Value<string?> _trace = new __Value<string?>(() => __config.Get("trace"));
        /// <summary>
        /// The flag to enable output trace log. It can also be sourced from the `SAKURACLOUD_TRACE` environment variables, or via a
        /// shared credentials file if `profile` is specified
        /// </summary>
        public static string? Trace
        {
            get => _trace.Get();
            set => _trace.Set(value);
        }

        private static readonly __Value<string?> _zone = new __Value<string?>(() => __config.Get("zone") ?? Utilities.GetEnv("SAKURACLOUD_ZONE") ?? "is1b");
        /// <summary>
        /// The name of zone to use as default. It must be provided, but it can also be sourced from the `SAKURACLOUD_ZONE`
        /// environment variables, or via a shared credentials file if `profile` is specified
        /// </summary>
        public static string? Zone
        {
            get => _zone.Get();
            set => _zone.Set(value);
        }

        private static readonly __Value<ImmutableArray<string>> _zones = new __Value<ImmutableArray<string>>(() => __config.GetObject<ImmutableArray<string>>("zones"));
        /// <summary>
        /// A list of available SakuraCloud zone name. It can also be sourced via a shared credentials file if `profile` is
        /// specified. Default:[`is1a`, `is1b`, `tk1a`, `tk1v`]
        /// </summary>
        public static ImmutableArray<string> Zones
        {
            get => _zones.Get();
            set => _zones.Set(value);
        }

    }
}
