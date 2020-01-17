

import logging
import sys
import os
from os.path import join, dirname, realpath
from flask import Flask
from flask_smorest import Api
from flask_cors import CORS
from autologging import TRACE

from flask import jsonify
from werkzeug.exceptions import default_exceptions
from werkzeug.exceptions import HTTPException

def init(config, main_config, initializer_key: str, initialized: dict):
    app = Flask(main_config.app_name)
    app.secret_key = '56ggdf6hfgpohhaf9'
    app.config['OPENAPI_URL_PREFIX'] = 'api'
    app.config['OPENAPI_REDOC_PATH'] = 'redoc'
    app.config['OPENAPI_VERSION'] = '3.0.2'

    app.config['OPENAPI_SWAGGER_UI_VERSION'] = '3.20.1'
    app.config['OPENAPI_SWAGGER_UI_PATH'] = 'swagger'

    app.config['PERM_FILE'] = join(dirname(realpath(__file__)), 'perm.json')

    CORS(app)

    api = Api(app)

    @app.errorhandler(Exception)
    def err_handler(error):
        response = jsonify({
            "error": repr(error)
        })
        response.status_code = 500
        return response


    # logging init
    log_level = config.log_level or 'DEBUG'
    _log_level = (logging.getLevelName(log_level), TRACE)[log_level == 'TRACE']
    logging.basicConfig(level=_log_level, stream=sys.stdout,
                        format="%(asctime)s;%(levelname)s:%(filename)s,%(lineno)d:%(name)s.%(funcName)s:%(message)s")

    # # init version
    __version__ = main_config.app_version
    logging.getLogger('initializer').info('%s app version', __version__)

    # werzeug
    werkzeug_logger = logging.getLogger('werkzeug')
    werkzeug_logger.setLevel('ERROR')
    
    return app, api
