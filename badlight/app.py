from flask import Flask


_VERSION = '0.0.1'
_API_ROOT = 'api/v1'


def create_app():
    app = Flask(__name__)

    @app.route('/version', methods=['GET'])
    def version():
        return f'<div>{_VERSION}</div>'

    from .blueprints import register_blueprints

    register_blueprints(app, _API_ROOT)

    return app
