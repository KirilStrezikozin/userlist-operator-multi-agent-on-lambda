from collections.abc import Sequence

from strands import tool

from core.logger import logger
from schemas import User, UserFilterResult

from .agent import filter_agent


@tool
def user_filter(
    users: Sequence[User],
    filtering_criteria_prompt: str,
) -> str:
    """
    Filter the list of users according to the given filtering criteria and return
    the filtered result.

    Args:
        users: List of users
        filtering_criteria_prompt: Filtering criteria to apply to the list
    """

    logger.info("Calling user_filter")

    prompt = f"Users:\n{users}\n\nFiltering criteria:\n{filtering_criteria_prompt}"

    filtered_users = filter_agent.structured_output(
        UserFilterResult,
        prompt,
    )

    return filtered_users.model_dump_json()
