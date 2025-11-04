from .schemas import User, Users, UsersSummaryRequest


def get_users_tool() -> Users:
    # TODO: query a real db
    users = Users(
        users=[
            User(**{"id": 1, "name": "Alice", "age": 24, "city": "Berlin"}),
            User(**{"id": 3, "name": "Charlie", "age": 29, "city": "Warsaw"}),
            User(**{"id": 2, "name": "Bob", "age": 31, "city": "Kyiv"}),
        ]
    )

    return users


def make_summary_tool(
    request: UsersSummaryRequest,
) -> str:
    users = request.users

    if len(users) == 0:
        return "Found 0 users"

    unique_cities = set(user.city for user in users)
    summary = (
        f"Found {len(users)} user{'s' if len(users) > 1 else ''} "
        f"from {len(unique_cities)} "
        f"{'different cities' if len(unique_cities) > 1 else 'city'}"
    )

    return summary
