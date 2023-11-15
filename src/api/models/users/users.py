from pydantic import BaseModel

class User(BaseModel):
    user_id: int
    personal_token: str
    name: str
    mail: str