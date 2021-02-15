from flask import Blueprint, request, jsonify, session
from flask_cors import cross_origin

from models import nodes as m_nodes
from models import xmind_documents as m_xdocs

from services import microsoft_auth as ms_auth
from services import file_management

from services.exceptions import DTreeValidationError
from services.xmind_parser.dtree import DTree
from services.xmind_parser.node_type import to_str

user_dtree_api = Blueprint('user_dtree', __name__)


@user_dtree_api.route("/", methods=['POST'])
@cross_origin(supports_credentials=True)
def upload_file():
    if not ms_auth.is_authorised_user(session.get("user")):
        return "Forbidden", 403
    if 'file' not in request.files:
        return "No file - bad request", 400
    xmind_file = request.files['file']
    if xmind_file.filename == '':
        return "No selected file - bad request", 400
    # TODO: move this section in services?
    xmind_zipfile, xmind_file_as_bytes = file_management.open_xmind_file(xmind_file)
    if xmind_zipfile:
        secure_filename = file_management.get_secure_filename(xmind_file.filename)
        path_name = file_management.create_new_path()
        try:
            dtree = DTree(filename=secure_filename,
                         dir_name=path_name,
                         from_memory=xmind_zipfile)
        except DTreeValidationError as err:
            print(err)
            return "Bad request", 400
        dtree_dump = dtree.get_content()
        dtree_nodes = dtree_dump.pop("nodes")
        # TODO: Exceptions
        document_id = m_xdocs.insert_document(dtree_dump)
        if not document_id:
            return "Bad request", 400
        for node in dtree_nodes:
            m_nodes.insert_node(to_str(node), document_id)
        file_management.save_xmind_files(xmind_file_as_bytes, dtree)
        return "Ok", 200
    return "Bad request", 400
