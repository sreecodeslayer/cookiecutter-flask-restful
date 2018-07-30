from marshmallow import (
    fields,
    validate,
    post_load
)

from {{cookiecutter.app_name}}.extensions import ma
from {{cookiecutter.app_name}}.models import Users

class ObjectId(fields.Field):
    def _serialize(self, value, attr, obj):
        if value is None:
            return ''
        return str(value)


class UserSchema(ma.Schema):
    id = ObjectId(dump_only=True)
    username = ma.String(required=True)
    email = ma.String(required=True,
                      validate=validate.Email(
                          error='Not a valid email address'))
    passwd_digest = ma.String(load_only=True, required=True)

    @post_load
    def make_user(self, data):
        return Users(**data)

