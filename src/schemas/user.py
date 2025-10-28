from collections.abc import Sequence

from .base import Base


class User(Base):
    id: int
    name: str
    age: int
    city: str


class Users(Base):
    users: Sequence[User]


class UserDataFetchResult(Users):
    summary: str


class UserFilterResult(Base):
    filtered_users: Sequence[User]
