import json

from flask import Blueprint, request, jsonify, send_from_directory

from controllers.dtree import get_document_nodes, get_actual_document_id

from services.exceptions import PyMongoError

dtree_api = Blueprint('dtree', __name__)


@dtree_api.route('/', methods=['GET'])
def get_node():
    query_parameters = request.args

    try:
        node = get_document_nodes(query_parameters.get("document_id"))
    except PyMongoError as err:
        return f"Resource could not be found, {err}", 404

    return jsonify(node)


@dtree_api.route('/id', methods=['GET'])
def get_document_id():
    try:
        node = get_actual_document_id()
    except PyMongoError as err:
        return f"Resource could not be found, {err}", 404

    return jsonify(node)


# TODO: rename path on mongo
@dtree_api.route("/files/<path:path>")
def get_file(path):
    return send_from_directory("data", path)
