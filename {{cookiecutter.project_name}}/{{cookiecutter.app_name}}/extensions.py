from passlib.context import CryptContext
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_mongoengine import MongoEngine

db = MongoEngine()
jwt = JWTManager()
ma = Marshmallow()
pwd_context = CryptContext(schemes=['pbkdf2_sha512'], deprecated='auto')
