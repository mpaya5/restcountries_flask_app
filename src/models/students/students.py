from pydantic import BaseModel, Field, EmailStr

class StudentModel(BaseModel):
    name: str = Field(..., description="The name of the student")
    email: EmailStr = Field(..., description="The email of the student")

class GetStudentModel(BaseModel):
    id: int = Field(..., description="The identifier number for the student")
    name: str = Field(..., description="The name of the student")
    email: EmailStr = Field(..., description="The email of the student")

class StudentID(BaseModel):
    student_id: int = Field(..., description="The student id you want to interact with")

class StudentCreate(BaseModel):
    id: int = Field(..., description="The identifier number for the student")
    name: str = Field(..., description="The name of the student")
    email: EmailStr = Field(..., description="The email of the student")
    token: str = Field(..., description="The token created for the student, share it carefully")

class StudentDelete(BaseModel):
    student_id: int = Field(..., description="The Student deleted")
    message: str = Field(..., description="The result of the execution")