from {{cookiecutter.app_name}}.extensions import db, pwd_context
from datetime import datetime, timedelta


class Users(db.Document):
    '''Mongodb Model for Users'''
    username = db.StringField(required=True, unique=True)
    email = db.EmailField(unique=True)
    passwd_digest = db.StringField()

    meta = {
        'indexes': ['username', 'email']
    }

    def __init__(self, arg):
        super(Users, self).__init__()
        self.passwd_digest = pwd_context.hash(self.passwd_digest)

    def __repr__(self):
        return '(User : %s)' % self.username
