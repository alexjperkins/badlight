from flask import Flask, jsonify


_VERSION = "0.0.1"
_API_ROOT = "api/v1"


def create_app():
    app = Flask(__name__)

    @app.route("/version", methods=["GET"])
    def version():
        return jsonify({"version": _VERSION}), 200

    from .blueprints import register_blueprints

    register_blueprints(app, _API_ROOT)

    return app
