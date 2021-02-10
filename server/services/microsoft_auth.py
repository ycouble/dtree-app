import msal

import app_config

from services.user_whitelist import USER_WHITELIST

ME_ENDPOINT = 'https://graph.microsoft.com/v1.0/me'


def load_cache(token_cache):
    cache = msal.SerializableTokenCache()
    if token_cache:
        cache.deserialize(token_cache)
    return cache


def save_cache(session, cache):
    if cache.has_state_changed:
        session["token_cache"] = cache.serialize()


def build_msal_app(cache=None, authority=None):
    return msal.ConfidentialClientApplication(
        app_config.CLIENT_ID, authority=authority or app_config.AUTHORITY,
        client_credential=app_config.CLIENT_SECRET, token_cache=cache)


def build_auth_code_flow(redirect_url, authority=None, scopes=None):
    return build_msal_app(authority=authority).initiate_auth_code_flow(
        scopes or [],
        redirect_uri=redirect_url)


def get_token_from_cache(session, scope=None):
    # This web app maintains one cache per session
    cache = load_cache(session.get("token_cache"))
    cca = build_msal_app(cache=cache)
    accounts = cca.get_accounts()
    if accounts:  # So all account(s) belong to the current signed-in user
        result = cca.acquire_token_silent(scope, account=accounts[0])
        save_cache(session, cache)
        return result


def is_authorised_user(user_session):
    return user_session and user_session.get("preferred_username") in USER_WHITELIST