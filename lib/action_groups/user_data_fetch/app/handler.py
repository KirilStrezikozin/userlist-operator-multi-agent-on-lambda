from typing import Annotated
from aws_lambda_powertools.event_handler.openapi.params import Body
from aws_lambda_powertools.utilities.typing import LambdaContext

from .tools import get_users_tool, make_summary_tool
from .schemas import UsersSummaryRequest

from .app import app, logger, tracer


@app.get(
    "/users",
    description="Fetches a list of users with their information from a database",
    tags=["users"],
)
@tracer.capture_method
def get_users() -> Annotated[
    str, Body(description="JSON payload with a list of users")
]:
    logger.info("Serving get_users")
    return get_users_tool().model_dump_json()


@app.post(
    "/summary",
    description="Generate a summary of a list of users",
    tags=["users"],
)
@tracer.capture_method
def make_summary(
    users: Annotated[
        UsersSummaryRequest, Body(description="JSON payload with a list of users")
    ],
) -> Annotated[str, Body(description="Summary of the list of users")]:
    logger.info("Serving make_summary")
    return make_summary_tool(users)


@logger.inject_lambda_context
@tracer.capture_lambda_handler
def lambda_handler(event: dict, context: LambdaContext):
    logger.info(event)
    return app.resolve(event, context)
