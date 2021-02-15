from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo
from flask_session import Session


mongo = PyMongo()

def create_app(app_config):
    app = Flask("DTree")
    app.config.from_object(app_config)

    Session(app)
    CORS(app)

    mongo.init_app(app)

    return app