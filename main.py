from src.api.app_instance import app
from src.api.routes import root, admin, student

app.include_router(root.router)
app.include_router(admin.router, prefix='/admin', tags=["admin"])
app.include_router(student.router, prefix="/student", tags=["student"])