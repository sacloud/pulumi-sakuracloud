// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Manages a SakuraCloud sakuracloud_webaccel_certificate.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as sakuracloud from "@pulumi/sakuracloud";
 * import * from "fs";
 *
 * const site = sakuracloud.getWebAccel({
 *     name: "your-site-name",
 * });
 * const foobar = new sakuracloud.WebAccelCertificate("foobar", {
 *     siteId: site.then(site => site.id),
 *     certificateChain: fs.readFileSync("path/to/your/certificate/chain"),
 *     privateKey: fs.readFileSync("path/to/your/private/key"),
 * });
 * ```
 */
export class WebAccelCertificate extends pulumi.CustomResource {
    /**
     * Get an existing WebAccelCertificate resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: WebAccelCertificateState, opts?: pulumi.CustomResourceOptions): WebAccelCertificate {
        return new WebAccelCertificate(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'sakuracloud:index/webAccelCertificate:WebAccelCertificate';

    /**
     * Returns true if the given object is an instance of WebAccelCertificate.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is WebAccelCertificate {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === WebAccelCertificate.__pulumiType;
    }

    /**
     * .
     */
    public readonly certificateChain!: pulumi.Output<string>;
    /**
     * .
     */
    public /*out*/ readonly dnsNames!: pulumi.Output<string[]>;
    /**
     * .
     */
    public /*out*/ readonly issuerCommonName!: pulumi.Output<string>;
    /**
     * .
     */
    public /*out*/ readonly notAfter!: pulumi.Output<string>;
    /**
     * .
     */
    public /*out*/ readonly notBefore!: pulumi.Output<string>;
    /**
     * .
     */
    public readonly privateKey!: pulumi.Output<string>;
    /**
     * .
     */
    public /*out*/ readonly serialNumber!: pulumi.Output<string>;
    /**
     * .
     */
    public /*out*/ readonly sha256Fingerprint!: pulumi.Output<string>;
    /**
     * .
     */
    public readonly siteId!: pulumi.Output<string>;
    /**
     * .
     */
    public /*out*/ readonly subjectCommonName!: pulumi.Output<string>;

    /**
     * Create a WebAccelCertificate resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: WebAccelCertificateArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: WebAccelCertificateArgs | WebAccelCertificateState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as WebAccelCertificateState | undefined;
            inputs["certificateChain"] = state ? state.certificateChain : undefined;
            inputs["dnsNames"] = state ? state.dnsNames : undefined;
            inputs["issuerCommonName"] = state ? state.issuerCommonName : undefined;
            inputs["notAfter"] = state ? state.notAfter : undefined;
            inputs["notBefore"] = state ? state.notBefore : undefined;
            inputs["privateKey"] = state ? state.privateKey : undefined;
            inputs["serialNumber"] = state ? state.serialNumber : undefined;
            inputs["sha256Fingerprint"] = state ? state.sha256Fingerprint : undefined;
            inputs["siteId"] = state ? state.siteId : undefined;
            inputs["subjectCommonName"] = state ? state.subjectCommonName : undefined;
        } else {
            const args = argsOrState as WebAccelCertificateArgs | undefined;
            if ((!args || args.certificateChain === undefined) && !opts.urn) {
                throw new Error("Missing required property 'certificateChain'");
            }
            if ((!args || args.privateKey === undefined) && !opts.urn) {
                throw new Error("Missing required property 'privateKey'");
            }
            if ((!args || args.siteId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'siteId'");
            }
            inputs["certificateChain"] = args ? args.certificateChain : undefined;
            inputs["privateKey"] = args ? args.privateKey : undefined;
            inputs["siteId"] = args ? args.siteId : undefined;
            inputs["dnsNames"] = undefined /*out*/;
            inputs["issuerCommonName"] = undefined /*out*/;
            inputs["notAfter"] = undefined /*out*/;
            inputs["notBefore"] = undefined /*out*/;
            inputs["serialNumber"] = undefined /*out*/;
            inputs["sha256Fingerprint"] = undefined /*out*/;
            inputs["subjectCommonName"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(WebAccelCertificate.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering WebAccelCertificate resources.
 */
export interface WebAccelCertificateState {
    /**
     * .
     */
    certificateChain?: pulumi.Input<string>;
    /**
     * .
     */
    dnsNames?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * .
     */
    issuerCommonName?: pulumi.Input<string>;
    /**
     * .
     */
    notAfter?: pulumi.Input<string>;
    /**
     * .
     */
    notBefore?: pulumi.Input<string>;
    /**
     * .
     */
    privateKey?: pulumi.Input<string>;
    /**
     * .
     */
    serialNumber?: pulumi.Input<string>;
    /**
     * .
     */
    sha256Fingerprint?: pulumi.Input<string>;
    /**
     * .
     */
    siteId?: pulumi.Input<string>;
    /**
     * .
     */
    subjectCommonName?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a WebAccelCertificate resource.
 */
export interface WebAccelCertificateArgs {
    /**
     * .
     */
    certificateChain: pulumi.Input<string>;
    /**
     * .
     */
    privateKey: pulumi.Input<string>;
    /**
     * .
     */
    siteId: pulumi.Input<string>;
}
