from models import server_config as m_config
from models import xmind_documents as m_xdocs

from services import file_management

def get_document_nodes(document_id=None):
    if not document_id:
        document_id = m_config.get_config()["xmind_document_selected"]
    document = m_xdocs.find_document(document_id)
    document['id'] = str(document.pop('_id'))
    return document

def get_actual_document_id():
    document_id = m_config.get_config()["xmind_document_selected"]
    return str(document_id)