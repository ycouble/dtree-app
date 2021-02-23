import app_config

from routes import dtree, user, user_dtree, error
from services.create_app import create_app


# https://blog.miguelgrinberg.com/post/how-to-deploy-a-react--flask-project

#TODO: Logger

if __name__ == "__main__":
    app = create_app(app_config)

    app.register_blueprint(error.error_api)
    app.register_blueprint(dtree.dtree_api, url_prefix='/api/dtree')
    app.register_blueprint(user.user_api, url_prefix='/api/user')
    app.register_blueprint(user_dtree.user_dtree_api, url_prefix='/api/user/dtree')

    app.run(port=app_config.PORT, debug=app_config.DEBUG, threaded=True)


# API Description

# GET /api/dtree/node -> Get default version & root node
# GET /api/dtree/node/<:id> -> Get default version & specific node
# GET /api/dtree/<:id>/node -> Get specific version & root node 
# GET /api/dtree/<:id>/node/<:id> -> Get specific version & specific node
# GET /api/dtree/version -> Get default document version

# GET /api/user/login -> Redirect user to oauth page
# GET /api/user/connected -> Test if user is connected
# GET /api/user/redirect -> Store token in session
# GET /api/user/logout -> Logout user from session

# POST /api/user/dtree -> upload new file
# POST /api/user/dtree/<:id>/default -> Set default dtree
# GET /api/user/dtree -> get list off existing app
# DELETE /api/user/dtree/<:id> -> delete old version


# from services.xmind_parser.dtree import DTree
# from services.exceptions import DTreeValidationError

# if __name__ == "__main__":
#     try:
#         dtree = DTree(filename="OAD Salmonelles_v5.xmind", dir_name="data/")
#     except DTreeValidationError as err:
#         print(err)
#         exit(84)
#     print(dtree)
#     import pdb
#     pdb.set_trace()