from collections.abc import Sequence
from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, ConfigDict, StringConstraints


class Base(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class User(Base):
    id: int
    name: str
    age: int
    city: str


class UserField(StrEnum):
    id = "id"
    name = "name"  # type: ignore
    age = "age"
    city = "city"


class Users(Base):
    users: Sequence[User]


class FilterUsersRequest(Users):
    filtering_criteria: Annotated[str, StringConstraints(strict=True, max_length=1000)]


class FilterUsersResponse(Base):
    filtered_users: Sequence[User]
