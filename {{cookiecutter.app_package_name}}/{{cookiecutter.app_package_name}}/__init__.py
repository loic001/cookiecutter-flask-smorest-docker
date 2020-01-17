import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
from .config import load_from_instance_env
from .init import init

main_config = load_from_instance_env()
__version__ = main_config.app_version

initialized = init(main_config)

#flask_app
flask_app = initialized.flask_app
app, api = flask_app.app

#mongo initializer
mongo = initialized.mongo

# import your modules below (especially modules that require the app to be initialized)
from . import welcome
from . import entity