from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from {{cookiecutter.app_name}}.models import Users
from {{cookiecutter.app_name}}.schemas import UserSchema
from {{cookiecutter.app_name}}.extensions import db
from {{cookiecutter.app_name}}.commons.paginator import paginate


class UserResource(Resource):

    method_decorators = [jwt_required]

    def get(self, uid):
        schema = UserSchema()

        if not request.is_json:
            return jsonify({'msg': 'Missing JSON in request'}), 400

        user = Users.objects.get_or_404(id=uid)
        return {'user': schema.dump(user).data}

    def put(self, uid):
        schema = UserSchema(partial=True)

        if not request.is_json:
            return jsonify({'msg': 'Missing JSON in request'}), 400

        user, errors = schema.load(request.json)
        if errors:
            return errors, 422
        user = Users.objects.get_or_404(id=uid)

        return {'msg': 'User updated', 'user': schema.dump(user).data}

    def delete(self, uid):
        user = Users.objects.get_or_404(id=uid)

        return {'msg': 'User deleted'}
