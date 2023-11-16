from fastapi import HTTPException, APIRouter, Depends
from typing import List
import jwt
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

from src.models.students.db_students import DB_Students
from src.models.student_languages.db_student_languages import DB_StudentLanguages

from src.models.languages.languages import PercentageCountry, LanguageModel

from src.api.middlewares.header_verification import verify_headers_students

from src.utils.restcountries import RestCountriesAPI

router = APIRouter()

@router.get('/percentages/{language}', response_model=List[PercentageCountry])
async def get_percentages(
    language: int,
    _:bool = Depends(verify_headers_students)
):
    api_restcountries = RestCountriesAPI()
    return api_restcountries.get_percentage_population_by_language(language)