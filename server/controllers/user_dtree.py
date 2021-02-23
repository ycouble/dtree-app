from models import server_config as m_config
from models import xmind_documents as m_xdocs

from services import file_management

from services.exceptions import (DTreeValidationError,
                                 DTreeProgrammingError,
                                 FileUploadError,
                                 PyMongoError)
from services.xmind_parser.dtree import DTree


def save_xmind_file(xmind_file, user):
    xmind_zipfile, xmind_file_as_bytes = file_management.open_xmind_file(xmind_file)
    if not xmind_zipfile:
        raise FileUploadError("Xmind file not valid")
    secure_filename = file_management.get_secure_filename(xmind_file.filename)
    path_name = file_management.create_new_path()

    try:
        dtree = DTree(filename=secure_filename,
                        dir_name=path_name,
                        from_memory=xmind_zipfile)
        dtree_dump = dtree.get_content()
    except (DTreeValidationError, DTreeProgrammingError) as err:
        raise FileUploadError(f"Dtree error {err}")
    # dtree_nodes = dtree_dump.pop("nodes")

    try:
        document_id = m_xdocs.insert_document(dtree_dump)
        if not document_id:
            raise FileUploadError(f"Missing document id")
        # for node in dtree_nodes:
        #     m_nodes.insert_node(to_str(node), document_id)
        # OTHER API:
        m_config.update_config(document_id, user.get("preferred_username", ""))
    except PyMongoError as err:
        # TODO Delete concerning node in mongo
        raise FileUploadError(f"MongoDB error {err}")

    file_management.save_xmind_files(xmind_file_as_bytes, dtree)
