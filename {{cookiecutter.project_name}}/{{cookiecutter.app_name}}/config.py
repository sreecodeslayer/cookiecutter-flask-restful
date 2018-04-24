DEBUG = True
SECRET_KEY = "changeme"

HOST = '{{cookiecuter.db_host}}'
PORT = {{cookiecuter.db_port}}
DB = '{{cookiecuter.app_name|upper}}'

MONGODB_SETTINGS = [{
    'db': DB,
    'host': HOST,
    'port': PORT
}]
