import pulumi

import pulumi_sakuracloud

sw = pulumi_sakuracloud.Switch(
    "from-pulumi-with-python",
    name="from-pulumi-with-python",
    description="this resource was created by pulumi",
    tags=["tag1", "tag2"]
    )
pulumi.export('switch-id', sw.id)