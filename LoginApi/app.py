from src.config.configApi import app, ConfigApi
from src.routes.login.loginRoute import LoginRoute
from src.routes.user.userRoute import UserRoutes

def __init__():
    ConfigApi()
    UserRoutes()
    LoginRoute()

    app.debug = False

    app.run(port=3333)

__init__()