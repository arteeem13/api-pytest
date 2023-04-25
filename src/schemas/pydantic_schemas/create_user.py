from pydantic import BaseModel


class ModelCreateUser(BaseModel):
    name: str
    job: str
    id: str
    createdAt: str
