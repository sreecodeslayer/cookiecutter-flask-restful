from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_mongoengine import MongoEngine

db = MongoEngine()
jwt = JWTManager()
ma = Marshmallow()
pwd_context = pbkdf2_sha256