#!/usr/bin/bash

SCRIPTS_DIR="$(dirname "$(realpath "$0")")"
PROJECT_ROOT="$(dirname "$SCRIPTS_DIR")"

cd "$PROJECT_ROOT" &&
source ./.venv/bin/activate &&
allure serve -h 0.0.0.0 -p 9000 ./app_data/reports

