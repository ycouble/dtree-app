from flask import Blueprint, request, jsonify
from dtree.dtree import DTree

dtree_api = Blueprint('dtree', __name__)


@dtree_api.route('/', methods=['GET'])
def api_dtree_id():
    tree = DTree()

    query_parameters = request.args

    content = None
    if 'id' in request.args:
        node_id = query_parameters.get('id')
        content = tree.get_node_content(node_id)
    else:
        content = tree.get_node_content()

    if content is not None:
        return jsonify(content)
    else:
        return "Resource could not be found", 404
