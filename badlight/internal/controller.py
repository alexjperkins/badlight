from flask import jsonify, Blueprint


internal_blueprint = Blueprint("Internal", __name__)


@internal_blueprint.route('/__healthcheck__', methods=['GET'])
def healthcheck():
    return jsonify('healthy'), 200
