from src.api.app_instance import app
from src.api.routes import root, admin

app.include_router(root.router) # Sin prefijos y sin middleware, por si tenemos landing
app.include_router(admin.router, prefix='/admin', tags=["admin"])