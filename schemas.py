from typing import List

from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str

    class Config:
        arbitrary_types_allowed = True


class UploadImg(BaseModel):
    title: str
    description: str


class GetFile(BaseModel):
    user: User
    title: str
    description: str


class Message(BaseModel):
    message: str

