import os
from pathlib import Path

from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


_VERSION = "0.0.1"
_API_ROOT = "api/v1"
_PROJECT_ROOT = Path(__file__).parent

migrate = Migrate()
db = SQLAlchemy()


def create_app(*, environment=None):
    app = Flask(__name__)

    from .blueprints import register_blueprints
    from .schema import schema
    from .utils.bootstrap import bootstrap_models
    from .utils.graphql import initialize_graphql
    from .utils.config import initialize_config
    from .utils.environment import initialize_environment

    environment = environment or os.environ.get("BADLIGHT_ENVIRONMENT", "local")
    initialize_environment(environment=environment)
    initialize_config(app=app, environment=environment)
    initialize_graphql(app=app, schema=schema)

    db.init_app(app)
    # bootstraps multiple model files
    # must be performed before instatiating ``migrate``
    bootstrap_models(project_root=_PROJECT_ROOT)
    migrate.init_app(app, db)

    @app.route("/version", methods=["GET"])
    def version():
        return jsonify({"version": _VERSION}), 200

    register_blueprints(app, _API_ROOT)

    return app
