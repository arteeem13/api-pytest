from pydantic import BaseModel, Field, validator


class Data(BaseModel):
    id: int
    name: str
    year: int = Field(ge=2001)  # то же, что и @validator
    color: str
    pantone_value: str

    @validator("id")
    def id_equal_2(cls, value):
        if value != 2:
            raise ValueError("Id не равен 2!")
        else:
            return value


class Support(BaseModel):
    url: str
    text: str


class ModelSingleResource(BaseModel):
    data: Data
    support: Support
