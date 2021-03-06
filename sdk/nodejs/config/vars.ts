// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

let __config = new pulumi.Config("sakuracloud");

/**
 * The value of AcceptLanguage header used when calling SakuraCloud API. It can also be sourced from the
 * `SAKURACLOUD_ACCEPT_LANGUAGE` environment variables, or via a shared credentials file if `profile` is specified
 */
export let acceptLanguage: string | undefined = __config.get("acceptLanguage");
/**
 * The maximum number of SakuraCloud API calls per second. It can also be sourced from the `SAKURACLOUD_RATE_LIMIT`
 * environment variables, or via a shared credentials file if `profile` is specified. Default:`10`
 */
export let apiRequestRateLimit: number | undefined = __config.getObject<number>("apiRequestRateLimit");
/**
 * The timeout seconds for each SakuraCloud API call. It can also be sourced from the `SAKURACLOUD_API_REQUEST_TIMEOUT`
 * environment variables, or via a shared credentials file if `profile` is specified. Default:`300`
 */
export let apiRequestTimeout: number | undefined = __config.getObject<number>("apiRequestTimeout");
/**
 * The root URL of SakuraCloud API. It can also be sourced from the `SAKURACLOUD_API_ROOT_URL` environment variables, or
 * via a shared credentials file if `profile` is specified. Default:`https://secure.sakura.ad.jp/cloud/zone`
 */
export let apiRootUrl: string | undefined = __config.get("apiRootUrl");
/**
 * The name of zone to use as default for global resources. It must be provided, but it can also be sourced from the
 * `SAKURACLOUD_DEFAULT_ZONE` environment variables, or via a shared credentials file if `profile` is specified
 */
export let defaultZone: string | undefined = __config.get("defaultZone");
/**
 * The flag to enable fake of SakuraCloud API call. It is for debugging or developping the provider. It can also be sourced
 * from the `FAKE_MODE` environment variables, or via a shared credentials file if `profile` is specified
 */
export let fakeMode: string | undefined = __config.get("fakeMode");
/**
 * The file path used by SakuraCloud API fake driver for storing fake data. It is for debugging or developping the
 * provider. It can also be sourced from the `FAKE_STORE_PATH` environment variables, or via a shared credentials file if
 * `profile` is specified
 */
export let fakeStorePath: string | undefined = __config.get("fakeStorePath");
/**
 * The profile name of your SakuraCloud account. Default:`default`
 */
export let profile: string | undefined = __config.get("profile") || (utilities.getEnv("SAKURACLOUD_PROFILE") || "default");
/**
 * The maximum number of API call retries used when SakuraCloud API returns status code `423` or `503`. It can also be
 * sourced from the `SAKURACLOUD_RETRY_MAX` environment variables, or via a shared credentials file if `profile` is
 * specified. Default:`100`
 */
export let retryMax: number | undefined = __config.getObject<number>("retryMax");
/**
 * The maximum wait interval(in seconds) for retrying API call used when SakuraCloud API returns status code `423` or
 * `503`. It can also be sourced from the `SAKURACLOUD_RETRY_WAIT_MAX` environment variables, or via a shared credentials
 * file if `profile` is specified
 */
export let retryWaitMax: number | undefined = __config.getObject<number>("retryWaitMax");
/**
 * The minimum wait interval(in seconds) for retrying API call used when SakuraCloud API returns status code `423` or
 * `503`. It can also be sourced from the `SAKURACLOUD_RETRY_WAIT_MIN` environment variables, or via a shared credentials
 * file if `profile` is specified
 */
export let retryWaitMin: number | undefined = __config.getObject<number>("retryWaitMin");
/**
 * The API secret of your SakuraCloud account. It must be provided, but it can also be sourced from the
 * `SAKURACLOUD_ACCESS_TOKEN_SECRET` environment variables, or via a shared credentials file if `profile` is specified
 */
export let secret: string | undefined = __config.get("secret") || (utilities.getEnv("SAKURACLOUD_ACCESS_TOKEN_SECRET") || "");
/**
 * The API token of your SakuraCloud account. It must be provided, but it can also be sourced from the
 * `SAKURACLOUD_ACCESS_TOKEN` environment variables, or via a shared credentials file if `profile` is specified
 */
export let token: string | undefined = __config.get("token") || (utilities.getEnv("SAKURACLOUD_ACCESS_TOKEN") || "");
/**
 * The flag to enable output trace log. It can also be sourced from the `SAKURACLOUD_TRACE` environment variables, or via a
 * shared credentials file if `profile` is specified
 */
export let trace: string | undefined = __config.get("trace");
/**
 * The name of zone to use as default. It must be provided, but it can also be sourced from the `SAKURACLOUD_ZONE`
 * environment variables, or via a shared credentials file if `profile` is specified
 */
export let zone: string | undefined = __config.get("zone") || (utilities.getEnv("SAKURACLOUD_ZONE") || "is1b");
/**
 * A list of available SakuraCloud zone name. It can also be sourced via a shared credentials file if `profile` is
 * specified. Default:[`is1a`, `is1b`, `tk1a`, `tk1v`]
 */
export let zones: string[] | undefined = __config.getObject<string[]>("zones");
