from models import nodes as m_nodes
from models import server_config as m_config
from models import xmind_documents as m_xdocs

from services import file_management

from services.exceptions import PyMongoError
from services.xmind_parser.dtree import DTree
from services.xmind_parser.node_type import to_str

def get_multiple_node(nodes_id, document_id):
    nodes = []
    for node_id in nodes_id:
        node = m_nodes.find_node(node_id, document_id)
        nodes.append(node)
    return nodes

def get_formatted_node(node_id=None, document_id=None):
    if not document_id:
        document_id = m_config.get_config()["xmind_document_selected"]
    document = m_xdocs.find_document(document_id)
    if not node_id:
        node_id = document["root_node_id"]
    main_node = m_nodes.find_node(node_id, document_id)

    # TODO: Check node type ?
    children_id = main_node.pop("children_id", [])
    main_node["children"] = get_multiple_node(children_id, document_id)
    if "attachements_id" in main_node:
        attachements_id = main_node.pop("attachements_id", [])
        main_node["attachements"] = get_multiple_node(attachements_id, document_id)

    if main_node["type"] == "ATTACHEMENT":
        main_node["href"] = document["folder_name"] + main_node["href"]

    return main_node