from http import HTTPStatus
from typing import Annotated
from aws_lambda_powertools.event_handler.openapi.params import Body
from aws_lambda_powertools.utilities.typing import LambdaContext

from lib.action_groups.user_filter.app.schemas import (
    FilterUsersRequest,
    FilterUsersResponse,
)
from lib.action_groups.user_filter.app.tools import filter_users_tool

from .app import app, logger, tracer


@app.post(
    "/filter",
    description="Returns a filtered list of users filtered according to the given filtering criteria",
    tags=["users"],
    responses={
        HTTPStatus.BAD_REQUEST: {"description": "Filtering failed, invalid criteria"},
        HTTPStatus.OK: {"description": "List of users successfully fitlered"},
    },
)
@tracer.capture_method
def filter_users(
    request: FilterUsersRequest,
) -> Annotated[FilterUsersResponse, Body(description="Filtered list of users")]:
    logger.info("Serving filter_users")
    return filter_users_tool(request)


@logger.inject_lambda_context
@tracer.capture_lambda_handler
def lambda_handler(event: dict, context: LambdaContext):
    return app.resolve(event, context)
