#!/usr/bin/bash

SCRIPTS_DIR="$(dirname "$(realpath "$0")")"
PROJECT_ROOT="$(dirname "$SCRIPTS_DIR")"

cd "$PROJECT_ROOT" &&
source ./.venv/bin/activate &&
pytest --alluredir ./app_data/reports ./src/simbirsoft/tests/test_website.py
