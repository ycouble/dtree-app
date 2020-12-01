import flask

from flask import request, jsonify
from flask_cors import CORS
from dtree import DTree

app = flask.Flask("DTree")
app.config["DEBUG"] = True
CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

@app.route('/api/v1/dtree', methods=['GET'])
def api_dtree_id():
    query_parameters = request.args

    node = None
    if 'id' in request.args:
        node_id = int(query_parameters.get('id'))
        node = dtree.get_node(node_id)
    else:
        node = dtree.root_node
    
    if node is not None:
        return jsonify(node.get_content())
    else:
        return "<h1>404</h1><p>The resource could not be found.</p>", 404


if __name__ == "__main__":
    dtree = DTree()
    dtree.deep_print()
    app.run(host= "0.0.0.0", debug=True, port = 5000, threaded=True)