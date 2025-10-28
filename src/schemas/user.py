from collections.abc import Sequence
from typing import TypedDict

from .base import Base


class User(TypedDict):
    id: int
    name: str
    age: int
    city: str


class Users(Base):
    users: Sequence[dict]


class UserDataFetchResult(Users):
    summary: str


class UserFilterResult(Base):
    filtered_users: Sequence[dict]
