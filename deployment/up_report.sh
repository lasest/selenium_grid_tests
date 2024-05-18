#!/usr/bin/bash

DEPLOYMENT_DIR="$(dirname "$(realpath "$0")")"
PROJECT_ROOT="$(dirname "$BUILD_DIR")"
APP_DATA_DIR=$PROJECT_ROOT/app_data

mkdir -p $APP_DATA_DIR

cd $DEPLOYMENT_DIR

podman-compose down
podman-compose build
APP_DATA_DIR=$APP_DATA_DIR podman-compose up report-container
