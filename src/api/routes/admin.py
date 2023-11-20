from fastapi import HTTPException, APIRouter, Depends
from typing import List
from pydantic import Field
import jwt
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

from src.models.admin.admin import (AdminTokenResponse, GenerateAdminToken)
from src.models.students.students import (StudentModel, GetStudentModel, StudentID, StudentCreate, StudentDelete)
from src.models.languages.languages import (GetLanguageModel, LanguageModel, LanguageID, LanguageDelete, LanguageCreateAndUpdate)
from src.models.student_languages.student_languages import (StudentLanguageID, StudentLanguages)

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

from src.models.students.db_students import DB_Students
from src.models.languages.db_languages import DB_Languages
from src.models.student_languages.db_student_languages import DB_StudentLanguages

from src.api.middlewares.header_verification import verfiy_headers_admin

router = APIRouter()

load_dotenv()
ADMIN_PASS = os.getenv('ADMIN_PASS')

from src.utils.logger import AppLogger
logger = AppLogger('my_app')

# Ruta para generar un token JWT para el admin
@router.post("/token", response_model = AdminTokenResponse)
async def generate_admin_token(
    data: GenerateAdminToken
):

    if data.password != ADMIN_PASS:
        raise HTTPException(status_code=401, detail="Unauthorized")

    # Información que se incluirá en el token
    token_data = {
        "admin_pass": data.password,
        "exp": datetime.utcnow() + timedelta(hours=1)  # Token válido por 1 hora
    }

    # Recogemos el private key
    dir_path = os.path.dirname(os.path.realpath(__file__))
    private_key_path = os.path.join(dir_path, "..", "..", "..", "certs", "private.pem")
    
    with open(private_key_path, 'rb') as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
            )

    logger.info(f"{token_data}, {private_key}")

    token = jwt.encode(token_data, private_key, algorithm="RS256")

    return {"token": token}


"""
Rutas del admin para manejar los estudiantes
"""
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
    
    with open(private_key_path, 'rb') as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
            )
    
    # Añadimos el token al student
    token = jwt.encode(token_data, private_key, algorithm="RS256")
        
    return {
        "name":student.name,
        "email":student.email,
        "token":token,
        "id":student_id
    }


@router.put("/students/{student_id}", response_model=StudentModel)
async def update_student(
    student_id: int, 
    student: StudentModel,
    _: bool = Depends(verfiy_headers_admin)
):
    with DB_Students() as db:
        db.update(student_id, student.dict())
        
    return student


@router.delete("/students/{student_id}", status_code=200, response_model=StudentDelete)
async def delete_student(
    student_id: int,
    _: bool = Depends(verfiy_headers_admin)
):
    with DB_Students() as db:
        result = db.delete(student_id)
    
    return {"student_id": student_id, "message": result}


@router.get("/students/", response_model=List[GetStudentModel])
async def get_all_students(
    _: bool = Depends(verfiy_headers_admin)
):
    with DB_Students() as db:
        students = db.list_all()

    return students


"""
Rutas del admin para manejar los idiomas
"""
@router.post("/languages/", response_model=LanguageCreateAndUpdate)
async def add_language(
    language: LanguageModel,
    _: bool = Depends(verfiy_headers_admin)
):
    with DB_Languages() as db:
        language_id = db.add(language.name)

    return {"language_id": language_id, "name":language.name}


@router.put("/languages/{language_id}", response_model=LanguageCreateAndUpdate)
async def update_language(
    language_id: int, 
    language: LanguageModel,
    _: bool = Depends(verfiy_headers_admin)
):
    with DB_Languages() as db:
       db.update(language_id, language.dict())
    
    return language


@router.delete("/languages/{language_id}", status_code=200, response_model=LanguageDelete)
async def delete_language(
    language_id: int,
    _: bool = Depends(verfiy_headers_admin)
):
    with DB_Languages() as db:
        result = db.delete(language_id)
    
    return {"language_id": language_id, "message": result}


@router.get("/languages/", response_model=List[GetLanguageModel])
async def get_all_languages(
    _: bool = Depends(verfiy_headers_admin)
):
    with DB_Languages() as db:
        languages = db.list_all()

    return languages



@router.post("/students/subscribe", response_model=StudentLanguages)
async def student_subscribe(
    data: StudentLanguages,
    _: bool = Depends(verfiy_headers_admin)
):
    with DB_StudentLanguages() as db:
        db.add_student_to_language(data.student_id, data.language_id)

    return data



@router.post("/students/unsubscribe", response_model=StudentLanguages)
async def student_unsubscribe(
    data: StudentLanguages,
    _: bool = Depends(verfiy_headers_admin)
):
    with DB_StudentLanguages() as db:
        db.remove_student_from_language(data.student_id, data.language_id)

    return data


@router.get("/students/subscribes/{student_id}", response_model=List[StudentLanguageID])
async def get_all_student_subscribes(
    student_id: int,
    _: bool = Depends(verfiy_headers_admin)
):
    with DB_StudentLanguages() as db:
        return db.list_languages_by_student(student_id)



@router.get("/languages/subscribes/{language_id}", response_model=List[StudentLanguageID])
async def get_all_students_subscribed_to_language(
    language_id: int,
    _: bool = Depends(verfiy_headers_admin)
):
    with DB_StudentLanguages() as db:
        return db.list_students_by_language(language_id)
