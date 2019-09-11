// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * The provider type for the sakuracloud package. By default, resources use package-wide configuration
 * settings, however an explicit `Provider` instance may be created and passed during resource
 * construction to achieve fine-grained programmatic control over provider settings. See the
 * [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.
 *
 * > This content is derived from https://github.com/sacloud/terraform-provider-sakuracloud/blob/master/website/docs/index.html.markdown.
 */
export class Provider extends pulumi.ProviderResource {
    /** @internal */
    public static readonly __pulumiType = 'sakuracloud';

    /**
     * Returns true if the given object is an instance of Provider.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Provider {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Provider.__pulumiType;
    }


    /**
     * Create a Provider resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: ProviderArgs, opts?: pulumi.ResourceOptions) {
        let inputs: pulumi.Inputs = {};
        {
            inputs["acceptLanguage"] = args ? args.acceptLanguage : undefined;
            inputs["apiRequestRateLimit"] = pulumi.output(args ? args.apiRequestRateLimit : undefined).apply(JSON.stringify);
            inputs["apiRequestTimeout"] = pulumi.output(args ? args.apiRequestTimeout : undefined).apply(JSON.stringify);
            inputs["apiRootUrl"] = args ? args.apiRootUrl : undefined;
            inputs["retryInterval"] = pulumi.output(args ? args.retryInterval : undefined).apply(JSON.stringify);
            inputs["retryMax"] = pulumi.output(args ? args.retryMax : undefined).apply(JSON.stringify);
            inputs["secret"] = (args ? args.secret : undefined) || (utilities.getEnv("SAKURACLOUD_ACCESS_TOKEN_SECRET") || "");
            inputs["timeout"] = pulumi.output(args ? args.timeout : undefined).apply(JSON.stringify);
            inputs["token"] = (args ? args.token : undefined) || (utilities.getEnv("SAKURACLOUD_ACCESS_TOKEN") || "");
            inputs["trace"] = pulumi.output(args ? args.trace : undefined).apply(JSON.stringify);
            inputs["zone"] = (args ? args.zone : undefined) || (utilities.getEnv("SAKURACLOUD_ZONE") || "is1b");
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Provider.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a Provider resource.
 */
export interface ProviderArgs {
    readonly acceptLanguage?: pulumi.Input<string>;
    readonly apiRequestRateLimit?: pulumi.Input<number>;
    readonly apiRequestTimeout?: pulumi.Input<number>;
    readonly apiRootUrl?: pulumi.Input<string>;
    readonly retryInterval?: pulumi.Input<number>;
    readonly retryMax?: pulumi.Input<number>;
    /**
     * Your SakuraCloud APIKey(secret)
     */
    readonly secret?: pulumi.Input<string>;
    readonly timeout?: pulumi.Input<number>;
    /**
     * Your SakuraCloud APIKey(token)
     */
    readonly token?: pulumi.Input<string>;
    readonly trace?: pulumi.Input<boolean>;
    /**
     * Target SakuraCloud Zone(is1a | is1b | tk1a | tk1v)
     */
    readonly zone?: pulumi.Input<string>;
}
