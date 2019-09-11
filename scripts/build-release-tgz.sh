#!/usr/bin/env bash

set -o nounset -o errexit -o pipefail

ROOT=$(dirname $0)/..
PUBLISH_GOOS=("linux" "windows" "darwin")
PUBLISH_GOARCH=("amd64")

echo "Building plugin archive for release"
for OS in "${PUBLISH_GOOS[@]}"
do
    for ARCH in "${PUBLISH_GOARCH[@]}"
    do
        export GOOS=${OS}
        export GOARCH=${ARCH}

        ${ROOT}/scripts/build-release-plugin.sh
    done
done

