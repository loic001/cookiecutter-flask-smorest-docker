# {{cookiecutter.app_full_name}}

{{cookiecutter.app_full_name}} description...

## Quick Start

Run the application:

    pipenv install --dev
    pipenv shell
    export FLASK_APP={{cookiecutter.app_package_name}}
    export FLASK_ENV=development
    flask run

And open it in the browser at [http://127.0.0.1:5000/](http://127.0.0.1:8080/)


## Prerequisites

You must have a Python 3.6 in your PATH.
All the commands below should work on Windows and Linux.

This project use Pipenv for the development workflow.

## Development environment process

 - to install env and deps (regular + dev) : `pipenv install --dev` or `pipenv install --dev --skip-lock` to skip locking

 - to enter env shell: `pipenv shell` in app directory

 - to add more python dependencies: `pipenv install mypackage` in app directory
 
 
## Project architecture
If you have some scripts that are not useful for app execution, put them in `scripts` dir. Launch them with `python -m scripts.<script_file_without_py_extension>`

Flask project files are located in the `{{cookiecutter.app_package_name}}` dir and organized as follows.
```sh
run.py
setup.py
Dockerfile
requirments.txt
MANIFEST.in
+-- tests
+-- scripts #scripts - launch them with python -m automator.scripts.<script_file_without_py_extension>
+-- {{cookiecutter.app_package_name}}
|   +-- app_init.py
|   +-- app_config.py
|   +-- config.json
|   +-- utils
|   +-- entity1 #an entity/document/blueprint
|   |   +-- models.py #contains blocktrades model definition - [MongoEngine Documents]
        +-- schemas.py #contains marshmallow schemas(https://marshmallow.readthedocs.io/en/3.0/api_reference.html)
|   |   +-- resources.py #contains rest routes - [Flask REST blueprints](https://flask-rest-api.readthedocs.io/en/stable/quickstart.html)
|   |   +-- services.py #contains services
|   +-- entity2 #an entity/document/blueprint
|   |   +-- models.py
        +-- schemas.py
|   |   +-- resources.py
|   |   +-- services.py
```

## Deployment

### Todos
- Improve this readme
- Write doc (this file) to deploy to docker
