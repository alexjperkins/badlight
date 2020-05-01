from pathlib import Path
from urllib.parse import urlparse

import flask_migrate
from flask_sqlalchemy import SQLAlchemy
from graphene.test import Client as GraphQLClient
import pytest
from pytest_postgresql.factories import DatabaseJanitor

from badlight.app import create_app
from badlight.schema import schema as badlight_graphql_schema


@pytest.fixture(scope="session")
def app():
    app = create_app(environment='testing')
    with app.app_context():
        yield app


@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client


@pytest.fixture(scope="session", autouse=True)
def database(request, db_uri, postgres_db_version, app):
    parsed = urlparse(db_uri)
    user, password = parsed.netloc.split("@")[0].split(":")
    host, port = parsed.netloc.split("@")[1].split(":")
    db_name = parsed.path.replace("/", "")

    DatabaseJanitor(
        user=user,
        host=host,
        port=port,
        db_name=db_name,
        version=postgres_db_version,
        password=password
    ).init()
    flask_migrate.upgrade(directory="./migrations", revision="head")

    @request.addfinalizer
    def drop_database():
        DatabaseJanitor(
            user=user,
            host=host,
            port=port,
            db_name=db_name,
            version=postgres_db_version,
            password=password
        ).drop()


@pytest.fixture
def _shared_db_session(db_session, mocker):
    """
    This ensures that all interaction with the database, from seeds,
    application code or test fixtures themselves all interact with
    the exact same database session
    """
    mocker.patch("badlight.app.db.session", db_session)
    yield


@pytest.fixture(scope="session")
def _db(app):
    db = SQLAlchemy(app=app)
    return db


@pytest.fixture(scope="session")
def db_uri(app):
    return app.config['SQLALCHEMY_DATABASE_URI']


@pytest.fixture(scope="session")
def postgres_db_version(app):
    return app.config['POSTGRES_VERSION']


@pytest.fixture
def alembic_root(app):
    return str(Path(app.root_path) / "migrations")


@pytest.fixture
def graphql_client():
    return GraphQLClient(badlight_graphql_schema)
