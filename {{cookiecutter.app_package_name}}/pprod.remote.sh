#!/bin/bash
cd "$(dirname "$0")"

export TAG=$(git describe --abbrev=0)
export APP_NAME={{cookiecutter.app_package_name}}
ENVEXT=_pprod

docker build -t "harbor.dts.corp.local/digital/$APP_NAME:$TAG" -t "harbor.dts.corp.local/digital/$APP_NAME" . --pull

docker service rm "$APP_NAME"
docker service create --name "$APP_NAME$ENVEXT" -p 21000:8080 PREPROD