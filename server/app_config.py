import os
import configparser

config = configparser.ConfigParser()
config.read('.credentials.ini')

# Application port
PORT = 5000

DEBUG = True

# Application (client) ID of app registration
CLIENT_ID = config['microsoft_api']['client_id']
CLIENT_SECRET = config['microsoft_api']['client_secret']

AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app
# AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

# You can find the proper permission names from this document
# https://docs.microsoft.com/en-us/graph/permissions-reference
SCOPE = ["User.Read"]

# Specifies the token cache should be stored in server-side session
SESSION_TYPE = "filesystem"
SECRET_KEY = config['dtree_app']['secret_key']

# Set-up Cors headers
CORS_HEADERS = 'Content-Type'
