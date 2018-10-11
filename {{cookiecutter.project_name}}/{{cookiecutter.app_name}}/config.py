import os


class Development:
    DEBUG = True
    SECRET_KEY = "changeme"

    HOST = '{{cookiecutter.db_host}}'
    PORT = {{cookiecutter.db_port}}
    DB = '{{cookiecutter.app_name|upper}}'

    MONGODB_SETTINGS = [{
        'db': DB,
        'host': HOST,
        'port': PORT
    }]


class Production(Development):
	DEBUG = False
    SECRET_KEY = "sup3rs3cr3tk3yf0rPr0duct10N"
    HOST = os.getenv('MONGO_HOST','localhost')
    PORT = os.getenv('MONGO_HOST',27017)


    MONGODB_SETTINGS = [{
        'db': DB,
        'host': HOST,
        'port': PORT
    }]


configuration = {
	'dev':Development,
	'production':Production
}
