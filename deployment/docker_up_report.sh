#!/usr/bin/bash

DEPLOYMENT_DIR="$(dirname "$(realpath "$0")")"
PROJECT_ROOT="$(dirname "$DEPLOYMENT_DIR")"
APP_DATA_DIR="$PROJECT_ROOT/app_data"

mkdir -p "$APP_DATA_DIR"

cd "$DEPLOYMENT_DIR"

SIMBIRSOFT_APP_DATA_PATH="$APP_DATA_DIR" docker compose down
SIMBIRSOFT_APP_DATA_PATH="$APP_DATA_DIR" docker compose up report-container
