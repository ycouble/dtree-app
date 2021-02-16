from flask import Blueprint, request, jsonify, session
from flask_cors import cross_origin

from controllers.user_dtree import save_xmind_file

from services import microsoft_auth as ms_auth
from services.exceptions import FileUploadError

user_dtree_api = Blueprint('user_dtree', __name__)


@user_dtree_api.route("/", methods=['POST'])
@cross_origin(supports_credentials=True)
def upload_xmind_file():
    user = session.get("user")
    if not ms_auth.is_authorised_user(user):
        return "Forbidden", 403
    if 'file' not in request.files:
        return "No file - bad request", 400
    xmind_file = request.files['file']
    if xmind_file.filename == '':
        return "No selected file - bad request", 400
    try:
        save_xmind_file(xmind_file, user)
    except FileUploadError as err:
        return f"{err}", 400
    return "Ok", 200
