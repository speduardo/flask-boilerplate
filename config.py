import os
from datetime import timedelta


class Config(object):
    DEBUG = os.getenv('FLASK_DEBUG') or False
    TESTING = False
    ERROR_404_HELP = False
    PORT = int(os.getenv('PORT', 5000))
    SECRET_KEY = os.getenv('SECRET_KEY') or 'my-hard-secret-key'

    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY') or 'my-hard-secret-key'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(
        minutes=int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES'))
    )
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(
        days=int(os.getenv('JWT_REFRESH_TOKEN_EXPIRES'))
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

    DATABASE_CONNECT_OPTIONS = {}

    ENABLED_MODULES = (
        'auth',

        'users',
        #'teams',

        'api',
    )

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True
    SQLALCHEMY_ECHO = True
    # Define the database
    SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}'.format('mysql+pymysql', os.getenv('DATABASE_USERNAME'),
                                                           os.getenv('DATABASE_PASSWORD'), os.getenv('DATABASE_HOST'),
                                                           os.getenv('DATABASE_PORT'), os.getenv('DATABASE_NAME'))


class TestingConfig(Config):
    TESTING = True
    # Define the database
    SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}'.format('mysql+pymysql', os.getenv('DATABASE_USERNAME'),
                                                           os.getenv('DATABASE_PASSWORD'), os.getenv('DATABASE_HOST'),
                                                           os.getenv('DATABASE_PORT'), os.getenv('DATABASE_NAME'))


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEVELOPMENT = False
    # Define the database
    SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}'.format('mysql+pymysql', os.getenv('DATABASE_USERNAME'),
                                                           os.getenv('DATABASE_PASSWORD'), os.getenv('DATABASE_HOST'),
                                                           os.getenv('DATABASE_PORT'), os.getenv('DATABASE_NAME'))


key = Config.SECRET_KEY
basedir = Config.PROJECT_ROOT

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
