#!/usr/bin/bash

SCRIPTS_DIR="$(dirname "$(realpath "$0")")"
PROJECT_ROOT="$(dirname "$SCRIPTS_DIR")"
APP_DATA_DIR="$PROJECT_ROOT/app_data"

mkdir -p "$APP_DATA_DIR"
mkdir -p "$APP_DATA_DIR/export"
mkdir -p "$APP_DATA_DIR/reports"

cd "$PROJECT_ROOT" &&
source ./.venv/bin/activate &&
pytest --alluredir ./app_data/reports ./src/simbirsoft/tests/test_website.py
