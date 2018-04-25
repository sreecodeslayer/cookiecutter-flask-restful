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
