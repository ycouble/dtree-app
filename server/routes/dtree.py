import json

from flask import Blueprint, request, jsonify

from controllers.dtree import get_formatted_node

from services.exceptions import PyMongoError

dtree_api = Blueprint('dtree', __name__)


@dtree_api.route('/', methods=['GET'])
def get_node():
    query_parameters = request.args

    try:
        node = get_formatted_node(query_parameters.get("id"))
    except PyMongoError as err:
        return f"Resource could not be found, {err}", 404

    return jsonify(node)

