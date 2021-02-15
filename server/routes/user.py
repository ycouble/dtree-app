import app_config

from flask import Blueprint, request, jsonify, session
from flask_cors import cross_origin

from services import microsoft_auth as ms_auth

user_api = Blueprint('user', __name__)


@user_api.route("/login", methods=['GET'])
@cross_origin(supports_credentials=True)
def login():
    test = True
    # TODO: Check comment below
    # Technically we could use empty list [] as scopes to do just sign in,
    # here we choose to also collect end user consent upfront
    query_parameters = request.args

    if 'redirect_url' in request.args:
        redirect_url = query_parameters.get('redirect_url')
        session["flow"] = ms_auth.build_auth_code_flow(
            redirect_url=redirect_url, scopes=app_config.SCOPE)
        return jsonify({"auth_uri": session["flow"]["auth_uri"]}), 200
    else:
        return "Bad request", 400


@user_api.route("/connected", methods=['GET'])
@cross_origin(supports_credentials=True)
def is_connected():
    response = {"connected": "user" in session}
    return jsonify(response), 200


# Its absolute URL must match your app's redirect_uri set in AAD
@user_api.route("/redirect", methods=['GET'])
@cross_origin(supports_credentials=True)
def authorized():
    try:
        cache = ms_auth.load_cache(session.get("token_cache"))
        result = ms_auth.build_msal_app(cache=cache).acquire_token_by_auth_code_flow(
            session.get("flow", {}), request.args)
        if "error" in result:
            return jsonify({
                "authorized": False,
                "error": result.get("error"),
                "error_description": result.get("error_description")
            }), 200 
        session["user"] = result.get("id_token_claims")
        ms_auth.save_cache(session, cache)
    except ValueError as error:  # Usually caused by CSRF
        pass  # Simply ignore them
    if not request.args or not ms_auth.is_authorised_user(session.get("user")):
        username = ""
        if session.get("user"):
            username = session.get("user").get("preferred_username", "")
        return jsonify({
            "authorized": False,
            "error": "Forbidden",
            "error_description": f"Authorization denied for this user {username}\nPlease contact the website administrator."
        }), 200
    return jsonify({"authorized": True}), 200


@user_api.route("/logout", methods=['GET'])
@cross_origin(supports_credentials=True)
def logout():
    # TODO: Handle logout without redirect and set API on valraiso account
    query_parameters = request.args

    if 'redirect_url' in request.args:
        redirect_url = query_parameters.get('redirect_url')

        # Wipe out user and its token cache from session
        session.clear()
        # Also logout from your tenant's web session
        logout_uri = (app_config.AUTHORITY + "/oauth2/v2.0/logout" +
                      "?post_logout_redirect_uri=" + redirect_url)
        return jsonify({"logout_uri": logout_uri}), 200
    else:
        return "Bad request", 400

# @user_api.route("/graphcall")
# def graphcall():
#     token = ms_auth.get_token_from_cache(session, app_config.SCOPE)
#     if not token:
#         return redirect(url_for("login"))
#     graph_data = requests.get(  # Use token to call downstream service
#         ms_auth.ME_ENDPOINT,
#         headers={'Authorization': 'Bearer ' + token['access_token']},
#     ).json()
#     return render_template('display.html', result=graph_data)
