import pdb
import msal

from flask import Flask, request, jsonify, session, redirect
from flask_cors import CORS, cross_origin
from flask_session import Session
from werkzeug.middleware.proxy_fix import ProxyFix

import app_config
from dtree.dtree import DTree

app = Flask("DTree")
app.config["DEBUG"] = True
app.config.from_object(app_config)
Session(app)
CORS(app)

# app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)


@app.errorhandler(404)
def not_found(e):
    return "Route forbidden", 403


@app.route("/api/login", methods=['GET'])
@cross_origin(supports_credentials=True)
def login():
    # TODO: Check comment below
    # Technically we could use empty list [] as scopes to do just sign in,
    # here we choose to also collect end user consent upfront
    query_parameters = request.args

    if 'redirect_url' in request.args:
        redirect_url = query_parameters.get('redirect_url')
        session["flow"] = _build_auth_code_flow(
            redirect_url=redirect_url, scopes=app_config.SCOPE)
        return jsonify({"auth_uri": session["flow"]["auth_uri"]}), 200
    else:
        return "Bad request", 400


@app.route("/api/connected", methods=['GET'])
@cross_origin(supports_credentials=True)
def is_connected():
    response = {"connected": "user" in session}
    return jsonify(response), 200


# Its absolute URL must match your app's redirect_uri set in AAD
@app.route("/api/redirect", methods=['GET'])
@cross_origin(supports_credentials=True)
def authorized():
    try:
        cache = _load_cache()
        result = _build_msal_app(cache=cache).acquire_token_by_auth_code_flow(
            session.get("flow", {}), request.args)
        if "error" in result:
            return jsonify({
                "authorized": False,
                "error": result.get("error"),
                "error_description": result.get("error_description")
            }), 200
        session["user"] = result.get("id_token_claims")
        _save_cache(cache)
    except ValueError as error:  # Usually caused by CSRF
        pass  # Simply ignore them
    return jsonify({"authorized": True}), 200


@app.route("/api/logout", methods=['GET'])
@cross_origin(supports_credentials=True)
def logout():
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


# @app.route("/graphcall")
# def graphcall():
#     token = _get_token_from_cache(app_config.SCOPE)
#     if not token:
#         return redirect(url_for("login"))
#     graph_data = requests.get(  # Use token to call downstream service
#         app_config.ENDPOINT,
#         headers={'Authorization': 'Bearer ' + token['access_token']},
#     ).json()
#     return render_template('display.html', result=graph_data)


@app.route('/api/dtree', methods=['GET'])
def api_dtree_id():
    query_parameters = request.args

    content = None
    if 'id' in request.args:
        node_id = query_parameters.get('id')
        content = dtree.get_node_content(node_id)
    else:
        content = dtree.get_node_content()

    if content is not None:
        return jsonify(content)
    else:
        return "Resource could not be found", 404


def _load_cache():
    cache = msal.SerializableTokenCache()
    if session.get("token_cache"):
        cache.deserialize(session["token_cache"])
    return cache


def _save_cache(cache):
    if cache.has_state_changed:
        session["token_cache"] = cache.serialize()


def _build_msal_app(cache=None, authority=None):
    return msal.ConfidentialClientApplication(
        app_config.CLIENT_ID, authority=authority or app_config.AUTHORITY,
        client_credential=app_config.CLIENT_SECRET, token_cache=cache)


def _build_auth_code_flow(redirect_url, authority=None, scopes=None):
    return _build_msal_app(authority=authority).initiate_auth_code_flow(
        scopes or [],
        redirect_uri=redirect_url)


def _get_token_from_cache(scope=None):
    cache = _load_cache()  # This web app maintains one cache per session
    cca = _build_msal_app(cache=cache)
    accounts = cca.get_accounts()
    if accounts:  # So all account(s) belong to the current signed-in user
        result = cca.acquire_token_silent(scope, account=accounts[0])
        _save_cache(cache)
        return result


app.jinja_env.globals.update(
    _build_auth_code_flow=_build_auth_code_flow)  # Used in template

if __name__ == "__main__":
    dtree = DTree()
    # dtree.deep_print()
    # pdb.set_trace()
    app.run()
