from typing import Annotated

from aws_lambda_powertools.event_handler.openapi.params import Body

from .app import app, logger, tracer
from .schemas import User, Users


@app.get(
    "/users",
    description="Fetches a list of users with their information from a database",
    tags=["users"],
)
@tracer.capture_method
def get_users() -> Annotated[Users, Body(description="List of users")]:
    logger.info("Serving get_users")

    # TODO: query a real db
    users = Users(
        users=[
            User(**{"id": 1, "name": "Alice", "age": 24, "city": "Berlin"}),
            User(**{"id": 3, "name": "Charlie", "age": 29, "city": "Warsaw"}),
            User(**{"id": 2, "name": "Bob", "age": 31, "city": "Kyiv"}),
        ]
    )

    return users
