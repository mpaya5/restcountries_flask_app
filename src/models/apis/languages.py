from pydantic import BaseModel, Field

class LanguageModel(BaseModel):
    name: str = Field(..., description="The name of the language")

class GetLanguageModel(BaseModel):
    id: int = Field(..., description="The language id")
    name: str = Field(..., description="The name of the language")

class LanguageID(BaseModel):
    language_id: int = Field(..., description="The language id you want to interact with")

class LanguageDelete(BaseModel):
    language_id: int = Field(..., description="The language deleted")
    message: str = Field(..., description="The result of the execution")

class LanguageCreateAndUpdate(BaseModel):
    language_id: int = Field(..., description="The language id")
    name: str = Field(..., description="The language name")


class PercentageCountry(BaseModel):
    name: str = Field(..., description="Name of the country"),
    population: int = Field(..., description="Population number"),
    percentage: str = Field(..., description="Percentage number")


class LanguagePercentage(BaseModel):
    language: str = Field(..., description="The language we will use for search the population percentage")