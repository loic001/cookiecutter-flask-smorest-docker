from mongoengine import Document, StringField

class Entity(Document):
    meta = {
        'db_alias': 'sandbox'
    }
    a_field = StringField(required=True)