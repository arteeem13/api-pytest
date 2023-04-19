from typing import List

from pydantic import BaseModel
from pydantic import validator


class Datum(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str

    @validator("email")
    def check_contains_domain_reqres_in_email(cls, email):
        if "@reqres.in" in email:
            return email
        else:
            raise ValueError("Email не содержит домен @reqres.in")


class Support(BaseModel):
    url: str
    text: str


class ModelDelayedResponse(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[Datum]
    support: Support
