using System.Collections.Generic;
using System.Threading.Tasks;

using Pulumi;
using Pulumi.Sakuracloud;

class Program
{
    static Task<int> Main()
    {
        return Deployment.RunAsync(() =>
        {
            var sw = new Switch("from-pulumi-with-csharp", new SwitchArgs
            {
                Name = "from-pulumi-with-csharp",
                Tags = new string[] { "tag1", "tag2" },
                Description = "this resource was created by pulumi"
            });

            new Dictionary<string, object?>
            {
                { "Name", sw.Name }
            };
        });
    }
}
