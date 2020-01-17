#!/bin/bash
if [[ "$1" == "PREPROD" ]]; then
#   my_background_scrip.sh &
    pipenv run waitress-serve --listen=*:8080 {{cookiecutter.app_package_name}}:app
elif [[ "$1" == "PROD" ]]; then
    pipenv run waitress-serve --listen=*:8080 {{cookiecutter.app_package_name}}:app
else
    pipenv run waitress-serve --listen=*:8080 {{cookiecutter.app_package_name}}:app
fi