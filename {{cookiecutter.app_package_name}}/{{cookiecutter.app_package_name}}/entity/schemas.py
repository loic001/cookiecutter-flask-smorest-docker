from marshmallow import Schema, fields

from ..marshmallow_ext.schemas import PaginatedQuerySchema, PaginatedResponseSchema

# Base Schemas
class EntityBaseSchema(Schema):
    class Meta:
        strict = True
        ordered = True
    a_field = fields.String(description='My field description', example='example doc field', required=True)

# MyEntity Schema Model
class EntitySchema(EntityBaseSchema):
    pass

# BlockTradesCmeList
class EntityListGetQuerySchema(EntityBaseSchema, PaginatedQuerySchema):
    pass

class EntityListGetResponseSchema(PaginatedResponseSchema):
    entities = fields.List(fields.Nested(EntitySchema))