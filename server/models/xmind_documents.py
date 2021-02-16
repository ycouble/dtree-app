import datetime
from schema import Schema, And, Use

from models import schema
from services.create_app import mongo
from services.exceptions import PyMongoError

#TODO: Logger

def insert_document(document_info): 
    document_info["datetime"] = datetime.datetime.now()
    # TODO: error handling
    if not schema.is_valid(document_schema, document_info):
        raise PyMongoError(f"Schema not valid.")
    inserted = mongo.db.xmind_documents.insert_one(document_info).inserted_id
    return inserted

def find_document(document_id):
    finder = mongo.db.xmind_documents.find({"_id": document_id})
    # TODO error handling on length
    if finder.count() == 0:
        raise PyMongoError(f"Not document found. ({document_id})")
    return finder[0]

document_schema = Schema({
    'display_name': And(Use(str)),
    'folder_name': And(Use(str)),
    'root_node_id': And(Use(str), lambda s: len(s) == 36 or len(s) ==  26),
    'node_length': And(Use(int)),
    'datetime': And()
})