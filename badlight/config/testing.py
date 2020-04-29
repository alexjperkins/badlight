from .common import CommonConfig


class TestingConfig(CommonConfig):
    TESTING = True
    FLASK_ENV = "testing"
