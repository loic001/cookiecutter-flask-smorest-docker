from flask.views import MethodView
from flask_smorest import Blueprint

from .. import api
from .. import main_config
from .schemas import WelcomeGetResponseSchema, WelcomeGetArgsSchema

welcome_bp = Blueprint('welcome', 'welcome', url_prefix='/', description='Welcome')

@welcome_bp.route('')
class Welcome(MethodView):

    # !!! authenticate decorator MUST be the last decorator - MUST be placed at the end !!!
    # !!! Also, as_kwargs in arguments decorator must be True if you use the authenticate decorator !!!
    @welcome_bp.arguments(WelcomeGetArgsSchema, location='query', as_kwargs=True)
    @welcome_bp.response(WelcomeGetResponseSchema)
    def get(self, **kwargs):
        """Welcome route

        Show api info
        ---
        """
        # groups = kwargs.get('groups')
        return {
            'app_fullname': main_config.app_name,
            'app_name': main_config.package_name,
            'app_version': main_config.app_version
        }

api.register_blueprint(welcome_bp)