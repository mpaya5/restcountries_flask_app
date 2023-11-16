from pydantic import BaseModel, Field

class AdminTokenResponse(BaseModel):
    token: str

class GenerateAdminToken(BaseModel):
    password: str = Field(..., description="La contraseña de la plataforma es necesaria para poder crear tokens válidos de una hora para el admin.")