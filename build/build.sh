#/bin/bash

BUILD_DIR="$(dirname "$(realpath "$0")")"
PROJECT_ROOT="$(dirname "$BUILD_DIR")"

echo "Starting build"

echo "Using directory $PROJECT_ROOT as project root" &&
cd "$PROJECT_ROOT" &&

echo "Building report image..." &&
podman build -t simbirsoft_report -f "$BUILD_DIR/Dockerfile_report" --ignorefile "$BUILD_DIR/.dockerignore" . &&

echo "Building test image..." &&
podman build -t simbirsoft_test -f "$BUILD_DIR/Dockerfile_test" --ignorefile "$BUILD_DIR/.dockerignore" . &&

echo "Build finished successfully"
