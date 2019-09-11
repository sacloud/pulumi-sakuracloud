#!/bin/bash
set -o nounset -o errexit -o pipefail

PROVIDER_NAME="sakuracloud"

ROOT=$(dirname $0)/..
WORK_PATH=$(mktemp -d)
VERSION=$(jq -r '.version' < "${ROOT}/sdk/nodejs/bin/package.json")
PLUGIN_PACKAGE_NAME="pulumi-resource-${PROVIDER_NAME}-v${VERSION}-$(go env GOOS)-$(go env GOARCH).tar.gz"
PLUGIN_PACKAGE_DIR="$ROOT/bin"
PLUGIN_PACKAGE_PATH="${PLUGIN_PACKAGE_DIR}/${PLUGIN_PACKAGE_NAME}"

# When crossbuilding, we want to ensure we have .exe for the windows binaries.
BIN_SUFFIX=
if [ "$(go env GOOS)" = "windows" ]; then
    BIN_SUFFIX=".exe"
fi

go build \
   -ldflags "-X github.com/sacloud/pulumi-${PROVIDER_NAME}/pkg/version.Version=${VERSION}" \
   -o "${WORK_PATH}/pulumi-resource-${PROVIDER_NAME}${BIN_SUFFIX}" \
   "${ROOT}/cmd/pulumi-resource-${PROVIDER_NAME}"

# Tar up the plugin
tar -czf ${PLUGIN_PACKAGE_PATH} -C ${WORK_PATH} .

