package examples

import (
	"os"
	"path"
	"path/filepath"
	"testing"

	"github.com/stretchr/testify/assert"

	"github.com/pulumi/pulumi/pkg/testing/integration"
)

func TestExamples(t *testing.T) {
	token := os.Getenv("SAKURACLOUD_ACCESS_TOKEN")
	if token == "" {
		t.Skipf("Skipping test due to missing SAKURACLOUD_ACCESS_TOKEN environment variable")
	}
	secret := os.Getenv("SAKURACLOUD_ACCESS_TOKEN_SECRET")
	if secret == "" {
		t.Skipf("Skipping test due to missing SAKURACLOUD_ACCESS_TOKEN_SECRET environment variable")
	}
	cwd, err := os.Getwd()
	if !assert.NoError(t, err, "expected a valid working directory: %v", err) {
		return
	}

	// base options shared amongst all tests.
	base := integration.ProgramTestOptions{
		Config: map[string]string{
			"sakuracloud:token":  token,
			"sakuracloud:secret": secret,
		},
	}
	jsBase := base.With(integration.ProgramTestOptions{
		Dependencies: []string{
			// JavaScript dependencies
			"@sacloud/pulumi_sakuracloud",
		},
	})
	pythonBase := base.With(integration.ProgramTestOptions{
		Dependencies: []string{
			filepath.Join("..", "sdk", "python", "bin"),
		},
	})

	examples := []integration.ProgramTestOptions{
		// List each test
		jsBase.With(integration.ProgramTestOptions{Dir: path.Join(cwd, "minimum-ts")}),
		pythonBase.With(integration.ProgramTestOptions{Dir: path.Join(cwd, "minimum-py")}),
	}

	if !testing.Short() {
		// Append any longer running tests
	}

	for _, ex := range examples {
		example := ex
		t.Run(example.Dir, func(t *testing.T) {
			integration.ProgramTest(t, &example)
		})
	}
}
