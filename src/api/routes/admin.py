from fastapi import HTTPException, APIRouter, Depends
import jwt
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

from src.models.admin.admin import (AdminTokenResponse, GenerateAdminToken)
from src.models.students.students import (StudentModel, StudentID, StudentCreate, StudentDelete)
from src.models.languages.languages import (LanguageModel, LanguageID, LanguageDelete, LanguageCreateAndUpdate)

from src.models.students.db_students import DB_Students
from src.models.languages.db_languages import DB_Languages

from src.api.middlewares.header_verification import verfiy_headers_admin

router = APIRouter()

load_dotenv()
ADMIN_PASS = os.getenv('ADMIN_PASS')

# Ruta para generar un token JWT para el admin
@router.post("/token", response_model = AdminTokenResponse)
async def generate_admin_token(
    password: GenerateAdminToken
):
    if password != ADMIN_PASS:
        raise HTTPException(status_code=401, detail="Unauthorized")

    # Información que se incluirá en el token
    token_data = {
        "admin": True,
        "exp": datetime.utcnow() + timedelta(hours=1)  # Token válido por 1 hora
    }

    # Recogemos el private key
    dir_path = os.path.dirname(os.path.realpath(__file__))
    private_key_path = os.path.join(dir_path, "..", "..", "..", "certs", "private.pem")
    
    with open(private_key_path, 'r') as key_file:
        private_key = serialization.load_pem_private_key(key_file.read())

    token = jwt.encode(token_data, private_key, algorithm="RS256")

    return {"token": token}


# Rutas para estudiantes
@router.post("/students/", response_model=StudentCreate)
async def add_student(
    student: StudentModel,
    _: bool = Depends(verfiy_headers_admin)
):
    with DB_Students() as db:
        student_id = db.add(student.dict())

    # Creamos el token para el student
    # Información que se incluirá en el token
    token_data = {
        "student_id":student_id
    }

    # Recogemos el private key
    dir_path = os.path.dirname(os.path.realpath(__file__))
    private_key_path = os.path.join(dir_path, "..", "..", "..", "certs", "private.pem")
    
    with open(private_key_path, 'r') as key_file:
        private_key = serialization.load_pem_private_key(key_file.read())
    
    # Añadimos el token al student
    student.token = jwt.encode(token_data, private_key, algorithm="RS256")
        
    return student


@router.put("/students/{student_id}", response_model=StudentModel)
async def update_student(
    student_id: StudentID, 
    student: StudentModel,
    _: bool = Depends(verfiy_headers_admin)
):
    with DB_Students() as db:
        db.update(student_id, student.dict())
        
    return student


@router.delete("/students/{student_id}", status_code=200, response_model=StudentDelete)
async def delete_student(
    student_id: StudentID,
    _: bool = Depends(verfiy_headers_admin)
):
    with DB_Students() as db:
        result = db.delete(student_id)
    
    return {"student_id": student_id, "message": result}



# Rutas para idiomas
@router.post("/languages/", response_model=LanguageCreateAndUpdate)
async def add_language(
    language: LanguageModel,
    _: bool = Depends(verfiy_headers_admin)
):
    with DB_Languages() as db:
        language_id = db.add(language.dict())

    return {"language_id": language_id, "name":language.name}


@router.put("/languages/{language_id}", response_model=LanguageCreateAndUpdate)
async def update_language(
    language_id: LanguageID, 
    language: LanguageModel,
    _: bool = Depends(verfiy_headers_admin)
):
    with DB_Languages() as db:
       db.update(language_id, language.dict())
    
    return language


@router.delete("/languages/{language_id}", status_code=200, response_model=LanguageDelete)
async def delete_language(
    language_id: LanguageID,
    _: bool = Depends(verfiy_headers_admin)
):
    with DB_Languages() as db:
        result = db.delete(language_id)
    
    return {"language_id": language_id, "message": result}