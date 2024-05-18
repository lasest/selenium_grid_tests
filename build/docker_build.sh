#/bin/bash

BUILD_DIR="$(dirname "$(realpath "$0")")"
PROJECT_ROOT="$(dirname "$BUILD_DIR")"

echo "Starting build"

echo "Using directory $PROJECT_ROOT as project root" &&
cd "$PROJECT_ROOT" &&

echo "Building report image..." &&
docker buildx build -t simbirsoft_report -f "$BUILD_DIR/Dockerfile_report" . &&

echo "Building test image..." &&
docker buildx build -t simbirsoft_test -f "$BUILD_DIR/Dockerfile_test" . &&

echo "Build finished successfully"

