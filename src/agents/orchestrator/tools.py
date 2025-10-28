from collections.abc import Sequence

from strands import tool

from core.logger import logger
from schemas import FinalAnalyticsCount, FinalAnalyticsResult, User


@tool
def final_analytics(
    users: Sequence[User], summary: str, filtered_users: Sequence[User]
) -> str:
    """
    Construct the final analytics.

    Args:
        users: Fetched list of users.
        summary: Short summary of the fetched list of users.
        filtered_users: Filtered list of users.
    """

    logger.info("Calling final_analytics")

    return FinalAnalyticsResult(
        users=filtered_users,
        summary=summary,
        count=FinalAnalyticsCount(unfiltered=len(users), filtered=len(filtered_users)),
    ).model_dump_json()
