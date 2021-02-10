import os

# Application port
PORT = 5000

DEBUG = True

# Application (client) ID of app registration
CLIENT_ID = "06b0e518-e191-4997-a88b-1a3972e53928"

# Placeholder - for use ONLY during testing.
CLIENT_SECRET = "L4.N~94_yTc~KqTd4BH.07.DJXAFsUmuN5"
# In a production app, we recommend you use a more secure method of storing your secret,
# like Azure Key Vault. Or, use an environment variable as described in Flask's documentation:
# https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
# CLIENT_SECRET = os.getenv("CLIENT_SECRET")
# if not CLIENT_SECRET:
#     raise ValueError("Need to define CLIENT_SECRET environment variable")

AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app
# AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

# You can find the proper permission names from this document
# https://docs.microsoft.com/en-us/graph/permissions-reference
SCOPE = ["User.ReadBasic.All"]

# Specifies the token cache should be stored in server-side session
SESSION_TYPE = "filesystem"
SECRET_KEY = "changeme"

# Set-up Cors headers
CORS_HEADERS = 'Content-Type'
