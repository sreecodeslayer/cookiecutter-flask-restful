from .paginator import paginate
import os


def loadconf():
    '''
    Load the server configuration
    '''
    env = os.getenv('{{cookiecutter.app_name|upper}}_ENV', 'dev').lower()
    config = conf[env]
    return config
