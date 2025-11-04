import pytest

from ..app.exceptions import (
    InvalidFilteringCriteriaException,
)
from ..app.schemas import FilterUsersRequest, User
from ..app.tools import filter_users_tool


@pytest.fixture
def sample_users():
    return [
        User(id=1, name="Alice", age=25, city="Paris"),
        User(id=2, name="Bob", age=30, city="London"),
        User(id=3, name="Charlie", age=35, city="Paris"),
        User(id=4, name="John Doe", age=28, city="Berlin"),
    ]


def make_request(users, criteria):
    return FilterUsersRequest(users=users, filtering_criteria=criteria)


def test_filter_age_greater_than(sample_users):
    req = make_request(sample_users, "age > 30")
    res = filter_users_tool(req)
    assert [u.name for u in res.filtered_users] == ["Charlie"]


def test_filter_age_with_only_prefix(sample_users):
    req = make_request(sample_users, "only age >= 30")
    res = filter_users_tool(req)
    assert [u.name for u in res.filtered_users] == ["Bob", "Charlie"]


def test_filter_city_equals(sample_users):
    req = make_request(sample_users, "city = Paris")
    res = filter_users_tool(req)
    assert [u.name for u in res.filtered_users] == ["Alice", "Charlie"]


def test_filter_name_contains(sample_users):
    req = make_request(sample_users, "name contains John")
    res = filter_users_tool(req)
    assert [u.name for u in res.filtered_users] == ["John Doe"]


def test_invalid_age_value(sample_users):
    req = make_request(sample_users, "age = abc")
    with pytest.raises(InvalidFilteringCriteriaException):
        filter_users_tool(req)


def test_invalid_field_name(sample_users):
    req = make_request(sample_users, "country = France")
    with pytest.raises(InvalidFilteringCriteriaException):
        filter_users_tool(req)
