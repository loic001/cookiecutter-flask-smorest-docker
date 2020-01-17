#!/bin/bash
cd "$(dirname "$0")"

export TAG=$(git describe --abbrev=0)
export APP_NAME={{cookiecutter.app_package_name}}
ENVEXT=_dev

docker build -t "harbor.dts.corp.local/digital/$APP_NAME:$TAG" -t "harbor.dts.corp.local/digital/$APP_NAME" . --pull

docker service rm "$APP_NAME"
docker service create --name "$APP_NAME$ENVEXT" -p 31000:8080 --secret dgt_web_pool_keytab --env KRB5_KTNAME='/run/secrets/dgt_web_pool_keytab' --env INSTANCE_ENV=DEV --env KERBEROS_DEBUG="off" "harbor.dts.corp.local/digital/$APP_NAME" DEV