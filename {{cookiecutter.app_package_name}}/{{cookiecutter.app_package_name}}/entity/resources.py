from autologging import logged
import logging

from flask.views import MethodView
from flask_smorest import Api, Blueprint, Page

from ..mongoengine_ext.helper import paginated_query

from .. import api
from .models import Entity
from .services import service
from .schemas import EntitySchema
from .schemas import EntityListGetQuerySchema, EntityListGetResponseSchema


entity_bp = Blueprint('entity', 'entity',
                               url_prefix='/entity', description='My Entities Operations')

@logged
@entity_bp.route('')
class EntityList(MethodView):

    @entity_bp.arguments(EntityListGetQuerySchema(), location='json')
    @entity_bp.response(EntityListGetResponseSchema)
    def get(self, args):
        """Find cme my entity by query

        Return a paginated response of entities
        ---
        """
        mongo_query_params = {
            'a_field': args.get('a_field')
        }
        self.__log.debug(mongo_query_params)
        return paginated_query(Entity,
                               mongo_query_params, page=args.get('page'),
                               per_page=args.get('per_page'),
                               show_total_count=args.get('show_total_count'),
                               envelope='entities')

api.register_blueprint(entity_bp)