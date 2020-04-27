import pytest

from badlight.app import create_app


@pytest.fixture(scope="session")
def app():
    app = create_app()
    with app.app_context():
        yield app


@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client
