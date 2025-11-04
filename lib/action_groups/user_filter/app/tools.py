from .exceptions import InvalidFilteringCriteriaException
from .schemas import (
    FilterUsersRequest,
    FilterUsersResponse,
    User,
    UserField,
)
from .types import FilterComparisonOp, FilterOp


def filter_users_tool(request: FilterUsersRequest) -> FilterUsersResponse:
    users = request.users
    criteria_seq = request.filtering_criteria.split()

    filtered_users: list[User]

    match criteria_seq:
        case ["only", *rest] | rest:  # "only" keyword at the beginning is optional
            match rest:
                case [UserField.age.value as attr, op_name, value] if (
                    value.isdigit() and op_name in FilterComparisonOp.keys()
                ):
                    value = int(value)
                    pass

                case [
                    UserField.name.value | UserField.city.value as attr,  # type: ignore
                    op_name,
                    value,
                ] if op_name in FilterOp.keys():
                    pass

                case _:
                    raise InvalidFilteringCriteriaException

            op = FilterOp[op_name]
            filtered_users = [
                user for user in users if op(attr, getattr(user, attr), op_name, value)
            ]

    return FilterUsersResponse(filtered_users=filtered_users)
