from alembic import command
from alembic.config import Config
from alembic.script import ScriptDirectory
from sqlalchemy import create_engine


def make_alembic_config(uri, folder):
    config = Config()
    config.set_main_option("script_location", folder)
    config.set_main_option("sqlalchemy.url", uri)
    return config


def prepare_schema_from_migrations(uri, config, revision="head"):
    """
    Apply migrations to a database.
    """
    engine = create_engine(uri)
    script = ScriptDirectory.from_config(config)
    command.upgrade(config, revision)
    return engine, script
