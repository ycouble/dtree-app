import app_config

from flask import Flask
from flask_cors import CORS
from flask_session import Session
# from werkzeug.middleware.proxy_fix import ProxyFix

from routes import dtree, user

app = Flask("DTree")
app.config.from_object(app_config)
Session(app)
CORS(app)

app.register_blueprint(dtree.dtree_api, url_prefix='/api/dtree')
app.register_blueprint(user.user_api, url_prefix='/api/user')

# app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)


@app.errorhandler(404)
def not_found(e):
    return "Route forbidden", 403


# https://blog.miguelgrinberg.com/post/how-to-deploy-a-react--flask-project

if __name__ == "__main__":
    app.run(port=app_config.PORT, debug=app_config.DEBUG, threaded=True)
