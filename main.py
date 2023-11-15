from src.api.app_instance import app
from src.api.routes import root

app.include_router(root.router) # Sin prefijos y sin middleware, por si tenemos landing
app.include_router()