PROJECT_NAME := sakuracloud Package
include build/common.mk

PACK             := sakuracloud
PACKDIR          := sdk
PROJECT          := github.com/sacloud/pulumi-${PACK}
NODE_MODULE_NAME := @pulumi/${PACK}
TF_NAME          := ${PACK}

TFGEN           := pulumi-tfgen-${PACK}
PROVIDER        := pulumi-resource-${PACK}
VERSION         := $(shell scripts/get-version)
PYPI_VERSION    := $(shell scripts/get-py-version)

DOTNET_PREFIX  := $(firstword $(subst -, ,${VERSION:v%=%})) # e.g. 1.5.0
DOTNET_SUFFIX  := $(word 2,$(subst -, ,${VERSION:v%=%}))    # e.g. alpha.1
DOTNET_VERSION := $(strip ${DOTNET_PREFIX})-preview-$(strip ${DOTNET_SUFFIX})

TESTPARALLELISM := 4

OS := $(shell uname)
EMPTY_TO_AVOID_SED := ""

prepare::
	@if test -z "${NAME}"; then echo "NAME not set"; exit 1; fi
	@if test -z "${REPOSITORY}"; then echo "REPOSITORY not set"; exit 1; fi
	@if test ! -d "cmd/pulumi-tfgen-x${EMPTY_TO_AVOID_SED}yz"; then "Project already prepared"; exit 1; fi

	mv "cmd/pulumi-tfgen-x${EMPTY_TO_AVOID_SED}yz" cmd/pulumi-tfgen-${NAME}
	mv "cmd/pulumi-resource-x${EMPTY_TO_AVOID_SED}yz" cmd/pulumi-resource-${NAME}

	if [[ "${OS}" != "Darwin" ]]; then \
		sed -i 's,github.com/sacloud/pulumi-sakuracloud,${REPOSITORY},g' go.mod; \
		find ./ ! -path './.git/*' -type f -exec sed -i 's/[x]yz/${NAME}/g' {} \; &> /dev/null; \
	fi

	# In MacOS the -i parameter needs an empty string to execute in place.
	if [[ "${OS}" == "Darwin" ]]; then \
		sed -i '' 's,github.com/sacloud/pulumi-sakuracloud,${REPOSITORY},g' go.mod; \
		find ./ ! -path './.git/*' -type f -exec sed -i '' 's/[x]yz/${NAME}/g' {} \; &> /dev/null; \
	fi

