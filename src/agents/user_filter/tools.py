from strands import tool

from schemas import UserFilterResult, Users

from .agent import filter_agent


@tool
def user_filter(users: Users, filtering_criteria_prompt: str) -> UserFilterResult:
    """
    Filter the list of users according to the given filtering criteria and return
    the filtered result.

    Args:
        users: List of users
        filtering_criteria_prompt: Filtering criteria to apply to the list
    """

    prompt = (
        f"Users:\n{users.model_dump_json()}\n\n"
        f"Filtering criteria:\n{filtering_criteria_prompt}"
    )

    filtered_users = filter_agent.structured_output(
        UserFilterResult,
        prompt,
    )

    return filtered_users
