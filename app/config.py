import os


class Config(object):

    basedir = os.path.abspath(os.path.dirname(__file__))

    POSTGRES_SERVICE_NAME = os.getenv(
        "POSTGRES_SERVICE_NAME", default='127.0.0.1')
    POSTGRES_USER = os.getenv("POSTGRES_USER", default='postgres_user')
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", default='postgres_pass')
    POSTGRES_DB = os.getenv("POSTGRES_DB", default='postgres_db')

    SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{pw}@{url}/{db}'.format(
        user=POSTGRES_USER, pw=POSTGRES_PASSWORD, url=POSTGRES_SERVICE_NAME, db=POSTGRES_DB)


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DebugConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = os.getenv('SECRET_KEY', default='9JaLkLmiZWJmJEHHEKGb')


config_dict = {
    'Production': ProductionConfig,
    'Debug': DebugConfig
}
