"""This code is mostly taken from:

``https://github.com/gianchub/alembic-verify/blob/master/alembicverify/util.py``

This repo hasn't been active for a while; but has a nice solution for
comparing models and migrations
"""
import pytest
from sqlalchemydiff import compare
from sqlalchemydiff.util import (
    destroy_database, get_temporary_uri, new_db, prepare_schema_from_models,
)
from sqlalchemy.ext.declarative import declarative_base

from ..helpers.database.alembic import (
    make_alembic_config,
    prepare_schema_from_migrations,
)


@pytest.fixture(scope="module")
def uri_left(db_uri):
    return get_temporary_uri(db_uri)


@pytest.fixture(scope="module")
def uri_right(db_uri):
    return get_temporary_uri(db_uri)


@pytest.fixture
def alembic_config_left(uri_left, alembic_root):
    return make_alembic_config(uri_left, alembic_root)


@pytest.fixture
def new_db_left(uri_left):
    new_db(uri_left)
    yield
    destroy_database(uri_left)


@pytest.fixture
def new_db_right(uri_right):
    new_db(uri_right)
    yield
    destroy_database(uri_right)


@pytest.mark.usefixtures("new_db_left")
@pytest.mark.usefixtures("new_db_right")
def test_model_migration_comparision(
    database, uri_left, uri_right, alembic_config_left
):
    prepare_schema_from_migrations(uri_left, alembic_config_left)
    prepare_schema_from_models(uri_right, declarative_base())

    result = compare(uri_left, uri_right, set(['alembic_version']))
    assert result.is_match