# NOTE: Since the plugin is published using the nodejs style semver version
# We set the PLUGIN_VERSION to be the same as the version we use when building
# the provider (e.g. x.y.z-dev-... instead of x.y.zdev...)
build:: tfgen provider
	for LANGUAGE in "nodejs" "python" "go" "dotnet" ; do \
		$(TFGEN) $$LANGUAGE --overlays overlays/$$LANGUAGE/ --out ${PACKDIR}/$$LANGUAGE/ || exit 3 ; \
	done
	cd ${PACKDIR}/nodejs/ && \
		sed -i.bak -e "s/@pulumi\/sakuracloud/@sacloud\/pulumi_sakuracloud/g" ./package.json && \
		sed -i.bak -e "s/@pulumi\/sakuracloud/@sacloud\/pulumi_sakuracloud/g" ./*.ts && \
		sed -i.bak -e "s/terraform-providers/sacloud/g" ./*.ts && \
		rm *.bak && \
		yarn install && \
		yarn run tsc && \
		cp ../../README.md ../../LICENSE package.json yarn.lock ./bin/ && \
		sed -i.bak "s/\$${VERSION}/$(VERSION)/g" ./bin/package.json
	cd ${PACKDIR}/python/ && \
		cp ../../README.md . && \
		sed -i.bak -e "s/terraform-providers/sacloud/g" pulumi_sakuracloud/*.py pulumi_sakuracloud/*.md pulumi_sakuracloud/config/*.md \pulumi_sakuracloud/config/*.py && \
		rm pulumi_sakuracloud/*.bak && \
		rm pulumi_sakuracloud/config/*.bak && \
		perl -pe "s;check_call\(\['pulumi', 'plugin', 'install', 'resource', 'sakuracloud', '\x24\{PLUGIN_VERSION\}'\]\);check_call\(\['pulumi', 'plugin', 'install', 'resource', 'sakuracloud', '\x24\{PLUGIN_VERSION\}', '--server', 'https://github.com/sacloud/pulumi-sakuracloud/releases/download/\x24\{PLUGIN_VERSION\}'\]\);g" -i setup.py && \
		perl -pe "s;pulumi plugin install resource sakuracloud \x24\{PLUGIN_VERSION\};pulumi plugin install resource sakuracloud \x24\{PLUGIN_VERSION\} --server https://github.com/sacloud/pulumi-sakuracloud/releases/download/\x24\{PLUGIN_VERSION\};g" -i setup.py && \
		$(PYTHON) setup.py clean --all 2>/dev/null && \
		rm -rf ./bin/ ../python.bin/ && cp -R . ../python.bin && mv ../python.bin ./bin && \
		sed -i.bak -e "s/\$${VERSION}/$(PYPI_VERSION)/g" -e "s/\$${PLUGIN_VERSION}/$(VERSION)/g" ./bin/setup.py && \
		cd ./bin && $(PYTHON) setup.py build sdist
	cd ${PACKDIR}/dotnet/ && \
		echo "${VERSION:v%=%}" >version.txt && \
		dotnet build /p:Version=${DOTNET_VERSION}

tfgen::
	go install -ldflags "-X github.com/sacloud/pulumi-${PACK}/pkg/version.Version=${VERSION}" ${PROJECT}/cmd/${TFGEN}

provider::
	go install -ldflags "-X github.com/sacloud/pulumi-${PACK}/pkg/version.Version=${VERSION}" ${PROJECT}/cmd/${PROVIDER}

lint::
	golangci-lint run

install::
	GOBIN=$(PULUMI_BIN) go install -ldflags "-X github.com/sacloud/pulumi-${PACK}/pkg/version.Version=${VERSION}" ${PROJECT}/cmd/${PROVIDER}
	[ ! -e "$(PULUMI_NODE_MODULES)/$(NODE_MODULE_NAME)" ] || rm -rf "$(PULUMI_NODE_MODULES)/$(NODE_MODULE_NAME)"
	mkdir -p "$(PULUMI_NODE_MODULES)/$(NODE_MODULE_NAME)"
	cp -r ${PACKDIR}/nodejs/bin/. "$(PULUMI_NODE_MODULES)/$(NODE_MODULE_NAME)"
	rm -rf "$(PULUMI_NODE_MODULES)/$(NODE_MODULE_NAME)/node_modules"
	cd "$(PULUMI_NODE_MODULES)/$(NODE_MODULE_NAME)" && \
		yarn install --offline --production && \
		(yarn unlink > /dev/null 2>&1 || true) && \
		yarn link
	cd ${PACKDIR}/python/bin && $(PIP) install --user -e .

test_all::
	PATH=$(PULUMI_BIN):$(PATH) go test -v -count=1 -cover -timeout 1h -parallel ${TESTPARALLELISM} ./examples
	PATH=$(PULUMI_BIN):$(PATH) go test -v -count=1 -cover -timeout 1h -parallel ${TESTPARALLELISM} ./tests/...

.PHONY: build_tgz
build_tgz:
	./scripts/build-release-tgz.sh

.PHONY: publish_npm
publish_npm:
	cd ${PACKDIR}/nodejs/bin && \
	npm publish --access public

.PHONY: publish_pypi
publish_pypi:
	cd ${PACKDIR}/python/bin && \
	twine upload --repository pypi dist/*

.PHONY: prepare_docker_build
prepare_docker_build:
	docker build -t pulumi-sakuracloud-builder .

.PHONY: build_docker
build_docker:
	docker run -it --rm -v $(PWD):$(PWD) -w $(PWD) -e GOPROXY=https://proxy.golang.org pulumi-sakuracloud-builder make build_tgz
