#!/usr/bin/bash

podman-compose down
podman-compose build
podman-compose up selenium-hub selenium-node-firefox
