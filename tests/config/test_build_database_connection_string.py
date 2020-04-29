import pytest

from badlight.config import build_database_connection_uri_string


@pytest.fixture
def mock_correct_db_env(monkeypatch):
    monkeypatch.setenv('POSTGRES_USER', 'user')
    monkeypatch.setenv('POSTGRES_PASSWORD', 'password')
    monkeypatch.setenv('POSTGRES_HOST', 'host')
    monkeypatch.setenv('POSTGRES_PORT', 'port')
    monkeypatch.setenv('POSTGRES_DB', 'db')


@pytest.fixture
def mock_incorrect_db_env(monkeypatch):
    monkeypatch.delenv('POSTGRES_USER', raising=True)


def test_build_database_connection_uri_string_correct_env(mock_correct_db_env):
    conn_str = build_database_connection_uri_string(
        environment='local',
    )
    assert conn_str == f"postgres://user:password@host:port/db"


def test_build_database_connection_uri_string_incorrect_env(mock_incorrect_db_env):
    with pytest.raises(KeyError):
        build_database_connection_uri_string(
            environment='local',
        )


def test_build_database_connection_uri_string_invalid_env():
    with pytest.raises(RuntimeError):
        build_database_connection_uri_string(
            environment='invalid'
        )


def test_build_database_connection_uri_string_testing(mock_correct_db_env):
    conn_str = build_database_connection_uri_string(
        environment='testing',
    )
    assert conn_str == f"postgres://user:password@host:port/db_testing"
