from marshmallow import fields, validate
from {{cookiecutter.app_name}}.extensions import ma


class ObjectId(fields.Field):
    def _serialize(self, value, attr, obj):
        if value is None:
            return ''
        return str(value)


class UserSchema(ma.Schema):
    _id = ObjectId(load_only=True)
    username = ma.String(required=True)
    email = ma.String(required=True,
                      validate=validate.Email(
                          error='Not a valid email address'))
    password_digest = ma.String(load_only=True, required=True)


    class Meta:
        # Fields to expose
        fields = ('email', 'username', '_id')
