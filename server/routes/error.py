from flask import Blueprint, request, jsonify

error_api = Blueprint('error', __name__)

@error_api.errorhandler(404)
def not_found(e):
    return "Route forbidden", 403

