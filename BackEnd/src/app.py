from src.config.configApi import app, ConfigApi
from src.routes.login.loginRoute import LoginRoute
from src.routes.user.userRoute import UserRoutes
from src.routes.enterprise.enterpriseRoute import EnterpriseRoutes
from src.routes.stock.stockRoute import StockRoutes

def __init__():
    ConfigApi()
    UserRoutes()
    EnterpriseRoutes()
    StockRoutes()
    LoginRoute()

    app.debug = False

    app.run(port=3333)
