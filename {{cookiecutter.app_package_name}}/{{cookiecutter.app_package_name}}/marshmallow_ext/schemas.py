from marshmallow import Schema, fields
from marshmallow.validate import Range


# Schemas for pagination query
class PaginatedQuerySchema(Schema):
    class Meta:
        strict = True
        ordered = True
    page = fields.Integer(missing=1, example=1)
    per_page = fields.Integer(missing=100, validate=Range(min=1, max=300), example=15)
    show_total_count = fields.Boolean(missing=False, example=True)


class PaginatedResponseSchema(Schema):
    class Meta:
        strict = True
        ordered = True
    page = fields.Integer(example=1)
    per_page = fields.Integer(example=15)
    count = fields.Integer(example=1)
    total_count = fields.Integer(example=5000)