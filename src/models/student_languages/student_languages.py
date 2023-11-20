from pydantic import BaseModel, Field

class StudentLanguages(BaseModel):
    student_id: int = Field(..., description="The student id")
    language_id: int = Field(..., description="The language id")

class StudentLanguageID(BaseModel):
    id: int = Field(..., description="The id of your request")