
from schema import Schema, And, Use, Optional
from bson.objectid import ObjectId

from models import schema
from services.create_app import mongo


# TODO: logger

def insert_node(node, document_id):
    to_insert = {}
    # TODO: check document exist
    to_insert["document_id"] = document_id
    to_insert["node_info"] = node
    # TODO: error handling
    if not schema.is_valid(node_schema, to_insert):
        return None
    inserted = mongo.db.nodes.insert_one(to_insert).inserted_id
    return inserted

def find_node(node_id, document_id):
    finder = mongo.db.nodes.find({
        "document_id": document_id, "node_info": {"id": node_id}})
    # TODO error handling on length
    if len(finder) == 0:
        return None
    return finder[0].get("node_info", {})


node_schema = Schema({
    'document_id': And(Use(ObjectId)),
    'node_info': {
        'title': And(Use(str)),
        Optional('description'): And(Use(str)),
        'type': And(Use(str)),
        'id': And(Use(str), lambda s: len(s) == 36 or len(s) ==  26),
        'children_id': And(Use(list)),
        Optional('attachements_id'): And(Use(list)),
        Optional("href"): And(Use(str))
    }
})

# Possible key depending nodes type:
#   APP_NAME = ['title', 'description', 'type', 'id', 'children_id', 'attachement_id']
#   STEP = ['title', 'description', 'type', 'id', 'children_id', 'attachement_id']
#   QUESTION = ['title', 'type', 'id', 'children_id', 'attachement_id']
#   ANSWER = ['title', 'type', 'id', 'children_id']
#   ATTACHEMENT = ['title', 'type', 'id', 'children_id', 'href']
#   EXTERNAL_LINK = ['title', 'type', 'id', 'children_id', 'href']
#   SKIP = ['title', 'description', 'type', 'id', 'children_id', 'attachement_id']