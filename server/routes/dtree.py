import json

from flask import Blueprint, request, jsonify

from services.xmind_parser.dtree import DTree
from services.xmind_parser.node_type import NodeTypeEncoder
from services.exceptions import DTreeValidationError

dtree_api = Blueprint('dtree', __name__)


@dtree_api.route('/', methods=['GET'])
def api_dtree_id():
    try:
        tree = DTree()
    except DTreeValidationError as err:
        print(err)
        exit(84)

    query_parameters = request.args

    content = None

    # TODO: Return error 
    try:
        if 'id' in request.args:
            node_id = query_parameters.get('id')
            content = tree.get_node(node_id).get_content()
        else:
            content = tree.get_root_node().get_content()
        children_id = content.pop("children_id", [])
        content["children"] = []
        for child_id in children_id:
            content["children"].append(tree.get_node(child_id).get_content())
            
    except DTreeValidationError as err:
        print(err)

    print(json.dumps(content, cls=NodeTypeEncoder))
    if content is not None:
        return jsonify(json.dumps(content, cls=NodeTypeEncoder))
    else:
        return "Resource could not be found", 404
