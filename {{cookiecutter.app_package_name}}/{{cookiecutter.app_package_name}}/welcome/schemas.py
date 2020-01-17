

from marshmallow import Schema, fields


class WelcomeGetResponseSchema(Schema):
    class Meta:
        strict = True
        ordered = True
    app_version = fields.String(description='The app version')
    app_fullname = fields.String(description='The app fullname')
    app_name = fields.String(description='The app name')

class WelcomeGetArgsSchema(Schema):
    class Meta:
        strict = True
        ordered = True
    arg = fields.String(description='The arg param', required=False)