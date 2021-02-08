import flask

from flask import request, jsonify
from flask_cors import CORS
from dtree.dtree import DTree

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

    content = None
    if 'id' in request.args:
        node_id = query_parameters.get('id')
        content = dtree.get_node_content(node_id)
    else:
        content = dtree.get_node_content()
    
    if content is not None:
        return jsonify(content)
    else:
        return "<h1>404</h1><p>The resource could not be found.</p>", 404


if __name__ == "__main__":
    dtree = DTree()
    # dtree.deep_print()
    # import pdb; pdb.set_trace()
    app.run(host= "0.0.0.0", debug=True, port = 5000, threaded=True)