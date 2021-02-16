import datetime
from schema import Schema, And, Use
from bson.objectid import ObjectId

from models import schema
from services.create_app import mongo
from services.exceptions import PyMongoError

#TODO: Logger

def update_config(document_id, username):
    to_insert = {
        "xmind_document_selected": document_id,
        "username": username,
        "datetime": datetime.datetime.now()
    }
    # TODO: error handling
    if not schema.is_valid(config_schema, to_insert):
        raise PyMongoError(f"Schema not valid.")
    inserted = mongo.db.server_config.insert_one(to_insert).inserted_id
    return inserted

def get_config():
    finder = mongo.db.server_config.find({}).sort([("_id", -1)]).limit(1)
    # TODO error handling on length
    if finder.count() == 0:
        raise PyMongoError(f"No server config found.")
    return finder[0]

config_schema = Schema({
    'xmind_document_selected': And(Use(ObjectId)),
    'username': And(Use(str)),
    'datetime': And()
})