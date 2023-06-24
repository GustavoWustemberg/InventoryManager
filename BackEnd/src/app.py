from src.config.configApi import ConfigApi
from src.config.configApi import app
from src.routes.login.loginRoute import LoginRoute
from src.routes.user.userRoute import UserRoutes
from src.routes.enterprise.enterpriseRoute import EnterpriseRoutes
from src.routes.stock.stockRoute import StockRoutes

ConfigApi()
UserRoutes()
EnterpriseRoutes()
StockRoutes()
LoginRoute()

app.debug = False

app.run(port=3333)
