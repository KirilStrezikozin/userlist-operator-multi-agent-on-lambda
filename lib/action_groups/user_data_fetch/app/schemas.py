from collections.abc import Sequence

from pydantic import BaseModel, ConfigDict


class Base(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class User(Base):
    id: int
    name: str
    age: int
    city: str


class Users(Base):
    users: Sequence[User]


class UserDataFetchResult(Users):
    summary: str
