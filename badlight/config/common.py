import os

from . import build_database_connection_uri_string


class CommonConfig:
    ### --- FLASK --- ###
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    FLASK_ENV = os.environ.get("BADLIGHT_ENVIRONMENT", "local")

    ### --- SQLALCHEMY --- ###
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### --- POSTGRESQL --- ###
    @property
    def SQLALCHEMY_DATABASE_URI(self):
        return build_database_connection_uri_string(environment=self.FLASK_ENV)

    @property
    def POSTGRES_VERSION(self):
        return 12.1
