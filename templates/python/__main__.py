import pulumi
import pulumi_sakuracloud as sakuracloud

# Create a SakuraCloud resource (Switch)
sw = sakuracloud.Switch('my-switch')

# Export the name of the bucket
pulumi.export('switch_id',  sw.id)
