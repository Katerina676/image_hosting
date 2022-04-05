from typing import Optional

from ormar import Model, Integer, String, ModelMeta, ForeignKey
from db import database, metadata


class MainMeta(ModelMeta):
    database = database
    metadata = metadata


class User(Model):
    class Meta(MainMeta):
        pass

    id: int = Integer(primary_key=True)
    username: str = String(max_length=100)


class Image(Model):
    class Meta(MainMeta):
        pass

    id: int = Integer(primary_key=True)
    title: str = String(max_length=50)
    description: str = String(max_length=250)
    file: str = String(max_length=1000)
    user: Optional[User] = ForeignKey(User)