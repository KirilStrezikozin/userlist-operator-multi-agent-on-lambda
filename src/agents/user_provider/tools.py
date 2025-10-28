from collections.abc import Sequence

from strands import tool

from core.logger import logger
from schemas import User, UserDataFetchResult

from .agent import userlist_summary_agent


@tool
async def fetch_users() -> Sequence[User]:
    """
    Fetch a list of all users from a database.
    """

    logger.info("Calling fetch_users")

    # TODO: query a real db
    return [
        User(**{"id": 1, "name": "Alice", "age": 24, "city": "Berlin"}),
        User(**{"id": 3, "name": "Charlie", "age": 29, "city": "Warsaw"}),
        User(**{"id": 2, "name": "Bob", "age": 31, "city": "Kyiv"}),
    ]


@tool
async def user_data_fetch() -> str:
    """
    Fetch a list of all users from a database and
    create a short summary of the fetched result.
    """

    logger.info("Calling user_data_fetch")
    users = await fetch_users()

    logger.info("Calling userlist_summary_agent")
    summary_response = userlist_summary_agent(str(users))

    return UserDataFetchResult(
        users=users, summary=str(summary_response)
    ).model_dump_json()
